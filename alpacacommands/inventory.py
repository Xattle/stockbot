#!/usr/bin/python3

################################INVENTORY UTILITY FOR ALPACA API#################################
#	The following is a python3 utility for trading using Alpaca API as the trading platform.	#
#	In order to use this, you need  the proper variables set in your bashrc or bash_profile.	#
#	For   more   details,   please   read   the  API  Docs  @   https://docs.alpaca.markets/	#
#																								#
#	Things to still implement for this utility:													#
#	Arguments for:																				#
#		all closed, all open, closed by symbol, open by symbol									#
#		list portfolio, cancel open by symbol, cancel all open									#
#																								#
#################################################################################################

import alpaca_trade_api as tradeapi
import argparse
import sys

parser = argparse.ArgumentParser()
api = tradeapi.REST()

parser.add_argument("option1",help="Choose which inventory utility to use. Options are orders, portfolio, cancel.")
parser.add_argument("-s","--status",help="Used with list. Orders to be queried. Options are open, closed, or all. Defaults to open.", default="open")
parser.add_argument("-l", "--limit",help="Used with list. Set the max amount of orders to be queried.", default="100")
parser.add_argument("-af","--after",help="Used with list. Exclusive. Optional. Only includes orders after included timestamp.")
parser.add_argument("-un","--until",help="Used with list. Exclusive. Optional. Only includes orders submitted until the included timestamp.")
parser.add_argument("-d","--direction",help="Used with list. Chronological order of the listed orders. Options are asc or desc. Defaults to asc.",default="asc")
parser.add_argument("-bot","--bot",help="Removes all headers for use with bot.",action="store_true")
parser.add_argument("-sym","--symbol",help="Targeted stock symbol")

#must be below arguements
args = parser.parse_args()


if args.option1 == "orders":
	order=api.list_orders(
			status=args.status,
			limit=args.limit,
			after=args.after,
			until=args.until,
			direction=args.direction
		)
	#print(order)
	length = len(order)
	for i in range(length):
		print('----------------------------------------------------')
		print('Symbol:{}'.format(order[i].symbol))
		print('Qty:{}'.format(order[i].qty))
		print('Submitted:{}'.format(order[i].submitted_at))
		print('Time in Force:{}'.format(order[i].time_in_force))
		print('Type:{}'.format(order[i].type))
		print('Status:{}'.format(order[i].status))
		print('ID:{}'.format(order[i].id))
		print('----------------------------------------------------')
	
if args.option1 == "portfolio":
	flags='false'
	if args.bot:
		portfolio=api.get_position(args.symbol)
		print(portfolio)
		flags='true'
	if flags == 'true':
		sys.exit()
	portfolio=api.list_positions()
	for position in portfolio:
		print('----------------------------------------------------')
		print('Symbol:{}'.format(position.symbol))
		print('Qty:{}'.format(position.qty))
		print('Avg Entry Price:{}'.format(position.avg_entry_price))
		print('Current Price:{}'.format(position.current_price))
		print('Cost Basis:{}'.format(position.cost_basis))
		print('Current Total Value:{}'.format(position.market_value))
		print('----------------------------------------------------')
		
if args.option1 == "cancel":
	print("cancel")
	
	

"""
closed_orders = api.list_orders(
    status='closed',
    limit=100
)

open_orders = api.list_orders(
    status='open',
    limit=100
)

print(open_orders)

# Get only the closed orders for a particular stock
closed_aapl_orders = [o for o in closed_orders if o.symbol == 'AAPL']
print(closed_aapl_orders)

# Get our position in AAPL.
#aapl_position = api.get_position('AAPL')

# Get a list of all of our positions.
portfolio = api.list_positions()

# Print the quantity of shares for each position.
for position in portfolio:
    print("{} shares of {}".format(position.qty, position.symbol))"""
