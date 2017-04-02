import pygame
pygame.init()
import pickle
import habilidades

NEGRO  = ( 0,  0,  0)
BLANCO = (255, 255, 255)
NARANJA=(255, 133, 51)

class Bicho():
    def __init__(self):
        self.nombre = ""
        self.vivo=True
        self.nivel=5
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

class Carta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface([150,250])
        self.image.fill(NEGRO)
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.bicho=""
        self.activo=False
        self.objetivable=False
        self.recursos=5

habilidadactivada=pygame.image.load("images/habilidad.png")
habilidadseleccionada=pygame.image.load("images/habilidadseleccionada.png")
habilidadbloqueada=pygame.image.load("images/habilidadbloqueada.png")
ataqueimg=pygame.image.load("images/ataque.png")
paradoimg=pygame.image.load("images/parado.png")

class BotonHabilidad(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=(habilidadbloqueada)
        self.rect = self.image.get_rect()
        self.activo=False
        self.disponible=False
        self.numero=""
        self.carta=""
        self.habilidad=""
        self.objetivo=""  
        self.contador=0
        self.contaturnos=0
        self.turnos=0
        self.expl0=""
        self.expl1=""
        self.expl2=""
        self.expl3=""
atacante= BotonHabilidad()
apuntando=False
class Botonmaster(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image=pygame.Surface([85,85])
        self.image.fill(NEGRO)
        self.image.set_colorkey(NEGRO)
        self.rect=self.image.get_rect()
        pygame.draw.circle(self.image,  BLANCO,
            (self.rect.x + 43, self.rect.y + 43), 42, 0)

master = Botonmaster()
master.rect.x=1104
master.rect.y=605
botonniveles=Botonmaster()
botonniveles.rect.x=1104
botonniveles.rect.y=519

#declaraciones de lo jugadores que usaremos posteriormente
class Player():
    def __init__(self, num):
        self.numero=num
        self.recursos=0

player1=Player(1)
player2=Player(2)






#importar los bichos del documento bichos.txt
file=open('bichos.txt', 'rb')
listabichos=pickle.load(file)
file.close()
for bicho in listabichos:
    bicho.vida=bicho.vidamax
#generar los sprites encima de cada bicho
listacartas=pygame.sprite.Group()
listabotones=pygame.sprite.Group()

for bicho in listabichos:
    carta=Carta()
    carta.bicho=bicho
    carta.rect.x=(180+(230*(bicho.posicion-1)))
    carta.rect.y=(80+((bicho.player-1)*300))
    listacartas.add(carta)






#declaraciones iniciales con los elementos que definen la pantalla para todas las funciones

dimensiones=(1200,700)
pantalla=pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Prototipo Quelcom")
tablero = pygame.image.load("images/tablero.png").convert()
reloj = pygame.time.Clock()
fuentestats = pygame.font.Font(None, 20)
fuentenombre = pygame.font.Font(None, 30)
fuenteplayers=pygame.font.Font(None, 30)
fuentecritico=pygame.font.Font(None,15)
dice=pygame.image.load("images/dicesprite.jpg").convert()
diceroll=1

#generar los botones con los que le daremos al asunto
a=0
b=0
for carta in listacartas:
    for i in range(5):
        x=carta.bicho.posicion
        y=carta.bicho.player
        boton=BotonHabilidad()
        boton.rect.x=(180+(230*(x-1)))
        boton.rect.y=(80+((y-1)*300)+(i*50))
        boton.carta=carta
        boton.velocidad=carta.bicho.velocidad
        if (a%5==0):
            boton.habilidad="Atacar"
            a=0
            boton.disponible=True
            boton.numero=0
        else:
            if (a==1):
                boton.habilidad=carta.bicho.habilidad1
                boton.disponible=True
                boton.numero=1
            elif(a==2):
                boton.habilidad=carta.bicho.habilidad2
                boton.numero=2
            elif(a==3):
                boton.habilidad=carta.bicho.habilidad3
                boton.numero=3
            elif(a==4):
                boton.habilidad=carta.bicho.habilidad4
                boton.numero=4
        listabotones.add(boton)
        a+=1
listabotones=habilidades.asignarturnos(listabotones)
listabotones=habilidades.asignarexplicaciones(listabotones)
#declaraciones de listas y booleaons necsarias para las habilidades:
objetivosdefender=[]
cazabool=False
contraataquebool=False
templanzabool=False
venganzabool=False
sabiduriabool=False
tooltipbool=False
berserkbool=False
ojoletalbool=False
ultimobool=False
llamaralasangrebool=False
madretierrabool=False
mensaje=fuenteplayers.render(boton.carta.bicho.nombre+" ha utilizado "+boton.habilidad, True, NEGRO)


#Función para que no se borre la pantalla directamente
def esperar(x):
    done=False
    contador=0
    while not done:
            contador+=1
            if contador==x:
                return 0
                break
            for evento in pygame.event.get():
                if evento.type==pygame.KEYDOWN:
                    if evento.key==pygame.K_SPACE:
                        contador=x-1
            reloj.tick(20)

#Animación cuando el ataque acierta
def animacion(imagen, objetivo):
    for i in range(10):
        x=objetivo.bicho.posicion
        y=objetivo.bicho.player
        pantalla.blit(imagen,(180+(230*(x-1)),80+((y-1)*300)),((i*150),0,150,250))
        pygame.display.flip()
        reloj.tick(20)
        
#Elegir objetivos para las habilidades que lo requieran
def apuntarenemigos(boton):
    global apuntando
    global atacante
    apuntando=True
    atacante=boton
    mensaje=fuenteplayers.render("Elige un objetivo para la habilidad", True, NEGRO)
    for carta in listacartas:
        if carta.bicho.player!=boton.carta.bicho.player:
            carta.objetivable=True
            
def apuntaramigos(boton):
    global apuntando
    global atacante
    apuntando=True
    atacante=boton
    mensaje=fuenteplayers.render("Elige un objetivo para la habilidad", True, NEGRO)
    for carta in listacartas:
        if carta.bicho.player==boton.carta.bicho.player:
            carta.objetivable=True
            carta.activo=False
            
def apuntartodos(boton):
    global apuntando
    global atacante
    apuntando=True
    atacante=boton
    mensaje=fuenteplayers.render("Elige un objetivo para la habilidad", True, NEGRO)
    for carta in listacartas:
        carta.objetivable=True

def explicacion(raton):
    exdone=False
    for boton in listabotones:
        if boton.rect.collidepoint(raton) and boton.carta.activo==True:
            explica0=fuentestats.render(boton.expl0, True, NEGRO)
            explica1=fuentestats.render(boton.expl1, True, NEGRO)
            explica2=fuentestats.render(boton.expl2, True, NEGRO)
            explica3=fuentestats.render(boton.expl3, True, NEGRO)
            pygame.draw.rect(pantalla, NARANJA, [raton[0], raton[1], 250,80])
            pantalla.blit(explica0,[raton[0]+10, raton[1]+10])
            pantalla.blit(explica1,[raton[0]+10, raton[1]+25])
            pantalla.blit(explica2,[raton[0]+10, raton[1]+40])
            pantalla.blit(explica3,[raton[0]+10, raton[1]+55])
            pygame.display.flip()
    
    while not exdone:
        reloj.tick(20)
        for evento in pygame.event.get():
            if pygame.mouse.get_pos()!=raton:
                exdone=True
                break
                return True

    


def dibujarpantalla(m1, diceroll):
    #dibujos por pantalla
        
        pantalla.blit(tablero,[0,0])
        #diujar cada uno de los bichos con su royo
        for carta in listacartas:
            x=carta.bicho.posicion
            y=carta.bicho.player
            if (carta.bicho.vivo==False):
                imagen=pygame.image.load(carta.bicho.image5)
            elif(carta.objetivable==False):
                imagen=pygame.image.load(carta.bicho.image1)
            else:
                imagen=pygame.image.load(carta.bicho.image2)
            pantalla.blit(imagen,[180+(230*(x-1)),80+((y-1)*300)])
            #stats de todos los bichos
            if carta.bicho.vivo==True:
                nombre=fuentenombre.render(carta.bicho.nombre, True, NEGRO)
                pantalla.blit(nombre,[194+(230*(x-1)),97+((y-1)*300)])
                nivel=fuentenombre.render(str(carta.bicho.nivel), True, NEGRO)
                pantalla.blit(nivel, [300+(230*(x-1)),97+((y-1)*300)])
                vida=fuentestats.render(str(carta.bicho.vida), True, NEGRO)
                if(carta.bicho.vida>99):
                    pantalla.blit(vida, [240+(230*(x-1)),297+((y-1)*300)] )
                else:
                    pantalla.blit(vida, [245+(230*(x-1)),297+((y-1)*300)] )
                ataque=fuentestats.render(str(carta.bicho.ataque), True, NEGRO)
                pantalla.blit(ataque, [190+(230*(x-1)),260+((y-1)*300)] )
                defensa=fuentestats.render(str(carta.bicho.defensa), True, NEGRO)
                pantalla.blit(defensa, [210+(230*(x-1)),288+((y-1)*300)] )
                probcritico=fuentecritico.render(str(carta.bicho.prob_critico), True, NEGRO)
                multcritico=fuentecritico.render(str(carta.bicho.mult_critico), True, NEGRO)
                pantalla.blit((probcritico), [273+(230*(x-1)),288+((y-1)*300)] )
                mediocritico=fuentecritico.render("/x", True, NEGRO)
                pantalla.blit(mediocritico, [278+(230*(x-1)),288+((y-1)*300)] )
                pantalla.blit((multcritico), [285+(230*(x-1)),288+((y-1)*300)] )
                velocidad=fuentestats.render(str(carta.bicho.velocidad), True, NEGRO)
                pantalla.blit((velocidad), [300+(230*(x-1)), 260+((y-1)*300)] )
                #dibujar los botones encima de la carta si esta está activa
                if carta.activo==True:     
                    for boton in listabotones:
                        if boton.carta==carta:
                            pantalla.blit(boton.image,(boton.rect.x, boton.rect.y))
                            atacar=fuentecritico.render("Atacar", True, NEGRO)              
                            pantalla.blit(atacar, [230+(230*(x-1)),100+((y-1)*300)])
                            if boton.habilidad=="Atacar":
                                ca=fuentestats.render(str(boton.contaturnos), True, BLANCO)
                                pantalla.blit(ca, [200+(230*(x-1)),100+((y-1)*300)])           
                            h1=fuentecritico.render(carta.bicho.habilidad1, True, NEGRO)
                            pantalla.blit(h1, [230+(230*(x-1)),150+((y-1)*300)])
                            if boton.habilidad==carta.bicho.habilidad1:
                                c1=fuentestats.render(str(boton.contaturnos), True, BLANCO)
                                pantalla.blit(c1, [200+(230*(x-1)),150+((y-1)*300)])
                            h2=fuentecritico.render(carta.bicho.habilidad2, True, NEGRO)
                            pantalla.blit(h2, [230+(230*(x-1)),200+((y-1)*300)])
                            if boton.habilidad==carta.bicho.habilidad2:
                                c2=fuentestats.render("P", True, BLANCO)
                                pantalla.blit(c2, [200+(230*(x-1)),200+((y-1)*300)])
                            h3=fuentecritico.render(carta.bicho.habilidad3, True, NEGRO)
                            pantalla.blit(h3, [230+(230*(x-1)),250+((y-1)*300)])
                            if boton.habilidad==carta.bicho.habilidad3:
                                if boton.turnos<10000:
                                    c3=fuentestats.render(str(boton.contaturnos), True, BLANCO)
                                else:
                                    c3=fuentestats.render("P", True, BLANCO)
                                pantalla.blit(c3, [200+(230*(x-1)),250+((y-1)*300)])
                            h4=fuentecritico.render(carta.bicho.habilidad4, True, NEGRO)
                            pantalla.blit(h4, [230+(230*(x-1)),300+((y-1)*300)])
                            if boton.habilidad==carta.bicho.habilidad4:
                                if boton.turnos<10000:
                                    c4=fuentestats.render(str(boton.contaturnos), True, BLANCO)
                                else:
                                    c4=fuentestats.render("P", True, BLANCO)
                                pantalla.blit(c4, [200+(230*(x-1)),300+((y-1)*300)])
        #diujar los datos de los jugadores
        nombrejugador1=fuenteplayers.render("P. 1", True, NEGRO)
        nombrejugador2=fuenteplayers.render("P. 2", True, NEGRO)
        recursos1=fuentenombre.render(str(player1.recursos), True, NEGRO)
        recursos2=fuentenombre.render(str(player2.recursos), True, NEGRO)
        pantalla.blit((nombrejugador1),[20,165])
        pantalla.blit((recursos1), [20,190])
        pantalla.blit((nombrejugador2),[20,463])
        pantalla.blit((recursos2), [20,488])
        #pantalla.blit((botonniveles.image), [botonniveles.rect.x, botonniveles.rect.y])
        #dibujar el dado
        if dice:
            pantalla.blit(dice,(53,337),(((diceroll-1)*32),0,32,32))
        #dibujar los textos:
        pantalla.blit(m1,[330,650])
        pygame.display.flip()
        reloj.tick(20)

# fase en la que definimos que es lo que haremos en la batalla
def estrategia(turno):
    contatip=0
    botoneando=False
    #declaraciones de las listas para poder usarlas en aqui y en batalla y que sea la misma lista
    global objetivosdefender, tooltipbool
    # hacemos que aumenten los recursos por turno a cada player
    if turno<=5:
        player1.recursos+=(turno)
        player2.recursos+=(turno)
    else:
        player1.recursos+=5
        player2.recursos+=5
    for bicho in listabichos:
        if "veneno" in bicho.alterado:    
            mensaje=fuenteplayers.render(bicho.nombre +" está envenenado " , True, NEGRO)
            dibujarpantalla(mensaje, diceroll)
            if "madre_tierra" in bicho.alterado:
                mensaje=fuenteplayers.render("Le protege la sabiduria de Madre Tierra " , True, NEGRO)
                dibujarpantalla(mensaje, diceroll)
            else:
                bicho.vida-=10
                esperar(20)
                if "muerte_dentro" in bicho.alterado:
                    bicho.vida-=10
                    mensaje=fuenteplayers.render(bicho.nombre +" muere desde dentro " , True, NEGRO)
                    dibujarpantalla(mensaje, diceroll)
                    esperar(20)
                if bicho.vida<=0:
                    if ultimobool==True and bicho.nombre=="Jataka":
                        mensaje=fuenteplayers.render(habilidades.ultimoencaer(bicho), True, NEGRO)   
                    else:
                        mensaje=fuenteplayers.render(bicho.nombre+" ha muerto", True, NEGRO)
                        bicho.vivo=False
                    dibujarpantalla(mensaje, diceroll)
                    esperar(20)
        if bicho.vivo==False:
            if bicho.player==1:
                player1.recursos+=1
            if bicho.player==2:
                player2.recursos+=2
    #definir la imagen pertinente para cada botón
    for boton in listabotones:
        if boton.numero<=boton.carta.bicho.nivel:
            boton.disponible=True
        else:
            boton.disponible=False
        boton.contaturnos-=1
        if boton.contaturnos<=0:
            boton.contaturnos=0
        if boton.disponible==True and boton.contaturnos<=0:
            boton.image=habilidadactivada
        if boton.disponible==True and boton.contaturnos>0 and boton.turnos<1000:
            boton.image=habilidadbloqueada
            boton.disponible=False    
        if boton.disponible==True and boton.turnos>1000:
            boton.image=habilidadseleccionada
            boton.activo=True
            
    #controlamos los contadores de los botones que lo requieran
    for boton in listabotones:
        if boton.habilidad in ["defender", "cubrir", "caparazon"]:
            boton.contador-=1
    #controlamos las consecuencias del final de los contadores:
    for boton in listabotones:
        if boton.activo==True and boton.habilidad=="regeneracion" and boton.carta.bicho.vida<boton.carta.bicho.vidamax:
            boton.carta.bicho.vida+=10
            mensaje=fuenteplayers.render(boton.carta.bicho.nombre +" se regenera " , True, NEGRO)
            dibujarpantalla(mensaje, diceroll)
            esperar(20)
        if boton.activo==True and boton.habilidad=="riqueza_del_cielo":
            if boton.carta.bicho.player==1:
                player1.recursos+=1
            else:
                player2.recursos+=1
                
        if boton.habilidad in ["defender", "cubrir", "caparazon"] and boton.contador==0:
            mensaje=fuenteplayers.render("Se acaba el efecto de " + boton.habilidad, True, NEGRO)
            dibujarpantalla(mensaje, diceroll)
            esperar(20)
            if boton.habilidad=="defender":
                for carta in boton.objetivo:
                    carta.bicho.defensa-=30
            if boton.habilidad=="cubrir":
                boton.objetivo.bicho.defensa=int (boton.objetivo.bicho.defensa/2)
            if boton.habilidad=="caparazon":
                boton.carta.bicho.defensa=int(boton.carta.bicho.defensa/2)
    
            
    #done define que se acabe la fase de estrategia, one2 que se acabe el movimiento del player1
    done=False
    done2=False
    #apuntando define que se está apuntando un ataque o una habilidad, apuntando_niveles que alguien va a subir de nivel
    global apuntando
    apuntando=False
    apuntando_niveles=False
    mensaje=fuenteplayers.render("Estas en la fase de estrategia", True, NEGRO)
    dibujarpantalla(mensaje, diceroll)
    esperar(20)

    while not done:
        raton=pygame.mouse.get_pos()
        reloj.tick(20)
        if pygame.mouse.get_rel()==(0,0):
            contatip+=1
        else:
            contatip=0
        if contatip==4:
            explicacion(raton)
        if apuntando==False and apuntando_niveles==False:
            if not done2:
                mensaje=fuenteplayers.render("Mueve el player 1", True, NEGRO)
            else:
                mensaje=fuenteplayers.render("Mueve el player 2", True, NEGRO)

        #Recogida de informacion del teclado y el raton,
        for evento in pygame.event.get():
                
                botoneando=False
                if evento.type == pygame.QUIT:
                    done = True
                    return True
                elif evento.type==pygame.MOUSEBUTTONDOWN:
                    
                    #definimos qué hacer si el jugador toca el botón máster
                    if master.rect.collidepoint(raton):
                        if done2==False:
                            done2=True
                            for carta in listacartas:
                                carta.activo=False
                        else:
                            done=True
                    #definimos como funciona la subida de niveles de los bichos
                    elif botonniveles.rect.collidepoint(raton):
                        apuntando_niveles=True
                        for carta in listacartas:
                            carta.activo=False
                        if done2==False:
                            for carta in listacartas:
                                if carta.bicho.player==1:
                                    carta.objetivable=True
                        if done2==True:
                            for carta in listacartas:
                                if carta.bicho.player==2:
                                    carta.objetivable=True
                        mensaje=fuenteplayers.render("A quien quieres subir de nivel?", True, NEGRO)
                    #definimos que pasa cuando tocamos en un botón de habilidad si este está disponible y no activo      
                    for boton in listabotones:
                        if boton.rect.collidepoint(raton) and boton.carta.activo==True and boton.disponible==True:
                            botoneando=True
                            estacarta=boton.carta
                            for x in listabotones:
                                if x.carta== estacarta and x.turnos<10000:
                                    x.activo=False
                                    if x.disponible==True:
                                        x.image=habilidadactivada
                                    else:
                                        x.image=habilidadbloqueada
                            boton.activo=True
                            boton.image=habilidadseleccionada
                            if boton.habilidad in ["Atacar", "furia", "asesinar","golpe_toxico", "furia_porcina"]:                
                                apuntarenemigos(boton)      
                            if boton.habilidad=="defender":
                                boton.contador=3
                                objetivosdefender.clear()
                                for carta in listacartas:
                                    if carta.bicho.player==boton.carta.bicho.player and (carta.bicho.posicion==boton.carta.bicho.posicion+1 or carta.bicho.posicion==boton.carta.bicho.posicion-1):
                                        objetivosdefender.append(carta)
                                boton.objetivo=objetivosdefender
                            if boton.habilidad in ["curar", "cubrir", "sabiduria_astral", "calor_antiguo", "luz_y_luna"]:
                                boton.carta.activo=False
                                apuntaramigos(boton)
                            if boton.habilidad in ["defender", "sovocar", "liderar", "cuidar", "uno_contra_todos"]:
                                for carta in listacartas:
                                    carta.objetivable=False
                            

                    for carta in listacartas:
                        if carta.rect.collidepoint(raton) and carta.activo==False and apuntando==False and carta.bicho.vivo==True and apuntando_niveles==False:
                            if done2==False and carta.bicho.player==1:
                                carta.activo=True
                            if done2==True and carta.bicho.player==2:
                                carta.activo=True
                        elif carta.rect.collidepoint(raton) and botoneando==False  and carta.bicho.vivo==True and apuntando_niveles==False and apuntando==True:
                            atacante.objetivo=carta
                            apuntando=False
                            print(atacante.carta.bicho.nombre, "atacara a ", carta.bicho.nombre)
                            for carta in listacartas:
                                carta.objetivable=False
                        if carta.rect.collidepoint(raton) and apuntando_niveles==True and carta.bicho.vivo==True:
                            apuntando_niveles=False
                            if (done2==False and carta.bicho.player==2) or (done2==True and carta.bicho.player==1):
                                mensaje=fuenteplayers.render(carta.bicho.nombre+" no esta en tu equipo", True, NEGRO)
                                dibujarpantalla(mensaje, diceroll)
                            else:
                                if carta.bicho.player==1:
                                    playerx=player1
                                else:
                                    playerx=player2                                       
                                if playerx.recursos>=carta.recursos:
                                    if carta.bicho.nivel<5:
                                        carta.bicho.nivel+=1
                                        playerx.recursos-=carta.recursos
                                        carta.recursos+=5
                                        mensaje=fuenteplayers.render(carta.bicho.nombre+" ha subido de nivel", True, NEGRO)
                                        dibujarpantalla(mensaje,diceroll)
                                        esperar(15)
                                    else:
                                        mensaje=fuenteplayers.render(carta.bicho.nombre+" ya esta en su maximo nivel", True, NEGRO)
                                        dibujarpantalla(mensaje,diceroll)
                                        esperar(15)
                                else:
                                    mensaje=fuenteplayers.render("No tienes suficientes recursos para subir a "+carta.bicho.nombre, True, NEGRO)
                                    dibujarpantalla(mensaje,diceroll)
                                    esperar(15)
                            
                            for boton in listabotones:
                                if boton.numero<=boton.carta.bicho.nivel:
                                    boton.disponible=True                                      
                                    if boton.activo==True or boton.turnos==10000:
                                        boton.activo=True
                                        boton.image=habilidadseleccionada
                                    else:
                                        boton.image=habilidadactivada
                                    if boton.contaturnos>0 and boton.turnos<1000:
                                        boton.disponible=False
                                        boton.image=habilidadbloqueada
                            for carta in listacartas:
                                carta.objetivable=False
                    



        dibujarpantalla(mensaje, diceroll)
# fase en la que se resuelve lo que hemos decidido en la fase de estrategia

def batalla():
    global cazabool, contraataquebool, templanzabool, venganzabool, sabiduriabool, berserkbool, ojoletalbool,ultimobool
    global llamaralasangrebool, diceroll
    diceroll=1
    done=False
    contador=0
    #convertimos las habilidades seleccionadas en una lista ordenada por velocidad
    for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return True
    for carta in listacartas:
        carta.activo=False
    listavelocidades=[]
    for boton in listabotones:   
        if boton.activo==True:
            if boton.habilidad=="cazador":
                cazabool=True
            elif boton.habilidad=="contraataque":
                contraataquebool=True
            elif boton.habilidad=="vitalidad":
                vitalidad(boton)
            elif boton.habilidad=="templanza_del_mar":
                templanzabool=True
            elif boton.habilidad=="venganza_del_desierto":
                venganzabool=True
            elif boton.habilidad=="sabiduria_de_tierra":
                sabiduriabool=True
            elif boton.habilidad=="berserk":
                berskerbool=True
            elif boton.habilidad=="ojo_letal":
                ojoletalbool=True
            elif boton.habilidad=="ultimo_en_caer":
                ultimobool=True
            elif boton.habilidad=="llamar_a_la_sangre":
                llamaralasangrebool=True
            elif boton.habilidad=="camino_del_escudo":
                for atacante in listabotones:
                    if atacante.activo==True and atacante.carta.bicho.player!=boton.carta.bicho.player:
                        atacante.objetivo=boton.carta
                        boton.contaturnos=boton.turnos
            elif boton.habilidad=="muerte_desde_dentro":
                for bicho in listabichos:
                    if bicho.player!=boton.carta.bicho.player:
                        bicho.alterado.append("muerte_dentro")
            elif boton.habilidad=="madre_tierra":
                for bicho in listabichos:
                    if bicho.player==boton.carta.bicho.player:
                        bicho.alterado.append("madre_tierra")
                
            else:
                listavelocidades.append(boton)
                boton.contaturnos=boton.turnos
    ordenada=sorted(listavelocidades, key=lambda boton: boton.velocidad, reverse=True)
    mensaje=fuenteplayers.render("Estas en la fase de batalla", True, NEGRO)
    dibujarpantalla(mensaje, diceroll)
    esperar(20)
     # mensajes para informar de lo que estan haciendo los players
    for boton in ordenada:
        if boton.carta.bicho.vivo==True:
            # mensajes para llamar a las funciones correspondientes y mostrar los mensajes que tocan
            if boton.habilidad!="Atacar" and boton.turnos<10000:
                mensaje=fuenteplayers.render(boton.carta.bicho.nombre+" ha utilizado "+boton.habilidad, True, NEGRO)
                dibujarpantalla(mensaje, diceroll)
                esperar(20)
            #llamadas a las funciones de los ataques, las que son posibles en el documento habilidades.py
            if boton.habilidad=="Atacar":
                mensaje=fuenteplayers.render(boton.carta.bicho.nombre+" ataca a "+boton.objetivo.bicho.nombre, True, NEGRO)
                dibujarpantalla(mensaje, diceroll)
                esperar(20)
                atacar(boton)
                if ojoletalbool==True and boton.carta.bicho.nombre=="Nidansa" and boton.contador==3:
                    mensaje=fuenteplayers.render(boton.carta.bicho.nombre+" ataca a "+boton.objetivo.bicho.nombre, True, NEGRO)
                    dibujarpantalla(mensaje, diceroll)
                    esperar(20)
                    atacar(boton)
            if boton.habilidad=="defender":
                habilidades.defender(boton)
            if boton.habilidad=="furia":
                if cazabool==True:
                    for obj in listabotones:
                        if obj.carta.bicho.player==boton.carta.bicho.player:
                            obj.contaturnos-=1
                        if obj.contaturnos<=0:
                            obj.contaturnos=0
                boton.contaturnos=3
                boton.disponible=False
                boton.carta.bicho.ataque*=2
                atacar(boton)
                boton.carta.bicho.ataque= int (boton.carta.bicho.ataque/2)
            if boton.habilidad=="sovocar":
                sovocar(boton)
            if boton.habilidad=="curar":
                habilidades.curar(boton)
            if boton.habilidad=="cubrir":
                habilidades.cubrir(boton)
            if boton.habilidad=="asesinar":
                atacar(boton)
                esperar(10)
                atacar(boton)
            if boton.habilidad=="liderar":
                liderar(boton)
            if boton.habilidad=="cuidar":
                cuidar(boton)
            if boton.habilidad=="uno_contra_todos":
                if cazabool==True:
                    for obj in listabotones:
                        if obj.carta.bicho.player==boton.carta.bicho.player:
                            obj.contaturnos-=1
                        if obj.contaturnos<=0:
                            obj.contaturnos=0
                for carta in listacartas:
                    if boton.carta.bicho.player!= carta.bicho.player:
                        boton.objetivo=carta
                        atacar(boton)
            if boton.habilidad=="golpe_toxico":
                atacar(boton)
                if boton.contador==2:
                    boton.objetivo.bicho.alterado.append("veneno")
            if boton.habilidad=="sabiduria_astral":
                boton.objetivo.bicho.velocidad+=20
            if boton.habilidad=="caparazon":
                boton.carta.bicho.defensa*=2
                boton.contador=2
            if boton.habilidad=="calor_antiguo":
                boton.objetivo.bicho.vida+=50
                if boton.objetivo.bicho.vida>=boton.objetivo.bicho.vidamax:
                    boton.objetivo.bicho.vida=boton.objetivo.bicho.vidamax
            if boton.habilidad=="furia_porcina":
                boton.carta.bicho.ataque=boton.carta.bicho.ataque+(boton.carta.bicho.vidamax-boton.carta.bicho.vida)
                atacar(boton)
                boton.carta.bicho.ataque=boton.carta.bicho.ataque-(boton.carta.bicho.vidamax-boton.carta.bicho.vida)
            if boton.habilidad=="trampa_toxica":
                for carta in listacartas:
                    if carta.bicho.player!=boton.carta.bicho.player:
                        carta.bicho.alterado.append("veneno")
            if boton.habilidad=="luz_y_luna":
                boton.objetivo.bicho.vida=boton.objetivo.bicho.vidamax
                boton.objetivo.bicho.alterado=[]
            if boton.habilidad=="mandato_imperial":
                for objetivo in listabotones:
                    if objetivo.carta.bicho.player==boton.carta.bicho.player:
                        objetivo.contaturnos=0
                                
            for bicho in listabichos:
                if bicho.vida<=0 and bicho.vivo==True:
                    if ultimobool==True and bicho.nombre=="Jataka":
                        mensaje=fuenteplayers.render(habilidades.ultimoencaer(bicho), True, NEGRO)   
                    else:
                        mensaje=fuenteplayers.render(bicho.nombre+" ha muerto", True, NEGRO)
                        bicho.vivo=False
                    dibujarpantalla(mensaje, diceroll)
                    esperar(20)
    for boton in listabotones:
        if boton.activo==True:
            boton.activo=False
            boton.image=habilidadactivada
    for x in listavelocidades:
        listavelocidades.remove(x)
    for h in ordenada:
            ordenada.remove(h)
    print("despues de la batalla,",ordenada)
    
def atacar(boton): 
    global contraataquebool, templanzabool, venganzabool, berserkbool, ojoletalbool, llamaralasangrebool
    global diceroll
    diceroll=habilidades.atacar(boton) 
    if diceroll==1:
        mensaje=fuenteplayers.render("El ataque ha fallado", True, NEGRO)
        imagen=paradoimg
    elif diceroll==2:
        if boton.carta.bicho.velocidad<boton.objetivo.bicho.velocidad:
            mensaje=fuenteplayers.render("El ataque ha fallado", True, NEGRO)
            imagen=paradoimg
        elif boton.carta.bicho.velocidad>=boton.objetivo.bicho.velocidad:
            mensaje=fuenteplayers.render("El ataque ha acertado", True, NEGRO)
            imagen=ataqueimg
    elif diceroll==3:
        if 2*boton.carta.bicho.velocidad<boton.objetivo.bicho.velocidad:
            mensaje=fuenteplayers.render("El ataque ha fallado", True, NEGRO)
            imagen=paradoimg
        elif 2*boton.carta.bicho.velocidad>=boton.objetivo.bicho.velocidad:
            mensaje=fuenteplayers.render("El ataque ha acertado", True, NEGRO)
            imagen=ataqueimg
    elif diceroll>=4:
        if diceroll<boton.carta.bicho.prob_critico or boton.habilidad=="furia":
            mensaje=fuenteplayers.render("El ataque ha acertado", True, NEGRO)
            imagen=ataqueimg
        else:
            mensaje=fuenteplayers.render("El ataque ha sido critico", True, NEGRO)
            if venganzabool==True:
                if sabiduriabool==False or boton.objetivo.bicho.nombre!="Ityukta":
                    boton.objetivo.bicho.alterado.append("veneno")
            imagen=ataqueimg
    dibujarpantalla(mensaje, diceroll)
    animacion(imagen, boton.objetivo)
    esperar(10)
    if boton.objetivo.bicho.vida==0:
        mensaje=fuenteplayers.render(boton.objetivo.bicho.nombre+" ha muerto", True, NEGRO)
    if boton.contador==1:
        if templanzabool==True and boton.objetivo.bicho.nombre=="Geya":
            contraataque(boton)
    if boton.contador==2:
        if berserkbool==True and boton.objetivo.bicho.nombre=="Ceriman":
            boton.objetivo.bicho.ataque+=5
        if llamaralasangrebool==True and boton.carta.bicho.nombre=="Nemeo":
            mensaje=fuenteplayers.render("Nemeo llama a la sangre", True, NEGRO)
            boton.objetivo.bicho.vida-=10
            dibujarpantalla(mensaje, diceroll)
            esperar(25)
    if boton.contador==3:
        if contraataquebool==True and boton.objetivo.bicho.nombre=="Lerma":
            contraataque(boton)
            

def sovocar(atacante):
    for boton in listabotones:
        if boton.carta.bicho.player!=atacante.carta.bicho.player:
            boton.contaturnos+=1

def liderar(atacante):
    for boton in listabotones:
        if boton.carta.bicho.player==atacante.carta.bicho.player:
            boton.contaturnos-=1
        if boton.contaturnos<=0:
            boton.contaturnos=0

def cuidar(boton):
    for bicho in listabichos:
        if bicho.player==boton.carta.bicho.player:
            bicho.vida+=10
        if bicho.vida>= bicho.vidamax:
            bicho.vida=bicho.vidamax
            

def vitalidad(boton):
    if boton.carta.bicho.vida==boton.carta.bicho.vidamax:
        if boton.contador==0:
            boton.carta.bicho.velocidad*=2
            boton.contador+=1
    else:
        if boton.contador!=0:
            boton.carta.bicho.velocidad=int(boton.carta.bicho.velocidad/2)
            boton.contador=0

def contraataque(boton):
    cont=BotonHabilidad()
    cont.carta=boton.objetivo
    cont.objetivo=boton.carta
    atacar(cont)

def main():
    fin=False
    turno=0
    while not fin:
        turno+=1
        fin=estrategia(turno)
        if fin==True:
            break
        batalla()

    pygame.quit()



if __name__=="__main__":
    main()

