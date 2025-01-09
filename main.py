import b64
import hasher
import reverse


while True:
    choice = input('''1. reverse
2. base64
3. hash
q. quit
> ''').lower().strip()
    
    if choice == "1":
        # reverse
        parsed = reverse.inputhandler()
    
    elif choice == '2':
        # base64
        parsed = b64.inputhandler()
    
    elif choice == "3":
        # hash
        parsed = hasher.inputhandler()
    
    elif choice == 'q':
        print("quitting")
        break
    
    else:
        print("please input a valid input")
        continue
    
    if parsed == "quit":
        print()
        print("quit")
        continue
    else:
        print()
        print(f"output:\n{parsed}")
        print()
    

print("program exited. have a nice day!")