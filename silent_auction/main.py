from art import logo
import os
print(logo)
print("Welcome to the secret auction program")

new_dict={}  
any_other=False

def find_highest_bidder(record):
  highest_bid = 0
  winner = ""
  
  for i in record:
    bid_amount = int(record[i])
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = i
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not any_other:
  ask_name=input("What is your name?:")
  ask_bid=input("What is your bid?:")
  new_dict[ask_name]=ask_bid
  print(new_dict)    
    
  
  ask_for_more=input("Are there anyother bidders? Type 'yes or 'no'") 

  if ask_for_more=="no":
    any_other=True
    #adding_to_dict(ask_name,ask_bid)
    find_highest_bidder(new_dict)
  elif ask_for_more=="yes":
    os.system("cls")  
    #adding_to_dict(ask_name,ask_bid)