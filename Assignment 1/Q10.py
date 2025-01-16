import sys
#10.1
if len(sys.argv)!=3:
    print("Error")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print(f"The sum of {num1} and {num2} is: {num1 + num2}")

#10.2
string=sys.argv[1]
print(len(string))
