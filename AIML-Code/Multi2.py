import os

def main():
    print("PID of current process is :",os.getpid())
    print("PID of Parent process is :",os.getppid())

if __name__=="_main__":
    main()