from colorama import init
from termcolor import colored
from pyfiglet import figlet_format as format

def color_text():
    colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')
    msg = ''
    color = 'black'
    
    while not (msg and color in colors):
        msg = input("What woud you like to print? ")
        color = input("which color? ")
    
    return colored(format(msg), color = color)


def color_text2():
    msg = ''
    
    while not msg:
        msg = input("What would you like to print? ")
        
    while True:
        color = input("Which color? ")
        
        try:
            colored(format(msg), color = color)
        except KeyError:
            print('Color unavailable.')
        else:
            break
            
    print(colored(format(msg), color = color))
   