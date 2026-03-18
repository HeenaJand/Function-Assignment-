##Task5: Using Filter (): Filter Expensive Products 

price = [100,250,400,1200,50,2000,850]

greater_than_500= list(filter(lambda x:x>500,price))

less_than_equalto_500 = list(filter(lambda x: x<=500,price))

print(greater_than_500)

print(less_than_equalto_500)



