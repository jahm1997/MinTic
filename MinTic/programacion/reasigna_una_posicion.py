laprimera = ("hola", "mama", "papa", "helado", "delicioso" )
lasegunda = ("como te va", "como estás", "saludos!!")

def insertarPosicion(duple1):
    
    posicion = int(input("insetar en que pocisión quiere insertar su elemento: ")) # 
    elementoAInsertar = (input("inserte la palabra a ingresar: "),)
    nuevaDuple = duple1[0:posicion] + elementoAInsertar + duple1[posicion+1:]
    return nuevaDuple
    
print(insertarPosicion (laprimera))
print("jajajajjajajaajaja")