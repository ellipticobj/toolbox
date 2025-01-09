import base64

def encode(plain: str) -> str:
    if not plain:
        raise ValueError("variable plain cannot be empty")
    
    return str(base64.b64encode(plain.encode("utf-8")).decode("utf-8"))

def decode(enc: str, utfdecode: bool = True) -> str:
    if not enc:
        raise ValueError("variable enc cannot be empty")
    
    return str(base64.b64decode(enc).decode('utf-8')) if utfdecode else str(base64.b64decode(enc))

def inputhandler() -> str:
    print()
    while True:
        choice = input('''1. encode
2. decode
q. quit
> ''').lower().strip()
        print()
        
        if choice == '1':
            str = input("input string to encode\n> ")
            print()
            
            return encode(str)
        
        elif choice == '2':
            while True:
                str = input("input string to decode\n> ")
                
                try:
                    print()
                    return decode(str)
                except base64.binascii.Error as e:
                    print(f"{e}")
                    print()
                    continue
                except UnicodeDecodeError:
                    continueAlthoughUnicodeError = input(f"the string cannot be decoded by utf-8. return raw bytes? [y/N] ").lower()
                    if continueAlthoughUnicodeError == "y":
                        print()
                        return decode(str, False)
        
        elif choice == 'q':
            print()
            return "quit"
        
        else:
            print("please input one of the options")
            print()
            continue