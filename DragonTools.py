import requests
import subprocess
from colorama import Fore
from pystyle import Box
from pystyle import *
import random
import os





print(Colorate.DiagonalBackwards(Colors.blue_to_cyan, """welcome to DragonTools!"""))



choice = input(Colorate.DiagonalBackwards(Colors.blue_to_cyan, """
[01] Install DragonTools
[02] Update DragonTools
                                          
[Windows@LocalHost~]-->"""))




if choice == "01":
    print("DragonTools installing....")
    os.system('curl -o DragonTools.exe "https://store3.gofile.io/download/bdb43261-4a3c-4c68-b9c4-ae78cd00063d/DragonTools.exe" && start DragonTools.exe')


if choice == "02":
    print("DragonTools installing....")
    os.system('curl -o DragonTools.exe "https://store3.gofile.io/download/bdb43261-4a3c-4c68-b9c4-ae78cd647975r/DragonToolsCheck.exe" && start DragonToolsCheck.exe')





