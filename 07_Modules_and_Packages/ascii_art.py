from colorama import init
from termcolor import colored
from pyfiglet import figlet_format as format

init()
colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')

msg = input("what would you like to print? ")
if not msg:
   msg = 'Spring'

color = input("what color? ") 

try: 
   result = colored(format(msg), color = color)
   print(result)
except KeyError:
   print(colored(format(msg), color = 'green'))