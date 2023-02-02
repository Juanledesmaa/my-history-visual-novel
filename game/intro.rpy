# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    def beepy_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("sounds/bleep005.ogg", loop=True)
            renpy.sound.set_volume(0.15, 0, "sound")
        elif event == "slow_done":
            renpy.sound.stop(fadeout=1)

    renpy.music.register_channel("soundEffect", "sfx") 

define audio.correct = "sounds/correct.wav"
define audio.error = "sounds/error.wav"
define audio.airplane = "sounds/airplane.wav"

# define juanito = Character("Juanito", image="juanito")
define juanito = Character("Juanito", callback=beepy_voice)

default first_choice_done = False
# player_name, try to call player_name always with {color=#f00}[player_name]!{/color}
default player_name = ""
default default_player_name = "querido amigo"


# The game starts here.
label intro:

    scene bg maracaibo
    with fade
    show juanito talking at halfsize, left
    with moveinleft
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
    play soundEffect error fadeout 0.5 fadein 0.5 noloop volume 0.05

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
    play soundEffect correct fadeout 0.5 fadein 0.5 noloop volume 0.10

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


# Part 2

label intro_part_two:
    juanito "Bueno, ¿por donde puedo continuar?"
    juanito "Ahh si, luego de esa ultima ocasion ella partio para puerto rico"
    hide juanito

    play soundEffect airplane fadeout 0.5 fadein 2 noloop volume 0.05
    show bg avion
    with pushright

    show juanito talking at halfsize, left
    with moveinleft

    juanito "Y poco tiempo despues de eso yo me fui para Argentina"
    juanito "Hay tantas cosas que me hubiera gustado decirle antes"
    juanito "Hay algo en ella que me parecia muy genial y no se lo dije en ese momento"
    juanito "Te pregunto a ti, {color=#f00}[player_name]{/color}"



label intro_part_two_menu_choice:

    juanito "¿Tienes idea de que era eso que me parecia genial?"

    menu:
        "Su sonrisa.":
            jump intro_part_two_menu_choice_wrong_answer
        "Su cabello pintado":
            jump intro_part_two_menu_choice_correct_answer
        "Su personalidad.":
            jump intro_part_two_menu_choice_wrong_answer
        "Sus ojos":
            jump intro_part_two_menu_choice_wrong_answer

label intro_part_two_menu_choice_wrong_answer:
    play soundEffect error fadeout 0.5 fadein 0.5 noloop volume 0.10

    juanito "No, realmente eso no fue"
    juanito "¿Te parece si lo vuelves a intentar?"
    jump intro_part_two_menu_choice

label intro_part_two_menu_choice_correct_answer:
    play soundEffect correct fadeout 0.5 fadein 0.5 noloop volume 0.10

    ## Feliz
    juanito "Sii, correcto. Eso me llamaba mucho la atencion en ella"
    juanito "La verdad en ese entonces era algo que me parecia genial su estilo de pelo, le llegue a ver el pelo verde, rosado y blanco"
    juanito "Y la verdad era algo que me parecia super genial y atrevido en ella"
    juanito "Esto fue algo muy importante en nuestra futura comunicacion debido a que este talento de ella el cual comenzo como hobby"
    ## Apenado
    juanito "Llego a convertirse en su trabajo. Tuve la suerte de que varias veces publicaba en instagram cosas relacionadas a su trabajo y yo aprovechaba estas ocasiones para escribirle"

    ## Telefono

label intro_part_two_argentina:
    show bg argentina_paisaje
    with dissolve

    juanito "Estar en argentina fue una experiencia increible para mi, al igual que ella mi hobby se convirtio en mi carrera"
    juanito "Y esto es algo que me encanta que compartimos en comun"
    juanito "Ella solia pintar el cabello a sus amigas y a ella misma, yo siempre ame todo lo relacionado a las computadoras"

    ## Usar el telefono
    juanito "Sinceramente los primeros años no charlamos mucho, sin embargo siempre estaba atento a que subiera una foto"
    juanito "Pero muchas veces me ganaba la timidez, piensenlo. ¿Yo en Argentina, ella en Puerto Rico que podia decirle que nos acercara mas?"

    # always start with this, it hides the regular text box, brings up the phone and has a short delay
    # most of these calls include delays to make this look nicer
    # you can find the code behind these calls in aPhone1080.rpy

    call phone_start(2) #there are 2 phone face's 0 and 1 blue and purple
    $ phone_too = "" #who the conversation is with

    # this brings up the message, first slot is the name, and second is the content
    # notice how it has _start at the end, the first one is special as there are no delays before it. use this for the first message
    call message_start("logobeba", "", "Hey, this is a phone texting thingy")
    # the format
    #first is the avatar (see bPhone.rpy for these)
    #second is the of who sent the message (me would be the person who owns the phone)
    #third is the message
    #same format for message_start and message

    # added an alternate way to reply from the player perspective, this time the name doesnt show if you think its extra
    call message_reply("Oh really? What does it do lol")
    #this is a reply it's always from the owner of the phone
    #and who it is being sent too

    # this one is the same as the above one, but instead it has one more place for you to set an image
    # you have to make the image be small enough to fit the screen or its gonna stretch weird!

    call message_img("logobeba", "", "With it I can send you messages and images!\nClick the image to see it full size.", 0)
    #texts with images are the same format for sending a message but with a number before who it is sent too.
    #data for the images are in a python [list] so first is 0 then 1,2,3
    #see bPhone for putting images in the list and adding avatars
