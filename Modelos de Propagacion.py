import math as m

#Programa Propagacion de Ondas
#Nombre: Jorge Montalvo

#Definimos las funciones para los modelos que tenemos

#Modelo Exponente de perdida
def expPerdida():
    print("El modelo exponente de perdida en el esacio tiene un factor n cuyos valores tipicos en entornos son: ")
    print("Ingrese el valor de n en base a la tabla:");
    print("-------------------------------------------------------------")
    print("Opcion -        Entorno              -          Factor n     ")
    print("   1    -    EspacioLibre            -               2       ")
    print("   2    -   AreaUrbana RadioCelular  -          2.7 a 3.5    ")
    print("   3    -   Sombreado RadioCelular   -            3 a 5      ")
    print("   4    -    LOS en edificios        -          1.6 a 1.8    ")
    print("   5    -   ObstruccionEdificios     -            4 a 6      ")
    print("   6    -   ObstruccionFabricas      -            2 a 3      ")
    print("-------------------------------------------------------------")
    n=float(input("Ingrese el valor de n:"))
    if n==2:
        print("EspacioLibre")
    elif n>=2.7 and n<=3.5:
        print("AreaUrbana RadioCelular")
    elif n>=3 and n<=5:
        print("Sombreado RadioCelular")
    elif n>=1.6 and n<=1.8:
        print("LOS en edificios ")
    elif n>=4 and n<=6:
        print("ObstruccionEdificios")
    elif n>2 and n<=3:
        print("ObstruccionFabricas")
    #Ingresamos las variables con las que vamos a trabajar
    #L=20log(F)+10nlog(D)-147.56
    D=float(input("Ingrese la distancia entre antenas medida en metros:"))
    F=float(input("Ingrese la frecuencia en Hz:"))
    Factor=10*n
    Ld=m.log(D,10)
    Lf=m.log(F,10)
    #Definomos la perdida en el espacio libre
    L=(20*Lf)+(Factor*Ld)-147.56

    print("La perdida en el espacio con exponente es: L(dB)= ",L)
    
    
    
#Modelo Okumura-Hata
def okumura():
    print("Este modelo se caracteriza por ser usado en espacion urbanos y suburbanos")
    F=float(input("Ingrese la frecuencia en MHz:"))
    Ht=float(input("Ingrese la altura de la antena de transmisión en metros: "))
    Hr=float(input("Ingrese la altura de la antena de recepcion en metros: "))
    D=float(input("Ingrese la distancia entre las antenas en Km (1km-20Km): "))
    L=0
    Control=0
    if F<=300:
        #Para frecuencias menorea a 300Mhz
        Ahr=8.29*(m.pow(m.log(1.54*Hr,10),2))-1.1
        L=69.55+(26.56*m.log(F,10))-(13.8*m.log(Ht,10))-Ahr+(m.log(D,10)*(44.9-(6.55*m.log(Ht,10))))
        t_u=int(input('Elija el tipo de urbanización SubUrbano[1] o Rural[2]: [1/2]: '))
        if t_u==1:
            Control=1
        elif t_u==2:
            Control=2
    elif F>300 and F<1500:
        #Para frecuencias ente 300 a 1500 MHz
        Ahr=3.2*(m.pow(m.log(11.75*Hr,10),2))-4.97
        L=69.55+(26.56*m.log(F,10))-(13.8*m.log(Ht,10))-Ahr+(m.log(D,10)*(44.9-(6.55*m.log(Ht,10))))
        t_u=int(input('Elija el tipo de urbanización SubUrbano[1] o Rural[2]: [1/2]: '))
        if t_u==1:
            Control=1
        elif t_u==2:
            Control=2
    elif F>= 1500 and F<=2000:
        #Para Frecuencias mayores Implementamos el Modelo Hata Modificado
        Ahr=3.2*(m.pow(m.log(11.75*Hr,10),2))-4.97
        print("Para Frecuencias entre 1500-2000 MHz tenemos las siguientes Opciones de la tabla")
        print("----------------------------------------")
        print("  Tipo de Urbanizacion    -   Valor CM  ")
        print("       Sub-Urbano         -       0     ")
        print("      Urbano-Grande       -       3     ")
        print("----------------------------------------")
        Opcion=int(input("Elija modelo [1/2]: "))
        CM=0
        if Opcion==1:
            CM=0
        elif Opcion==2:
            CM=CM+3
        L=46.3+(33.9*m.log(F,10))-(13.82*m.log(Ht,10))-Ahr+(m.log(D,10)*(44.9-(6.55*m.log(Ht,10))))+CM
        
    #Para estimar en area suburbana en frecuencias menores de 1500 MHz en areas suburbanas y vacias creamos una variable de control
    
    if Control==1:
        L=L-(2*m.pow(m.log((F/28),10),2))-5.4
        print("La perdida es: L(dB)",L)
    elif Control==2:
        L=L-(4.78*m.pow(m.log((F/28),10),2))-(18.733*m.log(F,10))-40.98
        print("La perdida es: L(dB)",L)
    else:
        print("La perdida es: L(dB)",L)

    
    
    
   
    
    



#Programa Principal
print("--------------------------------------")
print("**************Bienvenido**************")
print("--------------------------------------")
print("Elija el modelo de propagación:")
print("1)Modelo de Propagación-Exponente de perdida")
print("2)Modelo de Propagación-Okumura Hata")
e=int(input("Escoja el modelo(1,2):"));
while e!=1 and e!=2:
    e=int(input("Escoja un modelo de la lista entre(1,2):"));
if e==1:
    #Funcion del Modelo -Exponente de Perdida
    expPerdida()
elif e==2:
    #Funcion del Modelo -Okumura Hata
    okumura()
