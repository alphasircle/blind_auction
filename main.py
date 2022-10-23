from replit import clear
from art import logo
print(logo + "\n\n\n")

print("Highest bid auction app\n")

name_bid_dictionary = {} #dictionary for storing names and bids
#takes name and bid values and stores in dictionary
def bid_dictionary(name, bid):
  name_bid_dictionary[name] = bid
#to check which bid is highest and bidder name  
highest_bid = 0
bid_winner = ""
def calculate():
  global highest_bid
  global bid_winner
  for key in name_bid_dictionary:
    if name_bid_dictionary[key] > highest_bid:
      highest_bid = name_bid_dictionary[key]
      bid_winner = key
#checks if there are more bidders and adds to dictionary, if not ends program and returns highest bid and bidder name
def more_bidders():
  is_more_users = True
  while is_more_users:
    user_input_question = input('Are there more bidders? Type "yes" or "no".\n').lower()
    if user_input_question == "yes":
      is_more_users = False
      clear()
      user_input()
    elif user_input_question == "no":
      is_more_users = False
      clear()
      calculate()
      print(f'The winner is {bid_winner} with a bid ${highest_bid}')
    else:
      clear()
      print('Wrong input. Try again.')
#takes bidder name and his bet
def user_input():
  global user_num_input
  user_name_input = input('What is your name?\n') 
  is_num_input = True
  while is_num_input:
    user_num_input = input('What is your bid?\n$')
    if user_num_input.isnumeric():
      user_num_input = int(user_num_input)
      is_num_input = False
    else:
      clear()
      print('Wrong input. Try again.')    
  bid_dictionary(name = user_name_input, bid = user_num_input)
  more_bidders()
#calls first function to start program
user_input()