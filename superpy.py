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
def main():
    pass
#start superpy command tool
#create the parser
buy_parser=argparse.ArgumentParser(prog='superpy', description='buy_inventory')
#add the arguments
buy_parser.add_argument('id', help='identification number of the product bought', type = int)
buy_parser.add_argument('product_name', help = 'name of the product bought', type = str)
buy_parser.add_argument('buy_price', help='cost price of the product bought', type = float)
buy_parser.add_argument('expiration_date', help='expiration date of the product bought: yyyy-mm-dd', type = str)
#execute the parse_args() method
args = buy_parser.parse_args()

print(vars(args))

#create the parser
sell_parser=argparse.ArgumentParser(prog='superpy', description='sell_inventory')
#add the arguments
sell_parser.add_argument('id', help='identification number of the product sold', type = int)
sell_parser.add_argument('bought_id', help = 'name of the product bought', type = str)
sell_parser.add_argument('sell_date', help='date of the product sold: yyyy-mm-dd', type = int)
sell_parser.add_argument('sell-price', help='price of the product sold', type = float)

csv_buy_rowlist = [
    ['id', 'product_name', 'buy_price', 'expiration_date']
    [1, 'milk', 1.50, 2022-10-10]
    [2, 'bread', 2.50, 2022-10-10]
    [3, 'butter', 3.50, 2022-10-10]
]
csv_sell_rowlist = [
    ['id', 'product_name', 'sell_date', 'sell_price']
    [1, 'milk', 2022-10-13, 2.50]
    [2, 'bread', 2022-10-14, 3.50]
    [3, 'butter', 2022-10-15, 4.50]
]

with open('buy.csv', 'w', newline = ' ') as file:
    writer = csv.writer(file, delimiter=' ')
    writer.writerows(csv_buy_rowlist)

with open('sell.csv', 'w', newline = ' ') as file:
    writer = csv.writer(file, delimiter=' ')
    writer.writerows(csv_sell_rowlist)



if __name__ == "__main__":
    main()
