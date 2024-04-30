from tkinter import Menu
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext




class VentanaPrincipal:
    def on_enter(self, event):
        event.widget.config(bg="grey")

    def on_leave(self, event):
        event.widget.config(bg="#142157")
    
    def __init__(self, root):
        # Variables que se analizan
        # Ventana principal
        self.root = root
        self.root.title("Proyecto #2 - 202201336")
        self.root.geometry("625x650")
        self.root.configure(bg="white")
        self.root.resizable(0   ,0)
        # Frame principal
        titulo_frame = tk.Frame(root, bg="#142157")
        # Titulo label
        label_titulo = tk.Label(titulo_frame, text="Proyecto 2 Lenguajes Formales")
        label_titulo.config(font=("Arial", 16), bg="#142157", fg="white")
        label_titulo.pack(fill='both', expand= True)
        # Configuración del frame
        titulo_frame.place(x=0, y=0,)
        titulo_frame.config(width=625, height=50)
        titulo_frame.pack_propagate(0)
        # Frame de botones
        opciones_frame = tk.Frame(root, bg="#4A6EB0")
        # Botones
        boton_archivo = tk.Menubutton(opciones_frame, text="Archivo", bg="#142157", font=("Arial", 12), bd=0, fg="white", activeforeground='black')
        boton_archivo.place(x=10, y=10, width=150, height=30)
        # Opciones del boton archivo
        opciones=Menu(boton_archivo, tearoff=0)
        boton_archivo["menu"]=opciones
        opciones.add_command(label="Nuevo", font=("Arial", 12), activeforeground='black', command=self.abrir_archivo)
        opciones.add_command(label="Abrir", font=("Arial", 12), activeforeground='black', command=self.salir)
        opciones.add_command(label="Guardar", font=("Arial", 12), activeforeground='black', command=self.salir)
        opciones.add_command(label="Guardar Como", font=("Arial", 12), activeforeground='black', command=self.salir)               
        opciones.add_command(label="Salir", font=("Arial", 12), activeforeground='black', command=self.salir)      
        
        # Boton analisis
        boton_analisis = tk.Menubutton(opciones_frame, text="Análisis", bg="#142157", font=("Arial", 12), bd=0, fg="white", activeforeground='black')
        boton_analisis.place(x=161, y=10, width=150, height=30)
        # Opciones del boton traducir
        opciones=Menu(boton_analisis, tearoff=0)
        boton_analisis["menu"]=opciones
        opciones.add_command(label="Generar sentencias MongoDB", font=("Arial", 12), activeforeground='black', command=self.traducir_archivo)

        # Boton tokens
        boton_tokens = tk.Menubutton(opciones_frame, text="Tokens", bg="#142157", font=("Arial", 12), bd=0, fg="white", activeforeground='black')
        boton_tokens.place(x=312, y=10, width=150, height=30)
        # Opciones del boton traducir
        opciones=Menu(boton_tokens, tearoff=0)
        boton_tokens["menu"]=opciones
        opciones.add_command(label="Ver Tokens", font=("Arial", 12), activeforeground='black', command=self.traducir_archivo)

        #boton errores
        boton_errores = tk.Menubutton(opciones_frame, text="Errores", bg="#142157", font=("Arial", 12), bd=0, fg="white", activeforeground='black')
        boton_errores.place(x=463, y=10, width=150, height=30)
        # Opciones del boton traducir
        opciones=Menu(boton_errores, tearoff=0)
        boton_errores["menu"]=opciones
        opciones.add_command(label="Archivo de Errores", font=("Arial", 12), activeforeground='black', command=self.traducir_archivo)

        # Configuración del frame
        opciones_frame.place(x=0, y=50)
        opciones_frame.pack_propagate()
        opciones_frame.config(width=1200, height=50)

        # Frame del cuadro de texto
        cuadrotexto_frame = tk.Frame(root, bg="#0799B6")
        # Cuadro de texto
        self.areatexto = scrolledtext.ScrolledText(cuadrotexto_frame, font=("Arial", 12), bg="white",  width=60, height=28)
        self.areatexto.place(x=30, y=30)


        self.label_consola = tk.Label(cuadrotexto_frame, text="Prueba.txt ", font=("Arial", 12), fg="white", bg="#0799B6")   
        self.label_consola.place(x=30, y=5)
        # Configuración del frame
        cuadrotexto_frame.place(x=0, y=100)
        cuadrotexto_frame.pack_propagate()
        cuadrotexto_frame.config(width=1200, height=600)




    def traducir_archivo(self):
        return
    def abrir_archivo(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.areatexto.delete('1.0', tk.END)
                self.areatexto.insert(tk.END, content)


    def salir(self):
        self.root.quit()
        self.root.destroy()
        exit()
    
    def nuevo():
        return
 



if __name__ == "__main__":
    root = tk.Tk()
    ventana_principal = VentanaPrincipal(root)
    root.mainloop()