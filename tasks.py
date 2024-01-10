"""
Programador de tareas segun lo programado en DJANGO
"""
import pandas as pd
import numpy as np
import sqlite3
from funciones import *
# Direccion absoluta
PATH_ABS = 'E:/CPERv/Centralizacion de datos/click/main/media/'
# Lectura de las tareas
con = sqlite3.connect("./main/db.sqlite3")
df = pd.read_sql_query("SELECT * from acciones_tarea", con)
print(df[df.id==1])

# Lectura de las acciones
df_acciones = pd.read_sql_query("SELECT * from acciones_accion",con)
df_acciones.sort_values(by=['orden'],inplace=True)
id_tarea = np.array(df.id)
habilitar_tarea = np.array(df.habilitar)
tareas_zip = zip(id_tarea, habilitar_tarea)
# bucle para desarrollar todas las tareas
for tareas in tareas_zip:
    comprimir = zip(df_acciones[df_acciones.tareaID_id == tareas[0]].accion_model,
                df_acciones[df_acciones.tareaID_id == tareas[0]].imagen,
                df_acciones[df_acciones.tareaID_id == tareas[0]].texto,
                )
    if bool(tareas[1])==True:
        for accion in comprimir:
            pyautogui.FAILSAFE = True
            print(accion)
            if accion[0] == 'screen':
                path = PATH_ABS + accion[1] 
                screen(path)
            if accion[0]  == 'wait':
                wait(int(accion[2]))
            if accion[0]  == 'move':
                path2 = PATH_ABS + accion[1]
                move(path2)
            if accion[0]  == 'write_text':
                write_text(accion[2])
            if accion[0]  == 'push_enter':
                push_enter() 

