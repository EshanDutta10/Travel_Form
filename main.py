# we will be using the form we did in user input and storing the contents in a new file

from tkinter import *


def submit_form():
    win = Toplevel(root)
    win.title("Success!")
    Label(win, text="Your response has been submitted to our servers!\nWe will contact you shortly", bg="yellow").pack()
    Label(win, text="For more queries contact us on: xyz@gmail.com").pack()

    with open("response.txt","a") as file:
        i = int(1)
        if(food_var==0):
            food_response="no"
        else:
            food_response="yes"

        file.write(f"\n\nName: {name_var.get()}\nContact: {contact_var.get()}\nEmail: {email_var.get()}\nGender: {gender_var.get()}"
                   f"\nEmergency Contact: {altcontact_var.get()}\nFood: {food_response}\n\n ")
        i += 1


root = Tk()
root.geometry("450x350")
root.title("Travel Form")

Label(root, text="Travel Form Enquiry", font="comicsansms 15 bold").grid(row=0, column=3, pady=5)

Label(root, text="Name", font="comicsansms 10 ").grid(row=1, column=2, pady=5)
Label(root, text="Contact", font="comicsansms 10 ").grid(row=2, column=2, pady=5)
Label(root, text="Email", font="comicsansms 10 ").grid(row=3, column=2, pady=5)
Label(root, text="Gender", font="comicsansms 10 ").grid(row=4, column=2, pady=5)
Label(root, text="Alternate Contact", font="comicsansms 10 ").grid(row=5, column=2, pady=5)


name_var = StringVar()
contact_var = StringVar()
email_var = StringVar()
gender_var = StringVar()
altcontact_var = StringVar()
food_var = IntVar()

name_entry = Entry(root, textvariable=name_var).grid(row=1, column=3)
contact_entry = Entry(root, textvariable=contact_var).grid(row=2, column=3)
email_entry = Entry(root, textvariable=email_var).grid(row=3, column=3)
gender_entry = Entry(root, textvariable=gender_var).grid(row=4, column=3)
altcontact_entry = Entry(root, textvariable=altcontact_var).grid(row=5, column=3)
Checkbutton(text="Do you want to pre-book your meals?", variable=food_var).grid(row=6, column=3)

Button(text="Submit", command=submit_form).grid(column=3)


root.mainloop()
