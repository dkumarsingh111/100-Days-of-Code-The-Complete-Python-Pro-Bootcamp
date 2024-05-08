import os

print("Welcome to the secret auction program!")

is_continue = "yes"
auction_record = {}
max_auction_amount = 0
winner_name = ''

while is_continue == "yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    auction_record[name] = bid

    is_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    os.system('cls||clear')
    
for name in auction_record:
    if int(auction_record[name]) > max_auction_amount:
        max_auction_amount = int(auction_record[name])
        winner_name = name

print(f"The winner is {winner_name} with a bid of ${max_auction_amount}")