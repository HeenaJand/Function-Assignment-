## Task1 Basic Functions: Price After Discount 

def apply_discount(price, discount_percent=None):
    if discount_percent is None:
        discount_percent=5
    if discount_percent >60:
       discount_percent = 60
    discounted_price= price -(price*discount_percent/100)
    return discounted_price
print(apply_discount(1000,10))
print(apply_discount(500))
 





