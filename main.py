#PYTHON FUNCTIONS

def my_func():
    print("The classic... Hello World!")

my_func()

def countdown():
    start = 10

    while start > 0:
        print(f"T-MINUS {start}")
        start -= 1
        if start == 0:
            print("BLAST OFF!!!")

countdown()