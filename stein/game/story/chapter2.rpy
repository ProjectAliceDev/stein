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
    stop music fadeout 1.0
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
    play music t3
    "To no surprise, everyone was in the clubroom."
    "Yuri's in her usual place, reading another novel."
    "Completely phased, Natsuki's also in her typical spot reading manga."
    "Sayonika appears to be reading something on her phone."
    "And Sayori's doodling in her notebook, probably of everyone in the clubroom."
    "It was like as if nothing had happened at all."
    "Alice walks over to Sayonika, winking at Natsuki."
    
    # Call the appropriate scene from the poem game winner.
    python:
        preferred_alice = False
        preferred_sayori = False
        nextscene = "chapter_two_exclusive_choice"
        if poemwinner[0] != "natsuki":
            if poemwinner[0] == "monika":
                nextscene = "chapter_two_alice"
            else:
                nextscene = "chapter_two_" + poemwinner[0]


    call expression nextscene

    # MARK: Time for Poems... Maybe
    stop music fadeout 0.75
    scene bg club_day
    show sayori 1a at t11
    s 1r "Okay, everyone!"
    play music t5
    if not preferred_sayori:
        "I quickly jolt up, startled to hear that phrase."
        "Man, it's weird hearing her say that..."
        "I quick shrug it off and wait for the others to listen up."
    else:
        "I perk up and wait for another word from Sayori."
        "It's still kind of weird hearing Sayori say Monika's old catchphrase, but I guess it's tradition here."
        "The other girls perk up and we all head towards Sayori."
    show sayori at t31
    show natsuki 1a at t32
    show yuri 1a at t33
    s 1x "That pretty much wraps it up for today!"
    show natsuki at f32
    n 4m "Wait, don't we have to share poems?"
    show sayori at s31
    show natsuki at t32
    s 5a "Oh, right, ehehe..."
    mc "You forgot to write one, didn't you?"
    s 5d "Maybe..."
    show natsuki at f32
    n 4s "I might have forgotten to..."
    show yuri at f33
    show natsuki at s32
    y 4b "Uhh..."
    show yuri 4e at s33
    "Sayonika at Alice look down as soon as I look at them."
    mc "Wowie. I have no clue how we managed that."
    mc "I guess we should skip today."
    show sayori 1l at t31
    show natsuki 1u at t32
    show yuri 3o at t33
    "The girls all sheepishly look at me."
    "For a minute, I can kind of understand what Monika had to put up with."
    "And I'm not even the president."
    "One by one, the girls leave silently, not acknowledging me."
    "That is, except for Sayori."
    show natsuki at thide
    show yuri at thide
    hide natsuki
    hide yuri
    show sayori at t11
    "She continues to look at me sheepishly until I pipe up."
    mc "So I guess you're ready to go now?"
    s 1l "Y-yeah..."
    s 1k "Let's go."
    stop music
    show sayori at thide
    hide sayori

    # MARK: After the Club Meeting
    play music t3
    scene bg residential_day
    with wipeleft
    "Sayori and I walk back home, not a word between us."
    "Once we reach towards my house, I decide to speak up."
    show sayori 1k at t11
    mc "You know, you don't have to feel bad for not having a poem ready."
    s 3l "I know, I know."
    s "I just kind of feel bad for everyone forgetting."
    s "I'm guessing you didn't forget to."
    s 1g "Sorry... thta wasn't fair..."
    mc "It's okay, Sayori, stuff happens."
    mc "Just got to be ready next time, right?"
    s 1x "Yeah, that's it."
    s 4r "And next time, my poem will blow you away!"
    mc "Sure..."
    s 1x "Okay, challenge accepted!"
    mc "Wh-wha... Sayori!!!"
    s 4q "Hehe~"
    s "See you tomorrow."
    show sayori at thide
    hide sayori
    "Sayori skips over to her house, ready to take on that challenge."
    "Sometimes, I will never really understand her."
    "I pick up my phone to see if Alice had texted me."

    if preferred_alice:
        "I see a single notification."
        $ messages.receive("Alice", "Thanks for the fun time today! .^_~")
        "Well, that wasn't the notification I was expecting."
        "I'm guessing she'll text me later if she finds out anything."
        "Oh boy. What have I gotten myself into?"
    else:
        "Not surprisingly, there wasn't anything from her."
        "I assume she was busy driving Sayonika back or something."
        "I'm sure she'd text me back tomorrow or whenever she finds something out about earlier."

    "I put the phone back in my pocket and walk inside my house."
    return

