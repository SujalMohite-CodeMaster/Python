started = False
stop = False

while True:
    cmd = input("> ").upper()

    if cmd == "HELP":
        print("Start - To start the car") 
        print("Stop - To stop the car")      
        print("Quit - To exit the game")   
        
    elif cmd == "START":
        if started:
            print("Car is already started... what are you doing!")
        else:
            print("Car is Started...Ready to go ")
            started = True

    elif cmd == "STOP":
        if stop:
            print("Car is already stop...what the hell are you doing man ")
        else:
            print("Car stopped...")
            stop = True

    elif cmd == "QUIT":
        print("Game over...")
        break

    else: 
        print("I don't uderstand the command...")
    


