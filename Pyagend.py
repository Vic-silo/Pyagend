import tkinter as tk
from tkinter import messagebox
import pandas as pd
from PIL import ImageTk, Image

BACKG_ROOT = 'media/background.jpg'

class Gui(tk.Frame):

    def __init__(self, parent=None):
        '''
        Creacion del objeto GUI
        '''
        # Dataframe
        self.df = pd.DataFrame(
            columns=['Tarea', 'Descripcion', 'Dias', 'Frecuencia'])
        # Tkinter
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
        # self.h1 = tk.Label(self.parent,
        #                    text='AÑADA EVENTO',
        #                    foreground='blue')
        # Labels indicar campo de entrada
        self.l1 = tk.Label(self.parent, text='Tarea:')
        self.l2 = tk.Label(self.parent, text='Descripción:')
        self.l3 = tk.Label(self.parent, text='Tiempo duración:')
        self.l4 = tk.Label(self.parent, text='Frecuencia:')
        # Boton de AGREGAR
        self.btn1 = tk.Button(self.parent, text='AGREGAR', bg='light blue',
                              command=self.__agregar_datos)
        # Boton de CONSULTAR
        self.btn2 = tk.Button(self.parent, text='CONSULTAR', bg='light blue',
                              command=self.__consultar_datos)
        # Boton de MODIFICAR
        self.btn3 = tk.Button(self.parent, text='MODIFICAR', bg='light blue',
                              command=self.__modificar_datos)
        # Boton de ELIMINAR
        self.btn4 = tk.Button(self.parent, text='ELIMINAR', bg='light blue',
                              command=self.__eliminar_datos)
        # Boton de cierre de GUI
        self.btnExit = tk.Button(self.parent, text='SALIR', bg='red',
                                 fg='white', command=self.__Exit)
        # Campos de entrada
        self.in1 = tk.Entry(self.parent)
        # self.in1.insert(0,'')
        self.in2 = tk.Entry(self.parent)
        # self.in2.insert(0,'escribe aqui')
        self.in3 = tk.Entry(self.parent)
        # self.in3.insert(0,'escribe aqui')
        self.in4 = tk.Entry(self.parent)
        # self.in4.insert(0,'escribe aqui')
        
        # Posicionado de los elementos
        self.l1.place(x=70, y=150)
        self.in1.place(x=200, y=150)
        self.l2.place(x=70, y=170)
        self.in2.place(x=200, y=170)
        self.l3.place(x=70, y=190)
        self.in3.place(x=200, y=190)
        self.l4.place(x=70, y=210)
        self.in4.place(x=200, y=210)
        self.btn1.place(x=150, y=350)
        self.btn2.place(x=230, y=350)
        self.btn3.place(x=325, y=350)
        self.btn4.place(x=410, y=350)
        self.btnExit.place(x=550, y=350)

    def __Exit(self):
        '''
        Cierre de la aplicacion
        :return:
        '''
        self.parent.quit()
        self.parent.destroy()

    def __agregar_datos(self):
        '''
        Guarda los datos en dataframe
        :return:
        '''

        # Registra valores introducidos
        tarea=self.in1.get()
        descripcion=self.in2.get()
        dias=self.in3.get()
        frecuencia=self.in4.get()

        # Añadir datos al dataframe
        datos = {'Tarea': tarea, 'Descripcion': descripcion, 'Dias': dias,
                 'Frecuencia': frecuencia}

        self.df = self.df.append(datos, ignore_index=True)

        # Borrar datos
        self.in1.delete(0, tk.END)
        self.in2.delete(0, tk.END)
        self.in3.delete(0, tk.END)
        self.in4.delete(0, tk.END)

        print(self.df)

    def __consultar_datos(self):
        '''
        Consultar datos por TAREA
        :return:
        '''

        # Obtenemos valor de la consulta
        campo=self.in1.get()
        
        # Obtenemos datos de la consulta
        busqueda = self.df.index[self.df['Tarea'] == campo].tolist()
        busqueda = busqueda[0]
        
        # Borramos los datos de los campos y mostramos los encontrados
        self.in1.delete(0, tk.END)
        self.in2.delete(0, tk.END)
        self.in3.delete(0, tk.END)
        self.in4.delete(0, tk.END)
        
        # mostramos los datos encontrados
        self.in1.insert(0, self.df.iloc[busqueda]['Tarea'])
        self.in2.insert(0, self.df.iloc[busqueda]['Descripcion'])
        self.in3.insert(0, self.df.iloc[busqueda]['Dias'])
        self.in4.insert(0, self.df.iloc[busqueda]['Frecuencia'])

        # Mostramos consulta
        #messagebox.showinfo(title='RESULTADO CONSULTA',
        #                    message=df_busqueda)


    def __modificar_datos(self):
        '''
        Busca dato por TAREA y modifica por index
        :return:
        '''
        # Buscamos la fila a modificar
        indice = self.df.index[self.df['Tarea'] == self.in1.get()].tolist()
        indice = indice[0]

        # Ponemos los nuevos valores que hay en pantalla
        self.df.iloc[indice]['Tarea'] = self.in1.get()
        self.df.iloc[indice]['Descripcion'] = self.in2.get()
        self.df.iloc[indice]['Dias'] = self.in3.get()
        self.df.iloc[indice]['Frecuencia'] = self.in4.get()
        
        self.__consultar_datos()
        print(self.df)

    def __eliminar_datos(self):
        '''
        :return:
        '''
        # Buscamos la fila a borrar
        indice = self.df.index[self.df['Tarea'] == self.in1.get()].tolist()
        indice = indice[0]

        # Eliminamos la Tarea
        self.df = self.df.drop(indice)
        print(self.df)
