#!/usr/bin/python3

###################################SELL UTILITY FOR ALPACA API###################################
#	The following is a python3 utility for trading using Alpaca API as the trading platform.	#
#	In order to use this, you need  the proper variables set in your bashrc or bash_profile.	#
#	For   more   details,   please   read   the  API  Docs  @   https://docs.alpaca.markets/	#
#																								#
#	Things to still implement for this utility:													#
#	Arguments for:																				#
#																								#
#																								#
#																								#
#################################################################################################


import alpaca_trade_api as tradeapi
import argparse
import sys

parser = argparse.ArgumentParser()
api = tradeapi.REST()


parser.add_argument("symbol", help="Ticker symbol for the buy order.")
parser.add_argument("quantity", help="The quantity of stock to buy.")
parser.add_argument("-t", "--type", help="market, limit, stop, or stop_limit. Defaults to market", default="market")
parser.add_argument("-tif", "--timeinforce", help="day, gtc, opg, cls, ioc, fok. See https://docs.alpaca.markets/trading-on-alpaca/orders/ for details. Default is gtc.", default="gtc")
parser.add_argument("-l", "--limit", help="Required if type is limit or stop_limit.")
parser.add_argument("-sp", "--stop", help="Required if type is stop or stop_limit.")
parser.add_argument("-eh", "--extendedhours", help="Sets order eligibility in premarket/afterhours to true. Only applies to type=limit and time_in_force=day.", action="store_true")


#must be below arguements
args = parser.parse_args()


# Actually sell the thing
api.submit_order(
    symbol=args.symbol,
    qty=args.quantity,
    side='sell',
    type=args.type,
    time_in_force=args.timeinforce,
	limit_price=args.limit,
	stop_price=args.stop,
	extended_hours=args.extendedhours
	)

print("{} of {} have been listed for sale!".format(args.quantity,args.symbol))
