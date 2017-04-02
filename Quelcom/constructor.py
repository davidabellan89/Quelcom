import json
import pickle

class Bicho():
    def __init__(self):
        self.nombre=""
        self.vivo=True
        self.nivel=1
        self.player=""
        self.vidamax=""
        self.vida=""
        self.defensa=""
        self.ataque=""
        self.prob_critico=""
        self.mult_critico=""
        self.velocidad=""
        self.posicion=""
        self.alterado=["Normal"]
        self.image1=""
        self.image2=""
        self.image3=""
        self.image4=""
        self.image5=""
        self.habilidad1=""
        self.habilidad2=""
        self.habilidad3=""
        self.habilidad4=""
      

#listabichos=[bicho1,bicho2]
def leer():
    archivo=input("Por favor, introduce la ruta del archivo  ")
    file=open(archivo, 'rb')
    listabichos=pickle.load(file)
    file.close()    
    print("Nombre\tvida\tdefensa\tataque\tcritico\tvelocidad\t habilidades:")
    for bicho in listabichos:
        print(bicho.nombre,"\t", bicho.vidamax,"\t", bicho.defensa,"\t",bicho.ataque,"\t", bicho.prob_critico,"/",bicho.mult_critico,"\t", bicho.velocidad,"\t", bicho.habilidad1, bicho.habilidad2, bicho.habilidad3, bicho.habilidad4)
    
    
def crear():
    archivo=input("Por favor, introduce la ruta del archivo  ")
    file=open(archivo, 'wb')
    salir="n"
    
    bicho1=Bicho()
    bicho2=Bicho()
    bicho3=Bicho()
    bicho4=Bicho()
    bicho5=Bicho()
    bicho6=Bicho()
    bicho7=Bicho()
    bicho8=Bicho()

    listabichos=[bicho1, bicho2, bicho3, bicho4, bicho5, bicho6, bicho7, bicho8]

    for bicho in listabichos:
        bicho.nombre=input("Introduce el nombre de un bicho: ")
        bicho.player=int(input("A qué player pertenece? "))
        bicho.vidamax=int(input("Introduce la vida máxima del bicho: "))
        bicho.vida=bicho.vidamax
        bicho.defensa=int(input("Introduce la defensa: "))
        bicho.ataque=int(input("Introduce el ataque: "))
        bicho.prob_critico=int(input("Cuanto ha de salir en el dado para critico? "))
        bicho.mult_critico=float(input("Por cuanto multiplicamos si sale crítico? "))
        bicho.velocidad=int(input("Cual es la velocidad? "))
        bicho.posicion=int(input("Introduce la posicion del bicho: "))
        bicho.image1=input("Escribe la ruta de la imagen 1: ")
        bicho.image2=input("Escribe la ruta de la imagen 2: ")
        bicho.image3=input("Escribe la ruta de la imagen 3: ")
        bicho.image4=input("Escribe la ruta de la imagen 4: ")
        bicho.image5=input("Escribe la ruta de la imagen 5: ")
        bicho.habilidad1=input("Escribe el nombre de la habilidad 1: ")
        bicho.habilidad2=input("Escribe el nombre de la habilidad 2: ")
        bicho.habilidad3=input("Escribe el nombre de la habilidad 3: ")
        bicho.habilidad4=input("Escribe el nombre de la habilidad 4: ")
        
        a=input("Qué quieres hacer?\n1.-Introducir otro bicho \n2.-salir ")
        if (a=="2"):
            salir=input("Quieres salir? Y/N  ")
            if (salir=="Y"):
                break
    pickle.dump(listabichos, file)
    file.close()
    
def modificar():
    archivo=input("Por favor, introduce la ruta del archivo  ")
    file=open(archivo, 'rb')
    listabichos=pickle.load(file)
    file.close()
    x=0
    print("Nombre\tvida\tdefensa\tataque\tcritico\tvelocidad\t habilidades:")
    for bicho in listabichos:
        print(x,bicho.nombre,"\t", bicho.vidamax,"\t", bicho.defensa,"\t",bicho.ataque,"\t", bicho.prob_critico,"/",bicho.mult_critico,"\t", bicho.velocidad,"\t", bicho.habilidad1, bicho.habilidad2, bicho.habilidad3, bicho.habilidad4)
        x+=1
    y=int(input("Qué bicho quieres modificar?"))
    modi=listabichos[y]
    print("1.-Imágenes\n2.-posición\n3.-nombre\n4.-estadisticas")
    z=int(input("Qué quieres modificar?"))
    if (z==1):
        modi.image1=input("Escribe la ruta de la imagen 1: ")
        modi.image2=input("Escribe la ruta de la imagen 2: ")
        modi.image3=input("Escribe la ruta de la imagen 3: ")
        modi.image4=input("Escribe la ruta de la imagen 4: ")
        modi.image5=input("Escribe la ruta de la imagen 5: ")
    elif (z== 2):
        modi.posicion=int(input("Introduce la posicion del bicho: "))
    elif(z==3):
        modi.nombre=input("Introduce el nombre nuevo:")
    elif(z==4):
        print("1.-Vida máxima\n2.-defensa\n3.-ataque\n4.velocidad\n5.Prob. critico\n 6.Multipl.critico")
        z=int(input("Qué estadísticas quieres modificar?"))
        if z==1:
            modi.vidamax=int(input("Introduce su nueva vida máxima"))
        if z==2:
            modi.defensa=int(input("Introduce su nueva defensa"))
        if z==3:
            modi.ataque=int(input("Introduce su nuevo ataque"))
        if z==4:
            modi.velocidad=int(input("Introduce su neva velocidad"))
        if z==5:
            modi.prob_critico=int(input("Introduce su nueva probabilidad de critico"))
        if z==6:                  
            modi.mult_critico=omt(input("Introduce su nueva multiplicación de critico"))
            
    file=open(archivo, 'wb')
    pickle.dump(listabichos, file)
    
def main():
    a="x"
    x=0
    while a!="Y":
        x=int(input("Qué deseas hacer?: \n1.-Abrir un archivo \n2.-Crear un archivo\n3.-Modificar un archivo\n4.- Salir\n"))
        if(x<1 or x>4):
            print("Número incorrecto, prueba otra vez")
        elif(x==1):
            leer()
        elif(x==2):
            crear()
        elif(x==3):
            modificar()
        elif(x==4):
            a=input("Quieres salir? Y/N  ")



if __name__=="__main__":
    main()


