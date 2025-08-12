# Doigt: A Simple Autoclicker

Doigt (/dwɑ/, French for finger) is a simple, lightweight autoclicker for idle games like Cookie Clicker. It does one thing and does it well: click.

# Usage

Doigt is controlled by hotkeys and a graphical user interface (GUI).

- **Start clicking**: Press CTRL + ALT + C.

- **Stop clicking**: Press CTRL + ALT + S.

- **Adjust rate**: The clicks-per-second (CPS) can be set from 1 to 100 using the spinbox in the GUI. You can only change this rate while the program isn't clicking. Higher rates might strain older machines.

# Getting started

## Running from Source

First, make sure you have Python 3.11 and Tcl/Tk installed. Then, install the required libraries:

```bash
python3 -m pip install pynput pillow
```

Finally, run the program:

```bash
python3 main.py
```

## Building an executable

If you want a standalone program that doesn't require Python, you can use PyInstaller.

### Windows

```powershell
    pyinstaller -F --hidden-import tkinter --add-data "assets/pointer.png;assets/" --add-data "assets/github.png;assets" --icon "assets/pointer.ico" --onefile --windowed main.py -n doigt.exe
```

### Linux

```bash
    pyinstaller -F --hidden-import tkinter --add-data "assets/pointer.png:assets/" --add-data "assets/github.png:assets" --onefile --windowed main.py -n doigt
```

# Credits

- Libraries: Doigt uses [Tk](https://www.tcl-lang.org/) for its GUI and [pynput](https://pynput.readthedocs.io/en/latest/) for handling hotkeys and simulating clicks.

- Graphics: All graphics (except for the GitHub logo) were created from scratch by [Calypso](github.com/jesuiscalypso).

# License

This project is licensed under the MIT License. See the LICENSE.md file for details.
