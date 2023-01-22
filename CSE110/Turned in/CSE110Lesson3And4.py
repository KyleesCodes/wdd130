child_meal = float(input("What is the price of a child's meal? " ))
adult_meal = float(input("What is the price of an adult's meal? "))
drink_price= float(input("What is the price of a drink? "))
appetizer_price = float(input("What is the price of an appetizer? "))

children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
drinks = int(input("How many drinks are there? "))
appetizer = int(input("How many appetizers? "))
tax = float(input("What is the sales tax rate? "))

subtotal = (child_meal * children) + (adult_meal * adults) + (drink_price * drinks) + (appetizer_price * appetizer)
print("")
print(f"Subtotal: ${subtotal:.2f}")
sales_tax = (subtotal * tax)/100
print(f"Sales Tax: ${sales_tax:.2f}")
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")
print("")

payment = float(input("What is the payment amount? "))
tip_payment = float(input("Tip percentage: "))
tip_percentage = tip_payment/100
tip = total * tip_percentage
change = payment - (total + tip)
print(f"Change: ${change:.2f}")

