#                             *****PASSWORD MASKER*****                               #

password = input("Enter Your Password : ")
valid_length = len(password)>= 9
if valid_length :
    print("Now seems strong password 🔐. ")
    masking = password[0] + "*" * (len(password)-2) + password[-1]
    print("Masked Password Is Ready 🤩 : " , masking)

else:
    print("OOPS!😫 It doesn't contains minimum 9 letters .")
    password_1 = input("Enter Your Password 🔐 : ")
    print("Now seems strong password 🔐.: ")
    masking_1 = password_1[0] + "*" * (len(password_1)-2) + password_1[-1]
    print("Masked Password Is Ready 🤩 : " , masking_1)










