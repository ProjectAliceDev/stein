# 
# chapter3_reprise.rpy
# Forgotten
#
# Created by Marquis Kurt on 6/12/19.
# Copyright © 2019 Project Alice. All rights reserved.
#

init style alice_talk is default:
    font "mod_assets/CaviarDreams_Bold.ttf"

# MARK: Chapter 4 (Ending)
label chapter3_reprise:
    stop music fadeout 1.0
    scene black
    with trueblack
    window hide
    pause 1.5
    call updateconsole("swift SwitchViews.swift \-\-as=Alice", "Working...")
    pause 2.0
    call updateconsole("", "WARN: Dreemurr.swift is missing.\nThis might cause problems!")
    $ consolehistory = []
    call hideconsole
    scene bg residential_entrance_night with dissolve_scene_full
    pause 2.0
    play music a2
    $ style.say_dialogue = style.alice_talk
    "I slowly wake up from the couch, looking at the front door."
    "It's midnight already?"
    "Well, I didn't see that one coming."
    $ style.say_dialogue = style.normal
    return
