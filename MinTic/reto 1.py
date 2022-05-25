# print('Bienvenido a su entidad bancaria') //no necesitamos información extra

# Usuario = input('Digite Usuario ' )
Penalidad = 0.02
InteresesGenerados = 0.03
MontoFinal = 0

print('Bienvenido usuario' , Usuario)

# CapitalInicial = int(input('Ingrese su capital inicial ' ));    //corregir los inputs
# TiempoDePermanencia = int(input('Digite su tiempo de permanencia ' )) //corregir los inputs


# toca crear una función para que se ejecute al ser llamada al final.
if TiempoDePermanencia >= 2:
    MontoFinal = ((CapitalInicial * InteresesGenerados * TiempoDePermanencia )/12) + CapitalInicial
else:
    MontoFinal = CapitalInicial - (CapitalInicial * Penalidad) 

# llamar la función al final del texto.


# se pide retornar un valor, en este caso debe ser "return" y esté va dentro de la función.
print('para el usuario' , Usuario , 'La cantidad de dinero a recibir, segun el monto inicial' , CapitalInicial , 'Para un tiempo de ',TiempoDePermanencia  , 'Mes(es) es de:' , MontoFinal)

#el no necesita "mostrar" el resultado, necesita que se retorne un valor resultante, para el BOT evaluar igualdad de resultado(el de nosotros con el del sistema) ) TEST
