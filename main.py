import tkinter as tk
from tkinter import ttk
import pyodbc
from sshtunnel import SSHTunnelForwarder
import time

sv = '192.168.1.89'
port='1433'
bd = 'Parte Horas' 
usuario = 'usuario' 
contrasena = 'Manager21' 

'''with SSHTunnelForwarder(
    ('192.168.1.2', 22),
    ssh_username="admin",
    ssh_password="%it$2018",
    local_bind_address=('127.0.0.1', 1433),
    remote_bind_address=('192.168.1.89', 1433)) as server:
    server.start()
    print("Server Connected")

    conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+sv+"; port="+port+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)
    print('Conexion establecida')
    cursor = conexion.cursor()'''

def Actualizardb():
    named_tuple = time.localtime() # get struct_time
    #time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    fecha = time.strftime("%Y-%m-%d %H:%M:%S.000", named_tuple)
    conexion = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server}; SERVER="+sv+"; port="+port+";DATABASE="+bd+";UID="+usuario+";PWD="+contrasena)
    cursor = conexion.cursor()
    print(nombre_cb.get())
    consulta = "insert into Labores (labores, hora) values (?,?);"
    cursor.execute(consulta, nombre_cb.get(),fecha)
    cursor.commit()

main = tk.Tk()
main.title("Parte Horas")
main.columnconfigure(1, weight=2)
main.minsize(150,50)
main.maxsize(205,50)
selected_labor = tk.StringVar()
labores=['Clientes','Contabilidad','IT','Finca','Fabricación','Soporte Remoto','Legal','Cobros','Proveedores','Organización','SGC','SST','I&D','Publicidad']

botonAA = ttk.Button(
    main, 
    text="Nueva Actividad", 
    command=lambda:Actualizardb()
)
botonAA.grid(column=2, row=1, sticky=tk.E, padx=5, pady=5)

nombre_cb = ttk.Combobox(main, textvariable=selected_labor, width="18")
nombre_cb['values'] = labores
nombre_cb['state'] = 'readonly'  # normal
nombre_cb.grid(row=1, column=1)
nombre_cb.bind('<<ComboboxSelected>>', Actualizardb())


main.mainloop()