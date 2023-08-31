"""
Proyecto python 
Conversor de unidades
En este programa puedes introducir el tipo de dato que requieres convertir
a partir de las unidades que tengas.
"""



"""
    Funciones para comparar el tipo de valor que se va a convertir,
    independientemente si la medida sea de volumen, longitud, peso, todas siguen los
    mismos prefijos y las mismas unidades. Se hace una función para convertir a cada prefijo
"""
def mili(tipo_unidad2):
    """
funcion mili, se usa cunado el tipo de unidad que da el usuario empieza con ese prefijo
recibe el segundo tipo de unidad, lo comprueba, y hace las operaciones necesarias para
covertir la unidad, devuelve res
@param tipo_unidad2, la compara para saber el segundo tipo de unidad
@return res, el valor convertido
"""
    if (tipo_unidad2 == 2) :
        res = usuario * 10
    else :
        if (tipo_unidad2 == 3) :
            res = usuario * 100
        else :
            if (tipo_unidad2 == 4) :
                res = usuario * 1000
            else :
                if (tipo_unidad2 == 5) :
                    res = usuario * 10000
                else :
                    if (tipo_unidad2 == 6) :
                        res = usuario * 100000
                    else :
                        if (tipo_unidad2 == 7) :
                            res = usuario * 1000000
                        else :
                            print("Opción no válida")
    return(res)
#En caso de que las unidades que se vayan a convertir no sean prefijo mili, se compraran por centi
def centi(tipo_unidad2):
    """
funcion centi, se usa cunado el tipo de unidad que da el usuario empieza con ese prefijo
recibe el segundo tipo de unidad, lo comprueba, y hace las operaciones necesarias para
covertir la unidad, devuelve res
@param tipo_unidad2, la compara para saber el segundo tipo de unidad
@return res, el valor convertido
"""
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
    return(res)
#En caso de que las unidades que se vayan a convertir no sean prefijo centi, se comparan por deci



def deci(tipo_unidad2):
    """
funcion deci, se usa cunado el tipo de unidad que da el usuario empieza con ese prefijo
recibe el segundo tipo de unidad, lo comprueba, y hace las operaciones necesarias para
covertir la unidad, devuelve res
@param tipo_unidad2, la compara para saber el segundo tipo de unidad
@return res, el valor convertido
"""
    if (tipo_unidad2 == 1) :
        res = usuario / 100
    else :
        if (tipo_unidad2 == 3) :
            res = usuario / 10
        else :
            if (tipo_unidad2 == 4) :
                res = usuario * 10
            else :
                if (tipo_unidad2 == 5) :
                    res = usuario * 100
                else :
                    if (tipo_unidad2 == 6) :
                        res = usuario * 1000
                    else :
                        if (tipo_unidad2 == 7) :
                            res = usuario * 10000
                        else :
                            print("Opción no válida")
    return(res)

                            


#En caso de que las unidades que se vayan a convertir no sean prefijo deci, se comparan por M,L

def sufijo(tipo_unidad2):
    """
funcion sufijo, se usa cunado el tipo de unidad que da el usuario empieza con ese prefijo
recibe el segundo tipo de unidad, lo comprueba, y hace las operaciones necesarias para
covertir la unidad, devuelve res
@param tipo_unidad2, la compara para saber el segundo tipo de unidad
@return res, el valor convertido
"""
    if tipo_unidad2 == 1 :
        res = usuario / 1000
    else :
        if tipo_unidad2 == 2 :
            res = usuario / 100
        else :
            if tipo_unidad2 == 3 :
                res = usuario * 10
            else :
                if tipo_unidad2 == 5 :
                    res = usuario * 10
                else :
                    if tipo_unidad2 == 6 :
                        res = usuario * 100
                    else :
                        if tipo_unidad2 == 7 :
                            res = usuario * 1000
                        else :
                            print("Opción no válida")
    return(res)


#En caso de que las unidades que se vayan a convertir no sean M,L , se comparan por prefijo deca
def deca(tipo_unidad2):
    """
funcion deca, se usa cunado el tipo de unidad que da el usuario empieza con ese prefijo
recibe el segundo tipo de unidad, lo comprueba, y hace las operaciones necesarias para
covertir la unidad, devuelve res
@param tipo_unidad2, la compara para saber el segundo tipo de unidad
@return res, el valor convertido
"""
    if tipo_unidad2 == 1 :
        res = usuario / 10000
    else :
        if tipo_unidad2 == 2 :
            res = usuario / 1000
        else :
            if tipo_unidad2 == 3 :
                res = usuario / 100
            else :
                if tipo_unidad2 == 4 :
                    res = usuario / 10
                else :
                    if tipo_unidad2 == 6 :
                        res = usuario * 10
                    else :
                        if tipo_unidad2 == 7 :
                            res = usuario * 100
                        else :
                            print("Opción no válida")
    return(res)



