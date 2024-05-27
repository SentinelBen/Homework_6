from colorama import init, Back, Style
from art import *

init(autoreset=True)

print(Back.GREEN + "This is a sample text with a green background")

with open("requirements.txt", "w") as f:
    f.write("art\n")
    f.write("colorama\n")