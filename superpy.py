# Imports
import argparse
import csv
import os
import sys
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
    ['id', 'product_name', 'buy_price', 'expiration_date'],
    [1, 'milk', 1.50, 2022-10-10],
    [2, 'bread', 2.50, 2022-10-10],
    [3, 'butter', 3.50, 2022-10-10]
]
#write buy.csv in buy function
def buy(args):
    with open('buy.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(csv_buy_rowlist)
    #read buy.csv
    with open('buy.csv', 'r') as file:
        csv.reader = csv.reader(file)
        for line in csv.reader:
            return vars(buy.csv)
            

#define rows in sell.csv
csv_sell_rowlist = [
    ['id', 'product_name', 'sell_date', 'sell_price'],
    [1, 'milk', 2022-10-13, 2.50],
    [2, 'bread', 2022-10-14, 3.50],
    [3, 'butter', 2022-10-15, 4.50]
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
#define argument for buy parser
    buy.add_argument('id', help='identification number of the product bought', type = int)
    buy.add_argument('product_name', help = 'name of the product bought', type = str)
    buy.add_argument('buy_price', help='cost price of the product bought', type = float)
    buy.add_argument('-expiration_date', help = 'expiration date - format: YYYY-MM-DD', required = True, type = valid_date)
#define argument for sell parser
    sell.add_argument('id', help='identification number of the product sold', type = int)
    sell.add_argument('bought_id', help = 'name of the product bought', type = str)
    sell.add_argument('-sell_date', help='date of the product sold - format: YYYY-MM-DD', required = True, type = valid_date)
    sell.add_argument('sell-price', help='price of the product sold', type = float)
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
