##Task6: Combined Utility Function 

def process_prices(prices):
    
    discounted_prices=list(map(lambda x: x-(x*10/100), prices))
    filtered_prices=list(filter(lambda x:x>300,discounted_prices))
    return discounted_prices,filtered_prices
    
    discounted_prices, filtered_prices = process_prices([100,500,900,50,750])

print("Discounted Price:",discounted_prices)
print("Filtered Price:",filtered_prices)






