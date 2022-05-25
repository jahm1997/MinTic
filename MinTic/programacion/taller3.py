def AutoPartes(ventas:list):
    agenda = {}
    numero = (len(ventas))
    numeracion = 0
    while numeracion < numero:
        agenda[numeracion]= ventas[numeracion]
        numeracion += 1
    return agenda
print(AutoPartes([
    (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
    (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
    (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
    (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
    (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]))

def consultaRegistro(ventas,idProducto):
    contenedor=ventas.values()
    respuesta = "No hay registro de venta de ese producto"
    encontrados = []
    for buscamos in contenedor:
        if idProducto in buscamos:
            encontrados.append(f"Producto consultado : {buscamos[0]}  Descripción  {buscamos[1]}  #Parte  {buscamos[2]}  Cantidad vendida  {buscamos[3]}  Stock  {buscamos[4]}  Comprador {buscamos[5]}  Documento  {buscamos[6]}  Fecha Venta  {buscamos[7]}")
    print(respuesta if len(encontrados) == 0 else "\n".join(encontrados))

consultaRegistro(AutoPartes([
    (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
    (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
    (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
    (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
    (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)