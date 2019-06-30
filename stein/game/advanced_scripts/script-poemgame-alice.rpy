init python:
    import random

    class ForgottenPoemWord:
        def __init__(self, word, sPoint, nPoint, yPoint, aPoint, glitch=False):
            self.word = word
            self.sPoint = sPoint
            self.nPoint = nPoint
            self.yPoint = yPoint,
            self.aPoint = aPoint,
            self.glitch = glitch

    POEM_DISLIKE_THRESHOLD = 29
    POEM_LIKE_THRESHOLD = 45

    full_wordlist = []
    with renpy.file('poemwords.txt') as wordfile:
        for line in wordfile:

            line = line.strip()

            if line == '' or line[0] == '#': continue

            x = line.split(',')
            full_wordlist.append(ForgottenPoemWord(x[0],
                                                   float(x[1]),
                                                   float(x[2]),
                                                   float(x[3]),
                                                   float(x[4])))

    seen_eyes_this_chapter = False
    sayoriTime = renpy.random.random() * 4 + 4
    natsukiTime = renpy.random.random() * 4 + 4
    yuriTime = renpy.random.random() * 4 + 4
    aliceTime = renpy.random.random() * 4 + 4
    sayoriPos = 0
    natsukiPos = 0
    yuriPos = 0
    alicePos = 0
    sayoriOffset = 0
    natsukiOffset = 0
    yuriOffset = 0
    aliceOffset = 0
    sayoriZoom = 1
    natsukiZoom = 1
    yuriZoom = 1
    aliceZoom = 1

    def randomPauseSayori(trans, st, at):
        if st > sayoriTime:
            global sayoriTime
            sayoriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseNatsuki(trans, st, at):
        if st > natsukiTime:
            global natsukiTime
            natsukiTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseYuri(trans, st, at):
        if st > yuriTime:
            global yuriTime
            yuriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseAlice(trans, st, at):
        if st > aliceTime:
            global aliceTime
            aliceTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomMoveSayori(trans, st, at):
        global sayoriPos
        global sayoriOffset
        global sayoriZoom
        if st > .16:
            if sayoriPos > 0:
                sayoriPos = renpy.random.randint(-1,0)
            elif sayoriPos < 0:
                sayoriPos = renpy.random.randint(0,1)
            else:
                sayoriPos = renpy.random.randint(-1,1)
            if trans.xoffset * sayoriPos > 5: sayoriPos *= -1
            return None
        if sayoriPos > 0:
            trans.xzoom = -1
        elif sayoriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * sayoriPos
        sayoriOffset = trans.xoffset
        sayoriZoom = trans.xzoom
        return 0

    def randomMoveNatsuki(trans, st, at):
        global natsukiPos
        global natsukiOffset
        global natsukiZoom
        if st > .16:
            if natsukiPos > 0:
                natsukiPos = renpy.random.randint(-1,0)
            elif natsukiPos < 0:
                natsukiPos = renpy.random.randint(0,1)
            else:
                natsukiPos = renpy.random.randint(-1,1)
            if trans.xoffset * natsukiPos > 5: natsukiPos *= -1
            return None
        if natsukiPos > 0:
            trans.xzoom = -1
        elif natsukiPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * natsukiPos
        natsukiOffset = trans.xoffset
        natsukiZoom = trans.xzoom
        return 0

    def randomMoveYuri(trans, st, at):
        global yuriPos
        global yuriOffset
        global yuriZoom
        if st > .16:
            if yuriPos > 0:
                yuriPos = renpy.random.randint(-1,0)
            elif yuriPos < 0:
                yuriPos = renpy.random.randint(0,1)
            else:
                yuriPos = renpy.random.randint(-1,1)
            if trans.xoffset * yuriPos > 5: yuriPos *= -1
            return None
        if yuriPos > 0:
            trans.xzoom = -1
        elif yuriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * yuriPos
        yuriOffset = trans.xoffset
        yuriZoom = trans.xzoom
        return 0

    def randomMoveAlice(trans, st, at):
        global alicePos
        global aliceOffset
        global aliceZoom
        if st > .16:
            if alicePos > 0:
                alicePos = renpy.random.randint(-1,0)
            elif alicePos < 0:
                alicePos = renpy.random.randint(0,1)
            else:
                alicePos = renpy.random.randint(-1,1)
            if trans.xoffset * alicePos > 5: alicePos *= -1
            return None
        if alicePos > 0:
            trans.xzoom = -1
        elif alicePos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * alicePos
        aliceOffset = trans.xoffset
        aliceZoom = trans.xzoom
        return 0


