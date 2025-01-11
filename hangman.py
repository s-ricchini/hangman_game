import wikipedia
import random
import sys
import playsound

#TODO: agregar mas animale
#TODO: agregar sonido de error cuando te equivocas de letra

def main():
    letras_adivinadas = []
    letras_incorrectas = []
    vidas = 5
    palabra = choose_animal()
    pista = True
    
    while vidas != 0:
        print(F"Vidas: {vidas}")
        mostrar_tablero(palabra,letras_adivinadas)
        mostrar_etapas(vidas)
        
        #verifica input
        try:
            user = input("\nEscribe una letra: ").lower()
        except KeyboardInterrupt:
            sys.exit()
        except ValueError:
            pass
        except EOFError:
            if palabra_completa(palabra):
                print(f"Ganaste!, la palabra es {palabra}")
            else:
                vidas = 0
                break

        if (user in letras_adivinadas) or (user in letras_incorrectas):
            print("Ya elegiste esa letra")
            pass
        elif user in palabra:
            letras_adivinadas.append(user)
        else:
            letras_incorrectas.append(user)
            vidas -= 1
        
        #sugiere dar una pista al usuario (1 por partida)
        if vidas <= 2:
            while pista:
                pregunta = input("Queres una pista? (y/n)")
                if pregunta == "y":
                    pista_animal(palabra)
                    pista = False
                    break
                elif pregunta == "n":
                    pista = False
                    break
        if all(letra in letras_adivinadas for letra in palabra):
            print(f"¡Ganaste! El animal era '{palabra}'.")
            return
    mostrar_etapas(vidas)
    print(f"Perdiste!, el animal era {palabra} ")


def choose_animal():
    animales = [
    "perro", "gato", "caballo", "vaca", "oveja", "cerdo", "pollo", "pato", "ganso", 
    "loro", "aguila", "halcon", "buho", "leon", "tigre", "elefante", "jirafa", 
    "cebra", "rinoceronte", "hipopotamo", "canguro", "koala", "lobo", "zorro", 
    "oso", "delfin", "ballena", "tiburon", "pinguino", "foca", "cocodrilo", 
    "serpiente", "tortuga", "rana", "murcielago", "camaleon", "erizo", "mapache", 
    "ardilla", "ciervo", "castor", "cabra", "burro", "mono", "flamenco", "pelicano", 
    "calamar", "pulpo", "langosta", "cangrejo", "medusa"
    ]
    animal = random.choice(animales)
    return animal

def mostrar_tablero(palabra,letras):
    for i in range(len(palabra)):
        if palabra[i] in letras:
            print(palabra[i],end=" ")
        else:
            print("_",end=" ")
    return

def pista_animal(animal):
    wikipedia.set_lang("es")
    resumen = wikipedia.summary(animal,sentences = 2)
    censura = "#" * len(animal)
    resumen_censurado = resumen.replace(animal,censura)
    print(resumen_censurado)

def mostrar_etapas(vidas):
        etapas = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
        """
    ]
        if vidas == 0:
            print(etapas[5])
        else:
            print(etapas[5 - vidas])
    
def palabra_completa(palabra):
    x =input("Escribe la palabra entera: ")
    if x == palabra:
        return True

def sonidos(i):
    if i:
        # Good
        playsound.playsound("")
    else:
        # Wrong
        playsound.playsound("")
        
main()