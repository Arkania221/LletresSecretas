"""
1. ¿Que se ha de hacer? Un juego de adivina la palabra

    1.1. La palabra es de 5 letras.
    
    1.2. Las letras tienes tres estados: Desconocida "-", 
    en la posicion correcta "O", en la posicion incorrecta "X"
         
    1.3. No se puede perder, el juego continua hasta ganar,
    entonces se muestra un mensaje de felicitaciones

2. ¿Como lo hacemos?

    2.1. Se precisa una funcion para generar letras pseudo-aleatorias,
    sin importar random. ESTO SE TIENE QUE ACLARAR QUE LLEVO UNA HORA
    MIRANDO COMO COÑO TOMAR UN VALOR QUE VARIE ENTRE INICIOS DE PROGRAMA
    
        2.1.2. Utilizo un aleatorizador que hice en un codigo anterior
    
        2.1.1. Se creara una lista con las letras del abecedario
        asi tendremos forma de seleccionarlas
    
    2.2. Se precisa una funcion principal que gestiones intentos
    y proporcione las pistas
    
        2.2.1. Para el gestionar si es el primer intento o no se hace un bool
        en el primer intento todas las palabras estaran ocultas, por cada nuevo 
        intento se gestiona la pista dada
        
        2.2.2. Se comparara el contenido de palabra y palabra oculta
    
    2.3. Se precisa usar metodos basados en parametros de entrada
    y salida de variables.
    
    2.4. No entiendo
"""

tamaño_palabra = 5

def Aleatorizador():

    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]
    
    palabra = []
    a = 4387438
    b = 98980
    m = 2**32 - 1
    semilla = 343
    
    for i in range(tamaño_palabra):
        semilla = int(((a * semilla + b) % m) % 27)
        resultado = abc[semilla]
        palabra.append(resultado)
    return(palabra)


def Pistas(palabra):
   
    desconocida = "-"
    posicionada = "O"
    desposicion = "X" 

   while True:

        
        
 


        


def Programa():
    palabra = Aleatorizador()
    Pistas(palabra)
    
    
Programa()