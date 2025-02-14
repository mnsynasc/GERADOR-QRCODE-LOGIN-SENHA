try:
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import filedialog
except ImportError:
    print("Erro: O módulo 'tkinter' não está instalado ou não é suportado neste ambiente.")
    exit()

import qrcode
from PIL import Image, ImageTk

def gerar_qrcode():
    login = entry_login.get()
    senha = entry_senha.get()
    
    if not login or not senha:
        messagebox.showwarning("Erro", "Por favor, preencha o login e a senha.")
        return
    
    dados = f"{login}\t\n{senha}"
    qr = qrcode.make(dados)
    
    qr.save("qrcode.png")
    
    img = Image.open("qrcode.png")
    img = img.resize((200, 200))
    img = ImageTk.PhotoImage(img)
    
    label_qr.config(image=img)
    label_qr.image = img

def salvar_qrcode():
    filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])
    if filepath:
        qr = qrcode.make(f"{entry_login.get()}\n{entry_senha.get()}")
        qr.save(filepath)
        messagebox.showinfo("Sucesso", "QR Code salvo com sucesso!")

root = tk.Tk()
root.title("Gerador de QR Code")
root.geometry("400x450")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Login:").grid(row=0, column=0, padx=5, pady=5)
entry_login = tk.Entry(frame)
entry_login.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Senha:").grid(row=1, column=0, padx=5, pady=5)
entry_senha = tk.Entry(frame, show="*")
entry_senha.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Gerar QR Code", command=gerar_qrcode).pack(pady=10)
tk.Button(root, text="Salvar QR Code", command=salvar_qrcode).pack(pady=10)

label_qr = tk.Label(root)
label_qr.pack(pady=10)

root.mainloop()
