informacion = {
    "id": 1,
    "nombre": "johana Fernandez",    
    "edad": 20,
    "primer_ingreso": True,

}

def cliente (informacion:dict):

    atraccion = {
    "X-Treme" : 20000,
    "Carros chocones" : 5000,
    "Sillas voladoras" : 10000
    }
    
    if informacion["edad"] > 18 and informacion["primer_ingreso"] == True:
        informacion["atraccion"]= "X-Treme"
        informacion["total_boleta"] = (atraccion["X-Treme"])-(atraccion["X-Treme"]*0.05)
        informacion["apto"] = True

    elif informacion["edad"] > 18 and informacion["primer_ingreso"] == False:
        informacion["atraccion"]= "X-Treme"
        informacion["total_boleta"] = (atraccion["X-Treme"])
        informacion["apto"] = True

    elif informacion["edad"] >= 15 and informacion["edad"] <18 and informacion["primer_ingreso"] == True:
        informacion["atraccion"]= "Carros chocones"
        informacion["total_boleta"] = (atraccion["Carros chocones"])-(atraccion["Carros chocones"]*0.07)
        informacion["apto"] = True

    elif informacion["edad"] >= 15 and informacion["edad"] <18 and informacion["primer_ingreso"] == False:
        informacion["atraccion"]= "Carros chocones"
        informacion["total_boleta"] = (atraccion["Carros chocones"])
        informacion["apto"] = True

    elif informacion["edad"] >= 7 and informacion["edad"] <15 and informacion["primer_ingreso"] == True:
        informacion["atraccion"]= "Sillas voladoras"
        informacion["total_boleta"] = (atraccion["Sillas voladoras"])-(atraccion["Sillas voladoras"]*0.05)
        informacion["apto"] = True
   
    elif informacion["edad"] >= 7 and informacion["edad"] <15 and informacion["primer_ingreso"] == False:
        informacion["atraccion"]= "Sillas voladoras"
        informacion["total_boleta"] = (atraccion["Sillas voladoras"])
        informacion["apto"] = True

    else:
        informacion["atraccion"]= "N/A"
        informacion["total_boleta"] = "N/A"
        informacion["apto"] = False


    otro_diccionario = {
        'nombre': informacion["nombre"],
        'edad': informacion["edad"],
        'atraccion': informacion["atraccion"],
        'apto': informacion["apto"],
        'primer_ingreso': informacion["primer_ingreso"],
        'total_boleta': informacion["total_boleta"]
        }
    
print(otro_diccionario)
print (cliente(informacion))
