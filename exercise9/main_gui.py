import tkinter as tk
from tkinter import messagebox
import logic

book = logic.PhoneBook()
displayed_contacts = []


def refresh_list(filtered=None):
    global displayed_contacts
    lst_contacts.delete(0, tk.END)

    displayed_contacts = filtered if filtered is not None else book.contact

    for cnt in displayed_contacts:
        lst_contacts.insert(tk.END, f"{cnt.name} - {cnt.phone_number}")


def btn_add_click():
    name = ent_name.get()
    phone = ent_phone.get()
    if not name or not phone:
        messagebox.showwarning("Error","please enter a name and phone number: ")    
        return
    
    try:
        book.add_contact(name , phone)
        book.save_to_csv()
        refresh_list()

        ent_name.delete(0, tk.END)
        ent_phone.delete(0, tk.END)
        messagebox.showinfo("Notice","the contact has seccessfuly saved :)")

    except ValueError as e:
        messagebox.showerror("Error" , str(e))

def btn_search_click():
    keyword = ent_search.get().lower()
    filtered = [c for c in book.contact if keyword in c.name.lower()]
    refresh_list(filtered)

def btn_delete_click():
    selected = lst_contacts.curselection()
    if not selected:
        messagebox.showwarning("Error", "please select a contact")
        return

    cnt = displayed_contacts[selected[0]]
    book.contact.remove(cnt)

    book.save_to_csv()
    refresh_list()


def btn_exit_click():
    book.save_to_csv()
    root.destroy()

def btn_load_click():
    book.load_from_csv()
    refresh_list()
    messagebox.showinfo("Notice","the file has read.")
    


#GUI


root = tk.Tk()
root.title("the master contact info")
root.geometry("500x300")


frame_top = tk.Frame(root)
frame_top.pack(pady=10) 

tk.Label(frame_top, text="name:").grid(row=0, column=0)
ent_name = tk.Entry(frame_top)
ent_name.grid(row=0, column=1, padx=5)



tk.Label(frame_top, text="Phone:").grid(row=0, column=2)
ent_phone = tk.Entry(frame_top)
ent_phone.grid(row=0, column=3, padx=5)


frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)


tk.Button(frame_buttons, text="Add Contatc", command=btn_add_click,
bg="#4CAF50", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="load file", command=btn_load_click,
bg="#FF9800", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="Delete", command=btn_delete_click).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons,text="Exit",command=btn_exit_click).pack(side=tk.LEFT, padx=5)


frame_search = tk.Frame(root)
frame_search.pack(pady=10)

tk.Label(frame_search, text="Search:").pack(side=tk.LEFT)
ent_search = tk.Entry(frame_search)
ent_search.pack(side=tk.LEFT, padx=5)
tk.Button(frame_search, text="Search", command=btn_search_click).pack(side=tk.LEFT)



tk.Label(root, text="The Contact List: ").pack(pady=(20, 0))
lst_contacts = tk.Listbox(root, width=50, height=15)
lst_contacts.pack(pady=5)



root.mainloop()