# Project 1 - TWO WHEELE FUEL CALCULATOR

distance = float(input(" Enter the total distance : "))
mileage = float(input(" Enter the vehicle mileage : "))
fuelprice= int(input(" Enter The Price of Fuel Per Litre is : "))

x = float( distance/mileage )
print(x,"litres fuel is required to cover",distance,"kms")

y = float(x*fuelprice)
print("The total cost of fuel to cover",distance,"kms is Rs",y)
