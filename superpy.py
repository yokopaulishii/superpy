import argparse
import csv
from datetime import date
from datetime import timedelta
from datetime import tzinfo
from datetime import datetime, date
import datetime as dt
import time
from csv import writer

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
        f_object.close()
    #in order to simultaneously add the same new products to both inventory and to buy.csv, open inventory.csv with append
    with open('inventory.csv', 'a')as f_object2:
        writer_object=writer(f_object2)
        writer_object.writerow(new_products_bought)
        f_object2.close()
    #this is an attempt to sum up all variables of bought_quantity in inventory.csv
    with open('inventory.csv') as f_object2:
        f_object2.next()
        total=sum(int(bought_quantity[2])for bought_quantity in csv.reader(f_object2))
        print(total)
        print(bought_quantity)

#define parsed sell arguments as fieldnames for sell function
fields = ['sell_id', 'sold_name', 'sold_quantity', 'sell_date', 'sell_price']
#initialize sell function with parsed sell arguments
def sell(sell_id, sold_name, sold_quantity, sell_date, sell_price):
    #implement parsed sell arguments in a list so you can insert new products in terminal
    new_products_sold = [sell_id, sold_name, sold_quantity, sell_date, sell_price]
    #open inventory.csv first to check if there is enough stock before sell function is initiated
    with open('inventory.csv', 'r') as f_object2: 
        #this is an attempt to sum up all bought_quantity in inventory.csv
        total=sum(int(bought_quantity[2])for bought_quantity in csv.reader(f_object2))
        csv.reader=csv.reader(f_object2)
        #to loop over all sold_quantity in inventory.csv
        for sold_quantity in f_object2:
            #if the total sum of sold_quantity is more than total (in inventory defined) 
            if sold_quantity < total:
                #if it is true
                while True:
                    #then print following comment in terminal:
                    print('This product is not in inventory and cannot be sold')     
            #otherwise open sell.csv and append new products that are sold and save
            else:
                with open('sell.csv', 'a') as f_object:
                    writer_object=writer(f_object)
                    writer_object.writerow(new_products_sold)
                    f_object.close()
    
def report(inventory, revenue, profit):
        print('ok')
    

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

    #inventory parser
    inventory_parser = subparsers.add_parser('inventory', help='register purchased product')
    inventory_parser.add_argument('--buy_id', help='insert product id', type=int)
    inventory_parser.add_argument('--bought_quantity', help='insert quantity of the product bought', type=int)
    inventory_parser.add_argument('--product_name', help='insert name of the product bought')
    inventory_parser.add_argument('--buy_price', help='insert product price', type=float)
    inventory_parser.add_argument('--expiration_date', help='best before- format: YYYY-mm-dd', type=valid_date)
    inventory_parser.add_argument('--date', help='specify the date of the inventory - format: YYYY-mm-dd', type=valid_date)
   
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

