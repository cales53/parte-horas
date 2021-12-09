import tkinter as tk
from tkinter import ttk
import pyodbc
from sshtunnel import SSHTunnelForwarder
import time

sv = '127.0.0.1'
port='1433'
bd = 'Parte Horas' 
usuario = 'usuario' 
contrasena = 'Manager21' 

def info():
    with SSHTunnelForwarder(
    ('190.147.177.209', 22),
    ssh_username="admin",
    ssh_password="%it$2018",
    local_bind_address=('127.0.0.1', 1433),
    remote_bind_address=('192.168.1.89', 1433)) as server:
        server.start()
        conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+sv+"; port="+port+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)
        cursor = conexion.cursor()
        print('conexion establecida')
        consulta = "select hora from Labores where labores = ?;"
        cursor.execute(consulta,'Clientes')
        tupleall = cursor.fetchall()
        horas = [_[0] for _ in tupleall]
        #fecha = time.strftime("%Y-%m-%d %H:%M:%S.000", horas[0])
        print(horas)
    analisiswin = tk.Tk()
    analisiswin.title("Parte Horas")
    analisiswin.columnconfigure(1, weight=2)
    analisiswin.minsize(150,60)
    analisiswin.maxsize(205,60)
    selected_labor = tk.StringVar()
    botonAn = ttk.Button(
    analisiswin, 
    text="Cerrar", 
    command=lambda:quit()
    )
    botonAn.grid(column=2, row=2, sticky=tk.E, padx=5, pady=0)
