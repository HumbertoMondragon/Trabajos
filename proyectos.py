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
def mili(unidad):
    """
funcion mili, se usa cuando el tipo de unidad que da el usuario empieza con ese prefijo
recibe el segundo tipo de unidad, lo comprueba, y hace las operaciones necesarias para
covertir la unidad, devuelve res
@param tipo_unidad2, la compara para saber el segundo tipo de unidad
@return res, el valor convertido
"""
    if (unidad == 2) :
        res = usuario * 10
    else :
        if (unidad == 3) :
            res = usuario * 100
        else :
            if (unidad == 4) :
                res = usuario * 1000
            else :
                if (unidad == 5) :
                    res = usuario * 10000
                else :
                    if (unidad == 6) :
                        res = usuario * 100000
                    else :
                        if (unidad == 7) :
                            res = usuario * 1000000
                        else :
                            print("Opción no válida")
    return(res)
#En caso de que las unidades que se vayan a convertir no sean prefijo mili, se compraran por centi
def centi(unidad):
    """
funcion centi, se usa cuando el tipo de unidad que da el usuario empieza con ese prefijo
recibe el segundo tipo de unidad, lo comprueba, y hace las operaciones necesarias para
covertir la unidad, devuelve res
@param tipo_unidad2, la compara para saber el segundo tipo de unidad
@return res, el valor convertido
"""
    if (unidad == 1) :
        res = usuario / 10
    else :
        if (unidad == 3) :
            res = usuario * 10
        else :
            if (unidad == 4) :
                res = usuario * 100
            else :
                if (unidad == 5) :
                    res = usuario * 1000
                else :
                    if (unidad == 6) :
                        res = usuario * 10000
                    else :
                        if (unidad == 7) :
                            res = usuario * 100000
                        else :
                            print("Opción no válida")
    return(res)
#En caso de que las unidades que se vayan a convertir no sean prefijo centi, se comparan por deci



def deci(unidad):
    """
funcion deci, se usa cuando el tipo de unidad que da el usuario empieza con ese prefijo
recibe el segundo tipo de unidad, lo comprueba, y hace las operaciones necesarias para
covertir la unidad, devuelve res
@param tipo_unidad2, la compara para saber el segundo tipo de unidad
@return res, el valor convertido
"""
    if (unidad == 1) :
        res = usuario / 100
    else :
        if (unidad == 3) :
            res = usuario / 10
        else :
            if (unidad == 4) :
                res = usuario * 10
            else :
                if (unidad == 5) :
                    res = usuario * 100
                else :
                    if (unidad == 6) :
                        res = usuario * 1000
                    else :
                        if (unidad == 7) :
                            res = usuario * 10000
                        else :
                            print("Opción no válida")
    return(res)

                            


#En caso de que las unidades que se vayan a convertir no sean prefijo deci, se comparan por M,L

def sufijo(unidad):
    """
funcion sufijo, se usa cuando el tipo de unidad que da el usuario empieza con ese prefijo
recibe el segundo tipo de unidad, lo comprueba, y hace las operaciones necesarias para
covertir la unidad, devuelve res
@param tipo_unidad2, la compara para saber el segundo tipo de unidad
@return res, el valor convertido
"""
    if (unidad == 1) :
        res = usuario / 1000
    else :
        if (unidad == 2) :
            res = usuario / 100
        else :
            if (unidad == 3) :
                res = usuario * 10
            else :
                if (unidad == 5) :
                    res = usuario * 10
                else :
                    if (unidad == 6) :
                        res = usuario * 100
                    else :
                        if (unidad == 7) :
                            res = usuario * 1000
                        else :
                            print("Opción no válida")
    return(res)


#En caso de que las unidades que se vayan a convertir no sean M,L , se comparan por prefijo deca
def deca(unidad):
    """
funcion deca, se usa cuando el tipo de unidad que da el usuario empieza con ese prefijo
recibe el segundo tipo de unidad, lo comprueba, y hace las operaciones necesarias para
covertir la unidad, devuelve res
@param tipo_unidad2, la compara para saber el segundo tipo de unidad
@return res, el valor convertido
"""
    if (unidad == 1) :
        res = usuario / 10000
    else :
        if (unidad == 2) :
            res = usuario / 1000
        else :
            if (unidad == 3) :
                res = usuario / 100
            else :
                if (unidad == 4) :
                    res = usuario / 10
                else :
                    if (unidad == 6) :
                        res = usuario * 10
                    else :
                        if (unidad == 7) :
                            res = usuario * 100
                        else :
                            print("Opción no válida")
    return(res)



#En caso de que las unidades que se vayan a convertir no sean prefijo deca, se comparan por hecto

