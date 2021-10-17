def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("The function finished running.")
    return wrapper

@announce
def hello():
    print(f"Hello World!")

hello()