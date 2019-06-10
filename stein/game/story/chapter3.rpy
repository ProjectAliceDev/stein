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
    $ messages.receive("Alice", "Hey, did you want to join me in heading out? Could use time to talk about investigation. .^_~")
    "Well, I guess there's nothing wrong with that."
    "I text her back: 'Sure, when?'"
    "Surprisingly, she responds back in an instant."
    $ messages.receive("Alice", "Two minutes? Idk, unsure of how long it takes for you to get already.")
    "Wait, what?"
    "She doesn't live that close by, and it takes a couple of minutes by car to get here..."
    "I try to get an answer: '???'"
    $ messages.receive("Alice", "Ngl, already here. .^_~")
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
    "I nod."
    return
