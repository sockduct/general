################################################################################
#
# GUI Programming with Tkinter (TK)
#
# 1) Setup widgets (graphical elements - button, scroll bar, check box, etc.
#    Use labels to display information, input to collect information
#    (e.g., buttons)
# 2) Use layout features to place widgets in main window display
# 3) Handle events (keyboard input, mouse movement/button presses, etc.
# 4) Main loop to continue waiting for user input as long as built widget
#    window exists (if it's closed, exit)
# 
################################################################################
#
# Imports
#from Tkinter import *
import Tkinter as tk

# Create main window for this program
root = tk.Tk()
# Create a label (widget) for our window
l = tk.Label(text="Hello World",font=("Helvetica",20))
# Call pack method for layout (place widget in main window)
# Tkinter has 3 layout methods - pack, grid and place
l.pack()
# Create a button widget for our window, link button press
# to sys.exit() function, but don't pass function with ()
# as this would execute it instead of passing a reference to it
b=tk.Button(text="Kill Me",command=tk.sys.exit)
# Again, call pack to add to layout
b.pack()
# Set event monitoring loop in motion
root.mainloop()

