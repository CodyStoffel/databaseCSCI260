from tkinter import *
from showCourses import ShowStr
from addCourses import addCourse

def addCourse():
    global root
    #grab_set()
    print("got here")
    

    win = Toplevel(root)
    win.title("Add a Course")
    # win.pack()

    leftframe = Frame(win)
    leftframe.pack(side=LEFT)

    rightframe = Frame(win)
    rightframe.pack(side=RIGHT)

    labelCourse = Label(leftframe, text = "Course Department")
    labelCourse.pack()
    textCourse = Text(rightframe, height=1, width=30)
    textCourse.pack()
    labelNumber = Label(leftframe, text = "Course Number")
    labelNumber.pack()
    textNumber = Text(rightframe, height=1, width=30)
    textNumber.pack()
    add = Button(rightframe, text = "Add the Course")
    add.pack(padx = 3, pady = 3)
    cancel = Button(leftframe, command = win.destroy, text = "Cancel")
    cancel.pack(padx = 3, pady = 3)
    #grab_release()

root = Tk()
#root.geometry("200x150")
frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

label = Label(frame, text = "Courses Currently Scheduled")
label.pack()

add = Button(leftframe, command=addCourse, text = "Add a Course")
add.pack(padx = 3, pady = 3)
remove = Button(leftframe, text = "Remove a Course")
remove.pack(padx = 3, pady = 3)
update = Button(leftframe, text = "Update a Course")
update.pack(padx = 3, pady = 3)

text = Text(rightframe, height=20, width=30)
text.pack()
text.insert(END, ShowStr())

root.title("Test")
root.mainloop()
