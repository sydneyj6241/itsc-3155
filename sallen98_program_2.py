#Program 2

#Getting first number 
firstNum = int(input("Please enter first number: "))

# Getting second number
secondNum = int(input("Please enter second number: "))

result = ""

for i in range(firstNum, secondNum+1):
    # Checking if i is divisible by 7 & not 5
    if i%7== 0 and i%5 != 0:
        result += str(i)+","

result = result[:-1]

#Final Result
print(result)