def hecto(unidad):
    """
funcion hecto, se usa cuando el tipo de unidad que da el usuario empieza con ese prefijo
recibe el segundo tipo de unidad, lo comprueba, y hace las operaciones necesarias para
covertir la unidad, devuelve res
@param tipo_unidad2, la compara para saber el segundo tipo de unidad
@return res, el valor convertido
"""
    if (unidad == 1) :
        res = usuario / 100000
    else :
        if (unidad == 2) :
            res = usuario / 10000
        else :
            if (unidad == 3) :
                res = usuario / 1000
            else :
                if (unidad == 4) :
                    res = usuario / 100
                else :
                    if (unidad == 5) :
                        res = usuario / 10
                    else :
                        if (unidad == 7) :
                            res = usuario * 10
                        else :
                            print("Opción no válida")
    return(res)
    
    
#En caso de que las unidades que se vayan a convertir no sean prefijo hecto, se comparan por kilo
def kilo(unidad):
    """
funcion kilo, se usa cuando el tipo de unidad que da el usuario empieza con ese prefijo
recibe el segundo tipo de unidad, lo comprueba, y hace las operaciones necesarias para
covertir la unidad, devuelve res
@param tipo_unidad2, la compara para saber el segundo tipo de unidad
@return res, el valor convertido
"""
    if (unidad == 1) :
        res = usuario / 1000000
    else :
        if (unidad == 2) :
            res = usuario / 100000
        else :
            if (unidad == 3) :
                res = usuario / 10000
            else :
                if (unidad == 4) :
                    res = usuario / 1000
                else :
                    if (unidad == 5) :
                        res = usuario / 100
                    else :
                        if (unidad == 6) :
                            res = usuario / 10
                        else :
                            print("Opción no válida")
    return(res)
    
"""
Aquí terminan las funciones donde se convierten las unidades, y comienza el ciclo while, donde el usuario
puede escoger cuantas unidades va a convertir, en cuanto el responda "No" con el numero 2, se detendrá el
código

"""
repeticiones = int(input("Introduce la cantidad de unidades que vas a convertir: "))
i = 1
valores = []
while (i <= repeticiones):
    #Pequeño menú donde el usuario escoge las unidades (Volumen, longitud)
    print("1. Longitud \n 2. Volumen")
    unidad_general = int(input("Teclea el número de la opción que necesites: "))
    if (unidad_general == 1):
        # Menu donde el usuario escoge las unidades que quiera convertir
        print("1. Milímetros \n 2. Centímetros \n 3. Decímetros \n 4. Metros \n 5. Decámetro \n 6. Hectómetro \n 7. Kilómetro")
        tipo_deseada = int(input("Teclea el número de la opcion que necesites: "))
        # Menu donde el usuario escoge las unidades que tenga
        print("1. Milímetros \n 2. Centímetros \n 3. Decímetros \n 4. Metros \n 5. Decámetro \n 6. Hectómetro \n 7. Kilómetro")
        tipo_actual = int(input("Teclea el número de la opcion que tengas a convertir: "))
    elif (unidad_general == 2):
        # Menu donde el usuario escoge las unidades que quiera convertir
        print("1. Mililitros \n 2. Centilitros \n 3. Decilitros \n 4. Litros \n 5. Decalitros \n 6. Hectolitros \n 7. Kilolitros")
        tipo_deseada = int(input("Teclea el número de la opcion que necesites: "))
    # Menu donde el usuario escoge las unidades que tenga
        print("1. Mililitros \n 2. Centilitros \n 3. Decilitros \n 4. Litros \n 5. Decalitros \n 6. Hectolitros \n 7. Kilolitros")
        tipo_actual = int(input("Teclea el número de la opcion que tengas a convertir: "))
    #Se le pide al usuario el valor a convertir
    usuario = float(input("Introduce el valor a convertir: "))
    #Aquí se manda a llamar la funcion que sea necesaria a partir de el tipo de unidad
    if(tipo_deseada == 1):
        res = mili(tipo_actual)
    elif(tipo_deseada == 2):
        res = (centi(tipo_actual))
    elif(tipo_deseada == 3):
        res = (deci(tipo_actual))
    elif(tipo_deseada == 4):
        res = (sufijo(tipo_actual))
    elif(tipo_deseada == 5):
        res = (deca(tipo_actual))
    elif(tipo_deseada == 6):
        res = (hecto(tipo_actual))
    elif(tipo_deseada == 7):
        res = (kilo(tipo_actual))
    else:
        print("No válido")
    
    i = i + 1
    print(res)
    valores.append(res)
    
print("Los valores fueron\n",valores)




                            
                        
    
        
        
        