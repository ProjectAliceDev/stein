image description = ParameterizedText(font="gui/font/Aller_Rg.ttf", size=24, xalign=0.5, yalign=0.35)

image contributor = ParameterizedText(font="gui/font/RifficFree-Bold.ttf", size=68, xalign=0.5, yalign=0.475)

define audio.credits_music = "mod_assets/HorrorEpic.mp3"

label ncredit(desc="description", cont="Contributor"):
    show description "[desc]" with dissolve
    pause 0.5
    show contributor "[cont]" with dissolve
    pause 3.5
    hide description with dissolve
    hide contributor with dissolve
    return

label ncredits:
    scene black with trueblack
    pause 0.5
    play music credits_music
    call ncredit(desc="A Doki Doki Literature Club! mod", cont="Forgotten")
    call ncredit(desc="Written by", cont="Marquis Kurt")
    call ncredit(desc="Overseen by", cont="Marquis Kurt, My Angle Alice (Aine)")
    call ncredit(desc="Characters drawn by", cont="Noelia, Cyrke, Cylent Night")
    call ncredit(desc="Backgrounds created by", cont="Cyrke, Gyrosona, Nuxill, yagamirai10")
    call ncredit(desc="Reviewed by", cont="Dusk Ealain")
    call ncredit(desc="Managed in GitHub with", cont="My Angle Alice (Aine)")
    call ncredit(desc="AliceOS developed by", cont="Marquis Kurt, My Angle Alice (Aine), GanstaKingOfSA, abduelhamit")
    call ncredit(desc="Sayonika created by", cont="My Angle Alice (Aine), Cyrke")
    call ncredit(desc="Credits music - \"Horror Epic\"", cont="audionautix.com")
    pause 3.0
    call ncredit(desc="Original games developed by", cont="Team Salvato, Joey Drew Studios")
    call ncredit(desc="With love, from", cont="Project Alice")
    return