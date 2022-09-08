import argparse
import csv
from datetime import date
from datetime import timedelta
from datetime import tzinfo
from datetime import datetime, date
import datetime as dt
import time
from csv import writer
import pandas as pd
import os
import matplotlib.pyplot as plt
from itertools import combinations
from collections import Counter
import rich

def valid_date(s):
    today = date.today()
    yesterday = today - timedelta(days = 1)
    yesterday2 = today - timedelta(days = 2)
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
         msg = "not a valid date: {0!r}".format(s)
    raise argparse.ArgumentTypeError(msg)

#to define fieldname of buy.csv file
fields = ['buy_id', 'product_name', 'bought_quantity', 'buy_price', 'expiration_date']
#start buy function with parsed arguments for buy.csv
def buy(buy_id, bought_quantity, product_name, buy_price, expiration_date):
    #new products that will be inserted in terminal under buy parse implemented in a list
    new_products_bought = [buy_id, bought_quantity, product_name, buy_price, expiration_date]
    #open a buy.csv in append mode
    with open('buy.csv', 'a') as f_object:
        writer_object=writer(f_object)
        writer_object.writerow(new_products_bought)
    #in order to simultaneously add the same new products to both inventory and buy.csv, then open inventory.csv with append
    with open('inventory.csv', 'a')as f_object2:
        writer_object=writer(f_object2)
        writer_object.writerow(new_products_bought)
   

#define parsed sell arguments as fieldnames for sell function
fields = ['sell_id', 'sold_name', 'sold_quantity', 'sell_date', 'sell_price']
#initialize sell function with parsed sell arguments
def sell(sell_id, sold_name, sold_quantity, sell_date, sell_price):
    #implement parsed sell arguments in a list so you can insert new products in terminal
    new_products_sold = [sell_id, sold_name, sold_quantity, sell_date, sell_price]
    #open inventory.csv first to check if there is enough stock before sell function is initiated
    with open('sell.csv', 'a') as f_object3:
        writer_object=writer(f_object3)
        writer_object.writerow(new_products_sold)
    #open revenue.csv to receive revenue data


def report(revenue, inventory, profit):
    #read sell.csv in pandas
    sell_data=pd.read_csv('sell.csv')
    #add a revenue column to sell.csv
    sell_data['revenue']=sell_data['sold_quantity']*sell_data['sell_price']
    #changing str to int in these two columns to iterate
    sell_data['sold_quantity']=pd.to_numeric(sell_data['sold_quantity'])
    sell_data['sell_price']=pd.to_numeric(sell_data['sell_price'])
    sell_data.head()
    #total sum of revenue
    sell_results=sell_data.groupby('sell_date').sum()['revenue']
    #visualize sell.csv
    plt.plot(sell_results.index, sell_results.values)
    plt.show()
    #read buy.csv in pandas   
    buy_data=pd.read_csv('buy.csv')
    #add a purchase cost column in buy.csv
    buy_data['purchase cost']=buy_data['buy_price']*buy_data['bought_quantity']
    #add a profit column in buy.csv
    buy_data['profit']=buy_data['revenue']-buy_data['purchase cost']
    #changing from str to int of these columns to iterate
    buy_data['bought_quantity']=pd.to_numeric(buy_data['bought_quantity'])
    buy_data['buy_price']=pd.to_numeric(buy_data['buy_price'])
    buy_data.head()
    #total sum of revenue
    buy_results=buy_data.groupby('buy_date').sum()['profit']
    #visualize sell.csv
    plt.plot(buy_results.index, buy_results.values)
    plt.show()

def parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    # Build buy parser
    buy_parser = subparsers.add_parser('buy', help='register purchased product')
    buy_parser.add_argument('--buy_id', help='insert product id', type=int)
    buy_parser.add_argument('--bought_quantity', help='insert quantity of the product bought', type=int)
    buy_parser.add_argument('--product_name', help='insert name of the product bought')
    buy_parser.add_argument('--buy_price', help='insert product price', type=float)
    buy_parser.add_argument('--expiration_date', help='best before- format: YYYY-mm-dd', type=valid_date)
    # Build sell parser
    sell_parser = subparsers.add_parser('sell', help='register sold product')
    sell_parser.add_argument('--sell_id', help='insert product bought id', type=int)
    sell_parser.add_argument('--sold_name', help='insert name of the product sold')
    sell_parser.add_argument('--sold_quantity', help='insert quantity of the product sold', type=int)
    sell_parser.add_argument('--sell_date', help='insert date of the sold product - format: YYYY-mm-dd', type=valid_date)
    sell_parser.add_argument('--sell_price', help='insert price of the product sold', type=float)
    # Build report parser
    report_parser = subparsers.add_parser('report', help='report transaction')
    report_parser.add_argument('--inventory', help='insert date of report inventory - format: YYYY-mm-dd', type=valid_date)
    report_parser.add_argument('--revenue', help='insert date of report revenue - format: YYYY-mm-dd', type=valid_date)
    report_parser.add_argument('--profit', help='insert date of report inventory - format: YYYY-mm-dd', type=valid_date)
    return parser.parse_args()

def main():
    args = parser()
    if args.command == 'buy' and 'inventory':
        buy(args.buy_id, args.product_name, args.bought_quantity, args.buy_price, args.expiration_date)
    elif args.command == 'sell':
        sell(args.sell_id, args.sold_name, args.sold_quantity, args.sell_date, args.sell_price)
    elif args.command == 'report':
        report(args.inventory, args.revenue, args.profit)

if __name__ == '__main__':
    main()