label fm_poemgame(transition=True):
    stop music fadeout 2.0
    scene bg notebook
    show screen quick_menu
    if persistent.playthrough == 0:
        show s_sticker at sticker_t1
    show n_sticker at sticker_t2
    if persistent.playthrough == 2 and chapter == 2:
        show y_sticker_cut at sticker_t3
    else:
        show y_sticker at sticker_t3
    show m_sticker at sticker_t4
    
    if transition:
        with dissolve_scene_full

    if persistent.playthrough == 3:
        play music ghostmenu
    else:
        play music t4

    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False

    if persistent.playthrough == 0 and chapter == 0:
        call screen alert("Let's write a poem.", "Pick words you think your favorite club member, current or honorary, will like. Something good might happen with whoever likes your poem the most!", ok_action=Return())
    python:
        poemgame_glitch = False
        played_baa = False
        progress = 1
        numWords = 20
        sPointTotal = 0
        nPointTotal = 0
        yPointTotal = 0
        aPointTotal = 0
        wordlist = list(full_wordlist)

        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        aliceTime = renpy.random.random() * 4 + 4
        sayoriPos = renpy.random.randint(-1,1)
        natsukiPos = renpy.random.randint(-1,1)
        yuriPos = renpy.random.randint(-1,1)
        alicePos = renpy.random.randint(-1,1)
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        aliceOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        aliceZoom = 1


        while True:
            ystart = 160
            if persistent.playthrough == 2 and chapter == 2:
                pstring = ""
                for i in range(progress):
                    pstring += "1"
            else:
                pstring = str(progress)
            ui.text(pstring + "/" + str(numWords), style="poemgame_text", xpos=810, ypos=80, color='#000')
            for j in range(2):
                if j == 0: x = 440
                else: x = 680
                ui.vbox()
                for i in range(5):
                    word = random.choice(wordlist)
                    wordlist.remove(word)
                    ui.textbutton(word.word, clicked=ui.returns(word), text_style="poemgame_text", xpos=x, ypos=i * 56 + ystart)
                ui.close()

            t = ui.interact()
            if not poemgame_glitch:
                if t.glitch:
                    poemgame_glitch = True
                    renpy.music.play(audio.t4g)
                    renpy.scene()
                    renpy.show("white")
                    renpy.show("y_sticker glitch", at_list=[sticker_glitch])
                elif persistent.playthrough != 3:
                    renpy.play(gui.activate_sound)
                    if t.sPoint >= 3.0:
                        renpy.show("s_sticker hop")
                    if t.nPoint >= 3.0:
                        renpy.show("n_sticker hop")
                    if t.yPoint[0] >= 3.0:
                        renpy.show("y_sticker hop")
                    if t.aPoint[0] >= 3.0:
                        renpy.show("m_sticker hop")
            else:
                r = random.randint(0, 10)
                if r == 0 and not played_baa:
                    renpy.play("gui/sfx/baa.ogg")
                    played_baa = True
                elif r <= 5: renpy.play(gui.activate_sound_glitch)
            sPointTotal += t.sPoint
            nPointTotal += t.nPoint
            yPointTotal += t.yPoint[0]
            aPointTotal += t.aPoint[0]
            progress += 1
            if progress > numWords:
                break

        if persistent.playthrough == 0:
            if chapter == 1:
                exec(ch1_choice[0] + "PointTotal += 5")
            unsorted_pointlist = {"sayori": sPointTotal, "natsuki": nPointTotal, "yuri": yPointTotal, "alice": aPointTotal}
            pointlist = sorted(unsorted_pointlist, key=unsorted_pointlist.get)

            poemwinner[chapter] = pointlist[3]
        else:
            if nPointTotal > yPointTotal: poemwinner[chapter] = "natsuki"
            else: poemwinner[chapter] = "yuri"

        exec(poemwinner[chapter][0] + "_appeal += 1")

        if sPointTotal < POEM_DISLIKE_THRESHOLD: s_poemappeal[chapter] = -1
        elif sPointTotal > POEM_LIKE_THRESHOLD: s_poemappeal[chapter] = 1
        if nPointTotal < POEM_DISLIKE_THRESHOLD: n_poemappeal[chapter] = -1
        elif nPointTotal > POEM_LIKE_THRESHOLD: n_poemappeal[chapter] = 1
        if yPointTotal < POEM_DISLIKE_THRESHOLD: y_poemappeal[chapter] = -1
        elif yPointTotal > POEM_LIKE_THRESHOLD: y_poemappeal[chapter] = 1
        if aPointTotal < POEM_DISLIKE_THRESHOLD: a_poemappeal[chapter] = -1
        elif aPointTotal > POEM_LIKE_THRESHOLD: a_poemappeal[chapter] = 1

        exec(poemwinner[chapter][0] + "_poemappeal[chapter] = 1")

    $ config.allow_skipping = True
    $ allow_skipping = True
    stop music fadeout 2.0
    hide screen quick_menu
    show black as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    pause 1.0
    return


