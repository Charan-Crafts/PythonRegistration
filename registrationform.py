import tkinter as tk
from tkinter import messagebox

window=tk.Tk()
window.geometry("600x500")
window.title("Registration Form")

#Functions

def exit_application():

    window.destroy()
    print("Thanks")

def save():
    if messagebox.askokcancel(title="Save",message="Save file or Not") == True:
        with open("registerform.txt",'a+') as file:
            search_student=label1_entry.get()
            student_id_user=student_id_entry.get()
            student_name_user=student_name_entry.get()
            student_email_user=student_email_entry.get()
            student_password_user=password_entry.get()
            student_date_user=date_entry.get()
            course_input=course_var.get()
            file.write(f"Search Student Id=\t{search_student}\nStudent ID=\t{student_id_user}\nStudent Name=\t{student_name_user}\nStudent_Email=\t{student_email_user}\nStudent Password=\t{student_password_user}\nCourse=\t{course_input}\nDate=\t{student_date_user}\n---------------------------------------------------\n")

            #messagebox.showinfo(window,text="saved successfully")
    clear_application()
    
def clear_application():
    label1_entry.delete(0,tk.END)
    student_id_entry.delete(0,tk.END)
    student_name_entry.delete(0,tk.END)
    student_email_entry.delete(0,tk.END)
    password_entry.delete(0,tk.END)
    #course_var.delete(0,tk.END)
    date_entry.delete(0,tk.END)
    

#Widgets

title=tk.Label(window,text="Student Registration System",font=("bold",20),fg="White",bg="gray")

label1=tk.Label(window,text="Search Student by ID",font=("bold",15),padx=5,pady=10)

label1_entry=tk.Entry(window,width=50)

student_id=tk.Label(window,text="Student ID",font=("bold",15),padx=5,pady=10)

student_id_entry=tk.Entry(window,width=50)

student_name=tk.Label(window,text="Student Name",font=("bold",15),padx=5,pady=10)

student_name_entry=tk.Entry(window,width=50)

student_email=tk.Label(window,text="E-Mail ID",font=("bold",15),padx=5,pady=10)

student_email_entry=tk.Entry(window,width=50)

password=tk.Label(window,text="Password",font=("bold",15),padx=5,pady=10)

password_entry=tk.Entry(window,width=50,show="*")


course=tk.Label(window,text="Course",font=("bold",15),padx=5,pady=10)

date=tk.Label(window,text="Date",font=("bold",15),padx=5,pady=10)

date_entry=tk.Entry(window,width=50)




#Buttons

list1=["Python","Java","C++"]
course_var=tk.StringVar(window)
course_var.set("Select Course")
menu=tk.OptionMenu(window,course_var,*list1)
menu.config(font=("bold",10))

register=tk.Button(window,text="Register",font=("bold",15),bg="gray",command=save)

view=tk.Button(window,text="View",font=("bold",15),bg="gray")

update=tk.Button(window,text="Update",font=("bold",15),bg="gray")

delete=tk.Button(window,text="Delete",font=("bold",15),bg="gray")

clear=tk.Button(window,text="Clear",font=("bold",15),bg="gray",command=clear_application)

exit=tk.Button(window,text="Exit",font=("bold",15),bg="gray",command=exit_application)

#Button Pack
register.place(x=10,y=410)
view.place(x=120,y=410)
update.place(x=200,y=410)
delete.place(x=300,y=410)
clear.place(x=400,y=410)
exit.place(x=500,y=410)

#Packing

#title.pack()
title.grid(column=5,row=0,padx=5,pady=5)

label1.grid(column=0,row=2,padx=5,pady=5)

label1_entry.grid(column=5,row=2,padx=5,pady=5)

student_id.place(x=5,y=100)

student_id_entry.place(x=240,y=115)

student_name.place(x=5,y=150)

student_name_entry.place(x=240,y=163)

student_email.place(x=5,y=200)

student_email_entry.place(x=240,y=210)

password.place(x=5,y=250)

password_entry.place(x=240,y=265)

course.place(x=5,y=300)


menu.place(x=240,y=310,width=150)

date.place(x=5,y=350)
date_entry.place(x=240,y=365)
#student_id.grid()
#mainloop

window.mainloop()
