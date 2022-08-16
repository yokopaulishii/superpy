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
import time

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

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
    report_inventory=subparser.add_parser('report_inventory')
    report_revenue=subparser.add_parser('report_revenue')
    report_profit=subparser.add_parser('report_profit')
#define argument for buy parser
    buy.add_argument('--id', help='identification number of the product bought', type = int)
    buy.add_argument('--product_name', help = 'name of the product bought', type = str)
    buy.add_argument('--buy_quantity', action='count', help = 'quantity of the product bought')
    buy.add_argument('--buy_price', help='cost price of the product bought', type = float)
    buy.add_argument('--expiration_date', help = 'expiration date - format: YYYY-mm-dd', type = valid_date)
#define argument for sell parser
    sell.add_argument('--id', help='identification number of the product sold', type = int)
    sell.add_argument('--bought_id', help = 'name of the product bought')
    sell.add_argument('--sell_quantity', action='count', help='quantity of the product sold')
    sell.add_argument('--sell_date', help='date of the product sold - format: YYYY-mm-dd', type = valid_date)
    sell.add_argument('--sell-price', help='price of the product sold', type = float)
#define argument for report parser
    report_inventory.add_argument('--yesterday', help='date of the report - format: YYYY-mm-dd', type = valid_date)
    report_inventory.add_argument('--now', help='date of the report - format: YYYY-mm-dd', type = valid_date)
    report_revenue.add_argument('--yesterday', help='report revenue yesterday - format: YYYY-mm-dd', type = valid_date)
    report_revenue.add_argument('--today', help='report revenue today - format: YYYY-mm-dd', type = valid_date)
    report_revenue.add_argument('--date', help='report revenue specific day - format: YYYY-mm-dd', type = valid_date)
    report_profit.add_argument('--today', help='report profit today - format: YYYY-mm-dd', type = valid_date)
#execute the parse_args() method
    args = parser.parse_args()
    return vars(args)

#define rows in buy.csv
csv_buy_rowlist = [
    ['id', 'product_name', 'buy_quantity', 'buy_price', 'expiration_date'],
    [1, 'milk', 1, 1.50, 2022-10-10],
    [2, 'bread', 2, 2.50, 2022-10-10],
    [3, 'butter', 3, 3.50, 2022-10-10]
]
#write buy.csv in buy function
def buy(args):
    args=parser()
    current_date = dt.date.today()
    print(current_date)
    datet = '2022-08-12'
    #implement Expiration date with datetime module, strptime
    expiration_date = datetime.strptime(datet, '%Y-%m-%d').date()
    now = date.today()
    if expiration_date >= now:
        print('expired')
    elif expiration_date == now:
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
    args=parser()
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
    args=parser()
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
    args=parser()
    #open file in append mode
    with open('sell.csv', 'a+', newline='') as write_obj:
        #create a writer object from csv module
        csv_writer = writer(write_obj)
        #add contents of list as last row in the csv file
        csv_writer.writerow(args.id, args.bought_id, args.sell_quantity, args.sell_date, args.sell_price)
        return vars(append_sell(args))
    
def report(args):
    args=parser()
    with open('sell.csv','buy.csv' 'r') as file:
        csv.reader=csv.reader(file)
        for line in csv.reader:
            return vars(sell(args), buy(args))

def valid_date(s):
    args=parser()
    #today
    today = date.today()
    #yesterday
    yesterday = today - timedelta(days = 1)
    # Get 2 days earlier
    yesterday2 = today - timedelta(days = 2)
    if args.report == today:
        print("Today is: ", today)
    elif args.report == yesterday:
        print("Yesterday was: ", yesterday)
    elif args.report == yesterday2:
        print("Day before yesterday was: ", yesterday2)
    try:
        return time.strftime("%Y-%m-%d", time.localtime())
    except ValueError:
         msg = "not a valid date: {0!r}".format(s)
    raise argparse.ArgumentTypeError(msg)
    
    
def main():
    args = parser()
    if args.command == 'report_inventory':
        print(buy(args), sell(args))
    elif args.command == 'buy':
        print(buy(args))
    elif args.command == 'sell':
        print(sell(args))
    return vars(main), print('ok')

if __name__ == "__main__":
    main()
