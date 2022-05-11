#Entrada 
print("Escriba un numero entero")
numero=int(input())
#Proceso
if numero==1: 
    semana="lunes"
elif numero==2: 
    semana="martes"
elif numero==3: 
    semana="miercolesa"
elif numero==4: 
    semana="jueves"
elif numero==5: 
    semana="viernes"
elif numero==6: 
    semana="sabado"
elif numero==7: 
    semana="domingo"

else: print("no esta dentro de la semana")

#Salida
print("es", semana)