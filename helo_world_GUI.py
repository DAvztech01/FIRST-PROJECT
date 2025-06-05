import tkinter as tk # I want to use the tkinter libraryt o make a window with buttons and text.
def change_text():
    label.config(text="You clicked the button!")

# Create main application window
root = tk.Tk() # Create a blank window. Call it root.
root.title("Hello App") # Set the name oof the wwindow to 'Hello App'
root.geometry("300x150") # Width x Height # Make the window size 300 pixel wide and 150 pixels tall

# Create a label widget with "Hello, world!"
label = tk.Label(root, text="Hello, World", font=("Arial, 20")) # Create a pieace of text that says 'Hello, World!' and make the text big (front size, 20).
label.pack(pady=10) # Put the label (text) in the windo and add space (40 piixels) around it.

# Create a button to change labbel text
button = tk.Button(root, text="click Me", command=change_text, font=("Arial", 16), bg="lightblue")
button.pack(pady=10)

# Run the application loop
root.mainloop() # Start the app and keep the window open until the user closes it.

