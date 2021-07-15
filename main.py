import tkinter
from cryptography.fernet import Fernet
from PIL import Image, ImageTk
from tkinter import messagebox

def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key named `secret.key` from the current directory.
    """
    return open("secret.key", "rb").read()

def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    return decrypted_message.decode()

generate_key()

myKey = load_key()

root = tkinter.Tk()
root.geometry('650x550')
root.title('Encrypt - CryptoText')
# root.iconbitmap('/home/morteza/python/Class/Project/cryptoText/icon.ico')
# root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='/home/morteza/python/Class/Project/cryptoText/icon.png'))
root.iconphoto(False, tkinter.PhotoImage(file='icon.png'))

def encrypt_tk():
    text_data = user_text.get('0.0', tkinter.END).strip()
    if text_data == '':
        messagebox.showerror('Error', 'Text is Empty!')
        return

    text_to_encrypt = text_data.encode()
    f = Fernet(load_key())
    encrypted_message = f.encrypt(text_to_encrypt)
    result_text.delete('0.0', tkinter.END)
    result_text.insert('0.0', encrypted_message)

def decrypt_tk():
    text_data = user_text.get('0.0', tkinter.END).strip()
    if text_data == '':
        messagebox.showerror('Error', 'Text is Empty!')
        return

    text_to_decrypt = text_data.encode()
    
    result_text.delete('0.0', tkinter.END)
    result_text.insert('0.0', decrypt_message(text_to_decrypt))



image = tkinter.PhotoImage(file='banner.png')
tkinter.Label(root, image=image).pack()



user_text = tkinter.Text(root, height=10)
user_text.pack()

buttons_frame = tkinter.Frame(root)
buttons_frame.pack()

mybtn = tkinter.Button(buttons_frame, text='Encrypt', command=encrypt_tk)
mybtn.pack(side='left', pady=5, padx=10)

mybtn = tkinter.Button(buttons_frame, text='Decrypt', command=decrypt_tk)
mybtn.pack(side='left', pady=5, padx=10)

def show_about():
    about_page = tkinter.Toplevel(root)
    about_page.title('About Program')
    about_page.geometry('500x300')
    
    about_frame = tkinter.Frame(about_page)
    about_frame.pack()

    tkinter.Label(about_frame, text='CryptoText', font='Arial 18').pack(pady=10)

    img = tkinter.PhotoImage(file='/home/morteza/python/Class/Project/cryptoText/logo-dark.png')
    tkinter.Label(about_frame, image=img).pack()

    about_text_data = """This Program make with Love in Yazd"""
    tkinter.Message(about_frame, text=about_text_data, width=500, bg='red', font='Arial 12 bold').pack(fill='x', expand=1)


    about_page.mainloop()

# Menu
mainmenu = tkinter.Menu(root)

# Add submenu
file_menu = tkinter.Menu(mainmenu, tearoff=0)
file_menu.add_command(label='About', command=show_about)
mainmenu.add_cascade(label='Help', menu=file_menu)

root.config(menu=mainmenu)

result_text = tkinter.Text(root, height=10)
result_text.pack()

root.mainloop()
# message = "message I want to encrypt".encode()
# f = Fernet(load_key())
# encrypted_message = f.encrypt(message)
# print(encrypted_message)
# decrypt_message(encrypted_message)