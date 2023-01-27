init python:
    g = Gallery()

    g.button("a1")
    g.condition("persistent.a1")
    g.image("gallery/pic/Page1/1.png")

    g.button("a2")
    g.condition("persistent.a2")
    g.image("gallery/pic/Page1/2.png")

    g.button("a3")
    g.condition("persistent.a3")
    g.image("gallery/pic/Page1/3.png")

    g.button("a4")
    g.condition("persistent.a4")
    g.image("gallery/pic/Page1/4.png")

    g.button("a5")
    g.condition("persistent.a5")
    g.image("gallery/pic/Page1/5.png")

    g.button("a6")
    g.condition("persistent.a6")
    g.image("gallery/pic/Page1/6.png")

    g.button("a7")
    g.condition("persistent.a7")
    g.image("gallery/pic/Page1/7.png")

    g.button("a8")
    g.condition("persistent.a8")
    g.image("gallery/pic/Page1/8.png")

    g.button("a9")
    g.condition("persistent.a9")
    g.image("gallery/pic/Page1/9.png")


screen gallery_001:
    tag menu
    imagemap:
            ground "gui/main menu/idle.png"
            idle "gui/main menu/idle.png"
            hover "gui/main menu/hover.png"
            selected_idle "gui/main menu/sele.png"
            selected_hover "gui/main menu/selehover.png"

            text _("{color=#CFCFCF}{size=105}Gallery{/size}{/color}") xpos 465 ypos -5
            hotspot (1048, 146, 200, 82) action ShowMenu("load")
            hotspot (1047, 237, 202, 86) action ShowMenu("preferences")
            hotspot (1048, 328, 204, 84) action ShowMenu("gallery_001")
            hotspot (1045, 428, 203, 75) action ShowMenu("about")
            hotspot (1044, 517, 204, 79) action ShowMenu("help")
            hotspot (1102, 608, 86, 85) action Return()

            imagebutton auto "gallery/pic/Button/one_%s.png" action ShowMenu("gallery_001") xpos 50 ypos 200
            imagebutton auto "gallery/pic/Button/two_%s.png" action ShowMenu("gallery_002") xpos 50 ypos 280
            imagebutton auto "gallery/pic/Button/three_%s.png" action ShowMenu("gallery_003") xpos 50 ypos 360
            imagebutton auto "gallery/pic/Button/four_%s.png" action ShowMenu("gallery_004") xpos 50 ypos 440

    hbox:
        yalign 0.7
        xalign 0.4

        grid 3 3:
            spacing 15

            ## Row 1
            add g.make_button("a1","gallery/pic/cover/1_1.png", locked = "gallery/pic/cover/locked.png")
            add g.make_button("a2","gallery/pic/cover/1_2.png", locked = "gallery/pic/cover/locked.png")
            add g.make_button("a3","gallery/pic/cover/1_3.png", locked = "gallery/pic/cover/locked.png")


            ## Row 2
            add g.make_button("a4","gallery/pic/cover/1_4.png", locked = "gallery/pic/cover/locked.png")
            add g.make_button("a5","gallery/pic/cover/1_5.png", locked = "gallery/pic/cover/locked.png")
            add g.make_button("a6","gallery/pic/cover/1_6.png", locked = "gallery/pic/cover/locked.png")


            ## Row 3
            add g.make_button("a7","gallery/pic/cover/1_7.png", locked = "gallery/pic/cover/locked.png")
            add g.make_button("a8","gallery/pic/cover/1_8.png", locked = "gallery/pic/cover/locked.png")
            add g.make_button("a9","gallery/pic/cover/1_9.png", locked = "gallery/pic/cover/locked.png")
