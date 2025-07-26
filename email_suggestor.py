#                    ****** Email generator ******                    3

# Input Section
name = input("Enter your first and last name : ").split()

# Conversion Section
first_name = name [0].lower()
last_name = name [1].lower()
initial_1 = first_name[0].lower()
intial_2 = last_name[0].lower()
domain_name = "@gmail.com"
print("Here are your Suggested Emails -")

# Concatenation and printing section
email_1 = first_name+last_name+domain_name
email_2 = last_name+first_name+domain_name
email_3 = first_name+initial_1+intial_2+domain_name
email_4 = initial_1+intial_2+first_name+domain_name
email_5 = first_name+last_name+initial_1+intial_2+domain_name
print("1)",email_1)
print("2)",email_2)
print("3)",email_3)
print("4)",email_4)
print("5)",email_5)

