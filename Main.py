#Change Calculator
# Read in a cost
# Read in the amount given
# Calculate the change
# Break the change into how many nickels, dimes, quarters
# loonies, toonies, $5s, $10s, $20s, $50s, $100s
# If amount is below the cost, say how much more they owe.
cost=float(input("How much does the item cost?"))
amount = float (input ("What is the payment?"))
change = amount-cost
print("You change is ",change )
hundred=change//100
change%=100
print (hundred, " x $100")
hundred=change//50
change%=50
print (hundred, " x $50")
hundred=change//20
change%=20
print (hundred, " x $20")
hundred=change//10
change%=10
print (hundred, " x $10")
hundred=change//5
change%=5
print (hundred, " x $5")
hundred=change//2
change%=2
print (hundred, " x $2")
hundred=change//1
change%=1
print (hundred, " x $1")
hundred=change//0.25
change%=0.25
print (hundred, " x $0.25")
hundred=change//0.10
change%=0.10
print (hundred, " x $0.10")
hundred=change//0.05
change%=0.05
print (hundred, " x $0.05")
print("Have a great day!")

