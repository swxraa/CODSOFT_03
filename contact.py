import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Manager")

        # Create GUI components
        self.label_name = tk.Label(master, text="Name:")
        self.label_name.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_phone = tk.Label(master, text="Phone:")
        self.label_phone.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.entry_phone = tk.Entry(master)
        self.entry_phone.grid(row=1, column=1, padx=10, pady=5)

        self.label_email = tk.Label(master, text="Email:")
        self.label_email.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.entry_email = tk.Entry(master)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        self.label_address = tk.Label(master, text="Address:")
        self.label_address.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.entry_address = tk.Entry(master)
        self.entry_address.grid(row=3, column=1, padx=10, pady=5)

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.view_button = tk.Button(master, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.label_search = tk.Label(master, text="Search:")
        self.label_search.grid(row=6, column=0, sticky="w", padx=10, pady=5)
        self.entry_search = tk.Entry(master)
        self.entry_search.grid(row=6, column=1, padx=10, pady=5)

        self.search_button = tk.Button(master, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # Create contact list
        self.contacts = []

    def add_contact(self):
        # Get input from entry fields
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        # Check if required fields are not empty
        if not name or not phone:
            messagebox.showerror("Error", "Name and Phone are required fields.")
            return

        # Create a new contact object and add it to the contact list
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)

        # Clear entry fields after adding the contact
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

        messagebox.showinfo("Success", "Contact added successfully.")

    def view_contacts(self):
        # Display contacts in a new window
        view_window = tk.Toplevel(self.master)
        view_window.title("Contact List")

        # Create a text widget to display contacts
        contacts_text = tk.Text(view_window, height=10, width=40)
        contacts_text.pack(padx=10, pady=10)

        # Insert contact details into the text widget
        for contact in self.contacts:
            contacts_text.insert(tk.END, f"Name: {contact.name}\n")
            contacts_text.insert(tk.END, f"Phone: {contact.phone}\n")
            contacts_text.insert(tk.END, f"Email: {contact.email}\n")
            contacts_text.insert(tk.END, f"Address: {contact.address}\n\n")

    def search_contact(self):
        # Get search query from entry field
        query = self.entry_search.get().lower()

        # Create a list of contacts matching the search query
        matches = [contact for contact in self.contacts if query in contact.name.lower() or query in contact.phone]

        # Display search results in a new window
        search_window = tk.Toplevel(self.master)
        search_window.title("Search Results")

        # Create a text widget to display search results
        results_text = tk.Text(search_window, height=10, width=40)
        results_text.pack(padx=10, pady=10)

        # Insert search results into the text widget
        if matches:
            for contact in matches:
                results_text.insert(tk.END, f"Name: {contact.name}\n")
                results_text.insert(tk.END, f"Phone: {contact.phone}\n")
                results_text.insert(tk.END, f"Email: {contact.email}\n")
                results_text.insert(tk.END, f"Address: {contact.address}\n\n")
        else:
            results_text.insert(tk.END, "No contacts found matching the search query.")

def main():
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
