"""
Proyecto python 
Conversor de unidades
En este programa puedes introducir el tipo de dato que requieres convertir
a partir de las unidades que tengas.
"""

# Menu donde el usuario escoge las unidades que quiera convertir

print("1. Milímetros \n 2. Centímetros \n 3. Decímetros \n 4. Metros \n 5. Decámetro \n 6. Hectómetro \n 7. Kilómetro")
tipo_unidad = int(input("Teclea el número de la opcion que necesites: "))

# Menu donde el usuario escoge las unidades que tenga

print("1. Milímetros \n 2. Centímetros \n 3. Decímetros \n 4. Metros \n 5. Decámetro \n 6. Hectómetro \n 7. Kilómetro")
tipo_unidad2 = int(input("Teclea el número de la opcion que tengas a convertir: "))

#Se le pide al usuario el valor a convertir 
usuario = float(input("Introduce el valor a convertir: "))

#Se compara el tipo de valor que se quiere obtener

if tipo_unidad == 1 :
#Aqui se compara primero con milímetros
    if tipo_unidad2 == 2 :
        res = usuario * 10        
    else :
        if tipo_unidad2 == 3 :
            res = usuario * 100
        else :
            if tipo_unidad2 == 4 :
                res = usuario * 1000
            else :
                if tipo_unidad2 == 5 :
                    res = usuario * 10000
                else :
                    if tipo_unidad2 == 6 :
                        res = usuario * 100000
                    else :
                        if tipo_unidad2 == 7 :
                            res = usuario * 1000000
                        else :
                            print("Opción no válida")
#En caso de que las unidades que se vayan a convertir no sean milímetros, se compraran por centímetros
if tipo_unidad == 2 :
#Aqui se compara primero con milímetros
    if tipo_unidad2 == 1 :
        res = usuario / 10        
    else :
        if tipo_unidad2 == 3 :
            res = usuario * 10
        else :
            if tipo_unidad2 == 4 :
                res = usuario * 100
            else :
                if tipo_unidad2 == 5 :
                    res = usuario * 1000
                else :
                    if tipo_unidad2 == 6 :
                        res = usuario * 10000
                    else :
                        if tipo_unidad2 == 7 :
                            res = usuario * 100000
                        else :
                            print("Opción no válida")
#En caso de que las unidades que se vayan a convertir no sean centímetros, se comparan por Decímetros
if tipo_unidad == 3 :
#milímetros
    if tipo_unidad2 == 1 :
        res = usuario / 100        
    else :
#Centímetros
        if tipo_unidad2 == 2 :
            res = usuario / 10
        else :
#Metros
            if tipo_unidad2 == 4 :
                res = usuario * 10
            else :
#Decámetros
                if tipo_unidad2 == 5 :
                    res = usuario * 100
                else :
#Hectómetros
                    if tipo_unidad2 == 6 :
                        res = usuario * 1000
                    else :
#kilómetros
                        if tipo_unidad2 == 7 :
                            res = usuario * 10000
                        else :
                            print("Opción no válida")
#En caso de que las unidades que se vayan a convertir no sean Decímetros, se comparan por Metros
if tipo_unidad == 4 :
#milímetros
    if tipo_unidad2 == 1 :
        res = usuario / 1000        
    else :
#Centímetros
        if tipo_unidad2 == 2 :
            res = usuario / 100
        else :
#Decímetros
            if tipo_unidad2 == 3 :
                res = usuario / 10
            else :
#Decámetros
                if tipo_unidad2 == 5 :
                    res = usuario * 10
                else :
#Hectómetros
                    if tipo_unidad2 == 6 :
                        res = usuario * 100
                    else :
#kilómetros
                        if tipo_unidad2 == 7 :
                            res = usuario * 1000
                        else :
                            print("Opción no válida")
#En caso de que las unidades que se vayan a convertir no sean Metros, se comparan por Decámetros
if tipo_unidad == 5 :
#milímetros
    if tipo_unidad2 == 1 :
        res = usuario / 10000        
    else :
#Centímetros
        if tipo_unidad2 == 2 :
            res = usuario / 1000
        else :
#Decímetros
            if tipo_unidad2 == 3 :
                res = usuario / 100
            else :
#Metros
                if tipo_unidad2 == 4 :
                    res = usuario / 10
                else :
#Hectómetros
                    if tipo_unidad2 == 6 :
                        res = usuario * 10
                    else :
#kilómetros
                        if tipo_unidad2 == 7 :
                            res = usuario * 100
                        else :
                            print("Opción no válida")
#En caso de que las unidades que se vayan a convertir no sean Decámetros, se comparan por Hectómetros
if tipo_unidad == 6 :
#milímetros
    if tipo_unidad2 == 1 :
        res = usuario / 100000        
    else :
#Centímetros
        if tipo_unidad2 == 2 :
            res = usuario / 10000
        else :
#Decímetros
            if tipo_unidad2 == 3 :
                res = usuario / 1000
            else :
#Metros
                if tipo_unidad2 == 4 :
                    res = usuario / 100
                else :
#Decámetros
                    if tipo_unidad2 == 5 :
                        res = usuario / 10
                    else :
#kilómetros
                        if tipo_unidad2 == 7 :
                            res = usuario * 10
                        else :
                            print("Opción no válida")
#En caso de que las unidades que se vayan a convertir no sean Hectómetros, se comparan por Kilómetros
if tipo_unidad == 7 :
#milímetros
    if tipo_unidad2 == 1 :
        res = usuario / 1000000       
    else :
#Centímetros
        if tipo_unidad2 == 2 :
            res = usuario / 100000
        else :
#Decímetros
            if tipo_unidad2 == 3 :
                res = usuario / 10000
            else :
#Metros
                if tipo_unidad2 == 4 :
                    res = usuario / 1000
                else :
#Decámetros
                    if tipo_unidad2 == 5 :
                        res = usuario / 100
                    else :
#Hectómetros
                        if tipo_unidad2 == 6 :
                            res = usuario / 10
                        else :
                            print("Opción no válida")





print(res)
                            
                        
    
        
        
        