from yahoo_fin.stock_info import *
import cufflinks as cf
import pandas as pd
list = []
list_len = []
total_investment = []
list_profit_loss = []
stocks2 = [['AMD', 1, 75.65]]
for values in range(0, len(stocks2)):
    list_len = list_len + [len(stocks2[values])]
print('Ticker,  Current_Price,   1y_target,      Day_range,         P/E,      #Stocks,    price_purchased,   total_spent,  Profit/Loss ')
stock_name = [item[0] for item in stocks2]
num_of_stocks = [item[1] for item in stocks2]
purchase_price = [item[2] for item in stocks2]
for item in range(0, len(stock_name)):
    details = get_quote_table(stock_name[item])
    price = round(details["Quote Price"], 3)
    year_estimate = details["1y Target Est"]
    year_estimate = int(year_estimate)
    #fifty_two_week_range = details["52 Week Range"]
    #Vol = details["Volume"]
    Day_range = details["Day's Range"]
    PE_ratio = details["PE Ratio (TTM)"]
    profit_loss = round((price - purchase_price[item])*num_of_stocks[item], 3)
    #Market_Cap = details["Market Cap"]
    total_investment_price_per_stock = purchase_price[item] * num_of_stocks[item]
    total_investment = total_investment + [total_investment_price_per_stock]
    list_profit_loss = list_profit_loss + [profit_loss]
    list = list + [(stock_name[item], get_live_price(stock_name[item]), year_estimate, Day_range, PE_ratio,
                    num_of_stocks[item], purchase_price[item], total_investment_price_per_stock, profit_loss)]

for i in range(len(list)):
    print('{:<10s}{:^10.1f}{:^20.1f}{:^15s}{:^17.1f}{:^8.1f}{:^18.1f}{:^18.1f}{:^15.1f}'.format(list[i][0], list[i][1],
                                    list[i][2], list[i][3], list[i][4], list[i][5], list[i][6], list[i][7], list[i][8]))
total_investment = round(float(sum(total_investment)), 3)
list_profit_loss = round(float(sum(list_profit_loss)), 3)
current_value = total_investment + list_profit_loss
print("Total Investment = ", total_investment)
print("Net profit/Loss = ", list_profit_loss)
print("Current_Value = ", current_value)
