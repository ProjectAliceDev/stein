# MARK: Chapter Two
label chapter_two:
    stop music fadeout 1.5
    scene bg club_day
    with dissolve_scene_full
    play music t2
    call chapter_title(3, "An Unsettling Atmosphere")
    $ persistent.aliceos_permissions["Messages_notify"] = True

    "As usual, I find myself in the club room, ready for another meeting."
    "It's been a couple of days since we talked about the mini-festival we're throwing for ourselves."
    "The club room feels a little bit different today, though."
    "I can't quite put my finger on it."
    "I sigh and wait for one of the girls to arrive."
    window hide
    pause 2.5
    stop music fadeout 5.0
    window show
    "A few minutes pass."
    "Where is everyone?"
    "This is weird; no one is usually this late."
    "I hope I didn't miss a memo or something."
    "I decide to wait a little longer."
    window hide
    pause 2.0
    window show
    "Luckily, my fears subside as I hear footsteps."
    "{i}Finally{/i}..."
    "I prop myself up in one of the chairs as I watch Sayonika and Alice enter."
    show sayonika 1a at t21
    show alice 1a at t22
    "Recently, Alice has been tagging along with Sayonika after school to watch our meetings unfold."
    "In a way, she's kind of like an 'honorary member' of the club."
    "I'm not really sure what got her interested, though..."
    show alice at f22
    a 1b "Wowie."
    a 1i "[player], has it been this barren today?"
    show alice at t22
    mc "Yeah, you'd be surprised."
    mc "I've been sitting here for ten minutes. No one's showed up."
    show alice at f22
    a "There {i}is{/i} a meeting today, right?"
    a "Neither of us got a memo."
    show sayonika at f21
    show alice at t22
    sy 1r "Yeah, this is a bit weird."
    sy "I haven't heard anything from Sayori."
    sy "I hope everything's alright..."
    show sayonika at t21
    "Suddenly, I feel my phone vibrate."
    "I pick it up and view the notification that pops up."
    "It's from Natsuki."
    $ messages.receive("Natsuki", "Get your ass to the big classroom. There's something you need to see.")
    mc "Natsuki texted me."
    mc "We need to head to the big classroom."
    show sayonika at f21
    sy "The big classroom? How come?"
    show sayonika at t21
    mc "Se says there's something we need to see."
    show alice at f22
    a 2i "That phrase doesn't bode well."
    a 1q "I have a bad feeling about this."
    show alice at t22
    mc "I'm sure it's not that bad."
    mc "Let's go."
    show alice at thide
    hide alice
    show sayonika at thide
    hide sayonika
    "We leave the clubroom and head down to the big classroom."

    # MARK: Natsuki and The Big Reveal
    scene bg corridor
    with wipeleft
    "We make it to the hallway where the big classroom is."
    "Generally, the school uses this room for larger lectures or classes."
    "I think I've been in there only once."
    "However, something felt really off."
    "Alice and Sayonika stay close behind while I slowly approach the door."
    "My heart pounds really loudly as I reach for the door knob."
    a "There's something definitely off here."
    a "I don't know what it is, but I feel it."
    mc "I don't really want to go in here."
    mc "But we don't have a choice."
    "I gently open the door."
    scene bg m_classroom_skill with dissolve_scene_half
    play music td
    sy "Holy{w=0.25} shi{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.5
    stop sound
    hide screen tear
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    window hide
    pause 3.5
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    show fake_stop_error zorder 2:
        alpha 0.65
    pause 5.386
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    hide fake_stop_error
    window show
    "What the hell?"
    hide noise with dissolve
    hide vignette with dissolve
    "{i}What the hell???{/i}"
    "This...{w=1.0} this must be a joke."
    "A real sick one..."
    a "My God..."
    a "What in the name of fuck is this?"
    n "I... I honestly don't even know..."
    n "I hadn't texted Sayori about this. Or Yuri, for that matter..."
    n "I don't think they would handle this well at all."
    a "My stomach's not handling this well at all..."
    a "And mine's made out of freaking ink."
    "Alice leans over to a nearby trashcan and vomits."
    "Sayonika pulls out her phone and takes a picture before shutting the project off."
    scene bg m_classroom with dissolve
    stop music fadeout 2.5
    show sayonika 1o at t31
    show natsuki 5q at t32
    show alice 1u at t33 
    sy "Freaking hell."
    sy "I take it that was Monika..."
    n "Y-yeah..."
    n "Look, just don't tell {i}anyone{/i} that you saw this, okay?"
    n "I-it's not like I'm trying to protect them here or anything..."
    return
