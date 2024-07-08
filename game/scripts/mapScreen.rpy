screen MapScreen():
    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1080
        background "map.jpg"
        for p in places:
            if p.isActive:
                button:
                    xpos p.x
                    ypos p.y
                    text p.name color "#fff8f8" outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ]
                    action SetVariable("LocationID", p.ID), Return (p.name)