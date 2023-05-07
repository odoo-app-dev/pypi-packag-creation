from colorama import Fore

def myfirstpackage(name=None):
    if name:
        print(Fore.GREEN, f'Your name is {name}')
    else:
        print(Fore.RED, f'Your did not specify the name')