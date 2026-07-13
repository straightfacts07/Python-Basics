#guessing game
secret_number=9
guesses=0
guess_limit=3
while guesses<guess_limit:
    number=int(input('Guess:'))
    guesses+=1
    if number==secret_number:
      print("you won")
      break
    else:
     print("Try again")
else:
    print("oops u lost")