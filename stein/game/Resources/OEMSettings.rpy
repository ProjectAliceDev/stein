##################################################
## AliceOS OEM Configurations
# This file can be used to set OEM settings such
# as colors, fonts, and custom branding. In code,
# replace the default strings with the OEM
# counterparts.
##################################################

## Define whether you want the OEM mode on or off.
## Turning the OEM mode on will use OEM fonts and
## settings instead of AliceOS's defaults.

define aliceos.oem_mode = True

## Write the OEM information here. This will be 
## displayed on the AliceOS Pisa under the provider
## details.
## 
## Also, if you have a license to your game, write
## it here.
init -10 python:
    oem_info = """\
OEM Name: Project Alice
OEM Website: {a="https://about.aliceos.app"}https://about.aliceos.app{/a}
OEM Support Email: {a="mailto:hello@aliceos.app"}hello@aliceos.app{/a}
    """

    license = """\
[config.name] is a Doki Doki Literature Club fan mod that is not affiliated with Team Salvato or Joey Drew Studios and is not an official Bendy and the Ink Machine product. It is designed to be played only after the official game(s) has/have been completed, and contains spoilers for the official game(s). Game files for Doki Doki Literature Club are required to play this mod and can be downloaded for free at: http://ddlc.moe.
    """

##################################################
## Brand configurations
##################################################

## Define whether to use custom fonts in all of
## AliceOS. Fonts will need to be placed in the
## Resources/systemfont/OEM folder and match the
## font structure of AliceOS's fonts.

define aliceos.oem_use_custom_font = True

## Define the AliceOS OEM Colors here. This covers
## branding colors scaling from the 100 (lightest)
## to 900 (darkest). If you can make use of AliceOS's
## default color palette (Elementary), you can simply
## ignore this.

init -10 python:
    aliceos_oem_colors = {
        100: "",
        300: "",
        500: "",
        700: "",
        900: ""
    }


##################################################
## Pisa Configurations
##################################################

## Define whether you want to use large text for
## the Setup screen. The font sizes will adjust
## accordingly.

define aliceos.oem_large_pisa_font = False

##################################################
## ThrowASError Messages
##################################################

## Define your specific ASError messages (displayed)
## when ThrowASError is called (Stop error).
 
init -10 python:
    aliceos_oem_errors = {
        "": ""
    } 
