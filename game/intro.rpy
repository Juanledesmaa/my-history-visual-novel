# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define juanito = Character("Juanito", image="juanito")

default first_choice_done = False


# The game starts here.
label intro:

    scene bg maracaibo
    with fade
    show juanito talking at halfsize, left
    juanito "Hey! Hola! Bienvenido a mi historia."
    juanito "Este juego narra la historia de 2 personas que era imposible que se reencontraran."
    juanito "Sin embargo, Dios fue tan bueno que al igual que un eclipse nuestros caminos se volvieron a cruzar de una forma inesperada."


    ## Pensativo
    juanito "A ver, ¿Por donde podria empezar la historia?"

    ## feliz
    juanito "Ahh sii!"
    juanito "Beba y yo nos conocimos en un campamento de jovenes en el 2017"
    juanito "Luego de eso nos reencontramos una vez en mi ciudad \"Maracaibo\""
    juanito "Recuerdo que una de nuestras ultimas conversaciones fue acerca del sitio \ndonde viviriamos"
    juanito "Ella me menciono que iria a vivir a estados unidos y yo tenia todas las opciones \npara ir a estados unidos"
    
    jump intro_menu_choice


label intro_menu_choice:

    juanito "Entonces, ¿Que crees que respondi yo?"
    menu:
        "Si claro, voy a vivir en estados unidos.":
            jump wrong_choice_intro
        "Tengo planes en Argentina.":
            jump wrong_choice_intro
        "No tengo dinero.":
            jump wrong_choice_intro

label wrong_choice_intro:
    if first_choice_done == False:
        $ first_choice_done = True

        juanito "No, realmente eso no fue lo que paso"
        juanito "Igual que bueno que seleccionaste la opcion incorrecta, asi puedo explicarte un poco el juego"
        juanito "Cada vez que selecciones una opcion correcta sumas 10 puntos."
        juanito "Por el contrario, si seleccionas una incorrecta se restan 10."
        jump intro_menu_choice
    else:
        juanito "No, realmente eso no fue lo que paso, vuelve a intentarlo"
        jump intro_menu_choice

return
