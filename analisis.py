import tkinter as tk
from tkinter import Label, ttk
import pyodbc
from sshtunnel import _ThreadingForwardServer, SSHTunnelForwarder
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import time

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
        conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+sv+"; port="+port+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)
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
    cursor = conexion.cursor()
    consulta = "select hora from Labores where labores = ? and hora >= '2021-12-11';"
    cursor.execute(consulta,'Clientes')
    tupleall = cursor.fetchall()
    horas = [_[0] for _ in tupleall]
    for i in horas:
        print(i.day)
    
    if (horas[1].day - horas[0].day) == 0:
        durclientes = int((horas[1].timestamp() - horas[0].timestamp())/60)
    else:
        durclientes = 0
    consulta = "select hora from Labores where labores = ? and hora >= '2021-12-07';"
    cursor.execute(consulta,'Contabilidad')
    tupleall = cursor.fetchall()
    horas = [_[0] for _ in tupleall]
    if (horas[1].day - horas[0].day) == 0:
        durcontabilidad = int((horas[1].timestamp() - horas[0].timestamp())/60)
    else:
        durcontabilidad = 0
    print("duracion clientes ", durclientes, " minutos")
    print("duracion contabilidad ", durcontabilidad, " minutos")
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    langs = ['Clientes','Contabilidad','IT','Finca','Fabricación','Soporte Remoto','Legal','Cobros','Proveedores','Organización','SGC','SST','I&D','Publicidad']
    students = [ durclientes, durcontabilidad, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4 ]
    ax.bar(langs,students)
    plt.show()

