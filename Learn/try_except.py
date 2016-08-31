while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again   ")
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)