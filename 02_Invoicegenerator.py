# Project 2 - ONLINE SHOPPING INVOICE GENERATOR *****

#User Input Section
product= str(input(" Enter the Product Name :"))
quantity= int(input(" Enter the quantity you bought :"))
price_per_item= int(input(" Enter the price per item : \u20B9 "))
gst_= int(input(" Enter the GST (%): "))
discount_= int (input(" Enter the discount (%) : "))

#Logical sectional For Calculation---

total_before_tax= quantity*price_per_item
gst_amount = int ((gst_ / 100) * total_before_tax)
discount_amount = int ((discount_ / 100) * total_before_tax)
final_amount =int (total_before_tax + gst_amount - discount_amount )

# INVOICE SECTION 

print("\n****** 📑INVOICE OF YOUR PURCHASE📑******")
print("\nProduct :         ", product )
print("Quantity :         ", quantity)
print("Price Per Item :            \u20B9", price_per_item)
print("Total Price :               \u20B9", total_before_tax)
print("Gst Amount :                \u20B9", gst_amount)
print("Discounted Amount :         \u20B9", discount_amount)
print("----------------------------------")
print("Final Price To Pay Is :     \u20B9",final_amount)
print("\n******Thanks For Shopping From Flipkart******")
print("\n")


# Print Data Types 

# print("Datatype of product name : ", type(product))
# print("Datatype of Quantity : ", type(quantity))
# print("Datatype of Price Per Item : ", type(price_per_item))



