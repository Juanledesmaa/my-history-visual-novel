# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define juanito = Character("Juanito", image="juanito")

default first_choice_done = False
# player_name, try to call player_name always with {color=#f00}[player_name]!{/color}
default player_name = ""
default default_player_name = "querido amigo"


# The game starts here.
label intro:

    scene bg maracaibo
    with fade
    show juanito talking at halfsize, left
    juanito "Hey! Hola! Bienvenido a mi historia."
    juanito "Este juego narra la historia de 2 personas que era imposible que se reencontraran."
    juanito "Sin embargo, Dios fue tan bueno que al igual que un eclipse nuestros caminos se volvieron a cruzar de una forma inesperada."
    jump player_name_select_input

label player_name_select_input:
    # The phrase in the brackets is the text that the game will display to prompt 
    # the player to enter the name they've chosen.
    $ player_name = renpy.input("¿Cual es tu nombre o como te gustaria que te llamara? (Escribe tu nombre en el recuadro de abajo)")
    $ player_name = player_name.strip()
    # The .strip() instruction removes any extra spaces the player 
    # may have typed by accident.

    #  If the player can't be bothered to choose a name, then we
    #  choose a suitable one for them:
    if player_name == "":
        $ player_name= "querido amigo"

    # And get a nostalgic sigh from Seasons of Sakura fans!
    # Now the other characters in the game can greet the player.
  
    juanito "Un gusto saludarte, {color=#f00}[player_name]!{/color}"
    jump story_begin

label story_begin:
    ## Pensativo
    juanito "A ver, ¿Por donde podria empezar la historia?"

    ## feliz
    juanito "Ahh sii!"
    juanito "Beba y yo nos conocimos en un campamento de jovenes organizado por mi primo Orester en Venezuela en el 2017"
    juanito "Tiempo despues de eso nos reencontramos una vez en mi ciudad \"Maracaibo\""
    juanito "Aqui pueden apreciar un poco el fondo de mi ciudad natal"
    ## Tristeza
    juanito "Ahhh, me trae nostalgia recordar esos dias"
    juanito "Pero bueno, volviendo al punto de este juego y a la historia de Beba y yo"
    juanito "Recuerdo que una de nuestras ultimas conversaciones fue acerca del sitio donde viviriamos en el futuro"
    juanito "Ella estaba por mudarse a Puerto Rico y yo todavia no sabia que iba a ser de mi vida"
    ## Pensativo
    juanito "Una de las preguntas que me hizo es si me iria a vivir a estados unidos y yo teniendo todas las opciones y posibilidades para ir a estados unidos"
    
    jump intro_menu_choice
    

label intro_menu_choice:

    juanito "¿Que crees que respondi yo?"
    menu:
        "Si claro, voy a vivir en estados unidos.":
            jump wrong_choice_intro
        "Tengo planes en Argentina.":
            jump wrong_choice_intro
        "No tengo dinero":
            jump correct_choice_intro

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

label correct_choice_intro:
    if first_choice_done == False:
        ## Sorprendido
        juanito "Woow, la verdad no pense que lo adivinarias a la primera, {color=#f00}[player_name]!{/color}"
        jump correct_choice_intro_explanation_and_question
    else:
        juanito "Muy bien! Eso fue lo que respondi"
        jump correct_choice_intro_explanation_and_question


label correct_choice_intro_explanation_and_question:
    juanito "Aunque literalmente en ese momento le dije \"No tengo plata\" que es una expresión comun en mi pais"
    juanito "Pero acertaste bien, {color=#f00}[player_name]!{/color}"
    ## Verguenza
    juanito "Pues si!, en esta historia se van a repetir muchas situaciones asi donde pasaron cosas que ahora recuerdo y me dan verguenza"
    ## Feliz
    juanito "Con tu respuesta sumaste 10 puntos!"
    juanito "Puedes ver tu cantidad acumulada de puntos en la esquina superior derecha de tu pantalla"
    juanito "¿Te gustaria que te explicara las reglas del juego mas a detalle o te sientes confiado para continuar?"

    ## Ask for Game Rules
    menu:
        "Si, explicame por favor":
            jump game_explanation
        "Continuemos, me siento confiado!":
            jump skip_game_explanation

label game_explanation:
    juanito "Pues, este juego es muy sencillo:"
    juanito "Voy a contarte nuestra historia y te voy a ir presentando situaciones donde vas a tener que actuar como si fuera yo"
    ## Feliz
    juanito "Si respondes de la misma manera en la que yo respondi en aquel momento sumas 10 puntos"
    ## Verguenza
    juanito "Por el contrario, cada vez que respondas de forma erronea se te descontaran 10 puntos"
    juanito "Esta todo permitido con tal de contestar correctamente no tengas miedo de consultar con otros jugadores a tu alrededor"

label skip_game_explanation:
    juanito "Wow, estamos muy confiados por aqui. Seguro has jugado muchos juegos en el pasado o nos conoces demasiado bien"
