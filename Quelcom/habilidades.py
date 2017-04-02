import pygame
import random


class Habilidad():
    def __init__(self):
        self.nombre=""
        self.descripcion=""
        self.activo=False

def asignarturnos(listabotones):
    for boton in listabotones:
        if boton.habilidad in ["defender", "curar", "cubrir", "cuidar", "caparazon"]:
            boton.turnos=2
        if boton.habilidad in ["furia", "golpe_toxico", "calor_antiguo"]:
            boton.turnos=3      
        if boton.habilidad in ["sovocar", "uno_contra_todos", "sabiduria_astral", "furia_porcina", "liderar", "camino_del_escudo", "asesinar"]:
            boton.turnos=4
        if boton.habilidad in ["trampa_toxica"]:
            boton.turnos=5
        if boton.habilidad in ["luz_y_luna"]:
            boton.turnos=6
        if boton.habilidad in ["mandato_imperial"]:
            boton.turnos=8
        if boton.habilidad in ["regeneracion", "cazador","contraataque","vitalidad", "templanza_del_mar", "venganza_del_desierto", "riqueza_del_cielo",
                               "sabiduria_de_tierra", "berserk", "llamar_a_la_sangre","ojo_letal","ultimo_en_caer","muerte_desde_dentro","madre_tierra"] :
            boton.turnos=10000
            boton.contaturnos=10000
    return listabotones

def asignarexplicaciones(listabotones):
    for boton in listabotones:
        if boton.turnos==10000:
            turnacos="(Pasiva)"
        else:
            turnacos=str(boton.turnos)
        boton.expl0=boton.habilidad.upper()+" - "+turnacos
        if boton.habilidad=="Atacar":
            boton.expl1="Realiza daño en el objetivo"
            boton.expl2="dependiendo de velocidades,"
            boton.expl3="ataque, defensa, y dado"
        if boton.habilidad=="defender":
            boton.expl1="Aliados adyacentes"
            boton.expl2="+30 de defensa"
            boton.expl3="durante dos turnos"
        if boton.habilidad=="furia":
            boton.expl1="Realiza un ataque"
            boton.expl2="con el doble de fuerza"
            boton.expl3="sin afectar al critico"
        if boton.habilidad=="sovocar":
            boton.expl1="Las habilidades de guerreros"
            boton.expl2="enemigos tardan un turno"
            boton.expl3="mas en regenrarse"
        if boton.habilidad=="curar":
            boton.expl1="Cura 30 puntos de daño"
            boton.expl2="al objetivo"
        if boton.habilidad=="cubrir":
            boton.expl1="Dobla la defensa del objetivo"
            boton.expl2="durante dos turnos"
            boton.expl3=""
        if boton.habilidad=="asesinar":
            boton.expl1="Realiza dos ataques"
            boton.expl2="al objetivo"
            boton.expl3=""
        if boton.habilidad=="liderar":
            boton.expl1="Regenera en un punto las"
            boton.expl2="habilidades de tus guerreros"
            boton.expl3=""
        if boton.habilidad=="cuidar":
            boton.expl1="Cura diez puntos de vida"
            boton.expl2="a todo tu grupo"
            boton.expl3=""
        if boton.habilidad=="regeneracion":
            boton.expl1="Cada turno regenera"
            boton.expl2="10 puntos de vida"
            boton.expl3=""
        if boton.habilidad=="cazador":
            boton.expl1="Usar una habilidad regenera"
            boton.expl2="un punto el resto de habildiades"
            boton.expl3="de Nemeo"
        if boton.habilidad=="contraataque":
            boton.expl1="Al esquivar realiza automaticamente"
            boton.expl2="un ataque al enemigo"
            boton.expl3=""
        if boton.habilidad=="vitalidad":
            boton.expl1="Si tiene toda su vida la"
            boton.expl2="velocidad se multiplica por dos"
            boton.expl3=""
        if boton.habilidad=="templanza_del_mar":
            boton.expl1="Al bloquear realiza"
            boton.expl2="automáticamente un ataque"
            boton.expl3="al atacante"
        if boton.habilidad=="venganza_del_desierto":
            boton.expl1="Si hace daño critico"
            boton.expl2="envenena al enemigo"
            boton.expl3=""
        if boton.habilidad=="riqueza_del_cielo":
            boton.expl1="Recibes un punto de"
            boton.expl2="recursos adicional"
            boton.expl3="cada turno"
        if boton.habilidad=="sabiduria_de_tierra":
            boton.expl1="Ityutka es inumne"
            boton.expl2="a estados alterados"
            boton.expl3=""
        if boton.habilidad=="berserk":
            boton.expl1="Recibir daño aumenta"
            boton.expl2="el ataque de Ceriman"
            boton.expl3="en cinco puntos"
        if boton.habilidad=="uno_contra_todos":
            boton.expl1="Realiza un ataque contra"
            boton.expl2="todos los enemigos"
            boton.expl3=""
        if boton.habilidad=="golpe_toxico":
            boton.expl1="Realiza un ataque que si"
            boton.expl2="produce daño envenena"
            boton.expl3="al enemigo"
        if boton.habilidad=="sabiduria_astral":
            boton.expl1="Aumenta la velocidad del "
            boton.expl2="objetivo en 20 puntos"
            boton.expl3="permanentemente"
        if boton.habilidad=="caparazon":
            boton.expl1="Duplica la defensa de Geya"
            boton.expl2="durante dos turnos"
            boton.expl3=""
        if boton.habilidad=="ojo_letal":
            boton.expl1="Al atacar Nidansa si el "
            boton.expl2="enemigo esquiva el ataque"
            boton.expl3="vuelve a atacar"
        if boton.habilidad=="ultimo_en_caer":
            boton.expl1="Si Jataka va a morir hay"
            boton.expl2="un 50% de posibilidades"
            boton.expl3="de que siga viviendo"
        if boton.habilidad=="calor_antiguo":
            boton.expl1="Cura 50 puntos de vida"
            boton.expl2="al guerrero objetivo"
            boton.expl3=""
        if boton.habilidad=="furia_porcina":
            boton.expl1="Realiza un ataque sumando "
            boton.expl2="la fuerza de todo el daño "
            boton.expl3="recibido"
        if boton.habilidad=="llamar_a_la_sangre":
            boton.expl1="Los enemigos dañados por"
            boton.expl2="Nemeo reciben 10 puntos"
            boton.expl3="de daño adicional"
        if boton.habilidad=="trampa_toxica":
            boton.expl1="envenena a todos los"
            boton.expl2="enemigos"
            boton.expl3=""
        if boton.habilidad=="luz_y_luna":
            boton.expl1="Cura toda la vida de un"
            boton.expl2="aliado, eliminando los "
            boton.expl3="estados alterados"
        if boton.habilidad=="camino_del_escudo":
            boton.expl1="Durante un turno, todos"
            boton.expl2="los enemigos le hacen objetivo"
            boton.expl3="de sus ataques y habilidades"
        if boton.habilidad=="muerte_desde_dentro":
            boton.expl1="Los enemigos envenenados"
            boton.expl2="reciben diez puntos de daño"
            boton.expl3="adicional cada turno"
        if boton.habilidad=="mandato_imperial":
            boton.expl1="Todas las habilidades de"
            boton.expl2="tus guerreros vuelven a "
            boton.expl3="estar disponibles"
        if boton.habilidad=="madre_tierra":
            boton.expl1="Las habilidades de Ityukta"
            boton.expl2="Hacen objetivo a todo tu"
            boton.expl3="equipo"
            
    return listabotones

