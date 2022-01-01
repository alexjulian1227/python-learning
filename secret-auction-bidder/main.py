from replit import clear
from art import logo


print(logo)
print("Welcome to the Secret Auction Program.\n\n")


bid_info = {
  "Name": 0,
}
def add_bid(name,amount):
  # new_bid = {}
  bid_info[name] = amount
  
is_run = True
while is_run:
  bid_name = input("What is your name?\n")
  bid_amount = int(input("What's your bid? \n$"))

  add_bid(name = bid_name, amount = bid_amount)
  other_bid = input("Is there any other bidder for today? Type 'yes' or 'no'\n").lower()


#loop through program
  if other_bid == "no":
    max_key = max(bid_info, key=bid_info.get)  #getting max key and value
    max_value = max(bid_info.values())
    print(f"\n\n\nThe winner is {max_key} with highest bid for today of ${max_value}")
    is_run = False
    print(f"\n\nThank you for using our program!")
  else:
    clear()
    is_run = True
