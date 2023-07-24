print("Go calci")

n1 = float(input("Enter number: "))

op = str(input("select operation: +, -, /, *: "))

while (op in ["+", "-", "/", "*"]) == 0:
    op = str(input("select operation: +, -, /, *: "))
    

n2 = float(input("Enter next number: "))

no = 0

if op == "+":
    no = n1 + n2
elif op == "-":
    no = n1 - n2
elif op == "/":
    no = n1/n2
elif op == "*":
    no = n1*n2
else:
    no = "null"

print("Answer: ", str(no))