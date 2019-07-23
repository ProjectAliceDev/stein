# MARK: Chapter Four
label chapter_three:
    stop music fadeout 1.5
    scene bg bedroom
    with dissolve_scene_full
    play music t2
    call chapter_title(4, "All the Power")
    if not persistent.aliceos_permissions["Messages_notify"]:
        $ persistent.aliceos_permissions["Messages_notify"] = True
    "I look at the clock near me after groggily waking up."
    "8:30. On a Saturday."
    "I didn't really have any plans today, so I guess this is fine."
    "I get out of bed and take a look at my clothes, deciding on a decent-looking outfit before heading to the shower."
    "I don't take long getting ready, usually taking only about 10 minutes."
    "Once I finish, I take a look at my phone to see if Alice had texted me."
    "Luckily, she did text me, but it looks like it was very recent."
    $ messages.receiveMessage("Alice", "Hey, did you want to join me in heading out? Could use time to talk about investigation. .^_~")
    "Well, I guess there's nothing wrong with that."
    "I text her back: 'Sure, when?'"
    "Surprisingly, she responds back in an instant."
    $ messages.receiveMessage("Alice", "Two minutes? Idk, unsure of how long it takes for you to get already.")
    "Wait, what?"
    "She doesn't live that close by, and it takes a couple of minutes by car to get here..."
    "I try to get an answer: '???'"
    $ messages.receiveMessage("Alice", "Ngl, already here. .^_~")
    "Wha?"
    "How? How is she here already?"
    "I take a peek out of the window."
    "That is certainly Alice's car. She wasn't kidding."
    "I rush out of my room and head out the door, completely ignoring Sayori."

    # MARK: Meeting with Alice
    scene bg residential_day
    with wipeleft
    "Granted, she even wasn't outside, but still..."
    "I meet up with Alice when I step out of the fence."
    "She greets me with a warm smile while holding on to a travel coffee cup."
    show alice 1a at t11
    a 1b "Hey there, [player]."
    a "Sorry that I didn't tell you earlier. I didn't really plan this."
    a 2k "But, I figured that since I was going to be about..."
    mc "It's fine, I guess."
    mc "I wasn't planning on going anywhere today, anyway."
    a 1a "Fair enough."
    a "We'd better get going. I don't want to hold Craig up."
    mc "Craig?"
    "Alice motions me into her car. I take the front passenger seat as she goes to the driver's side."

    # MARK: Alice Car Scene (CG)
    # scene a_cg2_base with dissolve_cg
    "She starts driving as I try to relax in the seat."
    "Man, this passenger seat is weirdly positioned..."
    "It doesn't take long for Alice to notice me trying to position myself."
    a "You know, you can move the seat to however you like."
    a "You don't need to leave in that position. Sayonika just likes it that way."
    mc "I see."
    "I pull the handle of the seat and readjust myself."
    a "See? That's better, isn't it?"
    mc "Mhm."
    a "I'm sorry I didn't bring any coffee for you."
    a "Again, I didn't really think this through..."
    mc "It's fine."
    mc "I'm kind of curious, though, what's the grind?"
    a "Ah, it's a special flavor from Matrinas."
    a "They call it 'Logo'. What an interesting name..."
    mc "What does it taste like?"
    a "Would it make sense for me to say that it tastes like an abstract feeling?"
    mc "What do you mean?"
    a "Well, if you drink it black, I guess you could say it tastes like narcissism."
    a "I don't know, it's kind of hard to describe, really."
    mc "Huh. I wonder why they named it the way they did."
    a "For reasons we do not fully understand..."
    "I nod."
    "I look out the front window for a bit, watching the raindrops fall."
    "Alice and I mostly remain silent until she pipes up as we take a turn."
    stop music fadeout 1.25
    a "So, I was starting to do some research last night on Monika."
    a "I didn't realize just how important Monika is to the community."
    mc "Yup. Very smart, athletic..."
    mc "Was a part of the debate club before starting ours."
    mc "For the most part, she seemed like any normal popular smart girl."
    mc "That all kind of changed when the club festival happened."
    play music a1
    a "Funny enough, I did find out something relating to that."
    a "Wasn't there some sort of tragedy?"
    mc "Well, not necessarily."
    mc "The festival didn't turn out well for us, but there wasn't anything like murder or something..."
    mc "At least not that I know of..."
    a "Weird. I found an article that talked about some girl cutting herself repeatedly towards the end of that festival."
    a "They didn't mention any names, though."
    a "And oddly enough, no one noticed Monika's disappearance until the Tuesday after."
    a "That was when the first missing persons report was filed on her."
    a "Do you remember her saying anything to you during that time?"
    mc "No, she was awfully silent after the festival."
    mc "She'd look at me with puppy eyes and not say anything."
    mc "Almost like as if she wanted me to giver her attention, but she didn't want to talk about it."
    a "Oh, I know that feeling."
    a "To be frank, I pulled that sort of thing once with Joey, just to see his reaction."
    a "Next thing you know, this happens."
    a "But I guess that really isn't the same for Monika, now is it?"
    mc "Perhaps not."
    mc "But I don't think there's any real reason for anyone at our school to hate on Monika."
    mc "She wasn't necessarily the most socially adept girl, but no one hated her. Not even Natsuki."
    a "I suspected Natsuki at first but quickly dismissed it."
    a "If anything, she's more worried about the club's state rather than looking to exact revenge on some undefined enemy."
    a "At least that's how I see it."
    a "Well, maybe we'll find out something to contribute to our investigation soon."
    mc "Perhaps."
    stop music fadeout 1.5
    a "That being said, we should be nearby..."

    # MARK: At the Mall
    scene bg mall_cloudy with dissolve_cg
    show alice 1a at t11
    "Alice pulls into a parking lot space near a mall."
    mc "Hmm."
    a 1h "Sadly there aren't any stores that aren't attached to this thing."
    a 2k "It's unfortunate since my social skills aren't up to par, but I have to work with it."
    mc "I think you'll be fine. We should get a move on, though, it's raining."
    a 1i "Wow, it really is. Hurry along now!"
    show alice at thide
    hide alice
    "We get out of the car quickly. I rush over to a nearby tree."
    "Alice doesn't hesistate to grab my hand as we run into the mall."
    a "This is a whole lotta rain!"
    "Once we make it inside, we stop and try to catch our breath."
    "I follow Alice down the main halls as we arrive to an Apple Store."

    # MARK: At the Apple Store
    scene bg apple
    with wipeleft
    play music t8
    "Surprisingly, the store felt somewhat empty. Perhaps we arrived early."
    "Alice and I head to the back desks, toward an employee about my age."
    "'Craig', his name tag reads."
    $ cr_name = "Craig"
    show craig 1a at t21
    show alice 1a at t22
    "He perks his head up and waves at Alice."
    show craig at f21
    cr 1h "Hey, Alice. Here to pick up your order?"
    show alice at f22
    show craig at t21
    a 1e "Yup, the usual."
    a 1i "Kind of surprised to see it come later than usual."
    show craig at f21
    show alice 1h at t22
    cr 1f "Yeah, we started to get a bit worried when we heard the truck was coming late."
    cr "You know how it is whenever our stuff comes in later."
    cr 1h "Say, it looks like you brought a friend."
    show alice at f22
    show craig at t21
    a 1j "Sure did."
    a 2b "This is [player], a friend of Sayonika's."
    a "We're working together on something, so I brought him with me today."
    show craig at f21
    show alice at t22
    cr 1c "So I guess that means you're helping her move her stuff, right?"
    mc "I... guess?"
    cr "She may look strong, but she doesn't have the strength or willpower to move two Mac Pros at once."
    "Alice smirks, and Craig tries hard to hold back his laugh."
    show craig 1p at t21
    show alice 1j at t22
    "What did I get myself into?"
    show alice at f22
    a 1d "So, it appears it's been slow in here."
    show craig at f21
    show alice at t22
    cr 1d "It has been. The rain's probably doing it."
    cr "But it isn't just us, it's the whole mall."
    cr 1f "Very unusual, I'd say."
    stop music fadeout 1.5
    cr "What's also unusual is that guy that's over there."
    cr 1k "They've been staring at those iPhones for about an hour now."
    cr "I've been keeping an eye on them, but no one seems worried."
    cr 1d "Here, I'm going to the back room to get you your stuff."
    cr "Let me know if something odd happens, alright?"
    show alice at f22
    show craig at t21
    a 1h "You have my word."
    show alice at t22
    "Craig heads to the back room, ocassionally peeking over."
    show craig at thide
    hide craig
    show alice at t11
    "Alice peeks over my shoulder, trying to keep an eye on the hooded figure."
    a 2i "To be fair, I don't think that's even a guy."
    a "I'm getting kinda creeped out."
    a "She's just...{w=1.0} lingering."
    "Unexpectedly, we begin hearing the hooded figure hum to themself."
    show alice 1u at t11
    "Alice looks worried, probably because she recognizes the tune."
    a 1s "Oh, dear God..."
    mc "What is it?"
    a "I-I recognize that tune..."
    a "{i}Lonely Angel...{/i}"
    a 1t "Ha, ha, ha~..."
    a 1y5 "It's okay Alice, just keep cool..."
    mc "Uh, are you alright?"
    a 1v "E-eh... not really..."
    "As expected, Craig returns with a dolly and a few boxes."
    show craig 1d at t21
    show alice 1u at t22
    cr "And here's your or{w=0.5}der..."
    cr 1o "Uh, Alice, are you okay?"
    "Alice swallows, silenty responding with her eyes."
    show craig at f21
    cr 1e "That guy's not bothering you, are they?"
    show craig at t21
    mc "Not necessarily, but she's kind of freaking out."
    mc "I guess they hummed some tune she knows of."
    show craig at f21
    cr "Oh..."
    "Craig suddenly has an epiphany on the song in question and gulps."
    cr 1k "Oh..."
    cr 1l "Oh, Jesus..."
    cr 1e "I-I'm sorry, Alice."
    cr "Here. I'll talk to them."
    show craig at t21
    "Craig walks over to the hooded figure and starts speaking with them."
    "After a few minutes, the hooded figure leaves, nodding at Alice before walking off in another direction."
    "Craig returns to us, phased."
    show craig at f21
    cr 1k "Well, that was certainly awkward."
    cr 1d "I don't think she'll cause much of a problem anymore."
    show craig at t21
    "Alice weakly chuckles to herself."
    show alice at f22
    a 1p "I guess so."
    a "Well, thanks for the help, anyway."
    show craig at f21
    show alice at t22
    cr 1h "Okay, is there anything else I can help with?"
    cr "Or is strong boi [player] going to help you for the rest?"
    show alice at f22
    show craig at t21
    a 2b "I think he's got it, Craig."
    a "But thanks."
    a 1b "Good luck with the rest of today."
    show craig at f21
    show alice at t22
    cr 1h "You too, Alice. Until next time."
    show craig at thide
    hide craig
    show alice at t11
    "Craig walks off and looks around for any other customers."
    "I take one of the boxes while Alice takes the other."

    # MARK: Back to the Car / At The Loft
    scene bg mall_day
    with wipeleft
    "By the time we step outside into the mall's parking lot, the rain had already cleared up."
    "Alice sighs in relief."
    show alice 1a at t11
    a 1b "Oh, thank goodness."
    a "We won't need to run..."
    mc "That's a relief."
    "We walk back to the car and Alice pops open the trunk with her keys."
    "Once the door opens, we gently place the boxes in the trunk."
    mc "Huh. These kind of look like oversized cheese graters."
    a "Yeah, I know. They've done it before."
    a 2k "But hey, at least it's not a trashcan!"
    show alice at thide
    hide alice
    "We get into her car and drive off to the loft that she shares with Sayonika."

    scene bg residential_entrance
    with wipeleft
    play music t6
    "Without delay, we arrive back at the loft, safe and sound."
    "I prop open the door with a nearby boulder to aid both me and Alice in carrying the boxes."
    "Unsurprisingly, Sayonika pops around the corner, hearing all of the commotion from moving them."
    show sayonika 1ba at t21
    show alice 1a at t22
    sy "Oh, hey guys."
    sy 1bb "Looks like you were busy."
    show alice at f22
    a 2g "That's one way of putting it."
    a 1b "Here, take your cheese grater."
    show sayonika at f21
    show alice at t22
    sy 3bf "{i}Cheese grater...?{/i}"
    "Alice points to one of the boxes on the floor."
    "Sayonika takes a look at the side and squeals."
    show sayonika at h21
    sy 1bc "Uwa...{w=1.0} a new Mac Pro?!"
    sy "Alice, I thought you were getting some sort of card or something, but...{w=1.0} wowie!"
    show alice at f22
    show sayonika at t21
    a 2g "Darling, that trashcan of yours is on its last legs."
    a "You deserve a little better than that."
    a 2k "And you can grate your cheese with it, too!"
    a 1j "Ehehe..."
    show alice at t22
    "Sayonika remains speechless."
    "I kind of expected it since she got {i}two{/i} of them, and it's unlikely for Alice to need to use two of them together."
    "I do kind of wonder how she did manage to get two, though..."
    show alice at f22
    a 1a "Look, don't sweat it."
    a 1b "I need my dev to be at her best, and, to do that, we need the best hardware and software."
    a "Consider it a 'company asset'."
    show alice 1j at t22
    stop music fadeout 2.5
    "Sayonika gulps."
    "I can only imagine the flurry of emotions going through the poor girl's head right now."
    "Shocked, thankful, surprised..."
    "She still remains speechless."
    "Alice seems well aware of it, too."
    "The friendship between the two is really strong, and nothing will seem to change it."
    play music t10
    "Sayonika quivers, trying to say something."
    "In an instant, Alice goes in for a full embrace, hugging her while Sayonika bursts into tears of joy."
    "Watching it unfold was like seeing a romantic movie or Natsuki and Yuri finally getting along after Monika left."
    "Quite charming."
    "After a few minutes, Alice and Sayonika let go of each other, completely calm and relaxed."
    "The two remain silent for a few more minutes until Alice looks back at the boxes."
    stop music fadeout 3.0
    show sayonika 1bs at t21
    show alice at f22
    a 1b "Okay, kid, go set up your cheese grater."
    show alice at t22
    "Sayonika, without saying a word, takes one of the boxes up to her room."
    show sayonika at thide
    hide sayonika
    show alice 1f at t11
    "As soon as she's out of sight, Alice chuckles."
    a "She's wonderful, isn't she?"
    mc "The two of you are quite a dynamic duo."
    a 1g "It really is like that, I guess."
    a 1b "Come now, [player]. We've got work to do."
    "I pick up the remaining box and follow Alice to her office."
    
    # MARK: Alice's Office
    scene bg loft_alice
    with wipeleft
    play music t6
    "I take a moment to analyze my surroundings, taking in just how amazing her place looks."
    mc "Wow..."
    show alice 1a at t11
    a 1j "You like it?"
    mc "This is really impressive, Alice!"
    mc "You must feel really relaxed here."
    a 2g "It's one of the reasons why I bought this place."
    a "I was sold the moment they showed me this office."
    a 2k "Sayonika really loves it, too."
    show alice 1a at t11
    mc "I must say."
    mc "So, uh, where are we putting this?"
    a 1b "Oh, you can put it to the side for now."
    a 1p "I kind of forgot to get my monitor from the other room."
    a 1j "No worries, I can just set it up tonight."
    mc "Why don't you just grab it now? Might as well save you time, right?"
    a 1k "I, uh, I guess..."
    show alice at thide
    hide alice
    "Alice steps out to grab the monitor."
    "In the meantime, I pull out one of the blue chairs and sit down, looking out the window."
    "I can only imagine looking at this every day while working on something as stressful as what Alice does."
    "It doesn't take long before Alice returns with a huge monitor in hand."
    show alice 1a at t11
    a 1j "Ehehe... I probably should've boxed this up before moving it here..."
    mc "Holy smokes! That's one huge monitor..."
    a 1p "Yeah, coding work needs big spaces..."
    "I slowly and carefully take the monitor out of her hands."
    a 2k "Ooh! Uh..."
    show alice 1e at t11
    "Alice giggles, almost like a little girl."
    "She puts her hand to her face, almost as if she was listening on on gossip."
    "It certainly felt weird seeing Alice act this way."
    "In a way, she kind of reminded me of Moni-{nw}"
    "No. I shouldn't say that."
    "I quickly shrug it off and place the monitor on the table."
    a 1h "Uh, [player]... you alright?"
    "Crap. She saw me shrug."
    mc "I'm fine. Just a bad thought, that's all."
    a 2h "Bad thought?"
    mc "Yeah, it's nothing to worry about, Alice."
    mc "Better that I ignore it."
    a "If you say so."
    mc "I'm not sure how you want the cables going about and where this is getting placed, so I'll just get the computer out of the box for now."
    a 1a "Alright. Be careful with that cheese grater."
    "I open the box and pull out the styrofoam and computer, placing it on the table."
    "After watching Alice set up the monitor in the place she wants it, I follow through with the computer, placing it underneath."
    "I slowly back out after, making sure I don't hit myself or Alice by accident."
    mc "I think that does it."
    a 1b "Well, thanks. You didn't have to."
    a "I can take care of the rest later. Only takes an hour or so."
    mc "So... what now?"
    a "Well, uh..."
    a 1h "Crap. I forgot."
    mc "Don't sweat it."
    mc "I'm sure you'll think of something soon."
    "Suddenly, we hear Sayonika call out."
    sy "Guys!"
    show sayonika 1bd at t21
    show alice at t22
    stop music fadeout 1.5
    "Sayonika enters."
    sy 2bf "We didn't happen to make dinner plans, did we?"
    show alice at f22
    show sayonika at t21
    play music t8
    a 2k "Ahaha... is it that time already?"
    a "Wow, time flies."
    show alice 1f at t22
    "I look at my watch."
    mc "Yup. 4:30PM."
    mc "Man, the day went by pretty quickly..."
    mc "I don't know if Sayori wanted dinner or anything..."
    "I feel a buzz from my back pockets."
    mc "Hold up."
    "I grab my phone and look at the lock screen."
    $ messages.receiveMessage("Sayori", "I can't remember if we had dinner plans.")
    mc "Heh."
    mc "Apparently Sayori doesn't know either."
    show alice at f22
    a 2g "Why don't you ask her if she wants to join us, then?"
    show alice at t22
    "I reply back to Sayori as per Alice's suggestion."
    "It doesn't take long for Sayori to respond. She's got speedy fingers."
    $ messages.receiveMessage("Sayori", "That sounds lovely. Any way to get food in my stomach is great rn.")
    mc "Well, looks like that's a yes."
    show alice at f22
    a 1k "Oh, good!"
    a 1b "Let's see what we can work with, shall we?"
    show sayonika at thide
    show alice at thide
    hide sayonika
    hide alice
    "I follow the girls up to the kitchen."
    "This will certainly be an interesting dinner."
    scene black with fade
    return
