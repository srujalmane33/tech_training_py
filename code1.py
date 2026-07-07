# x = 5
# total= 0
# for i in range(1 ,x+1):
#     total = total+i
# print(total)



# def sum_for_loop(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total

# n = 5
# print(f"The sum of first {n} numbers is {sum_for_loop(n)}")


# num= "32"
# numFlaot = float(num)
# print("the float data is ",numFlaot," and the type of data is ",type(numFlaot))

# account_balance = int(input("Enter your current account balance: "))
# withdrawal_amount = int(input("Enter the amount to withdraw: "))

# if withdrawal_amount > account_balance:
#     print("Insufficient funds. Transaction declined.")
# else:
#     account_balance -= withdrawal_amount
#     print(f"Withdrawal successful. New account balance: {account_balance}")

username = "shreyash"
password ="123123"


Loginusername= str(input("Enter your username : "))
Loginpassword= str(input("Enter your password : "))


if Loginusername == username and Loginpassword == password:
    print("Login successful!")
else:
    print("Invalid username or password. Please try again.")