#simulation of a car game
#we build the engine
command=""
store=""
while True:
  command=input(">").lower()
  if command=="start":
      if(store=="start"):
           print("car has already started..")
      else:
          print("car started..")
  elif command=="stop":
      if(store=="stop"):
           print("car has already stopped..")
      else:
          print("car stopped..")
  elif command=="help":
      print("""
start- to start the car
stop - to stop the car
quit- to quit
            """)  
  elif command=="quit":
      break
  else:
      print("sorry i dont understand....")
  store=command   

    