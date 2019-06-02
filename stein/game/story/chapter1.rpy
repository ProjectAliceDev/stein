label chapter_one:
    scene bg bedroom 
    with dissolve_scene_full
    play music t2
    call chapter_title(2, "A Missing Checkpoint")

    "For a Saturday, things definitely could look better."
    "I look outside my window, watching the rain pour on the street."
    "Meanwhile, Sayori's doing some coloring in a notebook."
    "She got here earlier this morning and told me I overslept."
    "I guess last night really took a toll on me."
    "The rain pours a little harder, loud enough for Sayori to notice."
    show sayori 1bb at t11
    s "Ooh, that's some harsh rain there!"
    mc "Yeah, it's probably going to thunderstorm later at this rate."
    s "I hope not. I didn't bring any flashlights on me..."
    mc "It'll probably be at around midnight, I guess..."
    s 2bc "I'd prefer not at all!"
    mc "It's just a guess."
    "As soon as I finish my sentence, Sayori's phone rings."
    s 3bc "Oh, I wonder who that is..."
    "Sayori picks up her phone and responds with a cheerful hello."
    "I look out the window again and notice the rain travelling down the street, almost like a river."
    "I lose myself in watching the rain, almost oblivious to Sayori's conversation."
    "The rain subsided a little by the time I hear Sayori squeal."
    s 4bx "Ooh, sure!"
    s 4br "Okay, see you then!"
    "She hangs up the phone, placing it in her back pocket."
    s 1bx "Hey [player], Sayonika just called."
    s "She's inviting us to check out her place."
    mc "Did she? That's nice of her..."
    s "I don't know if you want to tag along, but I'm heading down there."
    s "Not really enjoying the rain."
    mc "I guess I could come..."
    s 4br "Great!"
    "I pick up my belongings while Sayori closes the window."
    "I turn off the light switch and close the door as we both leave my room."

    scene bg residential_entrance
    with wipeleft
    "It didn't take long before we make it to Sayonika's place."
    "I figured that Sayori and Sayonika exchanged information yesterday, so Sayori knew where she'd be."
    "Nonetheless, we wait for Sayonika to appear."
    "In an expected fashion, Sayonika walks in from the left, laptop in hand."
    show sayonika 1bb at t22
    show sayori 1ba at t21
    sy "Hey guys! Glad you could make it, despite the rain."
    show sayori at f21
    s 1bx "It wasn't too bad. It stopped as soon as [player] and I walked out the house."
    show sayonika at f22
    show sayori at t21
    sy 1bf "Wow, sounds like you lucked out there."
    sy "I'm sure Alice would get pretty scared going out in the rain."
    sy 3bi "Let's just say her and water don't get along very well."
    show sayonika at t22
    stop music fadeout 1.5
    mc "Are you saying that she has a phobia of water or something?"
    a "Oh, nothing like that, surprisingly."
    "Without notice, Alice slips in from behind."
    play music t6
    show alice 1a at t33
    show sayori at t31
    show sayonika 1bg at t32
    mc "Oh, hi Alice, I didn't see you slide in."
    show alice at f33
    a 1e "Angels like me are awfully silent, didn't you know that?"
    "Flattering."
    show sayonika at f32
    show alice 1a at t33
    sy 2bh "You'd be surprised."
    sy "She sometimes slips in while I'm super concentrated on something and startles me when she says something."
    sy "She's definitely aware."
    sy 1bi "Well, except when she's dealing with water."
    show alice at f33
    show sayonika 1bd at t32
    a 1k "I, uh, guess you could say I'm clumsy with any liquid that isn't ink."
    show sayori at f31
    show alice at t33
    s 1bb "Ink?"
    s "I guess you write a lot of books or something?"
    show sayonika at f32
    show sayori at t31
    sy 1bh "That's a long story, actually."
    sy 1bi "One that I don't think she's comfortable sharing with people she just met."
    sy 2bi "Considering yesterday's...{w=0.5} episode..."
    show alice at f33
    show sayonika at t32
    a 1p "Jeez, you make it sound like he murdered me or something."
    a "I'm clearly still alive, you know."
    a "And besides, I don't think he's pointlessly cruel."
    show sayori at f31
    show alice 1o at t33
    s 4bw "Uwaa~?!"
    s "What do you mean?!"
    show sayonika at f32
    show sayori 3bu at t31
    sy 1bh "Oh, she's just making a reference."
    sy 1bi "Probably not a good choice of words..."
    show sayori at f31
    show sayonika 1bg at t32
    s 1bg "Oh..."
    s 1bf "I don't get it."
    mc "I think she was making a reference to that portal game..."
    mc "I can't remember the name."
    "It takes Sayori a second before she realizes what I mean."
    s 1bc "Oh! You mean {i}Portal 2{/i}?"
    show sayori 1bb at t31
    mc "Was that what it was called?"
    "Alice sheepishly chuckles."
    show alice 1k at s33
    a "Ehehe..."
    "She slips her way out of the conversation, slightly embarassed."
    show alice at thide
    hide alice
    show sayori at t21
    show sayonika at f22
    sy 3bi "She, uh, doesn't go out much."
    sy "Her interpersonal skills haven't been the greatest for a long while."
    sy 3bo "It's a wonder she hasn't gone nuts at this point."
    sy "Or really lonely, for that matter..."
    show sayori at f21
    show sayonika at t22
    s 1bc "How long whave you known her for?"
    show sayonika at f22
    show sayori 1bb at t21
    sy 1bh "A couple of months at least."
    sy "I was looking for a part-time job when she found me."
    sy "She figured I'd be a good assistant developer for her."
    show sayori at f21
    show sayonika at t22
    s 1bx "I see. And it looks like she offers you a place to stay, too?"
    show sayonika at f22
    show sayori 1ba at t21
    sy 1bb "Yup, and I'm pretty grateful."
    sy 1bh "It's been a bit rough in my family, and it wasn't really helping me out."
    sy 1bb "So I knew I had to accept when Alice offered it."
    sy "It at least would help me in the long run for college, too."
    show sayonika at t22
    mc "Wow, that sounds wonderful."
    mc "Good for you!"
    "I hope that didn't sound sarcastic or demeaning."
    show sayonika at h22
    sy 4bb "Thank you!"
    "Oh, thank God."
    sy 1bb "Well, I guess I should give you a tour of the place."
    show sayori at thide
    show sayonika at thide
    hide sayori
    hide sayonika
    "We follow Sayonika through the loft, taking in the well-designed architecture."

    scene bg bedroom_sy
    with wipeleft
    "Finally, Sayonika shows us her bedroom."
    "Compared to the rest of the place, it felt a little cramped, but not too uncomfortable."
    "Sayori and Sayonika keep chit-chatting while I take a moment to absorb the room."
    "I notice a few interesting gadgets on her desk, probably to help her with her coding work."
    "She has a decently-sized bookshelf next to the desk with manuals for all sorts of languages. C#, Java, Swift, Python..."
    "Below the books were a few trinkets and accessories, even and old Macintosh."
    "The beige color contrasted with the bookshelf wood nicely, like as if it was on display."
    "It doesn't take long for Sayonika to notice me staring at it in awe."
    show sayonika 2bb at t11
    sy "Ah, yes, my dad's old Mac."
    sy "He used that thing for such a long time. Never broke on him once."
    sy "He told me stories about the kinds of things he did with it, and I guess that's how I got into programming."
    sy "Knowing that we have the power to control some beige box that sat on a desk with immense power..."
    sy 4bl "It's almost like magic."
    mc "Well, it certainly looks great on your bookshelf there."
    show sayori 3bc at t22
    show sayonika at t21
    s "Hey Sayonika, what's that trash can doing on your desk?"
    "Sayori points to a small black cylinder on her desk, next to the monitor."
    show sayonika at f21
    sy 2bi "Sayori, that's not a trash can..."
    sy 1bb "That's actually my computer. A Mac Pro from 2013."
    sy 1bd "It's kind of on its last legs."
    sy "While it did serve me a good six years, I am in dire need of an upgrade."
    sy 3bb "Luckily, I'm supposed to be picking up a new machine this week."
    sy "I believe Alice is getting some new equipment, too, so we're going together."
    sy "I just hope the Apple Store won't be super crowded like last week."
    show sayori at f22
    show sayonika 1ba at t21
    s 1bj "When isn't that place crowded?"
    s "I had to wait a while before I could get a new charging cable."
    s "Literally unacceptable!"
    "Sayori smirks while saying that last line."
    "Sayonika chuckles to herself."
    show sayonika at f21
    show sayori 1ba at t22
    sy 2bl "You know, Sayori, you're kind of like Alice in some ways..."
    "Unsurpisingly, we hear Alice approach us."
    show alice 1a at t33
    show sayonika at t31
    show sayori at t32
    a "Hey."
    a 1d "I just finished making the pull request, so the tests should be running."
    a "It's probably going to take a while before it gets reviewed."
    show sayonika at f31
    sy 1bh "Wow, you've patched that up real quick."
    sy "Looks like you're going to have to wait for Phil's OK."
    sy "I don't imagine he'll take long, though."
    show sayori at f32
    show sayonika 1bd at t31
    s 1bb "?"
    show alice at f33
    show sayori at t32
    a 2b "Sayonika and I are working on a project with a game studio."
    a "I'm just waiting for a review from one of the guys up there."
    a 1i "Unfortunately, I'm not able to disclose any details."
    show sayori at f32
    show alice at t33
    s 4bx "Ooh, a game?"
    show sayonika at f31
    show sayori at t32
    sy 1bh "It's been something we've been working on for a while."
    sy "It's kind of a sequel to an already-popular game."
    sy "The game studio we've been working with has been teasing it all week."
    sy 3bl "It's also been a nice way for me and Alice to bond."
    show sayonika 1ba at t31
    mc "What do you mean by that?"
    show sayonika at f31
    sy 2bb "I've learned a lot about Alice thanks to the project."
    sy "We've pretty much learned each others' quirks in what we do, but it's the first time I've really gotten to know her as a person."
    sy 1bs "She's got such an interesting story."
    sy "If you heard it, you'd probably think that I was reading a novel to you."
    sy 4ba "It's been a wonderful experience working hand-in-hand with an angel."
    show sayonika at t31
    "Chills go up my spine as soon as she said that."
    mc "I, uh, see..."
    "I fidget with the side of my shirt as Alice looks at me quizically..."
    show alice at f33
    a 1d "Wait a minute..."
    a 2g "You were that kid that was with the tall girl with a white ribbon at that game convention, weren't you?"
    mc "Wait, wha-{nw}"
    "Oh, of course."
    "She's talking about the one time where I took Monika to a gaming convention to talk with some programmers, shortly before she disappeared."
    "Did Alice see me there?"
    mc "..."
    mc "You saw me there?"
    a 1b "Of course! I'm remembering it now."
    a "You were taking her around and introducing her to some of the devs there."
    a "She would always keep nudging you, and it look like she flirted a few times."
    a "I think you even caught a glimpse of me with Sayonika before that girl tapped you."
    a 2n "I remember feeling so bad for you. She was like a little kid in a candy shop, I'm not gonna lie."
    mc "I guess I did, then..."
    show sayonika at f31
    show alice 1o at t33
    sy 1be "Oh yeah!"
    sy "And she would keep showing off a bit, too!"
    sy "No wonder you looked so familiar, [player]!"
    sy "Man, you must have the patience of a god or something..."
    show sayori at f32
    show sayonika at t31
    s 1bc "Are they talking about Monika?"
    show sayori at t32
    mc "Yeah, the one time I took her to that gaming convention."
    show sayori at f32
    s 4bx "Well, look at that. Such a small world..."
    show alice at f33
    show sayori 1bx at t32
    a 1e "That it is!"
    a 1g "I'm glad we figured out that mystery."
    a "It would've bugged me for weeks as to where I saw you from."
    a "Sayonika would probably never hear the end of it, too."
    a 1a "Isn't that right?"
    show alice at t33
    show sayonika at f31
    sy 1bq "Oh, I would..."
    sy 2bp "Once she's anxious about something, she's {i}anxious{/i}..."
    sy 1bi "Sometimes it's really bad..."
    sy 1bb "It usually works itself out, though."
    show sayonika at t31
    "Suddenly, Alice's phone rings."
    show alice at f33
    a 1d "Oh, my phone's ringing. Just a moment."
    stop music fadeout 1.0
    show alice 1c at t33
    "Alice picks up and responds."
    "Sayonika looks around the room, trying to ignore what Alice is saying."
    a 1i "Yeah, that really happened."
    a "Awfully inconvenient that I had to make sure Bertrum didn't decapitate me while I was grabbing a battery."
    show sayonika 1bo at t31
    "What in the world?"
    a 1l "What do you mean that's dangerous?"
    a "Of course that's dangerous! How do you think I felt when I went through that?"
    show sayori 1bn at t32
    "Sayori fidgets with her thumbs."
    a 1v "Phil, we're just trying to tell the story as it is. No frills."
    "I look down at the floor, pondering what Alice is talking about."
    a 1q "I'll.. I'll see what I can do about adding a checkpoint or something."
    a "You know how important this is to me, as well as Sayonika."
    "Sayori carefully plops on Sayonika's bed, staring at the ceiling."
    a "Understood. Bye."
    "Alice hangs up the phone and places it in her pocket."
    show alice at f33
    a 1i "Sorry about that. Just some storytelling problems."
    a "Looks like I'll need to add a checkpoint."
    a "He says it'd be too dangerous and would irritate gamers."
    show sayonika at f31
    show alice at t33
    sy 1bs "Don't worry. I'll take care of it for ya."
    sy "You're probably too shaken up, anyway."
    show sayonika at t31
    "Alice sighs."
    show alice at f33
    a 1v "Yeah..."
    a "Thanks anyway."
    show alice at thide
    hide alice
    show sayonika at t21
    show sayori 1be at t22
    "Alice promptly leaves, head slightly down."
    mc "Does this always happen?"
    show sayonika at f21
    play music t9
    sy 1br "Not really. This is a first."
    sy "Usually reviews are more successful and quick."
    sy 1bo "I guess Phil saw some potential flaw or whatever."
    sy "It's kind of a hard battle between keeping true to your own story and making it playable."
    sy 1br "Such a balance isn't easy, you know?"
    mc "I can imagine so."
    sy "I don't think I've seen her this distraught before."
    sy "She's usually rather placid nowadays."
    show sayori at f22
    show sayonika at t21
    s "Is she going to be okay?"
    show sayonika at f21
    show sayori at t22
    sy "I think so. It may take a while, though."
    show sayonika at t21
    "Sayori looks down on her phone and checks the time."
    show sayori at f22
    s 1bb "Wow, it's almost 4."
    s "I think [player] and I should get going..."
    show sayonika at f21
    show sayori at t22
    sy 1bs "Alright. Thanks for stopping by."
    show sayonika at t21
    mc "See you around."

    show sayonika at thide
    hide sayonika
    show sayori at thide
    hide sayori
    "Sayori and I make our way out of the loft."

    scene bg residential_day
    with wipeleft
    "We really didn't talk much on the walk back."
    "I guess we got a little shaken up after that call."
    "It takes us a while before Sayori opens her mouth."
    show sayori 1be at t11
    s "[player], do you think Alice will be alright?"
    mc "She'll be fine, Sayori."
    mc "I think she's learned to be resilient enough to handle it."
    mc "Not to mention Sayonika's there to help watch over things."
    s 3bg "I guess you're right."
    s "That call sounded pretty rough."
    s "I feel bad for her."
    mc "We all do."
    mc "But I'm sure she'll make it out alive."
    mc "I feel like she always does."
    s "Yeah..."
    s "I can't imagine being put under that kind of strain all the time."
    s 1bh "Do you think that's why Monika left us?"
    mc "S-Sayori..."
    "Sayori whimpers a little."
    s 4bv "Sometimes I feel like I've done something to cause her to go away."
    s "And it feels like that I'll never know what it was if I did do it."
    s "I get really worried sometimes."
    s "Maybe Monika offed herself..."
    s "I try really hard to not think about those things and look toward the future, but..."
    "I pull Sayori close."

    scene s_cg3 with dissolve_cg
    "I could feel the tears run down her cheek and onto my shirt as I hold her close."
    mc "Sayori..."
    mc "You can't keep putting yourself down like this."
    mc "None of us will ever know what happened to her or why, but the best we can do is pick up and move on."
    mc "And we'll help each other out when it gets rough."
    s "I know, I know..."
    s "I just..."
    mc "Don't worry. We're here for each other."
    s "It's scary, [player]..."
    s "The rainclouds... they just come and go as they please..."
    s "I can't stop thinking about her at times."
    s "I just hope she's okay wherever she is..."
    mc "I know it's rough, Sayori."
    mc "But we'll make it through together."
    "Sayori lowers her head a little bit."
    mc "Hey..."
    mc "I love you."
    "She perks her head up a bit."
    s "Love you, too..."

    scene bg residential_day
    show sayori 1bt at t11
    with dissolve_cg
    stop music fadeout 1.0
    "We release each other slowly."
    mc "Well, I guess we'd better get to making that dinner."
    mc "It's not going to cook itself."
    s 1by "Yeah, I guess so..."
    play music t8
    s "I still have the ground beef in the fridge."
    mc "Well, you'd better grab it before it disappears."
    s 1bj "Eeehhhhh, that's mean, [player]!"
    "Again, it doesn't take long before she smiles again."
    s 1br "Hehe... let's grab the meat."
    "I follow Sayori into her house and to the kitchen."
    "I wonder about her sometimes..."

    stop music fadeout 1.0
    scene black with fade
    pause 1.5
    return