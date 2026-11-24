P = float(input("Enter principal: "))
R = float(input("Enter rate: "))
T = float(input("Enter time in years: "))

SI = (P * R * T) / 100

print("Simple Interest = ₹%.2f" % SI)
print("Total Amount = ₹%.2f" % (P + SI))