# MARK: Chapter 3 - Exclusive Choice
# Only executed if winner of poem game is Natsuki.
label chapter_two_exclusive_choice:
    "Knowing how heated Natsuki was, I decide it's best to leave her be for now."
    "That being said, I'm kind of clueless as to where to go at this point..."
    stop music fadeout 1.5
    menu:
        "Who do I want to spend time with?"
        
        "Yuri":
            call chapter_two_yuri
        "Sayori":
            call chapter_two_sayori
        "Alice":
            call chapter_two_alice
    return

# MARK: Chapter 3 - Yuri Time
label chapter_two_yuri:
    "I hadn't really seen Yuri a whole lot today."
    "I guess I could check up on her and see what she's up to."
    play music t6
    "I slide right next to Yuri, pulling out the chair next to her."
    show yuri 1e at t11
    mc "Hey."
    "Yuri jumps unexpectedly."
    show yuri 3n at h11
    y "A-aah!"
    y 3o "[player], you, uh, startled me!"
    "Whoops, I forgot about that."
    mc "Sorry about that. I should've thought that through."
    mc "But since I'm here, is it alright if I spend some time with you today?"
    y "Y-eh...{w=1.0} uhh..."
    y 4c "Uuhhh...."
    mc "If you're not okay with it, I can just...{nw}"
    y 3q "No, no... it's f-fine..."
    y "I just didn't really, uh, prepare..."
    y 3o "Oh dear, I'm sorry..."
    mc "You're fine, Yuri."
    mc "You haven't done anything wrong."
    y "I, uh, know..."
    mc "Here, why don't we make some tea and relax a bit?"
    y 1q "Y-yeah, that w-works..."
    show yuri at thide
    hide yuri
    "Yuri gets up from her desk and goes to fill the pitcher up with water."
    "I take a look at the book she's reading, just to familiarize myself."
    "{i}The Illusion of Living{/i} by Joew Drew..."
    "I could've sworn I heard of this book before."
    "I wait patiently for Yuri to return."
    show yuri 1a at t11
    "She carries two cups over, now completely calm."
    y "Here we are."
    "She places a cup in front of me while swinging around to the other side to sit down again."
    mc "Thanks."
    "I take a sip from the cup."
    "Oolong."
    "Yuri takes a sip from hers and sighs."
    y 1m "Ah, yes."
    y "That's better."
    y 1f "I'm sorry, [player]. I don't know what got a hold of me earlier..."
    mc "It's alright now, Yuri."
    y "Unfortunately, I hadn't anticipated this, so I didn't bring another copy of the novel I'm reading."
    y 4a "But I, uh, am fine with sharing this one..."
    mc "It's all good, Yuri. And thanks."
    "Yuri opens the book to where she left off and slides it between the two of us."
    scene y_cg1_base with dissolve_cg
    "I scan the contents of the page to familarize myself while she starts reading on the left page."
    mc "So, what's this novel about?"
    y "Oh, it's a novel about how Joey Drew Studios and how they rose to fame and fell down."
    y "It's rather detailed and written in a very interesting way."
    mc "Why does that name sound familiar?"
    "I hear Alice stifle her laugh from across the room."
    "Yuri peeks her head up and notices her staring at her phone, trying to hold back."
    y "For a moment, I thought..."
    mc "Me too."
    y "You know, she really does look like Alice Angel, one of their characters."
    "She flips back a few pages until she finds an illustration."
    show y_cg1_exp1 at cgfade
    y "See?"
    "I look at the illustration for a bit, analyzing it."
    "The character on the page had the signature halo and horns, and the hair was parted very similarly."
    "I look back up at Alice."
    "{i}Is that...?{/i}"
    mc "Huh. You're right, Yuri. She really {i}does{/i} kind of look like her."
    y "I thought so."
    show y_cg1_exp2 at cgfade
    "Yuri smiles, relieved at my epiphany."
    hide y_cg1_exp1 at cgfade
    y "I've been watching her for a while now."
    y "You know, to kind of see if she'd do the same things as the character would."
    "We hear Alice giggle a bit."
    a "Oh, God! Ehehe~"
    "Everyone perks their head up, looking straight at Alice."
    a "Oops... sorry. Just, uh, a funny meme on Reddit."
    a "Carry on."
    "We all go back to focusing on each other."
    y "I don't know if that counts, but her character tends to giggle at things. A lot."
    y "Or that's at least how this book words it."
    mc "I don't know. It's probably just her just laughing at something programming-related..."
    show y_cg1_exp1 at cgfade
    hide y_cg1_exp2 at cgfade
    y "Oh? She's into programming like Sayonika?"
    mc "They work together. Alice pays her."
    hide y_cg1_exp1 at cgfade
    show y_cg1_exp2 at cgfade
    y "I see."
    mc "I got a bit of a weird question."
    mc "Does that book talk about anything related to, uh, stabbing?"
    hide y_cg1_exp2 at cgfade
    y "... what?"
    mc "Anything about Alice or someone getting stabbed in the back?"
    y "N-no... why are you asking that all of a sudden?"
    mc "Well, she showed me a scar earlier and told me she was stabbed."
    y "Oh..."
    y "Maybe I hadn't gotten to that yet..."
    mc "I'm sorry if that's a bit of a touchy subject. I just wanted to confirm my suspi-{nw}"
    return

