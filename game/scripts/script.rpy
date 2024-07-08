# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define m = Character("Megan", color="#dc38bf")
define n = Character("Nikki", color="#ff1111")
define c = Character("Chris", color="#4c0ddf")
define mc = Character("[persistent.player_name]", color="#4c0ddf")
define la = Character("landlady", color="#4c0ddf")
define ll = Character("landlady", color="#4c0ddf")
define tn = Character("tenant", color="#4c0ddf")
define ic = Character("Chris", who_color="#8888ff", what_color="#ffc266", what_italic=1)
define persistent.player_name = "Alex"

define slowfade = Fade(1.0, 0.5, 1.0)
define flash = Fade(0.1, 0.0, 0.2, color="#fff")

default Location= "map"
default LocationID = 0
default persistent.bonus_gallery_1 = False
default persistent.bonus_gallery_2 = False
default cheat_code_input = ""

define config.mouse = {}
define config.mouse['default'] = [ ( "gui/mouse.png", 0, 0) ]
define config.mouse['pressed_default'] = [ ( "gui/mouse2.png", 0, 0) ]

init python:
    def validate_cheat_code():
        if cheat_code_input == "codetest":
            persistent.bonus_gallery_2 = True
            renpy.hide_screen("cheat_menu")
            renpy.notify("Cheat code successful!")
        else:
            renpy.hide_screen("cheat_menu")
            renpy.notify("Cheat code failed!")


# The game starts here.
label start:
    stop music fadeout 3
    "What's your name?"
    
    $ persistent.player_name = renpy.input("My name is ", default='Alex', length=10).strip()
    mc "My name is [persistent.player_name]"

    call variables
    mc "Now you'll unlock the first pic of 2 of the first pic gallery item"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene gallery_1_1 with dissolve
    mc "Now the second pic of this sequence"
    scene gallery_1_2 with dissolve
    mc "Second pic of this gallery item unlocked"
    #scene bg room
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    scene null with dissolve
    mc "Now onto the second picture gallery item"
    scene gallery_2 with dissolve
    mc "Second picture unlocked"
    scene null with dissolve
    mc "Lastly the first render that unlocks another through persistent check"
    scene gallery_3_1 with dissolve
    mc "This one unlocks through a cheat menu"
    $ persistent.bonus_gallery_1=True
    call screen cheat_menu
    scene bookcase
    #call screen get_gallery_render(1)

    menu:
        "watch yoga instructions":
            jump yoga
        "map and inventory test":
            #jump nikdate
            jump mapTest

    #show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    e "call the popUp"
    scene null
    #call screen PopUp("pop up message")
    e "end of popUp"
    mc "{b}bold{/b}, {i}italic{/i} and whatnot like this"

label mapTest:
    mc "This is a test of the {size=+20}text size{/size}"
    mc "{b}bold{/b}, {i}italic{/i} and whatnot like this"
    #jump label2
    $ gameRunning = True
    while gameRunning:

        $ Location_img = Location.lower()
        if renpy.has_image(Location_img, exact=True):
            show expression Location_img

        menu:
            "Add apple":
                $ inventory[0].addItem()
                $ renpy.notify("Apple added")
            "Add sword":
                $ inventory[1].addItem()
                $ renpy.notify("Sword added")
            "Display number of apples":
                "You have [inventory[0].noOwned] apples"
            "Display number of swords":
                "You have [inventory[1].noOwned] swords"
            "Display weight":
                $ wt = inventory[0].currentWeight
                "The current weight is [wt]"
            "Open map":
                $ Location = renpy.call_screen("MapScreen", _layer="screens")
            "Visit sublocation":
                $ Location = renpy.call_screen("SubLocHUD", _layer="screens")
            "Button to advance time":
                $ blockToCall = ""
                "Time passed: 4 hours"
                $ calendar.addTime(4)
                "Date is: [calendar.output]"
                python:
                    for e in events:
                        if e.DateCheck(calendar):
                            blockToCall = e.Block
                if blockToCall <> "":
                    call expression blockToCall
                call eventCheck
    # This ends the game.

    return

label yoga:
    scene yoga_1_a_slow

label variables:
    $ calendar = Calendar(0, 0, 0, 0, ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    0, ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
    $ events[0]= Event(12, 2, 0, "evOne", True)
    $ events[0]= Event(16, 2, 0, "evTwo", True)
    $ inventory[0] = Item("apple", 1, 2, 0, 0)
    $ inventory[1] = Item("sword", 100, 20, 0, 1)
    return

label eventCheck:
    return

label evOne:
    "this is eventOne's block"
    $ events[0].setInactive()
    return

label evTwo:
    "this is eventTwo's block"
    $ events[0].setInactive()
    return

    
label movie1:
    scene movie01
    with dissolve
    pause
    return

label movie2:
    scene movie02
    with dissolve
    pause
    return

label movie3:
    scene movie03
    with dissolve
    pause
    return

label movie4:
    scene movie04
    with dissolve
    pause
    return