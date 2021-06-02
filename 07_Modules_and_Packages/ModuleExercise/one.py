# one.py
def say_one():
    print(f"I'm in one.py")

print("Top Level in one.py")

if __name__ == "__main__":
    say_one()
else:
    print("ONE.PY has been imported.")