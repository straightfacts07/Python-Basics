#ok you want the input as a number and then after entering it the 
#output will be spelling out that number

numbers={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero"
}

phone=input("enter your phone number:")
output=""
for i in phone:
    output +=numbers.get(i,"!") + " "
print(output)