def tirardado():
    diceroll=random.randrange(1,7)
    return diceroll
#si el contador del atacante es igual a uno, es que lo ha bloqueado. Si es igual a 2 es que le ha hecho daño. Si es igual a tres es que lo ha esquivado
def atacar(atacante):
    tirada=tirardado()
    daño=int(atacante.carta.bicho.ataque/atacante.objetivo.bicho.defensa)*10
    if tirada==1:
        atacante.contador=3
        return tirada
    elif tirada==2:
        if atacante.carta.bicho.velocidad<atacante.objetivo.bicho.velocidad:
            atacante.contador=3
            return tirada        
        elif atacante.carta.bicho.velocidad>=atacante.objetivo.bicho.velocidad:
            atacante.objetivo.bicho.vida-=daño
            if daño==0:
                atacante.contador=1
            else:
                atacante.contador=2
    elif tirada==3:
        if 2*atacante.carta.bicho.velocidad<atacante.objetivo.bicho.velocidad:
            atacante.contador=3
            return tirada
        elif 2*atacante.carta.bicho.velocidad>=atacante.objetivo.bicho.velocidad:
            atacante.objetivo.bicho.vida-=daño
            if daño==0:
                atacante.contador=1
            else:
                atacante.contador=2
            
    elif tirada>=4:
        if tirada<atacante.carta.bicho.prob_critico or atacante.habilidad=="furia":
            
            atacante.objetivo.bicho.vida-=daño
            if daño==0:
                atacante.contador=1
            else:
                atacante.contador=2
        else:
            daño=int((atacante.carta.bicho.ataque*atacante.carta.bicho.mult_critico)/atacante.objetivo.bicho.defensa)*10
            atacante.objetivo.bicho.vida-=daño
            if daño==0:
                atacante.contador=1
            else:
                atacante.contador=2
    return tirada

def defender(boton):
    boton.contador=2
    boton.disponible=False
    for carta in boton.objetivo:
        carta.bicho.defensa+=30

def curar(boton):
    boton.objetivo.bicho.vida+=30
    if boton.objetivo.bicho.vida>=boton.objetivo.bicho.vidamax:
        boton.objetivo.bicho.vida=boton.objetivo.bicho.vidamax

def cubrir(boton):
    boton.objetivo.bicho.defensa*=2
    boton.contador=2

def ultimoencaer(bicho):
    x=tirardado()
    if x<=3:
        bicho.vivo=False
        return(bicho.nombre + " ha muerto")
    else:
        bicho.vida=10
        return (bicho.nombre + " será el último en caer")

                

