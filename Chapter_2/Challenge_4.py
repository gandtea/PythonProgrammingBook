# Chapter 2, Challenge 4
# Write a Car Salesman program where the user enters the base price of a car. 
# The program should add on a bunch of extra fees such as tax, license, dealer prep, and destination charge. 
# Make tax and license a percent of the base price. 
# The other fees should be set values. 
# Display the actual price of the car once all the extras are applied.

base_price = int(input("What is the base price of the car? "))

tax = int(0.20 * base_price)
lic = int(0.15 * base_price)
deal_prep = 500
dest_charge = 400

print("Tax \t\t\t£", tax, "\nLicense fee \t\t£", lic, "\nDealer prep \t\t£", \
      deal_prep, "\nDestination charge \t£", dest_charge, "\nTotal \t\t\t£", \
      int(base_price+tax+lic+deal_prep+dest_charge), sep='')

input("\n\nPress the enter key to exit.")
