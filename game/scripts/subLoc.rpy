screen SubLocHUD():
    frame:
        xalign 0.0
        ypos 150
        vbox:
            for q in subLocations:
                if q.parent == LocationID:
                    button:
                        text q.name
                        action Return(q.name)
            button:
                text "\n\nRreturn to previous location"
                action Return(Location)