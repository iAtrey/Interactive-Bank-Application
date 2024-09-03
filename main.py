cust_data = {}
new_user_attributes = ['Name', 'Address', 'Phone num', 'Government ID', 'Amount']
# The 'new_user()' function to add a new user to the 'cust_data' dictionary.
import random

def new_user():
  # Step 1: Create a random five-digit account number and store it in 'acc_num' variable
  acc_num = random.randint(10000,999999)   # Write your code here
  while acc_num in cust_data:
    acc_num = random.randint(10000,999999)

  # Step 2: Create an empty list and store it in the 'new_user_inputs' variable.
  new_user_inputs = []
  # Write your code here


  # Step 3: Prompting the user to enter all of their required details one-by-one and add them to the list new_user_input.
  for i in range(len(new_user_attributes)):
    user_input = input("Enter " + new_user_attributes[i] + ":\n")
    if new_user_attributes[i] == 'amount':
      new_user_inputs.append(int(user_input))
    else:
      new_user_inputs.append(user_input)

  # Step 4: Creating a dictionary for the new user and add it to the cust_data dictionary.
  cust_data[acc_num] = dict(zip(new_user_attributes, new_user_inputs))

  # Step 5: Display the message on successfull account creation to the user.
  # Write your code here
  print("Account successfully created. Your account number is ", acc_num)

def existing_user():
  # Step 1: Ask the user to enter the existing account number and store it as an integer.
  acc_num = int(input("Enter your account number"))   # Write your code here
  while acc_num not in cust_data:
    acc_num = (input("Not found. Please enter your correct account number:\n"))

  # Step 2: Print the welcome message to the user.
  # Write your code here
  print("Enter 1 to check your balance.\nEnter 2 to withdraw an amount.\nEnter 3 to deposit an amount")
  # Step 3: Asking the user to select a valid choice.
  user_choice = input()
  while user_choice not in ['1','2','3']:
    print("\nInvalid input!")
    print("Enter 1 to check your balance.\nEnter 2 to withdraw an amount.\nEnter 3 to deposit an amount.")
    user_choice = input()

  # Step 4:
  # If 'user_choice == 1' then display the account balance i.e. 'cust_data[acc_num]['amount']'
  if user_choice == '1':
    # Write your code here
    print(cust_data[acc_num]["Amount"])
  # Else if 'user_choice == 2' then subtract the withdrawal amount from the available balance.
  elif user_choice == '2':
    amt = int(input("\nEnter the amount to be withdrawn:\n"))
    if int(amt) > int(cust_data[acc_num]['Amount']):
      print("\nInsufficient balance.\nAvailable balance:", cust_data[acc_num]['Amount'])
    else:
      new_amt = int(cust_data[acc_num]['Amount']) - amt
      cust_data[acc_num]['Amount'] = new_amt
      print("\nWithdrawal successful.\nAvailable Balance:", cust_data[acc_num]['Amount'])

  # Else if 'user_choice == 3' then add the deposit amount to the available balance.
  elif user_choice == '3':
    amt = int(input("\nEnter the amount to be deposited:\n"))
    new_amt = int(cust_data[acc_num]['Amount']) + amt
    cust_data[acc_num]['Amount'] = new_amt
    print("\nDeposit successful.\nAvailable Balance:", cust_data[acc_num]['Amount'])
while True:
  valid_inputs = ['1','2','3']
  print("Welcome to the Horizon Bank!")
  print("\nEnter 1 if you are a new customer.\nEnter 2 if you are an existing customer.\nEnter 3 to terminate the application.")

  user_choice = input()
  while user_choice not in ['1','2','3']:
    print("Invalid input!")
    print("Enter 1 if you are a new customer.\nEnter 2 if you are an existing customer.\nEnter 3 to terminate the application.\n")
    user_choice = input()

  # If the user enters 1, then call the 'new_user()' function (to create a new account for the user and get their personal details).
  # Write your code here
  if user_choice == "1":
    new_user()
    break
  # Else If the user enters 2, then call the 'existing_user()' function.
  elif user_choice == "2":
    existing_user()
    break
  # Write your code here

  # Else If the user enters 3, then terminate the application with the 'Thank you, for banking with us!' message.
  elif user_choice == "3":
    print("Thank you, for banking with us!")
    break
