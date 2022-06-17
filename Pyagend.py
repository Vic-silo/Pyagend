import tkinter as tk
from PIL import ImageTk, Image

BACKG_ROOT = 'media/background.jpg'


class Gui(tk.Frame):

    def __init__(self, parent=None):
        '''
        Creacion del objeto GUI
        '''
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.__initGUI()

    def __initGUI(self):
        '''
        Definición de las caracteristicas y widgets de la GUI
        :return:
        '''
        # Definicion de caracteristicas gráficas
        # Fondo de pantalla temático
        self.img = ImageTk.PhotoImage(Image.open(BACKG_ROOT))
        self.canvas = tk.Canvas(self.parent, width=600, height=400)
        self.canvas.create_image(0, 0, image=self.img, anchor='nw')
        self.canvas.pack(fill='both', expand=False)

        # Titulo de la GUI
        self.parent.title('PYAGEND')
        # Atributos varios
        self.parent.resizable(False, False)

        # Widgets GUI
        # Titulo herramienta
        self.h1 = tk.Label(self.parent,
                           text='AÑADA EVENTO',
                           foreground='blue')
        # Labels indicar campo de entrada
        self.l1 = tk.Label(self.parent, text='Tarea:')
        self.l2 = tk.Label(self.parent, text='Descripción:')
        self.l3 = tk.Label(self.parent, text='Tiempo duración:')
        self.l4 = tk.Label(self.parent, text='Frecuencia:')
        # Boton de prediccion
        # self.btn1 = tk.Button(self.parent, text='Predecir', bg='light blue',
        #                       command=self.__Predict)
        # Boton de cierre de GUI
        self.btnExit = tk.Button(self.parent, text='SALIR', bg='red',
                                 fg='white', command=self.__Exit)
        # Campos de entrada
        self.in1 = tk.Entry(self.parent)
        self.in1.insert(0,'escribe aqui')
        self.in2 = tk.Entry(self.parent)
        self.in2.insert(0,'escribe aqui')
        self.in3 = tk.Entry(self.parent)
        self.in3.insert(0,'escribe aqui')
        self.in4 = tk.Entry(self.parent)
        self.in4.insert(0,'escribe aqui')
        # Posicionado de los elementos
        self.h1.place(x=200, y=220)
        self.l1.place(x=70, y=250)
        self.in1.place(x=200, y=250)
        self.l2.place(x=70, y=270)
        self.in2.place(x=200, y=270)
        self.l3.place(x=70, y=290)
        self.in3.place(x=200, y=290)
        self.l4.place(x=70, y=310)
        self.in4.place(x=200, y=310)
        # self.btn1.place(x=730, y=150)
        self.btnExit.place(x=550, y=350)

    def __Exit(self):
        '''
        Cierre de la aplicacion
        :return:
        '''
        self.parent.quit()
        self.parent.destroy()

    # def agregar_datos(self):
    #     global nombre1, apellido1, dni1, correo1, telefono1
    #
    #     nombre1.append(ingresa_nombre.get())
    #     apellido1.append(ingresa_apellido.get())
    #     edad1.append(ingresa_edad.get())
    #     correo1.append(ingresa_correo.get())
    #     telefono1.append(ingresa_telefono.get())
    #
    #     ingresa_nombre.delete(0, END)
    #     ingresa_apellido.delete(0, END)
    #     ingresa_edad.delete(0, END)
    #     ingresa_correo.delete(0, END)
    #     ingresa_telefono.delete(0, END)
    #
    # def guardar_datos(self):
    #     global nombre1, apellido1, edad1, correo1, telefono1
    #     datos = {'Nombres': nombre1, 'Apellidos': apellido1, 'Edad': edad1,
    #              'Correo': correo1, 'Telefono': telefono1}
    #     nom_excel = str(nombre_archivo.get() + ".xlsx")
    #     df = pd.DataFrame(datos,
    #                       columns=['Nombres', 'Apellidos', 'Edad', 'Correo',
    #                                'Telefono'])
    #     df.to_excel(nom_excel)
    #     nombre_archivo.delete(0, END)