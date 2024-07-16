import tkinter as tk
from tkinter import messagebox


def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    
    if name != "" and phone != "":
        contact = f"{name} - {phone} - {email}"
        listbox_contacts.insert(tk.END, contact)
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Name and phone number are required.")


def delete_contact():
    try:
        selected_contact_index = listbox_contacts.curselection()[0]
        listbox_contacts.delete(selected_contact_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a contact to delete.")

root = tk.Tk()
root.title("Contact Book")


label_name = tk.Label(root, text="Name:", font="Arial 12")
label_name.grid(row=0, column=0, padx=10, pady=10)

entry_name = tk.Entry(root, font="Arial 12")
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_phone = tk.Label(root, text="Phone:", font="Arial 12")
label_phone.grid(row=1, column=0, padx=10, pady=10)

entry_phone = tk.Entry(root, font="Arial 12")
entry_phone.grid(row=1, column=1, padx=10, pady=10)

label_email = tk.Label(root, text="Email:", font="Arial 12")
label_email.grid(row=2, column=0, padx=10, pady=10)

entry_email = tk.Entry(root, font="Arial 12")
entry_email.grid(row=2, column=1, padx=10, pady=10)

button_add_contact = tk.Button(root, text="Add Contact", font="Arial 12", command=add_contact)
button_add_contact.grid(row=3, column=0, columnspan=2, pady=10)

button_delete_contact = tk.Button(root, text="Delete Contact", font="Arial 12", command=delete_contact)
button_delete_contact.grid(row=4, column=0, columnspan=2, pady=10)


listbox_contacts = tk.Listbox(root, height=10, width=50, bd=0, font="Arial 12")
listbox_contacts.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

scrollbar_contacts = tk.Scrollbar(root)
scrollbar_contacts.grid(row=5, column=2, sticky="ns")


listbox_contacts.config(yscrollcommand=scrollbar_contacts.set)
scrollbar_contacts.config(command=listbox_contacts.yview)

root.mainloop()
