import pandas as pd

def resumenCotizacion(fichero):
    df= pd.read_csv(fichero,sep="/",decimal=",",thousands=".", index_col=0)
    return pd.DataFrame([df.min(),df.max(),df.mean()],index=["Valor Maximo","Valor Minimo","Valor promedio"])

print(resumenCotizacion(#importarfichero))
