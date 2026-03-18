##Task3 Lambda Function: GST Calculator 

gst = lambda price: price+(0.18*price)
print(gst(100))

final_price = lambda price, discount =5: (gst(price)-gst(price)*discount/100)
print(final_price(100))


print(final_price(100,10))

print(final_price(200,15))



