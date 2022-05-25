informacion = {
	"id_cliente" : 1,
	"nombre" : "Johana Fernandes",
	"edad" : 3,
	"primer_ingreso" : False
}



def cliente (informacion:dict): 

    atraccion = {
    "X-Treme" : 20000,
    "Carros chonoces" : 5000,
    "Sillas voladoras" : 10000
    }
	
  
    if informacion["edad"] > 18 and informacion["primer_ingreso"]  == True :
        informacion["total_boleta"] = (atraccion["X-Treme"])-(atraccion["X-Treme"]*0.05)
        informacion["apto"] = True
        informacion["atraccion"] = "X-Treme"
    
    elif informacion["edad"] > 18 and informacion["primer_ingreso"]  == False :
        informacion["total_boleta"] = (atraccion["X-Treme"])
        informacion["apto"] = True
        informacion["atraccion"] = "X-Treme"
    
    elif informacion["edad"] >= 15 and informacion["edad"] <=18 and informacion["primer_ingreso"] == True:
        informacion["total_boleta"] = (atraccion["Carros chonoces"])-(atraccion["Carros chonoces"]*0.07)
        informacion["apto"] = True
        informacion["atraccion"] = "Carros chonoces"

    elif informacion["edad"] >= 15 and informacion["edad"] <=18 and informacion["primer_ingreso"] == False:
        informacion["total_boleta"] = (atraccion["Carros chonoces"])
        informacion["apto"] = True
        informacion["atraccion"] = "Carros chonoces"
    elif informacion["edad"] >=7 and informacion["edad"] < 15 and informacion["primer_ingreso"] == True:
        informacion["total_boleta"] = (atraccion["Sillas voladoras"])-(atraccion["Sillas voladoras"]*0.05)
        informacion["apto"] = True
        informacion["atraccion"] = "Sillas voladoras"
    elif informacion["edad"] >=7 and informacion["edad"] < 15 and informacion["primer_ingreso"] == False:
        informacion["total_boleta"] = (atraccion["Sillas voladoras"])
        informacion["apto"] = True
        informacion["atraccion"] = "Sillas voladoras"
    else: 
        informacion["apto"] = False
        informacion["atraccion"] = "N/A"
        informacion["total_boleta"] = "N/A"

    
    return {
        "nombre" : informacion["nombre"],
        "edad" : informacion["edad"],
        "atraccion" : informacion["atraccion"],
        "apto" : informacion["apto"],
        "primer_ingreso" : informacion ["primer_ingreso"],
        "total_boleta" : informacion["total_boleta"]        
    }

print (cliente(informacion))