def reverse(data: str) -> str:
    return ''.join([i for _, i in enumerate(data)][::-1])

def inputhandler() -> str:
    print()
    choice = input('''input string to reverse (q to quit)
> ''').lower().strip()
    print()
    
    if choice == 'q':
        return "quit"
    else:
        return reverse(choice)