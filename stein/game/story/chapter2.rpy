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

    # MARK: Natsuki in the Big Classroom
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
    show natsuki at f32
    n "Y-yeah..."
    n 4f "Look, just don't tell {i}anyone{/i} that you saw this, okay?"
    n 5s "I-it's not like I'm trying to protect them here or anything..."
    show natsuki at t32
    show alice 2h at t33
    "Alice raises her finger, wanting to comment, but I cut her off."
    mc "Yes, Alice, she is protecting them."
    mc "This is just kind of how Natsuki is; don't question it."
    mc "I don't fully understand, either."
    show alice 1h at t33
    "Alice lowers her finger."
    "Natsuki slugs me in the gut. Sayonika quietly chuckles."
    mc "Natsuki!!"
    show natsuki at f32
    n 1e "I'm being serious about something and that's what you come up with?"
    show alice at f33
    show natsuki at t32
    a 2k "I mean, to be fair, he kind of {i}did{/i} answer my question before I asked..."
    show alice at t33
    show natsuki 5s at t32
    "Natsuki steps back for a second."
    show sayonika at f31
    sy 3r "So what, are we going to just ignore this?"
    show natsuki at f32
    show sayonika at t31
    n 2f "Of course not, you dummy!"
    n 2q "I'll, uh... investigate it myself."
    n 1o "But I don't need you to get involved or anything!"
    show alice at f33
    show natsuki at t32
    a 2n "Natsuki, are you really sure you can handle it all by yourself?"
    a "That's got to be a lot of stress coming your way on top of what you're already dealing with."
    show alice at t33
    "Natsuki stomps her foot down."
    show natsuki at f32
    n 1e "You don't even know what I go through every day!"
    n "I'd be careful saying that kind of thing if I we-{nw}"
    show natsuki at t32
    show sayonika at f31
    sy 3p "Hey, give her some respect there!"
    sy "{i}You{/i} don't even know what she's gone through, either!"
    sy "Heck, she's even died once!"
    sy 2o "Wait, uh..."
    show sayonika 1k at f31
    show alice 1u at s33
    "Alice lowers her head as Sayonika thinks about what she just said."
    mc "Wait, what the hell do you mean by that?"
    "Alice steps out sheepishly."
    show alice at thide
    hide alice
    show sayonika at t21
    show natsuki at t22
    mc "Sayonika?"
    sy "Shit! I shouldn't have said that..."
    sy "She didn't, uh..."
    "I pause for a moment, shocked and hurt."
    "What the hell is going on?"
    "Why is this a big deal all of a sudden?"
    "I'd better get some answers, but I have to be careful about it."
    mc "I'm gonna, uh... {w=1.0}go check up on Alice."
    "I walk out the door and search for her in the hallway."
    show sayonika at thide
    show natsuki at thide
    hide sayonika
    hide natsuki
    
    # MARK: Confronting Alice
    stop music
    scene bg corridor
    with wipeleft
    "I look around to look for Alice, and it doesn't take long before I spot her at the end of the hallway."
    "She looks out the window, completely still. Not even a tear."
    show alice 1q at t11
    "I slowly approach her, making sure I don't scare her."
    mc "Alice, are you alright?"
    a 1n "Me? Eh, kind of..."
    play music t9
    a 1v "I just didn't expect her to say anything about...{w=0.5} that."
    mc "What did she mean about that?"
    mc "The wording was a bit unclear for me. I'm guessing it's symbolic?"
    a "No..."
    "She pulls her cardigan down a bit, revealing a scar across her chest."
    a 1q "She wasn't kidding."
    stop music fadeout 0.5
    a "I actually did die once. Stabbed right through the heart."
    a "I don't want to really get into the details or anything..."
    mc "Wow..."
    mc "I didn't realize..."
    a 1p "Eh, it's fine, really."
    play music t10 fadein 0.5
    a 1o "Just makes me a little more grateful to be alive now, you know?"
    mc "Yeah, that's true."
    a 1q "I'm just more worried about Natsuki."
    a "She can't possibly take all of that on, especially since she's still a student."
    a 1v "That and the fact that Sayonika snapped the way she did."
    a 2i "I'm not going to lie here. I'd take the chance to find out what's going on myself if I could."
    a 1k "I'm not really doing anything anyway."
    mc "I see."
    mc "Well, I'm sure if you make your case to Natsuki, she'd let you."
    mc "You probably have more experience than anyone else."
    a 2i "Not really, but I'm sure whoever did that is sending some kind of a message."
    a "And given that I {i}did{/i} see the halo and horns, this person isn't a fan of Monika... or me."
    a "They probably see Monika as a threat or some pawn in a bigger operation."
    a "I'll have to ask around, but I'm sure I can figure something out."
    mc "Well, if that's the case, I could help by talking to a couple of people."
    mc "It's the least I can do for this."
    a 1k "[player], you don't need to do anything."
    a 1g "I know you're probably busy, too, and I certainly wouldn't want to burden you."
    mc "It's fine. we can split the workload."
    mc "And we can compare notes when we need to."
    mc "Do we have a deal?"
    "Alice looks into my eyes for a bit before responding."
    a 1b "Alright, groupwork it is."
    a "I hope you're ready to work with angels."
    a "Let's head back before they get worried."
    show alice at thide
    hide alice
    "Alice takes my hand as we march back to the big classroom."
    "However, it appears that Sayonika and Natsuki had slipped out during our conversation."
    "Alice and I promptly decide to go back to the clubroom."
    
    # MARK: Back to the Clubroom
    scene bg club_day
    with wipeleft
    return
