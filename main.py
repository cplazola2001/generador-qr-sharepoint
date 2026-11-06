import os
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
import qrcode

def generar_qr(url, nombre):

    qr = qrcode.make(url)

    ruta_final = filedialog.asksaveasfilename(
    defaultextension=".png",
    filetypes=[("Imágenes PNG", "*.png")],
    initialfile=f"{nombre}_qr.png"
    )

    if not ruta_final:
            messagebox.showinfo("Aviso", "Guardado cancelado.")
            return False

    qr.save(ruta_final)
    return True

def main():
    url = entrada_url.get()

    if not url:
        messagebox.showinfo("Aviso", "Debes ingresar un enlace para generar el código QR.")
        return

    nombre = entrada_nombre.get().strip()

    if not nombre:
        messagebox.showinfo("Aviso", "Debes ingresar un nombre para guardar tu código QR.")
        return

    resultado = generar_qr(url, nombre)

    if not resultado:
        return
    else:
        estado.config(text = f"✅ QR generado correctamente. \n Documento: {nombre}_qr.png")

ventana = tk.Tk()
ventana.title("QR - Juzgado 7 | Sharepoint v2.0")
ventana.geometry("500x300")
ventana.configure(bg = "#35374B")

titulo = tk.Label(
    ventana,
    text = "Generador de Códigos QR",
    font = ("Arial", 18),
    bg = "#35374B",
    fg = "#F5F9F9"
)

instruccion = tk.Label(
    ventana,
    text = "Ingresa un enlace",
    font = ("Arial", 11),
    bg = "#35374B",
    fg = "#D8DEF9"
)

entrada_url = ctk.CTkEntry(
    ventana,
    placeholder_text = "Pega aquí el enlace de SharePoint",
    width = 400,
    bg_color = "#35374B",
    text_color="#25283F",
    placeholder_text_color="#64748B",
    fg_color = "#D8DEF9"
)

nombre_archivo = tk.Label(
    ventana,
    text = "Nombre del archivo",
    font = ("Arial", 11),
    bg = "#35374B",
    fg = "#D8DEF9"
)

entrada_nombre = ctk.CTkEntry(
    ventana,
    placeholder_text = "Ej. Oficio_cortinas_Titi_2026",
    width = 400,
    bg_color = "#35374B",
    text_color="#25283F",
    placeholder_text_color="#64748B",
    fg_color = "#D8DEF9"
)

boton = ctk.CTkButton(
    ventana,
    text = "Generar QR",
    command = main,
    bg_color = "#35374B",
    fg_color = "#7B85FF",
)

estado = tk.Label(
    ventana,
    text = "Esperando URL...",
    bg = "#3F456C",
    fg = "#F5F9F9"
)

if __name__ == "__main__":
    titulo.pack(pady=(12, 4))
    instruccion.pack(pady=(0, 12))

    entrada_url.pack(pady=(0,12))
    nombre_archivo.pack(pady=(0,6))
    entrada_nombre.pack(pady=(0,16))

    boton.pack(pady=(20, 20))
    estado.pack()
    ventana.mainloop()