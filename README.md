# hangman_game

El programa consiste en el clasico ahorcado. al jugador se la va a asignar un animal random (entre una lista de 50 animales) para que adivine.

El jugagor tiene 5 vidas, si elige mal una letra se le resta 1 vida, cuando se tiene 2 vidas aparece la opcion de "solicitar una pista", esta funcion lo que hace es conectarse con la api de wikipedia para imprimir un resumen de animal con el nombre de este censurado

Si se apreta control+d salta la opcion para escreibir toda la palabra de 1 vez. si la palabra no es correcta el jugador pierde instantaneamente.