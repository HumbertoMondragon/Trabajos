"""
Proyecto python 
Conversor de unidades
En este programa puedes introducir el tipo de dato que requieres convertir
a partir de las unidades que tengas.
"""
import random


"""
Funciones para comparar el tipo de valor que se va a convertir,
independientemente si la medida sea de volumen, longitud, peso, todas
siguen losmismos prefijos y las mismas unidades. Se hace una función
para convertir a cada prefijo
"""
def aleatorio():
    num = random.randint(1,7)
    print("La opción aleatoria fue: ",num)
    return num

def mili(unidad):
    """
    funcion mili, se usa cuando el tipo de unidad que da el usuario empieza    
    con ese prefijo recibe el segundo tipo de unidad, lo comprueba, y hace
    las operaciones necesarias para covertir la unidad, devuelve res
    @param tipo_unidad2, la compara para saber el segundo tipo de unidad
    @return res, el valor convertido
    """
    if (unidad == 2) :
        res = usuario * 10
    elif(unidad == 3) :
        res = usuario * 100
    elif(unidad == 4) :
        res = usuario * 1000
    elif(unidad == 5) :
        res = usuario * 10000
    elif(unidad == 6) :
        res = usuario * 100000
    elif(unidad == 7) :
        res = usuario * 1000000
    else:
        print(usuario)
    return(res)

def centi(unidad):
    """
    funcion centi, se usa cuando el tipo de unidad que da el usuario empieza
    con ese prefijo recibe el segundo tipo de unidad, lo comprueba, y hace las
    operaciones necesarias para covertir la unidad, devuelve res
    @param tipo_unidad2, la compara para saber el segundo tipo de unidad
    @return res, el valor convertido
    """
    if (unidad == 1) :
        res = usuario / 10
    elif(unidad == 3) :
        res = usuario * 10
    elif(unidad == 4) :
        res = usuario * 100
    elif(unidad == 5) :
        res = usuario * 1000
    elif(unidad == 6) :
        res = usuario * 10000
    elif(unidad == 7) :
        res = usuario * 100000
    else:
        print(usuario)
    return(res)


def deci(unidad):
    """
    funcion deci, se usa cuando el tipo de unidad que da el usuario empieza
    con ese prefijo recibe el segundo tipo de unidad, lo comprueba, y hace
    las operaciones necesarias para covertir la unidad, devuelve res
    @param tipo_unidad2, la compara para saber el segundo tipo de unidad
    @return res, el valor convertido
    """
    if (unidad == 1) :
        res = usuario / 100
    elif(unidad == 2) :
        res = usuario / 10
    elif(unidad == 4) :
        res = usuario * 10
    elif(unidad == 5) :
        res = usuario * 100
    elif(unidad == 6) :
        res = usuario * 1000
    elif(unidad == 7) :
        res = usuario * 10000
    else:
        print(usuario)
    return(res)

                            

def sufijo(unidad):
    """
    funcion sufijo, se usa cuando el tipo de unidad que da el usuario empieza
    con ese prefijo recibe el segundo tipo de unidad, lo comprueba, y hace
    las operaciones necesarias para covertir la unidad, devuelve res
    @param tipo_unidad2, la compara para saber el segundo tipo de unidad
    @return res, el valor convertido
    """
    if (unidad == 1) :
        res = usuario / 1000
    elif(unidad == 2) :
        res = usuario / 100
    elif(unidad == 3) :
        res = usuario / 10
    elif(unidad == 5) :
        res = usuario * 10
    elif(unidad == 6) :
        res = usuario * 100
    elif(unidad == 7) :
        res = usuario * 1000
    else:
        print(usuario)
    return(res)


def deca(unidad):
    """
    funcion deca, se usa cuando el tipo de unidad que da el usuario empieza
    con ese prefijo recibe el segundo tipo de unidad, lo comprueba, y hace
    las operaciones necesarias para covertir la unidad, devuelve res
    @param tipo_unidad2, la compara para saber el segundo tipo de unidad
    @return res, el valor convertido
    """
    if (unidad == 1) :
        res = usuario / 10000
    elif(unidad == 2) :
        res = usuario / 1000
    elif(unidad == 3) :
        res = usuario / 100
    elif(unidad == 4) :
        res = usuario / 10
    elif(unidad == 6) :
        res = usuario * 10
    elif(unidad == 7) :
        res = usuario * 100
    else:
        print(usuario)
    return(res)




