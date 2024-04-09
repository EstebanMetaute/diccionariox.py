import os
#Clasificacion de estudiantes de acuerdo a puntaje
ls_categoria1 = []#puntaje (30 - 50) y edad (15 - 20)
ls_categoria2 = []#puntaje (51 - 80) y edad ( 21 - 50)
ls_categoria3 = []#puntaje (01 - 100) y edad (31 - 50)
sw = True

def fnt_limpiar ():
    os.system('cls')
    print('\nBienvenido al sistema de calificacion de estudiantes')
    print('Autor: esteban')
    print('Institucion: Universidad catolica luis amigo')
    print('Categoria I: ',ls_categoria1)
    print('Categoria II: ',ls_categoria2)
    print('Categoria III: ',ls_categoria3)
    
def fnt_registrar(id, nombre, puntaje, edad):
    if id == '' or puntaje == '' or edad == '' or nombre == '':
        enter = input('\nDebe ingresar todos los datos <ENTER>')
    else:
        if id in ls_categoria1 or ls_categoria2 or ls_categoria3:#Si ese id se encuentra ya registrado
              enter = input('\nEsta persona ya se encuentra registrada <ENTER>')
        else:
            if (puntaje >= 30 and puntaje <= 50) and (edad >= 15 and edad <= 20):
                ls_categoria1.append([id,nombre,edad,puntaje])
            elif(puntaje >= 51 and puntaje <= 80) and (edad >= 21 and edad <= 30):
                ls_categoria2.append([id,nombre,edad,puntaje ])
            elif (puntaje >= 81 and puntaje <= 100) and (edad >= 31 and edad <= 50):
                ls_categoria3.append([id,nombre,edad,puntaje])
            enter = input(f'\nEstudiante (nombre) registrado con exito')
                
              
def fnt_selector(op):
    fnt_limpiar()
    if op == '1':
        idStr = input('Id: ')
        nombreStr = input('Nombres completos: ')
        edadInt = input(('Edad: '))
        puntajeInt = input(('Puntaje '))
        fnt_registrar(idStr,nombreStr,edadInt,puntajeInt)
        
while sw == True:
    fnt_limpiar()
    opcionesStr = input('\n\n<<<<< MENU PRINCIPAL >>>>>\n\n1. REGISTRAR\n2. CONSULTAR\n-> ')
    fnt_selector(opcionesStr)
    