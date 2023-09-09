#Funcion para convertir un numero decimal a octal, donde se recibe un digi a convertir en octal
def octal(dig):
    #Declaramos el divisor octal
    div = 8
    #Declaramos un array
    resto = []
    
    #Bluce while que se repite hasta se cumple hasta que dig sea mayor a  0
    while dig > 0:
        
        #Usamos el append para ir agregando los resultados de los restos en un array
        resto.append(dig % div)
        
        #Division del digito con el divisor octal
        dig = dig // div
        
    #Invertimos el array, ya que se lee los numero octal de abajo para arriba en las divisiones
    resto.reverse()
    
    #Transformamos el array en un string y lo guardamos en la variable octal_num
    octal_num = "".join(map(str, resto))
    
    #Retornamos el resultado
    return print("Numero octal:  " + octal_num) 


def hexa(dihexa):
    hexa = 16
    resto = []
    
    while dihexa > 0:
        resto.append(dihexa %  hexa)
        
        dihexa = dihexa // hexa
        
    resto.reverse()
    
    hexa_num = "".join(map(str, resto))
    
    return print("Numero hexadecimal " + hexa_num)
    
dig = int(input("Ingrese un digito a convertir en octal y hexa\n"))
dihexa = dig
print(octal(dig))
print(hexa(dihexa))







        
        