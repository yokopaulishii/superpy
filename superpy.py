# Imports
import argparse
import csv
from datetime import date
from datetime import timedelta
from datetime import tzinfo

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    pass
#import datetime for the concept of now, today, yesterday and expiration date
import datetime as dt
current_date = dt.date.today()
print(current_date)

from datetime import datetime, date

datet = '2022-08-03'

ExpirationDate = datetime.strptime(datet, '%Y-%m-%d').date()
now = date.today()
if ExpirationDate >= now:
    print('expired')
elif ExpirationDate == now:
    print('50% discount')
else: 
    print('expiration date 2022-10-10')

#import argparse for help function in command line
import argparse
#function command line Superpy
def main(command_line='Superpy'):
    #start initiating argparse
    parser = argparse.ArgumentParser('Superpy')
    parser.add_argument('inventory', type=str, help ='inventory info')
    subparsers = parser.add_argument(dest='command')
    #id, product_name and expiration date of the products bought, content of the file bought.csv
    buy = subparsers.add_parser('id', type = int, help = 'identification number of the bought product')
    buy.add_argument('product_name', type = str, help='name of the product')
    buy.add_argument('expiration_date', type = float, help ='expiration date: yyyy-mm-dd')
    #id, bought_id, sell_date and sell_price of the products sold, content of the file sold.csv
    sell = subparsers.add_parser('id', type = int, help = 'identification number of the sold product')
    sell.add_argument('sell_date', type = int, help = 'date of the sold product') 
    sell.add_argument('sell_price', type = float, help = 'price of the sold product') 
    #end of initiation argparse
    args = parser.parse_args(command_line)
   
  

#import CSV module to write and read csv files
import csv 

#open csv files bought.csv and sold.csv to read 
with open('bought.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    print(csv_reader)
    for line in csv_reader:
        print(line)
     


with open('sold.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    print(csv_reader)
    for line in csv_reader:
        print(line)

#open bought.csv and sold.csv to write
with open('bought.csv', 'w') as new_file:
    fieldnames = ['id', 'product_name', 'buy_date', 'buy_price', 'expiration_date']
    csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames, delimiter= '_')
    csv_writer.writeheader()
   
with open('sold.csv', 'w') as new_file:
    fieldnames = ['id', 'bought_id', 'sell_date', 'sell_price']
    csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames, delimiter= ' ')
    csv_writer.writeheader()




if __name__ == "__main__":
    main()
