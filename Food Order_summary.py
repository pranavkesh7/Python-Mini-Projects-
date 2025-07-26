#    Food Order Summary    # 


food_1 = input("Enter food item 1 : ")
price_1 = int(input("Enter Price Of Food Item 1 : "))

food_2 = input("Enter food item 2 : ")
price_2 = int(input("Enter Price Of Food Item 2 : "))

food_3= input("Enter food item 3 : ")
price_3 = int(input("Enter Price Of Food Item 3 : "))

item_1 = (food_1 , price_1)
item_2 = (food_2 , price_2)
item_3 = (food_3 , price_3)

Total_bill = price_1+price_2+price_3
print("The Total Bill Of The Food Items is : " , Total_bill)

print("Your Order Summary -")
print(item_1)
print(item_2)
print(item_3)
