stocks = {
    "GOOGLE": 520.54 ,
    "FB": 76.45 ,
    "YAHOO": 39.28 ,
    "AMAZON": 306.21 ,
    "APPLE": 99.76
}

# Sorts numerically
print(sorted(zip(stocks.values(), stocks.keys())))

# Sorts alphabetically
print(sorted(zip(stocks.keys(), stocks.values())))

# Grabs minimum number
print(min(zip(stocks.values(), stocks.keys())))

# Grabs maximum number
print(max(zip(stocks.values(), stocks.keys())))