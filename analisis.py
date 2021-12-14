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
langs = ['Clientes','Contabilidad','IT','Finca','Fabricación','Soporte Remoto','Legal','Cobros','Proveedores','Organización','SGC','SST','I&D','Publicidad']

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
    consulta = "select hora from Labores;"
    cursor.execute(consulta)
    tupleall = cursor.fetchall()
    horas = [_[0] for _ in tupleall]
    
    cursor.execute("select id from Labores;")
    tupleid = cursor.fetchall()
    ids = [_[0] for _ in tupleid]

    cursor.execute("select labores from Labores;")
    tuplelab = cursor.fetchall()
    labores = [_[0] for _ in tuplelab]

    i = 0
    while i < len(horas) - 1:
        if (horas[i + 1].day == horas[i].day):
            if (labores[i] != labores[i - 1]):
                #print(labores[i], labores[i + 1])
                #print(ids[i], horas[i])
                if (labores[i] == langs[0]):
                    durclientes = int((horas[i].timestamp() - horas[i - 1].timestamp())/60)
                elif (labores[i] == langs[1]):
                    durcontabilidad = int((horas[i].timestamp() - horas[i - 1].timestamp())/60)
                elif (labores[i] == langs[2]):
                    durit = int((horas[i].timestamp() - horas[i - 1].timestamp())/60)
                elif (labores[i] == langs[3]):
                    durfin = int((horas[i].timestamp() - horas[i - 1].timestamp())/60)
                elif (labores[i] == langs[4]):
                    durfab = int((horas[i].timestamp() - horas[i - 1].timestamp())/60)
                elif (labores[i] == langs[5]):
                    dursop = int((horas[i].timestamp() - horas[i - 1].timestamp())/60)
                elif (labores[i] == langs[6]):
                    durleg = int((horas[i].timestamp() - horas[i - 1].timestamp())/60)
                elif (labores[i] == langs[7]):
                    durcob = int((horas[i].timestamp() - horas[i - 1].timestamp())/60)
                elif (labores[i] == langs[8]):
                    durpro = int((horas[i].timestamp() - horas[i - 1].timestamp())/60)
                elif (labores[i] == langs[9]):
                    duror = int((horas[i].timestamp() - horas[i - 1].timestamp())/60)
                elif (labores[i] == langs[10]):
                    dursgc = int((horas[i].timestamp() - horas[i - 1].timestamp())/60)
                elif (labores[i] == langs[11]):
                    dursst = int((horas[i].timestamp() - horas[i - 1].timestamp())/60)
                elif (labores[i] == langs[12]):
                    durid = int((horas[i].timestamp() - horas[i - 1].timestamp())/60)
                elif (labores[i] == langs[13]):
                    durpub = int((horas[i].timestamp() - horas[i - 1].timestamp())/60)

        else:
            pass
            #print("Otros dias ", ids[i], horas[i])
            '''for x in langs:
                print(x)'''
        i = i + 1
    print("duracion clientes ", durclientes, " minutos")
    print("duracion contabilidad ", durcontabilidad, " minutos")
    print("duracion IT ", durit, " minutos")
    print("duracion finca ", durfin, " minutos")
    print("duracion Fabricacion ", durfab, " minutos")
    print("duracion Soporte y Servicio ", dursop, " minutos")
    print("duracion Legal ", durcob, " minutos")
    print("duracion Cobros ", durpro, " minutos")
    print("duracion Proveedores ", durpro, " minutos")
    print("duracion Organizacion ", duror, " minutos")
    print("duracion SGC ", dursgc, " minutos")
    print("duracion SST ", dursst, " minutos")
    print("duracion I&D ", durid, " minutos")
    print("duracion Publicidad ", durpub, " minutos")

    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    
    students = [ durclientes, durcontabilidad, durit, durfin, durfab, dursop,durleg,durcob,durpro,duror,dursgc,dursst,durid,durpub ]
    ax.bar(langs,students)
    plt.show()