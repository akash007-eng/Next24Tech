import tkinter as tk
from tkinter import ttk, messagebox

def SubmitRegistrationForm():
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    gender = gender_combobox.get()
    phonenum = phonenum_entry.get()
    address = address_entry.get()

    # Validation
    if not firstname or not lastname or not phonenum or not email or not age or not gender:
        messagebox.showerror("Error", "Please ensure that you have filled in all fields")
        return
    
    if len(phonenum) != 10:
        messagebox.showerror("Error", "Phone number should be exactly 10 digits")
        return

    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for Age")
        return
    
    try:
        phonenum = int(phonenum)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid Phone Number")
        return

    # Upon Successful Validation, Display the details
    messagebox.showinfo("Success", f"!!Registration Completed!!\nFirst Name: {firstname}\nLast Name: {lastname}\nEmail: {email}\nAge: {age}\nGender: {gender}\nPhone Number: {phonenum}\nAddress: {address}")

# Creating the Main Window
window = tk.Tk()
window.title("Simple Registration Form")
window.configure(bg="lightblue")  # Set background color for the window

# Creating Labels and Entries for each field
firstname_label = tk.Label(window, text="First Name:", bg="lightgreen", font=("Courier", 15, "bold italic"))
firstname_label.pack(padx=10, pady=5, anchor=tk.W)

firstname_entry = tk.Entry(window, font=("Courier", 15, "italic"))
firstname_entry.pack(padx=10, pady=5, ipadx=20, ipady=2)


lastname_label = tk.Label(window, text="Last Name:", bg="lightgreen", font=("Courier", 15, "bold italic"))
lastname_label.pack(padx=10, pady=5, anchor=tk.W)

lastname_entry = tk.Entry(window, font=("Courier", 15, "italic"))
lastname_entry.pack(padx=10, pady=5, ipadx=20, ipady=2)


email_label = tk.Label(window, text="Email:", bg="lightgreen", font=("Courier", 15, "bold italic"))
email_label.pack(padx=10, pady=5, anchor=tk.W)

email_entry = tk.Entry(window, font=("Courier", 15, "italic"))
email_entry.pack(padx=10, pady=5, ipadx=20, ipady=2)


age_label = tk.Label(window, text="Age:", bg="lightgreen", font=("Courier", 15, "bold italic"))
age_label.pack(padx=10, pady=5, anchor=tk.W)

age_entry = tk.Entry(window, font=("Courier", 15, "italic"))
age_entry.pack(padx=10, pady=5, ipadx=20, ipady=2)


gender_label = tk.Label(window, text="Gender:", bg="lightgreen", font=("Courier", 15, "bold italic"))
gender_label.pack(padx=10, pady=5, anchor=tk.W)

gender_combobox = ttk.Combobox(window, values=["Male", "Female", "Other"], font=("Courier", 15, "italic"))
gender_combobox.pack(padx=10, pady=5, ipadx=10, ipady=2)

phonenum_label = tk.Label(window, text="Phone Number:", bg="lightgreen", font=("Courier", 15, "bold italic"))
phonenum_label.pack(padx=10, pady=5, anchor=tk.W)

phonenum_entry = tk.Entry(window, font=("Courier", 15, "italic"))
phonenum_entry.pack(padx=10, pady=5, ipadx=20, ipady=2)

address_label = tk.Label(window, text="Address:", bg="lightgreen", font=("Courier", 15, "bold italic"))
address_label.pack(padx=10, pady=5, anchor=tk.W)

address_entry = tk.Entry(window, font=("Courier", 15, "italic"))
address_entry.pack(padx=10, pady=5, ipadx=20, ipady=2)

# Creating a Submit button to click after filling all the fields
submit_button = tk.Button(window, text="Submit", command=SubmitRegistrationForm,bg="blue", font=("Courier", 15, "bold italic"))
submit_button.pack(padx=10, pady=10, fill=tk.BOTH)

# To Run The Main Event Loop
window.mainloop()
