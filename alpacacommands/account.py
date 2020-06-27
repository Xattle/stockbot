#!/usr/bin/python3

#################################ACCOUNT UTILITY FOR ALPACA API##################################
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
account = api.get_account()


parser.add_argument("-id", "--id", help="Display the ID for the account.", action="store_true")
parser.add_argument("-an", "--accountnumber", help="Display the Account Number for the account.", action="store_true")
parser.add_argument("-s", "--status", help="Displays the account status as shown in Alpaca Documentation.", action="store_true")
parser.add_argument("-cy", "--currency", help="Displays the Currency type for the account.", action="store_true")
parser.add_argument("-c", "--cash", help="Display the cash balance for the account.", action="store_true")
parser.add_argument("-pv", "--portfoliovalue", help="Display the Total value of cash + holding positions. Depricated = to equity.", action="store_true")
parser.add_argument("-pdt", "--patterndaytrader", help="Whether or not the account has been flagged as a pattern day trader.", action="store_true")
parser.add_argument("-tsu", "--tradesuspendedbyuser", help="User setting. If true, the account is not allowed to place orders.", action="store_true")
parser.add_argument("-tdb", "--tradingblocked", help="If true, the account is not allowed to place orders.", action="store_true")
parser.add_argument("-tfb", "--transfersblocked", help="If true, the account is not allowed to request money transfers.", action="store_true")
parser.add_argument("-ab", "--accountblocked", help="If true, the account activity by user is prohibited.", action="store_true")
parser.add_argument("-ca", "--createdat", help="Timestamp this account was created at.", action="store_true")
parser.add_argument("-se", "--shortingenabled", help="Flag to denote whether or not the account is permitted to short.", action="store_true")
parser.add_argument("-lmv", "--longmarketvalue", help="Real-time MtM value of all long positions held in the account.", action="store_true")
parser.add_argument("-smv", "--shortmarketvalue", help="Real-time MtM value of all short positions held in the account.", action="store_true")
parser.add_argument("-e", "--equity", help="Cash + long_market_value + short_market_value.", action="store_true")
parser.add_argument("-le", "--lastequity", help="Equity as of previous trading day at 16:00:00 ET.", action="store_true")
parser.add_argument("-m", "--multiplier", help="Buying power multiplier that represents account margin classification. See API Docs for details.", action="store_true")
parser.add_argument("-bp", "--buyingpower", help="Display the buying power left for the account.", action="store_true")
parser.add_argument("-im", "--initialmargin", help="Reg T initial margin requirement (continuously updated value).", action="store_true")
parser.add_argument("-mm", "--maintenancemargin", help="Maintenance margin requirement (continuously updated value).", action="store_true")
parser.add_argument("-sma", "--sma", help="Value of special memorandum account (will be used at a later date to provide additional buying_power).", action="store_true")
parser.add_argument("-dc", "--daytradecount", help="The current number of daytrades that have been made in the last 5 trading days (inclusive of today).", action="store_true")
parser.add_argument("-lmm", "--lastmaintenancemargin", help="Your maintenance margin requirement on the previous trading day.", action="store_true")
parser.add_argument("-dbp", "--daytradingbuyingpower", help="Your buying power for day trades (continuously updated value).", action="store_true")
parser.add_argument("-rbp", "--regtbuyingpower", help="Your buying power under Regulation T (your excess equity - equity minus margin value - times your margin multiplier).", action="store_true")

parser.add_argument("-bot", "--bot", help="Display all information without headers for easy use with a bot", action="store_true")


#must be below arguements
args = parser.parse_args()


flags = 'false'

def arg_function( flagval ):
	global flags
	if args.bot:
		header = ''
	else:
		header = flagval + ':'
	flagval = 'account.' + flagval
	print (header + '{}'.format(eval(flagval)))
	flags = 'true'


while True:
	if args.id:
		arg_function('id')
	if args.accountnumber:
		arg_function('account_number')
	if args.status:
		arg_function('status')
	if args.currency:
		arg_function('currency')
	if args.cash:
                arg_function('cash')
	if args.portfoliovalue:
                arg_function('portfolio_value')
	if args.patterndaytrader:
                arg_function('pattern_day_trader')
	if args.tradesuspendedbyuser:
                arg_function('trade_suspended_by_user')
	if args.tradingblocked:
                arg_function('trading_blocked')
	if args.transfersblocked:
                arg_function('transfers_blocked')
	if args.accountblocked:
                arg_function('account_blocked')
	if args.createdat:
                arg_function('created_at')
	if args.shortingenabled:
                arg_function('shorting_enabled')
	if args.longmarketvalue:
                arg_function('long_market_value')
	if args.shortmarketvalue:
                arg_function('short_market_value')
	if args.equity:
                arg_function('equity')
	if args.lastequity:
                arg_function('last_equity')
	if args.multiplier:
                arg_function('multiplier')
	if args.buyingpower:
		arg_function('buying_power')
	if args.initialmargin:
                arg_function('initial_margin')
	if args.maintenancemargin:
                arg_function('maintenance_margin')
	if args.sma:
                arg_function('sma')
	if args.daytradecount:
                arg_function('daytrade_count')
	if args.lastmaintenancemargin:
                arg_function('last_maintenance_margin')
	if args.daytradingbuyingpower:
                arg_function('daytrading_buying_power')
	if args.regtbuyingpower:
                arg_function('regt_buying_power')

	if flags == 'true':
		sys.exit()
	else:
		break

print ('{}'.format(account))
