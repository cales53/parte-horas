import tkinter as tk
from tkinter import Label, ttk
import pyodbc
from sshtunnel import SSHTunnelForwarder
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

port='1433'
bd = 'Parte Horas' 
usuario = 'usuario' 
contrasena = 'Manager21' 

def info():
    try:
        sv = '192.168.1.89'
        conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+sv+"; port="+port+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)
    except:
        sv = '127.0.0.1'
        with SSHTunnelForwarder(
        ('190.147.177.209', 22),
        ssh_username="admin",
        ssh_password="%it$2018",
        local_bind_address=('127.0.0.1', 1433),
        remote_bind_address=('192.168.1.89', 1433)) as server:
            server.start()
            conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+sv+"; port="+port+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)
            cursor = conexion.cursor()
        with SSHTunnelForwarder(
        ('190.147.177.209', 22),
        ssh_username="admin",
        ssh_password="%it$2018",
        local_bind_address=('127.0.0.1', 1433),
        remote_bind_address=('192.168.1.89', 1433)) as server:
            server.start()
            cursor = conexion.cursor()
            print('conexion establecida')
            consulta = "select hora from Labores where labores = ?;"
            cursor.execute(consulta,'Clientes')
            tupleall = cursor.fetchall()
            horas = [_[0] for _ in tupleall]
            #fecha = time.strftime("%Y-%m-%d %H:%M:%S.000", horas[0])
            print(horas)
    '''analisiswin = tk.Tk()
    analisiswin.title("Parte Horas")
    analisiswin.columnconfigure(1, weight=2)
    analisiswin.minsize(150,60)

    figure = Figure(figsize=(14, 14), dpi=80)
    plot = figure.add_subplot(1, 1, 1)
    #plot.plot(0.5, 0.3, color="red", marker="o", linestyle="")'''
    '''cursor = conexion.cursor()
    consulta = "select labores from Labores;"
    cursor.execute(consulta)
    tupleall = cursor.fetchall()
    labores = [_[0] for _ in tupleall]
    print(labores)'''
    '''x = ['Clientes','Contabilidad','IT','Finca','Fabricación','Soporte Remoto','Legal','Cobros','Proveedores','Organización','SGC','SST','I&D','Publicidad']
    y = [ 1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4 ]
    plot.bar(x, y)

    canvas = FigureCanvasTkAgg(figure, analisiswin)
    canvas.get_tk_widget().grid(row=1, column=1)'''

    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    langs = ['C', 'C++', 'Java', 'Python', 'PHP']
    students = [23,17,35,29,12]
    ax.bar(langs,students)
    plt.show()


    '''botonAn = ttk.Button(
    analisiswin, 
    text="Cerrar", 
    command=lambda:quit()
    )
    botonAn.grid(column=2, row=2, sticky=tk.E, padx=5, pady=0)'''