# MARK: Chapter 3 - Sayori Time
label chapter_two_sayori:
    $ preferred_sayori = True
    "Sayori seems to be pretty upbeat right now."
    "I'm sure she wouldn't mind me joining in."
    play music t6
    show sayori 1a at t11
    "I casually slide next to Sayori, careful not to mess up her drawing."
    s 1x "Oh, hey [player]!"
    s "I guess you wanted to draw a bit?"
    mc "I figured I'd spend some time with you."
    mc "Kind of getting a bit bored right now."
    s "Fair enough. Here."
    "Sayori hands me a piece of construction paper and a box of crayons."
    s "I'm just doing some decorations for the mini-festival signs."
    mc "I see that. Which one is this for?"
    s 3c "Umm..."
    s "Why not make that one for the refreshments?"
    mc "Fair enough."
    show sayori 1b at t11
    "I take one of the crayons out and start writing the word 'Drinks' right on the paper."
    "Meanwhile, Sayori starts talking again."
    s 1c "You know, I've been kind of thinking lately..."
    s "Doesn't Alice seem familiar?"
    mc "I mean, I did meet her at the convention. Sort of."
    s "Well, I know that, but just... in general?"
    mc "Sayori, what are you talking about?"
    s "She kind of reminds me of a cartoon character I saw on TV once."
    s "You know, like one of the ones I fall asleep to at night."
    mc "The classics? Yeah, what about them?"
    s "She kind of looks like one of them. I can't remember the name, though."
    mc "I guess so?"
    show sayori 1b at t11
    "Sayori pulls out her phone and does a quick search."
    s 1c "Ah, here we are."
    "She shows me a picture of a cartoon character with the signature halo and horns, and her hair was parted similarly."
    "I look at Alice, who is engrossed in her phone."
    "{i}Is that...?{/i}"
    "I look back at Sayori, confounded."
    mc "Yeah, I see the resemblance."
    s 1x "That's what I thought. Apparently her name is Alice Angel."
    s 4r "Imagine that! We might have an angel in our presence."
    "We hear Alice giggle a bit."
    a "Oh, God! Ehehe~"
    "Everyone perks their head up, looking straight at Alice."
    a "Oops... sorry. Just, uh, a funny meme on Reddit."
    a "Carry on."
    "We all go back to focusing on each other."
    s 3m "Wow, she's even got the same giggle from the cartoons!"
    mc "Mhm."
    "I try to not think about the uncanny resemblance and continue drawing on the paper."
    s 1c "I wonder what got her into programming..."
    s "She doesn't seem the type."
    mc "My guess would be some sort of an epiphany, Sayori."
    mc "I don't know if I should say this, but she was stabbed once."
    s 1x "Oh, yeah, I know already."
    s 2c "Isn't that scar {i}huge{/i}? Almost like a machete went right through her..."
    s "But I guess that makes sense if she got into programming after that..."
    s 1d "Maybe like a second chance?"
    mc "Probably."
    mc "Did you want soda cans on this?"
    s 1c "Eh, maybe teacups would be better."
    s "But anyways, I need to get the club together. Hold on."
    return

