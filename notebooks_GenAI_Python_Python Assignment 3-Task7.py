##Task7: Mini Problem: Menu Using Function 

'Add price to the list'

def add_price(price_list,price):
    price_list.append(price)

'Return Average Price '
def get_average_price(prices_list):
    return sum(prices_list)/len(prices_list)


'Returns the Maximum Price '
def get_max_price(prices_list):
    return max(prices_list)

prices=[]

while True:
    print("1:Add price")
    print("2:Show Average price")
    print("3:Show Highest price")
    print("q: Quit")
    choice=input("Enter your choice:")
    if choice =="1":
        price= float(input("Enter price"))
        add_price(prices,price)
        print("Price added Successfully")
    elif choice=="2":
        print("Average price:",get_average_price(prices))
    elif choice=="3":
        print("Highest price:",get_max_price(prices))
    elif choice=="q":
        print("Quit the program")
        break
    else:
        print("Invalid choice")
print(prices)





