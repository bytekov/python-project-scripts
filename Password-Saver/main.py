from tkinter import *
from tkinter import messagebox
import pyperclip
import json
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    # Deletes password-field content
    password_inpt.delete(0,END)

    # Uses ASCII chr code to generate a random password
    password = ''.join([chr(random.randint(48,126)) for _ in range(0,8)])
    password_inpt.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    # Get all data input
    web_name = webname_inpt.get()
    item_mail = mail_inpt.get()
    item_pass = password_inpt.get()
    new_item = {
        web_name :{
          "email": item_mail,
          "password":item_pass
        }
    }

    try:
        # Checks for unfilled entries
        if len(item_pass) == 0 or len(web_name) == 0 or len(item_mail) == 0:
            raise ValueError('Empty entry')
        # Check for unfilled entries
    except ValueError:
        messagebox.showinfo('Error','You have unfilled fields in the form!')

    else:
        try:
            # Checks for unexistent json-file
            with open('password.json', 'r') as file:
                current_data = json.load(file)

        except FileNotFoundError or ValueError:
            # Create a new json and dumps new item if no file
            with open('password.json','w') as file:
                json.dump(new_item,file,indent=4)  

        else:
            # Reads, updates and write new data into json file
            with open('password.json', 'r') as file:
                current_data = json.load(file)
                current_data.update(new_item)

            with open('password.json' , 'w') as filr:
                json.dump(current_data,filr,indent=4)  
        finally:     
            # Sends data into clipboard      
            pyperclip.copy(item_pass)
            password_inpt.delete(0,END)
            webname_inpt.delete(0,END)

def search_func():
    # Get data
    search_term = webname_inpt.get()
    try:
        with open('password.json' ,'r') as file:
            inbound = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("Error" , f"Datafile not found")
    else:
        try:
            info_data = inbound[search_term]
        except KeyError:
            messagebox.showinfo("Error" , f"Search data \"{search_term}\" not found")
        else:
            messagebox.showinfo(search_term,f'Email: {info_data["email"]}\n\nPassword: {info_data["password"]}')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
app_image = PhotoImage(file = 'logo.png')
app_canv = Canvas(width=200 , height=200)
app_canv.create_image(100,100 , image=app_image)
app_canv.grid(row=0,column=1)

webname_txt = Label(window,text="Website Name:")
webname_txt.grid(row=1,column=0)
mail_txt = Label(window,text="Email:")
mail_txt.grid(row=2,column=0)
pass_txt = Label(window,text="Password:")
pass_txt.grid(row=3,column=0)

webname_inpt = Entry(window,width=55)
webname_inpt.grid(row=1,column=1,columnspan=2)
webname_inpt.focus()
mail_inpt = Entry(window,width=55)
mail_inpt.grid(row=2,column=1,columnspan=2)
mail_inpt.insert(END,"gamma@gmail.com")
password_inpt = Entry(window,width=36)
password_inpt.grid(row=3,column=1)

search_btn = Button(window,text="Search",width=15,command=search_func)
search_btn.grid(row=1,column=2)

gen_btn = Button(window,text="Generate Password",command=gen_pass)
gen_btn.grid(row=3,column=2)

save_btn = Button(window,width=46, text="Add Item", command=add_data)
save_btn.grid(row=4,column=1 , columnspan=2)

window.mainloop()