def hecto(unidad):
    """
    funcion hecto, se usa cuando el tipo de unidad que da el usuario empieza
    con ese prefijo recibe el segundo tipo de unidad, lo comprueba, y hace las
    operaciones necesarias para covertir la unidad, devuelve res
    @param tipo_unidad2, la compara para saber el segundo tipo de unidad
    @return res, el valor convertido
    """
    if (unidad == 1) :
        res = usuario / 100000
    elif(unidad == 2) :
        res = usuario / 10000
    elif(unidad == 3) :
        res = usuario / 1000
    elif(unidad == 4) :
        res = usuario / 100
    elif(unidad == 5) :
        res = usuario / 10
    elif(unidad == 7) :
        res = usuario * 10
    else:
        print(usuario)
    return(res)
    

def kilo(unidad):
    """
    funcion kilo, se usa cuando el tipo de unidad que da el usuario empieza
    con ese prefijo recibe el segundo tipo de unidad, lo comprueba, y hace
    las operaciones necesarias para  covertir la unidad, devuelve res
    @param tipo_unidad2, la compara para saber el segundo tipo de unidad
    @return res, el valor convertido
    """
    if (unidad == 1) :
        res = usuario / 1000000
    elif(unidad == 2) :
        res = usuario / 100000
    elif(unidad == 3) :
        res = usuario / 10000
    elif(unidad == 4) :
        res = usuario / 1000
    elif(unidad == 5) :
        res = usuario / 100
    elif(unidad == 6) :
        res = usuario / 10
    else:
        print(usuario)
    return(res)
    

repeticiones = int(input("\nIntroduce la cantidad de unidades que vas "
"a convertir: "))
i = 1
valores = []
while (i <= repeticiones):
    usuario = float(input("\nIntroduce el valor a convertir: "))
    print(" 1. Longitud \n 2. Volumen")
    unidad_general = int(input("Teclea el número de la opción que desees"
    " convertir: "))
    if (unidad_general == 1):
        print("\n1. Milímetros \n 2. Centímetros \n 3. Decímetros \n 4. Metros"
        "\n 5. Decámetro \n 6. Hectómetro \n 7. Kilómetro")
        tipo_actual = int(input("\nTeclea el número de la opcion que tengas "
        "a convertir: "))
        print("\n1. Milímetros \n 2. Centímetros \n 3. Decímetros \n 4. "
        "Metros \n 5. Decámetro \n 6. Hectómetro \n 7. Kilómetro"
        "\n 8. Aleatorio")
        tipo_deseada = int(input("\nTeclea el número de la opcion que"
        " necesites: "))
    elif (unidad_general == 2):
        print("\n1. Mililitros \n 2. Centilitros \n 3. Decilitros \n 4. Litros"
        "\n 5. Decalitros \n 6. Hectolitros \n 7. Kilolitros")    
        tipo_actual = int(input("\nTeclea el número de la opcion que tengas a"
        " convertir: "))
        print("\n1. Mililitros \n 2. Centilitros \n 3. Decilitros \n 4. Litros"
        "\n 5. Decalitros \n 6. Hectolitros \n 7. Kilolitros"
        "\n 8. Aleatorio")
        tipo_deseada = int(input("\nTeclea el número de la unidad a la que"
        " quieras llegar: "))
    if(tipo_deseada == 8):
        tipo_deseada = (aleatorio())
        
    #Aquí se manda a llamar la funcion que sea necesaria
    if(tipo_deseada == 1):
        resultado = mili(tipo_actual)
    elif(tipo_deseada == 2):
        resultado = (centi(tipo_actual))
    elif(tipo_deseada == 3):
        resultado = (deci(tipo_actual))
    elif(tipo_deseada == 4):
        resultado = (sufijo(tipo_actual))
    elif(tipo_deseada == 5):
        resultado = (deca(tipo_actual))
    elif(tipo_deseada == 6):
        resultado = (hecto(tipo_actual))
    elif(tipo_deseada == 7):
        resultado = (kilo(tipo_actual))
    else:
        print("No válido")
    
    i = i + 1
    print("\nEl valor es",resultado)
    valores.append(resultado)
print("\nLos valores fueron\n",valores)




                            
                        
    
        
        
        