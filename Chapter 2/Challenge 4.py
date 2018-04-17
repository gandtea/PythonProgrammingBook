# Chapter 2, Challenge 4
# Car Salesman program

base_price = int(input("What is the base price of the car? "))

tax = int(0.20 * base_price)
lic = int(0.15 * base_price)
deal_prep = 500
dest_charge = 400

print("Tax \t\t\t£", tax, "\nLicense fee \t\t£", lic, "\nDealer prep \t\t£", \
      deal_prep, "\nDestination charge \t£", dest_charge, "\nTotal \t\t\t£", \
      int(base_price+tax+lic+deal_prep+dest_charge), sep='')

input("\n\nPress the enter key to exit.")
