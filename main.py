from replit import clear
from art import logo

print(logo)

bidder_dictionary = {}
bidding_finished = False

def highest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The highest bidder is {winner} with amount {highest_bid}")
  
while not bidding_finished:
  name = input("What is your name? .\n")
  bid = eval(input("What is your bid? R"))

  bidder_dictionary[name] = bid
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
  if other_bidders == "no":
    bidding_finished = True
    clear()
    highest_bidder(bidder_dictionary)
  else:
    clear()



