#formatted strings
#u wanna dynamically generate text with some variables
first='john'
last='smith'
message= first +' [' +last + '] is a coder '
print(message)
#f = formatted string prefix it
#use curly braces to dynamically insert value
msg= f'{first} [{last}] is a programmer'
print(msg)