def cliente (informacion:dict) -> dict:
    nombre = str(informacion ["nombre"])
    edad = int(informacion ["edad"])
    primer_ingreso = informacion ["primer_ingreso"]
    if(edad>18):#Primer condicional ---> atraccion xtreme
        if(primer_ingreso == True):
            xtreme=20000
            xtreme-=xtreme*0.05
            informacion["atracción"] = "X-Treme"
            informacion["apto"] = True
            informacion["total_boleta"]= xtreme
        else:
            xtreme=20000
            informacion["atracción"] = "X-Treme"
            informacion["apto"] = True
            informacion["total_boleta"]= xtreme
    elif(edad>=15 and edad <= 18):#segundo condicional ---> carros chocones
        if(primer_ingreso == True):
            carros=5000
            carros=carros-carros*0.07
            informacion["atracción"] = "Carros chocones"
            informacion["apto"] = True
            informacion["total_boleta"]= carros
            #informacion["primer_ingreso"] = False # COMO ARREGLAR PARA QUE ME IMPRIMR EL PRIMER INGRESO SEA TRUE AL INICIO Y LUEGO SI LO CAMBIE A FALSE
        else:
            carros=5000
            informacion["atracción"] = "Carros chocones"
            informacion["apto"] = True
            informacion["total_boleta"]= carros
    elif(edad>=7 and edad < 15):
        if(primer_ingreso == True):#Tercer condicional ---> sillas voladoras
            sillas=10000
            sillas=sillas-sillas*0.05
            informacion["atracción"] = "Sillas voladoras"
            informacion["apto"] = True
            informacion["total_boleta"]= sillas
            #informacion["primer_ingreso"] = False # COMO ARREGLAR PARA QUE ME IMPRIMR EL PRIMER INGRESO SEA TRUE AL INICIO Y LUEGO SI LO CAMBIE A FALSE
        else:
            sillas=10000
            informacion["atracción"] = "Sillas voladoras"
            informacion["apto"] = True
            informacion["total_boleta"]= sillas
    elif( edad <7):
        informacion["atracción"] = "N/A"
        informacion["apto"] = False
        informacion["total_boleta"]= "N/A"
        
    informacion = {
        "nombre" : nombre,
        "edad": edad,
        "atraccion": informacion["atracción"],
        "apto":informacion["apto"],
        "primer_ingreso":informacion["primer_ingreso"],
        "total_boleta":informacion["total_boleta"]


    }   
    return informacion
    
informacion={
    "id_cliente" : 1,
    "nombre" : "Tatiana Ruiz",
    "edad" : 8,
    "primer_ingreso" : False }

print(cliente(informacion))