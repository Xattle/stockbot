#!/usr/bin/python3

###############################ORDERSTREAM UTILITY FOR ALPACA API################################
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



#must be below arguements
args = parser.parse_args()


conn = tradeapi.stream2.StreamConn()

# Handle updates on an order you've given a Client Order ID.
# The r indicates that we're listening for a regex pattern.
client_order_id = r'my_client_order_id'
@conn.on(client_order_id)
async def on_msg(conn, channel, data):
    # Print the update to the console.
    print("Update for {}. Event: {}.".format(client_order_id, data['event']))

# Start listening for updates.
print("Now listening for updates...")
conn.run(['trade_updates', 'account_updates'])