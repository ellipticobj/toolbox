import hashlib

def md5(data: str) -> str:
    return hashlib.md5(data.encode()).hexdigest()

def sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def sha1(data: str) -> str:
    return hashlib.sha1(data.encode()).hexdigest()

def blake2(data: str) -> str:
    return hashlib.blake2b(data.encode()).hexdigest()

def ripemd160(data: str) -> str:
    return hashlib.new("ripemd160", data.encode()).hexdigest()

def inputhandler() -> str:
    print()
    while True:
        choice = input('''1. md5
2. sha256
3. sha1
4. blake2
5. ripemd160
q. quit
> ''')
        print()
        if choice != 'q':
            data = input("input string to hash: ")
        
        if choice == "1": return md5(data)
        elif choice == "2": return sha256(data)
        elif choice == "3": return sha1(data)
        elif choice == "4": return blake2(data)
        elif choice == "5": return ripemd160(data)
        elif choice == "q": return "quit"
        else:
            print("please input a proper input")
            print()
            continue