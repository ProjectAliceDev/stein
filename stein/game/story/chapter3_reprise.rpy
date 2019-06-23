# 
# chapter3_reprise.rpy
# Forgotten
#
# Created by Marquis Kurt on 6/12/19.
# Copyright © 2019 Project Alice. All rights reserved.
#

style alice_talk is default:
    font "mod_assets/CaviarDreams_Bold.ttf"
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos
    text_align gui.text_xalign

# MARK: Chapter 4 (Ending)
label chapter_three_reprise:
    stop music fadeout 1.0
    scene black
    with trueblack
    window hide
    pause 1.5
    call updateconsole("swift SwitchViews.swift -as=Alice", "Working...")
    pause 2.0
    call updateconsole("", "WARN: Dreemurr.swift is missing.\nThis might cause problems!")
    $ consolehistory = []
    call hideconsole
    scene bg residential_entrance_night with dissolve_scene_full
    play music a2 fadein 10.0
    pause 2.0
    $ style.say_dialogue = style.alice_talk
    "I slowly wake up from the couch, looking at the front door."
    "It's midnight already?"
    "Well, I didn't see that one coming."
    "Groggily, I get up and take a look around, checking if anything is off."
    "At this point, anything can happen since Monika's disappearace."
    "That freaking girl..."
    window hide
    pause 1.5
    window show
    "Well, everything appears to be normal."
    "I can also hear Sayonika snoring away upstairs."
    "Damn. I don't think I've ever heard anyone snore that loud before in my life..."
    "Well, maybe..."
    "Oh well."
    "I hear light tapping at the front door."
    "It's probably a bunch of birds or something."
    window hide
    pause 5.0
    window show
    "I hear the tapping again suddenly."
    "I don't think birds are that well-synchronized."
    "I go towards the front door, grabbing my trusty axe on the side."
    "There's only one other person that's used one of these well..."
    "I hesitate and wait to hear the tapping again."
    window hide
    pause 10.0
    window show
    "The tapping returns, but a little louder."
    "I grip onto the axe tightly."
    "Jesus. Why am I so scared all of a sudden?"
    "It's okay, Alice, you've handled yourself before."
    "Right? I mean, I've done it before..."
    "Remember Boris?"
    "..."
    "The only thing that's protecting me from the unknown is this door."
    "And I'm not sure if I'm willing to open it and expose myself like this."
    "I'm given no other choice here."
    "I gently open the door."
    scene black with fade
    "Hello-{nw}"
    stop music fadeout 0.5
    scene black
    pause 0.25
    play sound metal_hit
    pause 3.75
    show monika oneeye at t11
    m "And so we finally meet{w=1.5}, Alice Angel..."
    m "What a pleasant{w=0.5}...{w=3.5} surprise."
    m "Filled with such...{w=3.0} {i}determination{/i}."
    $ style.say_dialogue = style.normal
    scene black with dissolve
    window hide
    call updateconsole("swift SwitchViews.swift -as=default", "Working...")
    pause 2.0
    call updateconsole("", "WARN: Dreemurr.swift is missing.\nThis might cause problems!")
    return
