prueba=[
 (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
 (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
 (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
 (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
 (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]

def AutoPartes(ventas:list):

    dVentas=dict()
    for idProducto,dProducto,pnProducto,cvProducto,sProducto,nComprador,cComprador,fVenta in ventas:        
        if dVentas.get(idProducto) == None:            
            dVentas[idProducto] = list()                 
        dVentas[idProducto].append((dProducto,pnProducto,cvProducto,sProducto,nComprador,cComprador,fVenta)) 
    return dVentas

print(AutoPartes(prueba))

def consultaRegistro(ventas,idProducto):
    dBusqueda = str()
    dConsulta = ventas
    print (dConsulta)
   
    if idProducto in dConsulta.keys():
        print(idProducto)
        Content = dConsulta[idProducto]
        print(Content)
        for i in range(len(Content)):
           
            dBusqueda += f'Producto consultado : {idProducto}  Descripción  {Content[i][0]}  #Parte  {Content[i][1]}  Cantidad vendida  {Content[i][2]}  Stock  {Content[i][3]}  Comprador {Content[i][4]}  Documento  {Content[i][5]}  Fecha Venta  {Content[i][6]} \n'
          
        dBusqueda = dBusqueda[:-1]           
    else:
       
        dBusqueda = 'No hay registro de venta de ese producto'
       
    print(dBusqueda)

consultaRegistro(AutoPartes(prueba), 2010)

### FORMA 1

# def AutoPartes(ventas: list):
#     return dict(zip(range(len(ventas)),ventas))

# def consultaRegistro(ventas:dict, idProducto):
#     bandera = False
#     for valor in ventas.values():
#         if valor[0] == idProducto:
#             print("Encontrado")
#             bandera = True
#     if bandera == False:
#         print("No encontrado")
        
# FORMA 2 CODIGO PROPIO
# def AutoPartes(ventas: list):
#     retorno = []
#     for venta in ventas:
#         dicc = {"idProd":venta[0],
#                 "dProducto":venta[1],
#                 "pnProducto":venta[2],
#                 "cvProducto":venta[3],
#                 "sProducto":venta[4],
#                 "nComprador":venta[5],
#                 "cComprador":venta[6],
#                 "fVenta":venta[7],
#                 }
#         retorno.append(dicc)
#     return retorno

# def consultaRegistro(ventas:dict, idProducto):
#     find = False
#     for venta in range(len(ventas)):
#         if ventas[venta]["idProd"] == idProducto:
#             print(f"Producto consultado : {ventas[venta]['idProd']} Descripción {ventas[venta]['dProducto']} #Parte {ventas[venta]['pnProducto']} Cantidad vendida {ventas[venta]['cvProducto']} Stock  {ventas[venta]['sProducto']} Comprador {ventas[venta]['cComprador']} Documento {ventas[venta]['idProd']} Fecha Venta {ventas[venta]['fVenta']}")
#             find = True
#     if find == False:
#         print("no encontrado")
        
        
## FORMA 3


# def AutoPartes(ventas: list):
#     venta = {}
#     for i in range(len(ventas)):
#         venta.update({i:ventas[i]})
#     return venta

# def consultaRegistro(venta, idProducto):
#     existe = False 
#     for item in  venta.values():
#         if item[0] == idProducto:
#             print(f"Producto consultado : {idProducto} Descripción {item[1]} #Parte {item[2]} Cantidad vendida {item[3]} Stock  {item[4]} Comprador {item[5]} Documento {item[6]} Fecha Venta {item[7]}")
#             existe = True
#     if existe != True:
#         print("No hay registro de venta de ese producto")


## FORMA 4


# def AutoPartes(ventas: list) :
#     venta_autopartes = {}
#     for idProducto, dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVentas in ventas:
#         if venta_autopartes.get(idProducto) ==None:
#             venta_autopartes[idProducto]=[]
#         venta_autopartes[idProducto].append((dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVentas))
#     return venta_autopartes



# def consultaRegistro(ventas, idProducto):
#     if idProducto in ventas:
#         for dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVentas in ventas[idProducto]:
#             print("Producto consultado :", idProducto, " Descripción ", dProducto,
# " #Parte ", pnProducto, " Cantidad vendida ", cvProducto, " Stock ",
# sProducto, " Comprador", nComprador, " Documento ", cComprador, " Fecha Venta ", fVentas)

#     else:
#         print("No hay registro de venta de ese producto")
        
        
## FORMA 5

# def AutoPartes(ventas:list):
#     agenda = {}
#     numero = (len(ventas))
#     numeracion = 0
#     while numeracion < numero:
#         agenda[numeracion]= ventas[numeracion]
#         numeracion += 1
#     return agenda

# def consultaRegistro(ventas,idProducto):
#     contenedor=ventas.values()
#     respuesta = "No hay registro de venta de ese producto"
#     encontrados = []
#     for buscamos in contenedor:
#         if idProducto in buscamos:
#             encontrados.append(f"Producto consultado : {buscamos[0]}  Descripción  {buscamos[1]}  #Parte  {buscamos[2]}  Cantidad vendida  {buscamos[3]}  Stock  {buscamos[4]}  Comprador {buscamos[5]}  Documento  {buscamos[6]}  Fecha Venta  {buscamos[7]}")
#     print(respuesta if len(encontrados) == 0 else "\n".join(encontrados))


# print(AutoPartes(ventas))
# consultaRegistro(AutoPartes(ventas),2010)
# consultaRegistro(AutoPartes(ventas),2010)