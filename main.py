# ------ libs ------ #
import os
from pystyle import *

# ------ setup ------ #  

banner_1 = Center.XCenter("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n")
banner_2 = Center.XCenter("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n")
banner_3 = Center.XCenter("▓▓░░░░░▓▓░░▓░░░▓▓▓░░░▓▓▓░░░▓▓▓▓▓▓░▓░░░▓▓▓▓▓▓░░░▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓▓▓\n")
banner_4 = Center.XCenter("▓░░░▓▓▓▓▓░░▓▓░░░▓▓▓░░░▓░░░▓▓▓▓▓▓░░▓░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓░░▓░░░▓▓▓\n")
banner_5 = Center.XCenter("▓▓▓░░░░▓▓░░▓▓▓░░░▓▓▓▓░░░░▓▓▓▓▓░░░▓▓░░░▓▓▓▓░░░▓▓▓▓▓▓░░░▓▓▓░░░▓▓░░░▓▓▓\n")
banner_6 = Center.XCenter("▓▓▓▓▓░░░▓░░░▓░░░▓▓▓▓▓▓░░░▓▓▓░░░░░░▓░░░░░░▓▓░░░▓▓▓▓░░░▓▓░░░░░░▓░░░░░░\n")
banner_7 = Center.XCenter("▓░░░░░░▓▓░░░▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓\n")
banner_8 = Center.XCenter("▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n")

os.system("cls" if os.name == "nt" else "clear")
Write.Print(banner_1 + "\n", Colors.rainbow, interval = 0.000000009)
Write.Print(banner_2 + "\n", Colors.rainbow, interval = 0.000000009)
Write.Print(banner_3 + "\n", Colors.rainbow, interval = 0.000000009)
Write.Print(banner_4 + "\n", Colors.rainbow, interval = 0.000000009)
Write.Print(banner_5 + "\n", Colors.rainbow, interval = 0.000000009)
Write.Print(banner_6 + "\n", Colors.rainbow, interval = 0.000000009)
Write.Print(banner_7 + "\n", Colors.rainbow, interval = 0.000000009)
Write.Print(banner_8 + "\n", Colors.rainbow, interval = 0.000000009)
location = Write.Input("Project location -> ", Colors.rainbow, interval = 0.000000009)
name = Write.Input("Env name -> ", Colors.rainbow, interval = 0.000000009)
Write.Print("Creating...", Colors.rainbow, interval = 0.000000009)
os.system(f"python -m venv {location}\{name}")
Write.Print("Done!", Colors.rainbow, interval = 0.000000009)
