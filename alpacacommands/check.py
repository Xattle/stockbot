#!/usr/bin/python3

##################################CHECK UTILITY FOR ALPACA API###################################
#	The following is a python3 utility for trading using Alpaca API as the trading platform.	#
#	In order to use this, you need  the proper variables set in your bashrc or bash_profile.	#
#	For   more   details,   please   read   the  API  Docs  @   https://docs.alpaca.markets/	#
#																								#
#	Things to still implement for this utility:													#
#	Arguments for:																				#
#		Checking the current value of a symbol													#
#		Checking the historic value of a symbol													#
#																								#
#################################################################################################


import alpaca_trade_api as tradeapi
import argparse
import sys

parser = argparse.ArgumentParser()
api = tradeapi.REST()


# Get our account information.
account = api.get_account()

parser.add_argument("symbol", help="The symbol you would like to check the price of.")

parser.add_argument("-bot", "--bot", help="Display all information without headers for easy use with a bot", action="store_true")

#must be below arguements
args = parser.parse_args()



