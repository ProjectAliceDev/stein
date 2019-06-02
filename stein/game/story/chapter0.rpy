label chapter_zero:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    call chapter_title(1, "Just Another Day")

    s "Heeeeeeeyyy!!"
    "As usual, I see my best friend Sayori running towards me, oblivious to the attention she's drawing to herself."
    "We've been friends since we were children and are in the same literature club together."
    "Well, the literature club part is a little more complicated..."
    "Sayori invited me to join, and I took the offer, but things took a turn for the worse after my first week."
    "The president of the club suddenly disappeared, and Sayori took her place as interim president."
    "The old president's name... Monika, I think it was?"
    "Eh. Sayori took her place anyway."
    "I stand idly on the sidewalk, waiting for Sayori to catch up."
    "Sayori, out of breath, finally reaches me and collects herself."
    show sayori 4p at t11
    s "Don't tell me you were going to leave without me again!"
    mc "Well, Sayori, you gave me no other choice."
    mc "I'm surprised you didn't oversleep again, Miss President."
    show sayori at s11
    s 5c "Hey, that's meeean!"
    mc "Well, if you want people to respect you as a president, you should start acting like one."
    show sayori at t11
    s 2i "I can't be all perfect, you know!"
    "Sayori fails to keep a straight face while staring at me."
    s 4r "Besides, you wouldn't be mean to me all the time!"
    mc "Whatever you need to tell yourself, Sayori..."
    "Sayori beams."
    s 1q "Ehehe~"
    "We start walking in the direction of our school, part of our routine."
    "Sayori stares off into the distance for a while, pondering something."
    s 1x "We should be getting a new club member today, [player]."
    s "I hear she's really good at tech stuff like Monika was."
    s 1b "It kind of makes me wonder whether she reads instruction mauals for sport..."
    mc "Sayori, not all programmers do that."
    s 2c "Well of course not!"
    s "I'm just thinking of all of the different kinds of things she might read."
    mc "I guess we'll find out if she shows up today, then."
    s "Today's supposed to be her first day."
    s "She transferred from another school, and they said that she'd start today."
    s 3c "Imagine that! A transfer this early in the year!"
    mc "At least she's transferring now and not halfway through the year."
    s 1a "I'll walk to that!"
    
    scene bg campus
    with wipeleft
    "It doesn't take long before we arrive at the entrance."
    "Sayori nudges me on the side, carefully pointing out a car near the front."
    "I can faintly hear voices from that direction."
    a "Alright. You know what to do if something happens."
    a "I'll pick you up at around 4. Sound alright?"
    sy "Yup, sounds good."
    sy "See ya."
    a "Bon journee."
    "The car drives off, revealing a schoolmate, picking at the side of her tie."
    s "Oh, I bet that's...{nw}"
    "Before Sayori finishes her sentence, the girl waves at us, smiling intently."
    "Sayori grabs my hand as we rush over."
    show sayori 2r at t21
    show sayonika 1a at t22
    s "Hello! You must be the new student, right?"
    show sayonika at f22
    sy 2l "I sure am!"
    sy 1b "The name's Sayonika."
    $ sy_name = "Sayonika"
    show sayori at f21
    show sayonika at t22
    s 3x "What a lovely name!"
    s "I'm Sayori, interim president of the literature club."
    s "And this is my best friend and club member, [player]."
    show sayori at t21
    mc "Nice to meet you."
    "I nod my head. Sayonika smiles sweetly."
    show sayonika 4a at h22
    sy "Hehe~"
    show sayori at f21
    s 1c "I wonder if we have the same classes together..."
    show sayonika at f22
    show sayori at t21
    sy 1f "Ooh, um..."
    show sayonika at t22
    "She pulls out a piece of paper from a folder in her backpack."
    "Sayori inspects the paper, checking every row and column."
    show sayori 1o at t21
    s "Mhm..."
    "I play with one of my backpack's straps while waiting for Sayori to come to a conclusion."
    show sayori at f21
    s 2x "Aha~!"
    s "It looks like we have the same science class..."
    s "And the same English class!"
    s 4r "Oh, this works out wonderfully!"
    show sayonika at f22
    show sayori at t21
    sy 3e "Great! I believe I have English as the first class today."
    show sayori at f21
    show sayonika at t22
    s 1x "I'd be more than happy to show you around!"
    s "See you at the meeting, [player]!"
    show sayori at thide
    hide sayori
    show sayonika at t11
    sy 4k "It's nice meeting you, [player]~"
    show sayonika at thide
    hide sayonika
    "Sayori leads Sayonika inside, pointing out everything."
    "I follow from behind at a distance."
    "I think she'll be alright."

    stop music fadeout 1.0
    scene bg club_day
    with wipeleft
    play music t3
    "It's the end of the usual school day before I know it, and I find myself in the clubroom yet again."
    "I patiently wait as the other girls stroll in, one by one."
    "Surprisingly, Natsuki arrives first, beating Yuri's strike of early attendance."
    show natsuki 1a at t11
    "As usual, she carries her baking tray over to a desk, completely oblivious to the fact that I'm in the room."
    "It takes her a while before she finally notices that I'm looking at her with a smile."
    show natsuki 4e at h11
    n "Sweet Alice Angel!"
    n "How long have you been staring at me like that for?"
    mc "Long enough for you to not notice until now."
    n 2e "Apparently."
    n "Now could you help me move these tables instead of staring at me like that, you dummy?"
    "Classic Natsuki."
    mc "Yeah, let's do that."
    show natsuki at thide
    hide natsuki
    "Natsuki moves out some tables from the back while I take a few from the center to form a bigger one."
    "Yuri enters the room as soon as we finish setting up the room."
    show yuri 1a at t11
    y "Oh, hello, [player] and Natsuki. I didn't expect you to be here so early..."
    show natsuki 1c at t22
    show yuri at t21
    n "Yeah. Figured I'd get a headstart with setting the room up and all."
    n "Didn't expect this guy to be staring at my skirt for so long before saying anything, though."
    mc "Wha-...{w=0.5} Natsuki!!!"
    show natsuki at f22
    show yuri 2e at t21
    n 4d "Relax, [player]! I was just joking."
    n 5d "I'm willing to wager that you were staring at the tray."
    show natsuki at t22
    mc "Uh, sure."
    show yuri at f21
    y 1f "How long have you been in here?"
    show yuri at t21
    mc "Since last period. It's pretty quick getting here when you're just a few doors down."
    show yuri at f21
    y 1b "Ah, I see."
    y "I'll set up the tea. Hang tight."
    show yuri at thide
    hide yuri
    show natsuki 5a at t11
    "Yuri walks off to the closet where she keeps the tea set."
    "Meanwhile, Natsuki looks out the door, than back to me."
    n 2c "Hey [player]..."
    n "Did you meet the new girl?"
    mc "Yeah, I just met her this morning."
    mc "She seems alright if you ask me."
    n 1c "I had her in science today."
    n "She seems really smart. Like a genius or something..."
    n "I hear she does a lot of programming in her spare time. Probably has a part-time job."
    n "Really nice, too."
    n 5q "I'm kind of hoping she doesn't turn out like Monika."
    n "Something was just not {i}right{/i} about that girl."
    mc "I think Sayonika will be okay."
    mc "She seems like she's got a hold of things."
    mc "As long as Sayori's leading the club, she'll be in a good place."
    n 5m "Yeah, as long as Sayori doesn't end up like Monika, either."
    "Yuri returns from setting up the tea."
    show yuri 1e at t21
    show natsuki at t22
    y "Did I miss anything?"
    show natsuki at f22
    n 4k "Not really. Just some chit-chat about the new girl, Sayonika."
    show yuri at f21
    show natsuki at t22
    y 2f "Oh, Sayonika?"
    y 1b "She seems like a fine young lady."
    y "Real talented with computers."
    y "A really inventive and curious gal at that."
    y 3c "She led such a wonderful discussion in history class today."
    show natsuki at f22
    show yuri 3a at t21
    n 3d "Well, good to see you have high opinions of her."
    n 5z "I bet you and her would be good reading buddies."
    show yuri at f21
    show natsuki at t22
    y 2f "Oh, is she joining us?"
    show natsuki at f22
    show yuri at t21
    n 1d "Apparently so."
    show natsuki at t22
    mc "Sayori said she'd be doing so this morning."
    mc "Speaking of which..."
    "I nod as both Sayori and Sayonika enter the clubroom."
    s "Hey there!"
    show yuri at t41
    show sayori 1x at t42
    show sayonika 1a at t43
    show natsuki at t44
    s "I hope everyone's doing well!"
    s "I'm excited to introduce you to our new member...{w=1.0} Sayonika!"
    show sayonika zorder 3 at f43
    sy 2b "Hey, everyone!"
    sy "I'm excited to get to know all of you."
    show sayonika zorder 2 at t43
    show yuri zorder 3 at f41
    y 1b "Oh, hello again, Sayonika."
    y "It's a pleasure to see you be a part of the literature club."
    show natsuki zorder 3 at f44
    show yuri zorder 2 at t41
    n 2d "I hope you don't mind some cupcakes with your reading."
    show natsuki zorder 2 at t44
    mc "Hello again, Sayonika. Welcome to the literature club."
    show sayori zorder 3 at f42
    s "Okay, everyone! Let's get settled in."

    scene bg club_day
    with wipeleft
    "We all gather around the table as Natsuki begins distributing the cupcakes."
    "Each cupcake had a different design on them, almost like the abstract art you'd find in a museum."
    "On the opposite end, Yuri starts pouring tea into our tea cups."
    "I look over each spot to make sure everyone has napkins in the meantime."
    "When Yuri and Natsuki finish distributing, they sit down in the respective places."
    "Surprisingly, they're sitting next to each other, something I hadn't seen before."
    "Sayori nods and starts speaking."
    show sayori 1x at t11
    s "Alright, now that we're settled in, let's talk business."
    s "As you all already know, Sayonika is joining us today as our newest club member."
    s "I hope you show her the same love and respect as we have done for all of our members."
    s 4r "Sayonika, I hope you find yourself comfortable here. Feel free to explore; have fun!"
    s 1x "With that said, there are a few announcements and things of that nature I have to discuss with you all."
    s 2c "I'm sure you all know that the fall break is coming up soon, meaning that our own mini-festival is around the corner."
    s "I'd definitely would like to spend our next meeting to discuss what we want to do for that, so please make sure you come!"
    s 3l "I wouldn't want to necessarily offend out previous president's work, but I would love to see something more fun and lighthearted than the club festival!"
    show sayonika 1f at t22
    show sayori 1a at t21
    sy "... previous president?"
    s 2l "Oh, that's right..."
    s "Don't worry about it; I don't want to burden you with that."
    show natsuki 5c at t33
    show sayori at t31
    show sayonika at t32
    n "Yeah, Sayori wasn't always president."
    n "We had a girl at the beginning of the year running this."
    n "She put a lot of effort into this club, you know. This was her 'hopes and dreams'."
    n "She kind of disappeared after the club festival, just one week after [player] joined us."
    n "She must've went insane or something."
    n "I don't know, it kind of felt like one of the novels Yuri reads so passionately."
    n 5q "Kind of sad, really."
    show natsuki at thide
    hide natsuki
    show sayori at t21
    show sayonika at f22
    sy 2i "I, uh...{w=1.0} see..."
    show sayonika 1d at t22
    show sayori at f21
    s 1h "I wouldn't worry about, Sayonika. The club's in good hands now."
    s 2d "She trusted me to make sure the club would still go on."
    s "Just relax and have fun, alright?"
    show sayonika at f22
    show sayori at t21
    sy 1b "Got it, captain!"
    show sayonika at thide
    hide sayonika
    show sayori at t11
    s 1x "Discussion aside, I hope everyone can make it to the next meeting to talk about the festival."
    s "Now, I don't believe I..."
    show sayori 1n at t11
    "Sayori thinks for a second, realizing what else she needed to say."
    s "Ooh, right! I almost forgot."
    s 3x "It's been a rough couple of weeks, and it'd be unfair to Sayonika if we did our usual routine, so we're going to skip the poems today, alright?"
    "Natsuki sighs in relief."
    "Yuri nods in agreement."
    s 4x "Alrighty then, that's all of the announcements!"
    s "Now, I believe Yuri said last time that we had a Scrabble set in the closet...?"
    "Before Sayori finishes her thought, Yuri arrives back at the table with Scrabble in her hand."
    s 1c "Wow, you're quick. I didn't even see you leave the table!"
    show yuri 1a at f22
    show sayori at t11
    y "Oh, I didn't say anything."
    y "Well, here's the game. Let's set up, shall we?"

    scene bg club_day
    with wipeleft
    "The five of us play a few rounds of Scrabble while munching away on the cupcakes."
    "Yuri won a couple of games, competing with Sayonika for a while."
    "Sayori and Natsuki watched, encouraging their clubmates to make the best moves."
    "Before we know it, the meeting is over."
    "Natsuki and I help rearrange the room while Yuri and Sayonika sweep the floors."
    "Sayori replaces the garbage bag in the trash can and takes out the old bag."
    "When we're finished with cleanup, we all gather around one last time."
    show sayori 4r at t11
    s "Alright, everyone! Thanks for coming; see you next time!"
    s 4x "And don't forget to bring your ideas."
    ny "Thanks! See you later."
    "Natsuki and Yuri leave the clubroom, talking about the Scrabble match."
    "Meanwhile, Sayonika approaches us, glancing at her watch."
    show sayonika 1h at t22
    show sayori 1a at t21
    sy "I'm surprised we finished so early..."
    mc "We usually don't take too long. We've had hour-long meetings before, but we decided to cut them a little bit."
    sy 1b "Well, thanks for a great first meeting."
    sy "I had a lot of fun today."
    show sayori at f21
    show sayonika at t22
    s 2x "That's wonderful, Sayonika!"
    s "I'm glad you had fun today."
    s "I'd love to hear your thoughts tomorrow on the festi-{nw}"
    show sayori at t21
    "Suddenly, we hear someone call out from the hallway."
    a "Sayonika?"
    a "Dear, where did you go?"
    mc "Huh. I wonder who that is..."
    "Sayonika panickingly looks down at her watch, then sighs in relief."
    show sayonika at f22
    sy 2i "Whew, it's only 3:50."
    sy "I guess she's here early."
    "Sayonika pokes her head out the door and waves."
    show sayonika 1b at t22
    sy "Hey! I'm over here!"
    "Sayonika return to the two of us."
    sy "My ride's here."
    "Shortly after, I notice a woman enter the clubroom quietly."
    "Sayori turns around as she notices me zero in on her unusual hair accessory."
    s "Oh, hi there!"
    s "We were just finishing up our club meeting."
    "The woman steps forward, joining our group."
    "Her halo-like ring in her hair bobs a bit as she walks towards us."
    "I hadn't seen anything like it before..."
    show alice 1b at t32
    show sayori at t31
    show sayonika at t33
    a "My apologies, I hope I wasn't interrupting anything..."
    "Her golden eyes lock onto mine rather intensely."
    "Her halo-like ring bobbed again as she tilted her head to the side."
    a 1i "Have... have we met before?"
    mc "Not that I know of..."
    a "I swear I've seen you before somewhere."
    show sayonika zorder 3 at f33
    sy "Oh, don't worry, Alice, he's just a member of the literature club I just joined."
    $ a_name = "Alice"
    sy "He won't bite."
    show sayonika zorder 2 at t33
    "{i}Alice...{/i}"
    "Where have I heard that name before?"
    "I sheepishly say something to stop the awkward silence."
    mc "Howdy..."
    "Luckily, Sayori notices the situation I've gotten into and steps in."
    show sayori zorder 3 at f31
    s 3x "Oh, hi there, Alice! You must be the one who dropped her off this morning, right?"
    s "I have to say, she's fitting in quite nicely and is such a charm in our club!"
    show alice zorder 3 at f32
    show sayori zorder 2 at t31
    a 1e "Well, that's wonderful. I feared she'd stick out like a sore thumb..."
    "She clears her throat and tries to disregard the fact that I'm in the room."
    "{i}Where have I seen her before?{/i}"
    a 2b "Well, Sayonika, I'm ready to leave when you are."
    a "I wouldn't want to rush you or anything... the compiler's going to be running for at least a good hour."
    show sayonika zorder 3 at t33
    show alice zorder 2 at t32
    sy 3a "Sounds good to me."
    sy "See you two later."
    "Alice nods and the two walk out of the clubroom."
    show sayonika at thide
    hide sayonika
    show alice at thide
    hide alice
    show sayori at t11
    s 1b "You looked a little uncomfortable there, [player]."
    s 1g "Are you okay?"
    mc "Yeah, I guess."
    mc "I had some sort of a brainfart or something."
    mc "Nothing else."
    s 1c "Alright. Let's get going, then."
    "Sayori and I leave the clubroom, closing the doors for the night."

    scene bg residential_day
    with wipeleft
    show sayori 1a at t11
    s 1x "Well, Sayonika was awfully nice."
    s "I'm glad she's finding her place in the club."
    mc "It looks like she had fun."
    mc "I'm certain she'll return tomorrow."
    s 1c "Yeah. And maybe that Alice lady could swing by, too?"
    mc "... maybe."
    "I shrug."
    s 3g "[player], are you {i}sure{/i} you're alright?"
    s "You seemed kind of spooked when you saw her."
    mc "I can't put my finger on it, but I feel like I've seen her before somewhere."
    mc "And she seemed to recognize me, too."
    mc "It was pretty weird."
    s 3h "You probably ran into her at somepoint or saw each other at a deli or something..."
    s "I meet all sorts of interesting people when I'm there."
    mc "Sayori, you're, like, {i}always{/i} there..."
    show sayori at s11
    s 5a "Ehehe... is that so..."
    mc "I'm not saying it's necessarily a bad thing..."
    show sayori at t11
    s 1c "I guess."
    s "Look, [player], don't stress over it."
    s "I'm sure everything will get sorted out within a couple of days."
    mc "I hope so."
    s 2d "Promise you won't linger on it?"
    mc "Promise."
    s 1q "Good. Now let's head to the deli real quick."
    mc "Sayori!!!"
    s "Ehehe~"
    show sayori at thide
    hide sayori
    
    stop music fadeout 1.0
    scene black with fade
    pause 1.5
    scene bg bedroom_night with dissolve_scene_full
    "I find myself unable to really sleep tonight."
    "I know I promised Sayori that I wouldn't worry about anything, but I am definitely shaken."
    "And, oddly enough, it has nothing to do with Alice."
    "I look at my nightstand and take a sip from my water cup."
    "The water runs down my throat like a soothing waterfall."
    "I lie back down and stare at the ceiling."
    "It's been so long since I've heard the name."
    "{i}Monika...{/i}"
    "None of us know how or why she disappeared."
    "After the club festival, she kind of stop... showing up."
    "Absent from school. Nowhere to be seen in town."
    "We hadn't heard anything. I think people have stopped looking."
    "Now it's October, almost three months since that day."
    "It's been different with Sayori as president, but all of us aren't the same because she disappeared."
    "And now here we are, talking about her again."
    "Like as if her disappearance happened yesterday."
    "I sigh, burying my face into my pillow."
    "{i}This is going to be a long, long night...{/i}"
    return