image bg eyes_move:
    "images/bg/eyes.png"
    parallel:
        yoffset 720 ytile 2
        linear 0.5 yoffset 0
        repeat
    parallel:
        0.1
        choice:
            xoffset 20
            0.05
            xoffset 0
        choice:
            xoffset 0
        repeat
image bg eyes:
    "images/bg/eyes.png"

image s_sticker:
    "gui/poemgame/s_sticker_1.png"
    xoffset sayoriOffset xzoom sayoriZoom
    block:
        function randomPauseSayori
        parallel:
            sticker_move_n
        parallel:
            function randomMoveSayori
        repeat

image n_sticker:
    "gui/poemgame/n_sticker_1.png"
    xoffset natsukiOffset xzoom natsukiZoom
    block:
        function randomPauseNatsuki
        parallel:
            sticker_move_n
        parallel:
            function randomMoveNatsuki
        repeat

image y_sticker:
    "gui/poemgame/y_sticker_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image y_sticker_cut:
    "gui/poemgame/y_sticker_cut_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image m_sticker:
    "mod_assets/images/chibis/alice.png"
    # "gui/poemgame/m_sticker_1.png"
    xoffset aliceOffset xzoom aliceZoom
    block:
        function randomPauseAlice
        parallel:
            sticker_move_n
        parallel:
            function randomMoveAlice
        repeat

image s_sticker hop:
    "gui/poemgame/s_sticker_2.png"
    xoffset sayoriOffset xzoom sayoriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "s_sticker"

image n_sticker hop:
    "gui/poemgame/n_sticker_2.png"
    xoffset natsukiOffset xzoom natsukiZoom
    sticker_hop
    xoffset 0 xzoom 1
    "n_sticker"

image y_sticker hop:
    "gui/poemgame/y_sticker_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image y_sticker_cut hop:
    "gui/poemgame/y_sticker_cut_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker_cut"

#Creepy hopping pic for yuri
image y_sticker hopg:
    "gui/poemgame/y_sticker_2g.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image m_sticker hop:
    "mod_assets/images/chibis/alice_hop.png"
    # "gui/poemgame/m_sticker_2.png"
    xoffset aliceOffset xzoom aliceZoom
    sticker_hop
    xoffset 0 xzoom 1
    "m_sticker"

image y_sticker glitch:
    "gui/poemgame/y_sticker_1_broken.png"
    xoffset yuriOffset xzoom yuriZoom zoom 3.0
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

transform sticker_t1:
    xcenter 75 yalign 0.9 subpixel True

transform sticker_t2:
    xcenter 175 yalign 0.9 subpixel True

transform sticker_t3:
    xcenter 275 yalign 0.9 subpixel True

transform sticker_t4:
    xcenter 350 yalign 0.9 subpixel True

transform sticker_glitch:
    xcenter 50 yalign 1.8 subpixel True

transform sticker_m_glitch:
    xcenter 100 yalign 1.35 subpixel True

transform sticker_move_n:
    easein_quad .08 yoffset -15
    easeout_quad .08 yoffset 0

transform sticker_hop:
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