#En caso de que las unidades que se vayan a convertir no sean prefijo deca, se comparan por hecto

def hecto(tipo_unidad2):
    """
funcion hecto, se usa cunado el tipo de unidad que da el usuario empieza con ese prefijo
recibe el segundo tipo de unidad, lo comprueba, y hace las operaciones necesarias para
covertir la unidad, devuelve res
@param tipo_unidad2, la compara para saber el segundo tipo de unidad
@return res, el valor convertido
"""
    if tipo_unidad2 == 1 :
        res = usuario / 100000
    else :
        if tipo_unidad2 == 2 :
            res = usuario / 10000
        else :
            if tipo_unidad2 == 3 :
                res = usuario / 1000
            else :
                if tipo_unidad2 == 4 :
                    res = usuario / 100
                else :
                    if tipo_unidad2 == 5 :
                        res = usuario / 10
                    else :
                        if tipo_unidad2 == 7 :
                            res = usuario * 10
                        else :
                            print("Opción no válida")
    return(res)
    
    
#En caso de que las unidades que se vayan a convertir no sean prefijo hecto, se comparan por kilo
def kilo(tipo_unidad2):
    """
funcion kilo, se usa cunado el tipo de unidad que da el usuario empieza con ese prefijo
recibe el segundo tipo de unidad, lo comprueba, y hace las operaciones necesarias para
covertir la unidad, devuelve res
@param tipo_unidad2, la compara para saber el segundo tipo de unidad
@return res, el valor convertido
"""
    if tipo_unidad2 == 1 :
        res = usuario / 1000000
    else :
        if tipo_unidad2 == 2 :
            res = usuario / 100000
        else :
            if tipo_unidad2 == 3 :
                res = usuario / 10000
            else :
                if tipo_unidad2 == 4 :
                    res = usuario / 1000
                else :
                    if tipo_unidad2 == 5 :
                        res = usuario / 100
                    else :
                        if tipo_unidad2 == 6 :
                            res = usuario / 10
                        else :
                            print("Opción no válida")
    return(res)
    


#Pequeño menú donde el usuario esci¿oge las unidades (Volumen, longitud)
print("1. Longitud \n 2. Volumen")
unidad_general = int(input("Teclea el número de la opción que necesites: "))

if (unidad_general == 1):
    # Menu donde el usuario escoge las unidades que quiera convertir
    print("1. Milímetros \n 2. Centímetros \n 3. Decímetros \n 4. Metros \n 5. Decámetro \n 6. Hectómetro \n 7. Kilómetro")
    tipo_unidad = int(input("Teclea el número de la opcion que necesites: "))
    # Menu donde el usuario escoge las unidades que tenga
    print("1. Milímetros \n 2. Centímetros \n 3. Decímetros \n 4. Metros \n 5. Decámetro \n 6. Hectómetro \n 7. Kilómetro")
    tipo_unidad2 = int(input("Teclea el número de la opcion que tengas a convertir: "))
elif (unidad_general == 2):
    # Menu donde el usuario escoge las unidades que quiera convertir
    print("1. Mililitros \n 2. Centilitros \n 3. Decilitros \n 4. Litros \n 5. Decalitros \n 6. Hectolitros \n 7. Kilolitros")
    tipo_unidad = int(input("Teclea el número de la opcion que necesites: "))
    # Menu donde el usuario escoge las unidades que tenga
    print("1. Mililitros \n 2. Centilitros \n 3. Decilitros \n 4. Litros \n 5. Decalitros \n 6. Hectolitros \n 7. Kilolitros")
    tipo_unidad2 = int(input("Teclea el número de la opcion que tengas a convertir: "))

#Se le pide al usuario el valor a convertir 
usuario = float(input("Introduce el valor a convertir: "))



#Aquí se manda a llamar la funcion que sea necesaria a partir de el tipo de unidad
if(tipo_unidad == 1):
    print(mili(tipo_unidad2))
elif(tipo_unidad == 2):
    print(centi(tipo_unidad2))
elif(tipo_unidad == 3):
    print(deci(tipo_unidad2))
elif(tipo_unidad == 4):
    print(sufijo(tipo_unidad2))
elif(tipo_unidad == 5):
    print(deca(tipo_unidad2))
elif(tipo_unidad == 6):
    print(hecto(tipo_unidad2))
elif(tipo_unidad == 7):
    print(kilo(tipo_unidad2))
else:
    print("No válido")




                            
                        
    
        
        
        