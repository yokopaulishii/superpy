# Imports
import argparse
import csv
import os
import sys
from csv import writer
from datetime import date
from datetime import timedelta
from datetime import tzinfo
from datetime import datetime, date
import datetime as dt

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

#define rows in buy.csv
csv_buy_rowlist = [
    ['id', 'product_name', 'buy_quantity', 'buy_price', 'expiration_date'],
    [1, 'milk', 1, 1.50, 2022-10-10],
    [2, 'bread', 2, 2.50, 2022-10-10],
    [3, 'butter', 3, 3.50, 2022-10-10]
]
#write buy.csv in buy function
def buy(args):
    command = input
    current_date = dt.date.today()
    print(current_date)
    datet = '2022-08-12'
    #implement Expiration date with datetime module, strptime
    ExpirationDate = datetime.strptime(datet, '%Y-%m-%d').date()
    now = date.today()
    if ExpirationDate >= now:
        print('expired')
    elif ExpirationDate == now:
        print('50% discount')
    else: 
        print('expiration date 2022-10-10')
    with open('buy.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(csv_buy_rowlist)
    #read buy.csv
    with open('buy.csv', 'r') as file:
        csv.reader = csv.reader(file)
        for line in csv.reader:
            return vars(buy.csv)

#append function that allows CMI input to add rows on buy.csv content 
def append_buy(args):
    #open file in append mode
    with open('buy.csv', 'a+', newline='') as write_obj:
        #create a writer object from csv module
        csv_writer = writer(write_obj)
        #add contents of list as last row in the csv file
        csv_writer.writerow(args.id, args.product_name, args.buy_quantity, args.buy_price, args.expiration_date)
        return vars(append_buy(args))
            

#define rows in sell.csv
csv_sell_rowlist = [
    ['id', 'product_name', 'sell_quantity', 'sell_date', 'sell_price'],
    [1, 'milk', 1, 2022-10-13, 2.50],
    [2, 'bread', 2, 2022-10-14, 3.50],
    [3, 'butter', 3, 2022-10-15, 4.50]
]
#write sell.csv in sell function
def sell(args):
    with open('sell.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(csv_sell_rowlist)
        #read sell.csv
    with open('sell.csv', 'r') as file:
        csv.reader=csv.reader(file)
        for line in csv.reader:
            return vars(sell.csv)

#append function that allows CMI input to add rows on sell.csv content 
def append_sell(args):
    #open file in append mode
    with open('sell.csv', 'a+', newline='') as write_obj:
        #create a writer object from csv module
        csv_writer = writer(write_obj)
        #add contents of list as last row in the csv file
        csv_writer.writerow(args.id, args.bought_id, args.sell_quantity, args.sell_date, args.sell_price)
        return vars(append_sell(args))

def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "not a valid date: {0!r}".format(s)
        raise argparse.ArgumentTypeError(msg)
# Yesterday, today and the day before yesterday's date
today = date.today()
print("Today is: ", today)
yesterday = today - timedelta(days = 1)
print("Yesterday was: ", yesterday)
# Get 2 days earlier
yesterday = today - timedelta(days = 2)
print("Day before yesterday was: ", yesterday)

def report(args):
    with open('sell.csv','buy.csv' 'r') as file:
        csv.reader=csv.reader(file)
        for line in csv.reader:
            return vars(sell(args), buy(args))

def parser():
#create the parent parser superpy and subparsers for her children buy and sell
#and to create their command line
#initiate Argparse
    parser = argparse.ArgumentParser(
    prog = 'superpy', 
    description = 'inventory',
    epilog = 'copyright (c) YPI'
    )
#initiate subparsers for buy and sell
    subparser=parser.add_subparsers(dest='command')
    buy=subparser.add_parser('buy')
    sell=subparser.add_parser('sell')
    report=subparser.add_parser('report')
#define argument for buy parser
    buy.add_argument('--id', help='identification number of the product bought', type = int)
    buy.add_argument('--product_name', help = 'name of the product bought', type = str)
    buy.add_argument('--buy_quantity', action='count', help = 'quantity of the product bought', type=int)
    buy.add_argument('--buy_price', help='cost price of the product bought', type = float)
    buy.add_argument('--expiration_date', help = 'expiration date - format: YYYY-mm-dd', required = True, type = valid_date)
#define argument for sell parser
    sell.add_argument('--id', help='identification number of the product sold', type = int)
    sell.add_argument('--bought_id', help = 'name of the product bought', type = str)
    sell.add_argument('--sell_quantity', action='count', help='quantity of the product sold', type= int)
    sell.add_argument('--sell_date', help='date of the product sold - format: YYYY-mm-dd', required = True, type = valid_date)
    sell.add_argument('--sell-price', help='price of the product sold', type = float)
#define argument for report parser
    report.add_argument('--report', help='date of the report - format: YYYY-mm-dd', dest=input, required = True, type = valid_date)
#execute the parse_args() method
    args = parser.parse_args()
    return vars(args)
    
def main():
    args = parser()
    if args.command == 'report':
        buy(args), sell(args)
    elif args.command == 'buy':
        buy(args)
    elif args.command == 'sell':
        sell(args)
    return vars(main)

if __name__ == "__main__":
    main()
