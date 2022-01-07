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
langs = ['duracion dia','Clientes','Contabilidad','IT','Finca','Fabricación','Soporte Remoto','Legal','Cobros','Proveedores','Organización','SGC','SST','I&D','Publicidad']

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
    c = 0
    co = 0
    csop = 0
    durclientes = 0
    durcontabilidad = 0
    durhorasdia = 480
    durit = 0
    durfin = 0
    durfab = 0
    dursop = 0
    durleg = 0
    durcob = 0
    durpro = 0
    duror = 0
    dursgc = 0
    dursst = 0
    durid = 0
    durpub = 0
    est = 1
    
    while i < len(horas) - 1:
        if (horas[i + 1].day == horas[i].day):
            if (labores[i] != labores[i - 1]):
                #print(labores[i], labores[i + 1])
                #print(ids[i], horas[i])
                if (labores[i] == langs[0]):
                    c = c + 1
                    durclientes = durclientes + int((horas[i + 1].timestamp() - horas[i].timestamp())/60)
                    print(c, labores[i - 1], horas[i - 1], labores[i], horas[i], labores[i + 1], horas[i + 1], durclientes)
                elif (labores[i] == langs[1]):
                    co = co + 1
                    durcontabilidad = durcontabilidad + int((horas[i + 1].timestamp() - horas[i].timestamp())/60)
                    #print(co, labores[i - 1], horas[i - 1], labores[i], horas[i], labores[i + 1], horas[i + 1], durcontabilidad)
                elif (labores[i] == langs[2]):
                    durit = durit + int((horas[i + 1].timestamp() - horas[i].timestamp())/60)
                elif (labores[i] == langs[3]):
                    durfin = durfin + int((horas[i + 1].timestamp() - horas[i].timestamp())/60)
                elif (labores[i] == langs[4]):
                    durfab = durfab + int((horas[i + 1].timestamp() - horas[i].timestamp())/60)
                elif (labores[i] == langs[5]):
                    csop = csop + 1
                    dursop = dursop + int((horas[i + 1].timestamp() - horas[i].timestamp())/60)
                    print(csop, labores[i - 1], horas[i - 1], labores[i], horas[i], labores[i + 1], horas[i + 1], dursop)
                elif (labores[i] == langs[6]):
                    durleg = durleg + int((horas[i + 1].timestamp() - horas[i].timestamp())/60)
                elif (labores[i] == langs[7]):
                    durcob = durcob + int((horas[i + 1].timestamp() - horas[i].timestamp())/60)
                elif (labores[i] == langs[8]):
                    durpro = durpro + int((horas[i + 1].timestamp() - horas[i].timestamp())/60)
                elif (labores[i] == langs[9]):
                    duror = duror + int((horas[i + 1].timestamp() - horas[i].timestamp())/60)
                elif (labores[i] == langs[10]):
                    dursgc = dursgc + int((horas[i + 1].timestamp() - horas[i].timestamp())/60)
                elif (labores[i] == langs[11]):
                    dursst = dursst + int((horas[i + 1].timestamp() - horas[i].timestamp())/60)
                elif (labores[i] == langs[12]):
                    durid = durid + int((horas[i + 1].timestamp() - horas[i].timestamp())/60)
                elif (labores[i] == langs[13]):
                    durpub = durpub + int((horas[i + 1].timestamp() - horas[i].timestamp())/60)
            elif (labores[i] == 'Horas Trabajadas'):
                est = -1*est
                print(est, labores[i], horas[i].day)
        else:
            durhorasdia = durhorasdia + int((horas[i + 1].timestamp() - horas[i].timestamp())/3600)
            print("Otros dias ", ids[i], horas[i], horas[i + 1], durhorasdia)
            '''for x in langs:
                print(x)'''
        i = i + 1
    print(durhorasdia)
    '''print("duracion clientes ", durclientes, " minutos")
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
    print("duracion Publicidad ", durpub, " minutos")'''

    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    
    students = [ durhorasdia/durhorasdia, durclientes, durcontabilidad, durit, durfin, durfab, dursop,durleg,durcob,durpro,duror,dursgc,dursst,durid,durpub ]
    ax.bar(langs,students)
    plt.show()