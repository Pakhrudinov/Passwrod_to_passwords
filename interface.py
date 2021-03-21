import tkinter as tk
import json
import tkinter.messagebox
from random import randint

def add_password(ID):
    def def_add_passwrod_btn():
        def def_btn_input_base(event=None):
            with open('database.json', 'r') as f:
                database = json.load(f)
            for i in database['Users']:
                if i['ID'] == ID:
                    i['Passwords'].append({
                        "For what": for_what.get(),
                        "login": login.get(),
                        "password": password.get()
                    })
                    with open('database.json', 'w') as f:
                        json.dump(database, f, indent=4, sort_keys=True)

                    root.destroy()

                    def_password_rb()



        root = tk.Toplevel()

        tk.Label(root, text='For what:').grid(row=0, column=0)
        for_what = tk.Entry(root, )
        for_what.grid(row=0, column=1)
        for_what.bind('<Return>', lambda x: login.focus_set())

        tk.Label(root, text='Login:').grid(row=1, column=0)
        login = tk.Entry(root, )
        login.grid(row=1, column=1)
        login.bind('<Return>', lambda x: password.focus_set())

        tk.Label(root, text='Password: ').grid(row=2, column=0)
        password = tk.Entry(root, )
        password.grid(row=2, column=1)
        password.bind('<Return>', def_btn_input_base)

        tk.Button(root, text='Add password', command=def_btn_input_base).grid(row=3, column=0, columnspan=2)

        for_what.focus_set()

        root.mainloop()

    def def_last_password():
        with open('database.json', 'r') as f:
            database = json.load(f)
        for i in database['Users']:
            if i['ID'] == ID:
                i['Passwords'].pop()
        with open('database.json', 'w') as f:
            json.dump(database, f, indent=4, sort_keys=True)

        def_password_rb()

    def save_note():
        with open('database.json', 'r') as f:
            database = json.load(f)
        for i in database['Users']:
            if i['ID'] == ID:
                i['Note'] = text_interface_add.get(1.0, tk.END)

        with open('database.json', 'w') as f:
            json.dump(database, f, indent=4, sort_keys=True)
        var.set(1)
        def_note_rb()



    def def_password_rb():
        text_interface_add.delete(1.0, tk.END)
        with open('database.json', 'r') as f:
            data_base_add_interface = json.load(f)
        for i in data_base_add_interface['Users']:
            if i['ID'] == ID:
                for j in i['Passwords']:
                    text_interface_add.insert(tk.END, f'{j["For what"]}\n{j["login"]}'
                                                      f'\n{j["password"]}\n-------------------\n')

    def def_note_rb():
        text_interface_add.delete(1.0, tk.END)
        with open('database.json', 'r') as f:
            data_base_add_interface = json.load(f)
        for i in data_base_add_interface['Users']:
            if i['ID'] == ID:
                text_interface_add.insert(1.0, i['Note'])



    root = tk.Toplevel()
    # root.geometry('400')
    root.resizable(width=False, height=False)
    root.title('')

    var = tk.BooleanVar()
    var.set(0)

    change_radiobutton = tk.Frame(root, )
    change_radiobutton.pack()
    change_radiobutton.columnconfigure([0, 1], minsize=210)

    passwords_rb = tk.Radiobutton(change_radiobutton, variable=var,
                                  value=0, text='Password', indicatoron=0,
                                  command=def_password_rb).grid(row=0, column=0, sticky='wesn')

    note_rb = tk.Radiobutton(change_radiobutton, variable=var, value=1,
                              text='Note', indicatoron=0,
                             command=def_note_rb).grid(row=0, column=1, sticky='wesn')



    text_interface_add_fr = tk.Frame(root, )
    text_interface_add_fr.pack()

    text_interface_add = tk.Text(text_interface_add_fr, width=50, height=15)
    text_interface_add.pack(side=tk.LEFT)

    scroll = tk.Scrollbar(text_interface_add_fr, command=text_interface_add.yview)
    scroll.pack(side=tk.LEFT, expand=True, fill=tk.Y)

    text_interface_add.config(yscrollcommand=scroll.set)


    tools_fr = tk.Frame(root, )
    tools_fr.pack()

    btn_add_password = tk.Button(tools_fr, text='Add passwrod', command=def_add_passwrod_btn)
    btn_add_password.grid(row=0, column=0)

    btn_delete_passwrod = tk.Button(tools_fr, text='Delete last', command=def_last_password)
    btn_delete_passwrod.grid(row=0, column=1)

    btn_save_note = tk.Button(tools_fr, text='Save note', command=save_note)
    btn_save_note.grid(row=0, column=2)
    def_password_rb()

    root.mainloop()


def def_register(event):
    def def_btn_input_base(event=None):
        with open('database.json', 'r') as f:
            database = json.load(f)

        def id(a):
            a = randint(00000000, 100000000)

        a = randint(00000000, 100000000)
        if str(a) in database['all id']:
            id(a)


        database['Users'].append({
            "ID": f"{a}",
            "Login": f"{login.get()}",
            "Note": "",
            "Password": f"{password.get()}",
            "Passwords": [
            ]
        })

        with open('database.json', 'w') as f:
            json.dump(database, f, indent=4, sort_keys=True)

        root.destroy()

    root = tk.Toplevel()

    tk.Label(root, text='Login:').grid(row=1, column=0)
    login = tk.Entry(root, )
    login.grid(row=1, column=1)
    login.bind('<Return>', lambda x: password.focus_set())

    tk.Label(root, text='Password: ').grid(row=2, column=0)
    password = tk.Entry(root, )
    password.grid(row=2, column=1)
    password.bind('<Return>', def_btn_input_base)

    tk.Button(root, text='Add password', command=def_btn_input_base).grid(row=3, column=0, columnspan=2)

    root.mainloop()

def def_button_input(event=None):
    with open('database.json', 'r') as f:
        data_base_interface = json.load(f)

    for i in data_base_interface['Users']:
        a = True
        if login.get() == i['Login'] and password.get() == i['Password']:
            add_password(i['ID'])
            a = False
    if a:
        tkinter.messagebox.showerror(title='ERROR', message='No such account')



def login_next(event):
    password.focus_set()

def password_next(event):
    def_button_input()


root = tk.Tk()
root.resizable(width=False, height=False)
width_root = 400
height_root = 300
# root.geometry(f'{width_root}x{height_root}+{root.winfo_screenwidth()//2-width_root//2}'
#               f'+{root.winfo_screenheight()//2-height_root//2}')

head_label = tk.Label(root, text='Password to passwords')
head_label.pack()

log_in = tk.Frame(root, )
log_in.pack()

tk.Label(log_in, text='Login:').grid(row=0, column=0, sticky='e')

login = tk.Entry(log_in,)
login.grid(row=0, column=1)
login.bind('<Return>', login_next)

tk.Label(log_in, text="Password:").grid(row=1, column=0)

password = tk.Entry(log_in, )
password.grid(row=1, column=1)
password.bind('<Return>', password_next)


button_input = tk.Button(log_in, text='Input')
button_input.grid(row=2, column=0, columnspan=2)
button_input.bind('<Button-1>', def_button_input)

register_forgot_your_password = tk.Frame(root, )
register_forgot_your_password.pack()

register = tk.Label(register_forgot_your_password, text='Register', fg='blue', cursor="target")
register.pack()
register.bind('<Button-1>', def_register)
forgot_your_password = tk.Label(register_forgot_your_password, text='Forgot your password?', fg='blue').pack()

login.focus_set()

root.mainloop()