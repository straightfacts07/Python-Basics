#small reusable code = function
#always define function first and then call it

#print functin takes some info
#we will also use parameters
#f= formatted string

def greet_user(first_name,last_name):
    
    print(f'hi {first_name} {last_name}')
    print('welcome aboard')


#parameter=in function i.e - name
#argument= what we pass whem we called the function i.e john,mary
print("start ")
greet_user("john","smith") #it will always need  argument
greet_user("mary","jane")
print("finish")
#when mixing positional and keyword argument
#one should always define positionsla argument first
#we have keyword arguments
#we dont have to worry about the positions
greet_user(last_name="smith",first_name="john")


