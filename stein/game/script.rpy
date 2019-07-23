# Entry point
label start:

    # ID of this playtrhoguh
    $ anticheat = persistent.anticheat

    # keep track of chapter
    $ chapter = 0

    # if they quit during a pause, we have to set _dismiss_pause to false again
    $ _dismiss_pause = config.developer

    # girl names
    $ s_name = "Sayori"
    $ m_name = glitchtext(12)
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    $ a_name = "???"
    $ cr_name = "Craig"
    $ sy_name = "???"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True

    if not persistent.playthrough == 1:
        if not persistent.saw_title:
            call title
        
        call chapter_zero
        call chapter_one
        $ chapter = 0 # Set for poem game reasons
        call fm_poemgame(True)
        call chapter_two
        call chapter_three
        call chapter_three_reprise
        call ncredits
        call end_overlay
    else:
        # Checks that the JavaScript server does not cause a buffer
        # overflow. If so, call the script to end the thread.
        python:
            import random
            javascript_serve = random.randint(1, 25)
            print("JavaScript Serve Code: " + str(javascript_serve))
        if javascript_serve >= 20:
            $ javascript_serve = None
            call end_js_32

        stop music
        $ ASHalt.halt(glitchtext(32))
        $ renpy.utter_restart()

    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
