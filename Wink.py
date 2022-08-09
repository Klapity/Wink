import rich, sys
from rich import table
from colorama import *
import os
from rich.traceback import install
from rich.markdown import Markdown
import keyboard
import win32gui, win32con
import readline
init()

for i in range(100):
    keyboard.press_and_release('ctrl+shift+plus')
for i in range(2):
    keyboard.press_and_release('ctrl+shift+-')
def pinput(prompt, text):
    def hook():
        readline.insert_text(text)
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    result = input(prompt)
    readline.set_pre_input_hook()
    return result

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)


install()

file = sys.argv[1]
lines = open(file).read()
keyboard.press_and_release("f11")
os.system("cls")


# Make a table and add the file content to it
table = table.Table(show_header=True, header_style="bold blue")
table.add_column(f"{file}", justify="center", style="bright")
table.add_row(f"{lines}", style="bold cyan")

rich.print(table)

# Get input from the user
print(f"{Fore.LIGHTBLUE_EX}[{Fore.WHITE}?{Fore.LIGHTBLUE_EX}]{Fore.WHITE} Is this the correct file? (y/n): {Fore.WHITE}", end="")
correct = input()

if "y" in correct.lower():
    while True:
        os.system("cls")
        text=f"""# {Fore.LIGHTBLUE_EX}Wink{Fore.WHITE} : {Fore.LIGHTBLUE_EX}{file}"""
        console = rich.console.Console()
        md = Markdown(text)
        console.print(md, style="bold cyan", highlight=True)
        print("")
        lineNum = 0
        lines = open(file).readlines()
        for line in lines:
            lineNum +=1
            rich.print(str(lineNum) + " > " + line.removesuffix("\n"))
        print(f"{Fore.LIGHTBLUE_EX}{lineNum+1}{Fore.WHITE} > ", end="")
        line = input()
        
        if line.startswith(".dl"):
            try:
                lines.remove(lines[-1])
            except Exception:
                pass
        
        elif line.startswith(".d"):
            try:
                lines.remove(lines[int(line.split()[1]) - 1])
            except Exception:
                pass
        
        elif line.startswith(".r"):
            try:
                lineList = line.split()
                lineChange = int(lineList[1])
                text = pinput(f"{Fore.LIGHTBLUE_EX}{lineChange}{Fore.WHITE} > ", lines[lineChange - 1].removesuffix("\n"))
                lines[lineChange - 1] = text + "\n"
            except Exception:
                pass
        
        elif line.startswith(".a"):
            try:
                lineList = line.split()
                lineChange = int(lineList[1])
                text = pinput(f"{Fore.LIGHTBLUE_EX}{lineChange}{Fore.WHITE} > ", "")
                lines.insert(lineChange, text + "\n")
            except Exception:
                pass
        
        elif line.startswith(".clear"):
            try:
                lines.clear()
            except Exception:
                pass
        
        elif line.startswith(".execute"):
            os.system("cls")
            linesRun = ""
            linesToAdd = str(lines).strip("[]").replace("'", "").replace("\\n", "\n").replace(", ", "")
            linesRun += linesToAdd
            exec(linesRun)
            print(f"{Fore.LIGHTBLUE_EX}[{Fore.WHITE}!{Fore.LIGHTBLUE_EX}]{Fore.WHITE} Executed {Fore.LIGHTBLUE_EX}{file}{Fore.LIGHTBLACK_EX}\nPress Enter To Go Back To Editing...", end="")
            input()

        elif line.startswith(".exit"):
            break
        
        else:
            lines.append(line + "\n")
        with open(file, "w") as f:
            f.writelines(lines)
            
        
        
