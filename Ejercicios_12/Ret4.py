from functools import reduce
ventas=[
    [6587, ("3268", 4, 25842.99), ("8274",18,23254.99), ("6548", 9, 48951.95), ("2547", 5, 8951.95)], 
  [6588, ("1254", 3, 115362.58), ("9744", 2, 99235.66)],
 
 ]



def facturacion(datos:list):
    numfact= datos.pop(0)
    recorrer_lista=list(map(lambda x:x[1]*x[2],datos))
    total=reduce(lambda x, y : x + y ,recorrer_lista)
    if total<600000:
        total +=25000

    return f"La fatura {numfact} tiene un total en pesos de {total:,.2f}"

def ordenes(rutinaContable):
    print('----------------- Inicio Registro diario --------------------------')
    imprimir = list(map(facturacion,rutinaContable))
    for x in imprimir:
        print(x)
    print('----------------- Fin Registro diario -----------------------------')










