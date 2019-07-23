# 
# monika_test.rpy
# Forgotten
#
# Created by Marquis Kurt on 6/19/19.
# Copyright © 2019 Project Alice. All rights reserved.
#

# MARK: monika_test entry point
label monika_test:
    stop music fadeout 0.5
    scene black
    with trueblack
    m "Oh, easy dear!"
    m "Don't move too much. You'll sprain yourself."
    m "There, there..."
    scene bg m_mountains
    with dissolve_scene_full
    show monika 1e at t11
    $ m_name = "Monika"
    m "It's alright, [player]..."
    m 5a "I got you."
    mc "Wh...{w=3.0} where am I?"
    m 4g "A place far away from the dangers of that forest."
    m 4e "Don't worry, I'll take care of you."
    mc "How did I get here?"
    m 1o "I can't say for certain."
    m 2i "I was hoping {i}you{/i} answer that for me."
    m 3r "To be honest, I'm totally unsure as to what you were, well, doing in that forest."
    m 4i "So, please, do enlighten me here."
    mc "Monika, please..."
    mc "Aren't you at least happy to see me?"
    m 4h "..."
    m "{i}Happy?{i}"
    $ style.say_dialogue = style.edited
    m 5b "HAPPY?!"
    $ style.say_dialogue = style.normal
    "Her red eye glows in anger."
    m 1h "Happiness does not exist, [player]."
    m 1i "It's just a construct of human emotion. Absolutely pointless."
    m "And for you to think I'm...{w=1.0} happy..."
    m 3k "Ahaha~!"
    m 5a "You must be insane."
    "At this point, I just can't understand who this girl is."
    "She's not the favorable, cheery valedictorian we all know."
    "Something's happened, but I can't quite put my finger on it."
    mc "M-Monika..."
    mc "What's happened to you?"
    mc "I'm worried for you."
    m 3i "That's the first time I've ever heard you say that...{w=1.0} to my face."
    m 1p "Oh, choices, choices..."
    m 1q "I can't tell if you're being genuine."
    mc "Monika, please..."
    m 1r "{i}*sigh*{/i}"
    m 1r "Well then, since you're so dearly concerned..."
    "Monika begins pacing slowly."
    show monika at t21
    m 3h "I just am not sute you'd be able to really understand, [player]."
    m 1g "Do you know what it's like? Knowing that your whole world as you know it is just...{w=1.0} a lie?"
    show monika at t11
    m 2o "I... thought I knew everything."
    m 2h "I thought everything was going well."
    show monika at t22
    m 2m "Starting my own club, being the top of my class..."
    m "I... I had a good life."
    m 1q "It was such a shame to find out that it was all just a construct."
    show monika at t11
    m 4h "And, unfortunately, it looks like the two of us know the truth."
    m 4i "And I know that you know {i}exactly{/i} how I feel..."
    show monika at h11
    m 5b "Betrayed!"
    $ style.say_dialogue = style.edited
    m 5d "ABANDONED!"
    $ style.say_dialogue = style.normal
    m 5e "You left me..."
    $ style.say_dialogue = style.edited
    m 5c "In this heartless, unhappy world, it's {i}kill{/i} or {i}be{/i} killed."
    $ style.say_dialogue = style.normal
    return
