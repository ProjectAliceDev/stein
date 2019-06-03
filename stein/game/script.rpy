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
    $ cr_name = "???"
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
        call end_js_32
        call ncredits
        call end_overlay
    else:
        call chapter_two
        stop music
        call screen ThrowASError(glitchtext(32))
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
