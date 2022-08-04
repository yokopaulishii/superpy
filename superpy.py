# Imports
import argparse
import csv
from datetime import date
from datetime import timedelta
from datetime import tzinfo
from datetime import datetime, date
import datetime as dt

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    pass
#import datetime for the concept of now, today, yesterday and expiration date
#import CSV module to write and read csv files
#implement the header of the bought.csv
header = ['id', 'product_name', 'buy_price', 'expiration_date']
#implement the data of the bought.csv
data = [
    [1, 'milk', 1.50, 2022-10-10]
    [2, 'bread', 2.50, 2022-10-10]
    [3, 'butter', 3.50, 2022-10-10]
]
#open the bought.csv in the write mode
with open('bought.csv', 'w') as f:
    #create the csv writer
    writer = csv.writer(f)
    #write the header
    writer.writerow(header)
    #write the data, multiple rows
    writer.writerows(data)
    print(f)
    #import argparse for help function in command line
    #start initiating argparse
def Superpy(buy, command_line):
    parser = argparse.ArgumentParser('Superpy')
    parser.add_argument('--debug', action='store_true', help ='print debug info')
    subparsers = parser.add_subparsers(dest = 'command')
    #id, product_name and expiration date of the products bought, content of the file bought.csv
    buy = subparsers.add_parser('id', type = int, help = 'identification number of the bought product')
    buy.add_argument('product_name', type = str, help='name of the product')
    buy.add_argument('expiration_date', type = float, help ='expiration date: yyyy-mm-dd')
    #end of initiation argparse
    args = parser.parse_args()
    #implement current date as datet with datetime module
    current_date = dt.date.today()
    print(current_date)
    datet = '2022-08-03'
    #implement Expiration date with datetime module, strptime
    ExpirationDate = datetime.strptime(datet, '%Y-%m-%d').date()
    now = date.today()
    if ExpirationDate >= now:
        print('expired')
    elif ExpirationDate == now:
        print('50% discount')
    else: 
        print('expiration date 2022-10-10')

#import CSV module to write and read csv files
#implement the header of the sold.csv
header = ['id', 'bought_id', 'sell_date', 'sell_price']
data = [
    [1, '1.milk', 2022-10-13, 2.50]
    [2, '2.bread', 2022-10-14, 3.50]
    [3, '3.butter', 2022-10-15, 4.50]
]
#open the sold.csv in the write mode
with open('sold.csv', 'w') as f:
    #create the csv writer
    writer = csv.writer(f)
    #write the header
    writer.writerow(header)
    #write the data, multiple rows
    writer.writerows(data)
    print(f)
    #import argparse for help function in command line
    #start initiating argparse
def Superpy(sell, command_line):
    parser = argparse.ArgumentParser('Superpy')
    parser.add_argument('--debug', action='store_true', help ='print debug info')
    subparsers = parser.add_subparsers(dest = 'command')
    #id, bought_id, sell_date and sell_price of the products sold, content of the file sold.csv
    sell = subparsers.add_parser('id', type = int, help = 'identification number of the sold product')
    sell.add_argument('sell_date', type = int, help = 'date of the sold product') 
    sell.add_argument('sell_price', type = float, help = 'price of the sold product') 
    #end of initiation argparse
    args = parser.parse_args()


if __name__ == "__main__":
    main()
