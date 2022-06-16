def AutoPartes(ventas:list):
    j=len(ventas)
    dicc={}
    for i in range(j):
        dicc[i]=[ventas[i]]
  
    return dicc
    
def consultaRegistro(ventas,idproducto): 
    dicc2={}
    for x in ventas:
        if idproducto==ventas[x][0][0]:
            dicc2[x]=ventas[x]
    res=''
    if len(dicc2)==0:
        res="No hay registro de venta de ese producto"
    else:
        for i in dicc2:
            res+= f"Producto consultado : {dicc2[i][0][0]} Descripción {dicc2[i][0][1]} #Parte {dicc2[i][0][2]} Cantidad vendida {dicc2[i][0][3]} Stock {dicc2[i][0][4]} Comprador {dicc2[i][0][5]} Documento {dicc2[i][0][6]} Fecha Venta {dicc2[i][0][7]}\n"
    return print(res)
    
consultaRegistro(AutoPartes([
 (9852,'Culata', 'XC9875',2,165,'Luis Molero',3455846,'14/06/2020'),
 (9852,'Culata', 'XC9875',2,165,'Jose Mejia',1355846,'14/06/2020'),
 (2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'14/06/2020'),
 (5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'14/06/2020')]), 9852)