# MARK: Chapter 3 - Alice Time
label chapter_two_alice:
    $ preferred_alice = True
    "If I'm going to be working with Alice a lot more, I should probably get to know her a little more."
    "It doesn't seem like she's doing much anyway other than looking at her phone or at whatever Sayonika's looking at."
    "I walk over to Alice and Sayonika and take a chair from a nearby desk."
    "Sayonika's too engrossed in her phone to even notice me, but Alice perks her head up."
    show alice 1a at t11
    play music t6
    a 1b "Oh, hey [player]."
    a "Surprised you wanted to sit next to me today."
    a 2p "Unfortunately, I really don't have anything."
    a "I didn't really plan for this."
    mc "It's fine. I didn't plan this either."
    "I slide the chair and sit next to Alice."
    a "Give me a second..."
    "She pulls out an iPad from her purse and places it between us."
    "She unlocks it and looks over her phone before tapping something on the iPad."
    a "Sorry, just making sure I do this handoff right..."
    a "Can never seem to get this first try."
    # TODO: Get a CG scene for this
    # scene a_cg1_base with dissolve_cg
    "She finally manages to get whatever she was reading up on the iPad without a hitch."
    a "I may be a developer, but this stuff still trips me up."
    mc "It looks like you were browsing..."
    "I squint at the display, unable to really recognize the app."
    mc "Uh..."
    a "That's Reddit."
    a "I use a different app called Apollo."
    a "I was just, uh, browsing programmer memes..."
    mc "I see..."
    "I really didn't understand what was going on on her screen, but it looked interesting enough."
    a "If you want, I can see if there's a book or something..."
    a "I'm sure I have something in there."
    "She taps and swipes away on the iPad like as she's performing a magical spell."
    "Finally, she gets the Books app open to her library."
    "The screen looked rather barren, as if she hasn't read anything."
    a "Hmm, looks like I don't have much. I should have better prepared, ehehe~"
    mc "You're fine."
    a "I mean, uh, I {i}guess{/i} we could read the Swift documentation together?"
    mc "I don't really know any programming, but I guess?"
    a "Ah. Maybe we could, uh..."
    "She frantically closes the Books app and looks for something else."
    "She eventually stops her finger over some app with an orange bird."
    "'Swift Playgrounds'."
    a "Guess this'll have to do. Sorry, [player], I {i}really{/i} should've better prepared..."
    mc "You're fine."
    "She opens the app and taps on a playground labelled \"Learn to Code 1\"."
    a "This should be alright. It's not much, but I'm sure you'll do just fine."
    a "Let me see if I have..."
    "She digs through her purse and pulls out a keyboard."
    "Tapping the space bar multiple times, she manages to get it to connect."
    a "Alright, let's see how you do."
    # scene a_cg1_addon with cg_dissolve
    "I pick up the keyboard and follow the instructions on the screen."
    "For the most part, it wasn't all that difficult to follow."
    "I quickly finish each page, hearing an approving noise from Alice occasionally."
    "I manage to reach the section about loops when Alice chimes in."
    a "Impressive, [player]! You're catching on really quickly."
    a "It took me a couple of hours to get to where you are."
    mc "Yeah, I'm kind of surprised, too."
    a "So what do you think so far?"
    mc "It's not bad, I guess."
    mc "I mostly play video games, so I guess this provides some insight."
    mc "What brought you into this, Alice?"
    a "Well, after I, uh... {w=1.0}woke up, I needed to find something to do to sustain myself."
    a "I saw someone in a café doing this kind of thing, and I asked them what they were doing."
    a "I was kind of hooked when I tried it out at an Apple Store a couple of days later."
    a "And I guess I've been at this ever since that."
    a "It's not much, but I'm able to sustain myself with the work I do in the App Store."
    a "That and working with Sayonika and that game publisher."
    mc "Wow, that's very interesting."
    mc "So do you usually use this, uh..."
    a "Language? Most of the time."
    a "A lot of the apps I write for the Mac and iPhone are written in Swift."
    a "The game I'm working on, though, is in another language called C# (C-sharp)."
    a "And my website is written with JavaScript."
    mc "You must know a lot."
    a "Kind of?"
    mc "So which one do you like the most?"
    "Alice thinks for a bit before speaking up."
    a "I guess that would go to Swift, hands down."
    a "It's just really easy to work with."
    a "Never really ran into a problem wi-{nw}"
    return
