import b64
import hasher

while True:
    choice = input('''1. base64
2. 
q. quit
''').lower().strip()
    print()
    
    if choice == '1':
        # base64
        parsed = b64.inputhandler()
    
    elif choice == "2":
        # hash
        parsed = hasher.inputhandler()
    
    elif choice == 'q':
        print("quitting")
        break
    
    else:
        print("please input a valid input")
        continue
    
    print(parsed)
    print()
    

print("program exited. have a nice day!")