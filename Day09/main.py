# This program is a secret auction.

import os
from art import logo
print(logo)

# This will clear the screen so other bider can't see previous bid. Note: 'cls' will work only on Windows, on Linux change to 'clear'.
clear = lambda: os.system('clear')

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""

  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder

  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))

  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")

  if should_continue == "no":
    bidding_finished = True
    clear()
    find_highest_bidder(bids)

  elif should_continue == "yes":
    clear()