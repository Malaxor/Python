# one.py
def func():
   print("func() in one.py")

print("Top Level in one.py")

if __name__ == "__main__":
   print("ONE.PY is being run directly")
else:
   print("ONE.PY has been imported.")