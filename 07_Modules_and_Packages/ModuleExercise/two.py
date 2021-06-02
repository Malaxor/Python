# two.py
import one

print("Top Level in two.py")

def say_two():
    print(f"My __name__ is {__name__}")
say_two()
one.say_one()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py has been imported")