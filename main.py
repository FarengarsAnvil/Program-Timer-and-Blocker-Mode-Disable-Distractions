import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter.ttk import *
import os
import psutil


#Initialises the Blocker Mode GUI Window with all the Requisite widgets aand closes the Main() ProgramTimer GUI Window
def blockMode():
    window.destroy()
    global Window2
    runningState = True
    Window2 = Tk()
    Window2.geometry("500x510")
    Window2.title("Blocker Mode: Disable Distractions")
    messagebox.showinfo("Usage", "Blocker mode is used to disable processes and applications from running by killing them automatically."
                                 "\n"
                                 "\nChoose the programs you want to disable, and then press start button."
                                 "\n"
                                 "\nBlocker mode is ended by closing the application.\nThen you can resume usage of the Programs that were blocked."
                                 "\n"
                                 "\nBlocker mode also resets on close, so you have to re-add the programs you want to disable everytime for now.")
    start = Button(Window2, text ="Start Blocker", command = startBlock).pack(pady = 35)
    selectButton = Button(Window2,text ="Choose Applications to disable:",command = blockFile).pack()
    Window2.mainloop()




#startButton onclick Function that starts the Blocker mode after having selected a program.
def startBlock():
      try:
         for process in psutil.process_iter():
             if process.name() in fileList:
               process.kill()
         Window2.after(1000, startBlock)

      except psutil.NoSuchProcess:
        Window2.after(1000, startBlock)
      except NameError:
        pass

#fetches the Program or Processes name in a string from the Filemenu and appends it to an List called fileList
def blockFile():
    global fileList
    fileList = []
    #fileList list holds the names of the Program .exe's.
    while True:
        global file
        filepath = askopenfilename(initialdir="C:\\Program Files", title="Select File")
        checker = [".exe"]
        # Checker array used to check if the Program selected is an .exe.
        # if File isn't an exe then it will loop back to FileMenu.
        file = os.path.basename(filepath)
        if filepath == "":
            break
            #If the user presses Cancel in filemenu it will return to Main GUI Window
        if any([x in file for x in checker]):
            fileList.append(file)
            messagebox.showinfo("Program Selected", "You have added " + file + " to blocklist")
            print(fileList)
            #Checks Program is an .exe and adds it to the fileList Array if so.
        else:
            messageTwo()


#Main GUI Window for progTimer application, Contains all the GUI Widgets: Buttons etc.
#Global variables are declared for the purpose of Widgets being functional and updating.
def main():
    global window
    global programTime
    global progress
    window = Tk()
    window.geometry("500x510")
    window.title("Program Timer")

    programTime = tkinter.IntVar()
    menubar = Menu(window)
    window.config(menu=menubar)
    optionMenu = Menu(menubar, tearoff=0, font=("Helvetica", 10))
    menubar.add_cascade(label="Options", menu=optionMenu)
    optionMenu.add_command(label="Switch to Block Mode", command=blockMode)
    optionMenu.add_separator()
    optionMenu.add_command(label="Help", command=displayHelp)
    optionMenu.add_separator()
    optionMenu.add_command(label="Exit", command=exitProg)

    # Buttons, Label Widgets, Entry widgets all Below
    startButton = Button(window, text="Start Timer", command=start).pack(side=TOP, pady=25)
    programButton = Button(window, text="Select Program:", command=openfile).pack(side=TOP)
    timerPrompt = Label(window, text="Enter Timer Duration:", font=("Helvetica", 10)).pack(pady=15)
    timeEntry = Entry(window, width=25, textvariable=programTime).pack()
    submitButton = Button(window, text="Confirm Timer", command=submit).pack(pady= 15)
    progress = DoubleVar()
    progressBar = Progressbar(window, orient = HORIZONTAL,  mode ="determinate", variable =progress).pack(pady = 15)
    #Progress Variable is reposnible for updating the Progressbar as time goes on.
    window.mainloop()



#Option menu exit function.
def exitProg():
    exit()

# Message 1 for the Help button Menubar. Info on how buttons work.
def messageOne():
    messagebox.showinfo("Help",
                        "You must enter the timer amount in the Textbox, and then press the Submit timer button in order for timer to function. This can be done before or After choosing a Program.")

# Message 2 for the Help button Menubar: Regarding filetype
def messageTwo():
    messagebox.showinfo("Help",
                        "When selecting a program it must be of the Filetype .exe Executable. ")

# Message 3 is about the Timer input, The number entered in textbox is the Number of MINUTES UNTIL PROGRAM ENDS.
def messageThree():
    messagebox.showinfo("Help",
                        "The Number you enter into the textbox is the number of Minutes until the Program is timed to Close.")


#Calls all 3 messages when the user clicks on the Help button in the options menu.
def displayHelp():
    messageOne()
    messageTwo()
    messageThree()


#Onclick function for the start button that starts the timer, and is responsible for progressBar updating.
def start():
   try:
    global progress
    global counter
    if counter ==timeInput:
      os.system("TASKKILL /F /IM " + file)
      messagebox.showinfo("Success", "Specified program has ended")
    else:
        progress.set((counter / timeInput) * 100)
        counter = counter + 1
        window.after(1000, start)
   except NameError:
       messagebox.showinfo("Info", "You must submit a timer and choose a Program before starting.")


#Grabs the value the user enters in the entrybox for the timer duration.
def submit():
    global counter
    minuteToSecond = 60
    counter = 0
    global timeInput
    timeInput = programTime.get() * minuteToSecond
    if programTime.get() < 1:
        messagebox.showerror("Error", "Please enter a number of minutes greater than or equal to 1 Minute.")

def openfile():
    # function opens the filemenu so the user can choose the program .exe to kill.
    # while loop used to ensure only exe's  are accepted to be terminated
    # File variable strips filepath head and holds File name with it's type
    while True:
        global file
        filepath = askopenfilename(initialdir="C:\\Program Files", title="Select File")
        checker = [".exe"]
        # Checker array used to check if the Program selected is an .exe
        # if File isn't an exe then it will loop back to FileMenu
        file = os.path.basename(filepath)
        if filepath == "":
            break
        if any([x in file for x in checker]):
            messagebox.showinfo("Program Selected", "You have selected " + file)
            break

        else:
            messageTwo()

#Calls the main GUI Window
main()

