image presents = Text("Project Alice presents", font="gui/font/Aller_Rg.ttf", size=28)

image title = Text("Forgotten", font="gui/font/RifficFree-Bold.ttf", size=128)
image subtitle = Text("A mod for Doki Doki Literature Club!", size=24)

image chapter_one_header = Text("Chapter 1", size=24)
image chapter_one_title = Text("Just Another Day", font="gui/font/RifficFree-Bold.ttf", size=84)

label title:
    stop music fadeout 2.0
    scene black
    with trueblack
    pause 1.5
    show presents at truecenter with fade
    pause 1.5
    scene black with fade
    show title with fade:
        xalign 0.5
        yalign 0.4
    pause 1.5
    show subtitle with dissolve:
        xalign 0.5
        yalign 0.6
    pause 2.0
    scene black with fade
    $ persistent.saw_title = True
    return

label chapter0_title:
    show chapter_one_header with dissolve:
        xalign 0.5
        yalign 0.3
    pause 0.5
    show chapter_one_title with dissolve:
        xalign 0.5
        yalign 0.5
    pause 1.5
    hide chapter_one_header with dissolve
    hide chapter_one_title with dissolve
    return