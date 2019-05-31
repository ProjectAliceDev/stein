image forgotten_end_overlay = "mod_assets/ForgottenDemoOverlay.png"
image demo_text = Text("See you in Chapter 3.", font="gui/font/RifficFree-Bold.ttf", size=84)
image innerpartysystem = "mod_assets/images/bg/ips_layer.png"

label end_overlay:
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    scene forgotten_end_overlay with dissolve_scene_full
    pause 0.5
    show demo_text at truecenter with dissolve
    pause 3.5
    hide demo_text with dissolve
    pause 3.5
    scene black with fade
    $ persistent.playthrough = 1
    $ config.allow_skipping = True
    $ allow_skipping = True
    $ renpy.quit()
    return

label end_js_32:
    stop music fadeout 1.0
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    scene black with trueblack
    pause 10.0
    scene innerpartysystem
    play music g1
    show monika g1 at face
    pause 1.0
    stop music
    play music g2
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    hide screen tear
    $ config.allow_skipping = True
    $ allow_skipping = True
    stop music
    scene black with trueblack
    return