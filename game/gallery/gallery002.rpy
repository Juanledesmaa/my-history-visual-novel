init python:

    g.button("2_1")
    g.condition("persistent.2_1")
    g.image("gallery/pic/Page2/1.png")

    g.button("2_2")
    g.condition("persistent.2_2")
    g.image("gallery/pic/Page2/2.png")

    g.button("2_3")
    g.condition("persistent.2_3")
    g.image("gallery/pic/Page2/3.png")

    g.button("2_4")
    g.condition("persistent.2_4")
    g.image("gallery/pic/Page2/4.png")

    g.button("2_5")
    g.condition("persistent.2_5")
    g.image("gallery/pic/Page2/5.png")

    g.button("2_6")
    g.condition("persistent.2_6")
    g.image("gallery/pic/Page2/6.png")

    g.button("2_7")
    g.condition("persistent.2_7")
    g.image("gallery/pic/Page2/7.png")

    g.button("2_8")
    g.condition("persistent.2_8")
    g.image("gallery/pic/Page2/8.png")

    g.button("2_9")
    g.condition("persistent.2_9")
    g.image("gallery/pic/Page2/9.png")

screen gallery_002:
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
        yalign 0.4
        xalign 0.4

        grid 3 3:
            spacing 15
            # Row 1
            add g.make_button("2_1","gallery/pic/cover/2_(1).png", locked = "gallery/pic/cover/locked.png")
            add g.make_button("2_2","gallery/pic/cover/2_(2).png", locked = "gallery/pic/cover/locked.png")
            add g.make_button("2_3","gallery/pic/cover/2_(3).png", locked = "gallery/pic/cover/locked.png")


            ## Row 2
            add g.make_button("2_4","gallery/pic/cover/2_(4).png", locked = "gallery/pic/cover/locked.png")
            add g.make_button("2_5","gallery/pic/cover/2_(5).png", locked = "gallery/pic/cover/locked.png")
            add g.make_button("2_6","gallery/pic/cover/2_(6).png", locked = "gallery/pic/cover/locked.png")


            ## Row 3
            add g.make_button("2_7","gallery/pic/cover/2_(7).png", locked = "gallery/pic/cover/locked.png")
            add g.make_button("2_8","gallery/pic/cover/2_(8).png", locked = "gallery/pic/cover/locked.png")
            add g.make_button("2_9","gallery/pic/cover/2_(9).png", locked = "gallery/pic/cover/locked.png")
