# import the tkinter module
import tkinter

# create a GUI Greeter class
class GUIGreeter:
    def __init__(self):
        # Create the main window
        self.window = tkinter.Tk()
        self.window.title("GUI Greeter")

        # Create the frames
        self.top_frame = tkinter.Frame(self.window)
        self.bottom_frame = tkinter.Frame(self.window)
    
        # Create variable to store selected language
        self.selected_language = tkinter.StringVar(value="Hello!")

        # Create the radio buttons
        self.english = tkinter.Radiobutton(self.top_frame,
                                           text='English',
                                           variable=self.selected_language,
                                           value="Hello!")
        self.french = tkinter.Radiobutton(self.top_frame,
                                           text='French',
                                           variable=self.selected_language,
                                           value="Bonjour!")
        self.spanish = tkinter.Radiobutton(self.top_frame,
                                           text='Spanish',
                                           variable=self.selected_language,
                                           value='¡Hola!')
        self.german = tkinter.Radiobutton(self.top_frame,
                                           text='German',
                                           variable=self.selected_language,
                                           value='Hallo!')

        # Pack the radio buttons
        self.english.pack(padx=100)
        self.french.pack(padx=100)
        self.spanish.pack(padx=100)
        self.german.pack(padx=100)

        # Start with English selected but no greeting
        self.english.select()

        # Create a Greet button
        self.greet_button = tkinter.Button(self.bottom_frame,
                                           text='Greet',
                                           command=self.greet)
        
        # Pack the Greet button
        self.greet_button.pack()

        # Create a label to display the greeting (empty intially)
        self.greeting_label = tkinter.Label(self.window, text="")
    
        # Pack the frames
        self.top_frame.pack(pady=20)
        self.bottom_frame.pack()
        self.greeting_label.pack(pady=20)

        # Start the main loop
        tkinter.mainloop()

    # define greet function
    def greet(self):
            # Update label with correct greeting
            self.greeting_label.config(text=str(self.selected_language.get()))

#Intro the program
print('**Johnny Moore - GUI Greeter**')
print('**CTEC 102-902**')
print('')
print('This program will create a GUI that will list options')
print('to greet you in four different languages.')
input('Press a key to run the GUI: ')

# Create an instance of the GUI Greeter class
greeter = GUIGreeter()