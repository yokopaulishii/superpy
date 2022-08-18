import argparse
import csv
from datetime import date
from datetime import timedelta
from datetime import tzinfo
from datetime import datetime, date
import datetime as dt
import time
from csv import writer

fields = ['id', 'product_name', 'bought_quantity', 'buy_price', 'expiration_date']
def buy(args):
    print(args.id, args.product_name, args.buy_price, args.expiration_date)
    with open('buy.csv', 'w') as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerow(fields)
    new_products_bought = [args.id, args.product_name, args.buy_price, args.expiration_date]
    with open('buy.csv', 'a') as f_object:
        writer_object=writer(f_object)
        writer_object.writerow(new_products_bought)
        f_object.close()
    with open('buy.csv', 'r') as file:
        csvFile=csv.reader(file)
        for lines in csvFile:
            print(lines)

fields = ['sell_id', 'bought_id', 'sold_quantity', 'sell_date', 'sell_price']
def sell(args):
    print(args.sell_id, args.bought_id, args.sold_quantity, args.sell_date, args.sell_price)
    with open('sell.csv', 'w') as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerow(fields)
    new_products_bought = [args.sell_id, args.bought_id, args.sold_quantity, args.sell_date, args.sell_price]
    with open('sell.csv', 'a') as f_object:
        writer_object=writer(f_object)
        writer_object.writerow(new_products_bought)
        f_object.close()
    with open('sell.csv', 'r') as file:
        csvFile=csv.reader(file)
        for lines in csvFile:
            print(lines)

def report(args):
    print(args.inventory_now, args.inventory_yesterday, args.revenue_today, args.revenue_yesterday, args.profit_today, args.profit_yesterday)

def valid_date(s):
    #today
    today = date.today()
    #yesterday
    yesterday = today - timedelta(days = 1)
    # Get 2 days earlier
    yesterday2 = today - timedelta(days = 2)
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
         msg = "not a valid date: {0!r}".format(s)
    raise argparse.ArgumentTypeError(msg)
                                            

def parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    # Build buy parser
    buy_parser = subparsers.add_parser('buy', help='register purchased product')
    buy_parser.add_argument('--id', help='insert product id', type=int)
    buy_parser.add_argument('--bought_quantity', help='insert quantity of the product bought', type=int)
    buy_parser.add_argument('--product_name', help='insert name of the product bought')
    buy_parser.add_argument('--buy_price', help='insert product price', type=float)
    buy_parser.add_argument('--expiration_date', help='best before- format: YYYY-mm-dd', type=valid_date)
   
    # Build sell parser
    sell_parser = subparsers.add_parser('sell', help='register sold product')
    sell_parser.add_argument('--sell_id', help='insert product bought id', type=int)
    sell_parser.add_argument('--bought_id', help='insert product bought id', type=int)
    sell_parser.add_argument('--sold_quantity', help='insert quantity of the product sold', type=int)
    sell_parser.add_argument('--sell_date', help='insert date of the sold product - format: YYYY-mm-dd', type=valid_date)
    sell_parser.add_argument('--sell_price', help='insert price of the product sold', type=float)

    # Build report parser
    report_parser = subparsers.add_parser('report', help='report transactions')
    report_parser.add_argument('--inventory_now', help='report inventory today - format:YYYY-mm-dd', type=valid_date)
    report_parser.add_argument('--inventory_yesterday', help='report inventory yesterday - format:YYYY-mm-dd', type=valid_date)
    report_parser.add_argument('--revenue_today', help='report revenue today - format:YYYY-mm-dd', type=valid_date)
    report_parser.add_argument('--revenue_yesterday', help='report revenue yesterday - format:YYYY-mm-dd', type=valid_date)
    report_parser.add_argument('--profit_today', help='report profit today - format:YYYY-mm-dd', type=valid_date)
    report_parser.add_argument('--profit_yesterday', help='report profit yesterday - format:YYYY-mm-dd', type=valid_date)

    return parser.parse_args()

def main():
    args = parser()
    if args.command == 'buy':
        buy(args)
    elif args.command == 'sell':
        sell(args)
    elif args.command == 'report':
        report(args)

if __name__ == '__main__':
    main()
