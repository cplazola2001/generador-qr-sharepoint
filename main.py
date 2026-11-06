import os
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
import qrcode

def seleccionar_pdf():
    filetypes = [("Documentos PDF", "*.pdf")]
    pdf = filedialog.askopenfilename(filetypes=filetypes)

    if pdf:
        ruta = os.path.basename(pdf)
        nombre = os.path.splitext(ruta)
        nombre_archivo = nombre[0]
        carpeta_guardado = os.path.dirname(pdf)
        return pdf, nombre_archivo, carpeta_guardado
    else:
        return None

def generar_qr(pdf, nombre_archivo, carpeta_guardado):

    qr = qrcode.make(pdf)

    ruta_final = os.path.join(carpeta_guardado, f"{nombre_archivo}_qr.png")

    qr.save(ruta_final)

def main():
    resultado = seleccionar_pdf()

    if not resultado:
        messagebox.showinfo("Aviso", "El usuario canceló. Intentar de nuevo.")
        return

    pdf, nombre_archivo, carpeta_guardado = resultado

    try:
        generar_qr(pdf, nombre_archivo, carpeta_guardado)

    except PermissionError:
        messagebox.showerror("Error", "No puedes guardar tu QR aquí. Asegúrate de tener tu PDF en una ubicación segura.")
        return

    estado.config(text = f"✅ QR generado correctamente. \n Documento: {nombre_archivo}")

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
    text = "Selecciona un documento PDF para generar su código QR.",
    font = ("Arial", 12),
    bg = "#35374B",
    fg = "#D8DEF9"
)

boton = ctk.CTkButton(
    ventana,
    text = "Seleccionar PDF",
    command = main,
    bg_color = "#35374B",
    fg_color = "#7B85FF",
)

estado = tk.Label(
    ventana,
    text = "Esperando documento...",
    bg = "#3F456C",
    fg = "#F5F9F9"
)

if __name__ == "__main__":
    titulo.pack()
    instruccion.pack()
    boton.pack(pady=80)
    estado.pack()
    ventana.mainloop()