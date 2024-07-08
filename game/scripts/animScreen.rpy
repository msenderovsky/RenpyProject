init python:
    def show_anim(name, at_list=[ ], layer=None, what=None, zorder=None, tag=None, behind=[ ], atl=None, transient=False, munge_name=True):
        renpy.store.anim_speed_menu = False
        for n in tuple(name):
            if ("_slow" in n) or ("_normal" in n) or ("_fast" in n) or ("_superfast" in n):
                renpy.store.anim_speed_menu = True

        potential_mode = None
        for element in name:
            if any(part in element for part in ("_slow", "_normal", "_fast", "_superfast")):
                potential_mode = element.split("_")[3]
                break
        mode = None
        if potential_mode and potential_mode in ("slow", "normal", "fast", "superfast"):
            mode = potential_mode
        renpy.store.mode_variations=["slow", "normal", "fast", "superfast"]
        if mode:
            renpy.store.anim_mode = mode


        renpy.store.anim_angle_menu = False
        for n in tuple(name):
            if ("_a" in n) or ("_b" in n) or ("_c" in n) or ("_d" in n):
                renpy.store.anim_angle_menu = True

        potential_angle = None
        for element in name:
            if any(part in element for part in ("_a", "_b", "_c", "_d")):
                potential_angle = element.split("_")[2]
                break
        angle = None
        if potential_angle and potential_angle in ("a", "b", "c", "d"):
            angle = potential_angle
        renpy.store.angle_variations=["a", "b", "c", "d"]
        if angle:
            renpy.store.anim_angle = angle

        renpy.store.anim_pos_menu = False
        for n in tuple(name):
            if ("_1" in n) or ("_2" in n) or ("_3" in n) or ("_4" in n) or ("_5" in n) or ("_6" in n) or ("_7" in n) or ("_8" in n) or ("_9" in n) or ("_10" in n) or ("_11" in n) or ("_12" in n) or ("_13" in n) or ("_14" in n):
                renpy.store.anim_pos_menu = True

        potential_pos = None
        for element in name:
            if any(part in element for part in ("_1", "_2", "_3", "_4","_5", "_6", "_7", "_8","_9", "_10", "_11", "_12","_13", "_14", "_15", "_16","_17", "_18", "_19", "_20")):
                potential_pos = element.split("_")[1]
                break
        pos = None
        if potential_pos and potential_pos in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"):
            pos = potential_pos
        renpy.store.pos_variations=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
        if pos:
            renpy.store.anim_pos = pos
        renpy.show(name=name, at_list=at_list, layer=layer, what=what, zorder=zorder, tag=tag, behind=behind, atl=atl, transient=transient, munge_name=munge_name)

    config.show = show_anim
    config.overlay_screens.append("anim_speed")
    config.overlay_screens.append("anim_angle")
    config.overlay_screens.append("anim_pos")

    anim_speed_menu = False
    anim_pos_menu = False
    anim_angle_menu = False


screen anim_speed():
    if anim_speed_menu:
        $ img = renpy.get_showing_tags(layer='master')
        if img:
            $ full_tag = img.pop()
            $ parts = full_tag.split("_", 4)
            #text "Parts: {}".format(parts)
            if len(parts) == 4:
                $ tag= parts[0]
                $ pos= parts[1]
                $ angle= parts[2]
                $ mode = parts[3]
                #text "tag: {} pos: {} angle: {} mode: {}".format(tag,pos,angle,mode)
            else:
                $ tag = "default"
                $ pos = "default"
                $ angle = "default"
                $ mode = "default"
                #text "tag: {} pos: {} angle: {} mode: {}".format(tag,pos,angle,mode)
            #$ tag, mode = img.pop().rsplit("_", 1)

            $ speed_amounts = len([speed for speed in ("slow", "slower", "normal", "fast", "faster", "superfast") if renpy.has_image(f"{tag}_{pos}_{angle}_{speed}")])
            vbox:
                yalign 0.5
                xalign 0.99
                spacing 10
                if (speed_amounts>1):
                    for speed in ("slow", "slower", "normal", "fast", "faster", "superfast"):
                        if renpy.has_image(f"{tag}_{pos}_{angle}_{speed}"):
                            imagebutton auto f"gui/navigation/speedarrow_{speed}_%s.png" action If(mode == speed, NullAction(), [SetScreenVariable("mode", speed),renpy.scene,Function(renpy.show, name="{}_{}_{}_{}".format(tag, pos, angle, speed)),With(dissolve)])selected (mode == speed)
                
screen anim_pos():
    if anim_pos_menu:
        $ img = renpy.get_showing_tags(layer='master')
        if img:
            $ full_tag = img.pop()  
            $ parts = full_tag.split("_", 4)  
            if len(parts) == 4:  #
                $ tag= parts[0]
                $ pos= parts[1]
                $ angle= parts[2]
                $ mode = parts[3]
                #text "tag: {} pos: {} angle: {} mode: {}".format(tag,pos,angle,mode)
            else:
                $ tag = "default"
                $ pos = "default"
                $ angle = "default"
                $ mode = "default"
                #text "tag: {} pos: {} angle: {} mode: {}".format(tag,pos,angle,mode)
            
            hbox:
                yalign 0
                xalign 0.5
                spacing 10
                
                for next_pos in renpy.store.pos_variations:
                    
                    if renpy.has_image(f"{tag}_{next_pos}_a_slow"):
                        imagebutton auto f"gui/navigation/{next_pos}_slow_%s.png" action [
                            SetScreenVariable("pos", next_pos),  
                            renpy.scene,
                            Function(renpy.show, name="{}_{}_a_slow".format(tag, next_pos)),
                            With(dissolve),
                            ]


screen anim_angle():
    if anim_angle_menu:
        $ img = renpy.get_showing_tags(layer='master')
        if img:
            $ full_tag = img.pop()  
            $ parts = full_tag.split("_", 4)  
            if len(parts) == 4:  
                $ tag= parts[0]
                $ pos= parts[1]
                $ angle= parts[2]
                $ mode = parts[3]
                #text "tag: {} pos: {} angle: {} mode: {}".format(tag,pos,angle,mode)
            else:
                $ tag = "default"
                $ pos = "default"
                $ angle = "default"
                $ mode = "default"
                #text "tag: {} pos: {} angle: {} mode: {}".format(tag,pos,angle,mode)
            #$ tag, mode = img.pop().rsplit("_", 1)
            
            $ angle_amounts = len([angle for angle in ("a", "b", "c", "d") if renpy.has_image(f"{tag}_{pos}_{angle}_{mode}")])
            vbox:
                yalign 0.5
                xalign 0
                spacing 10
                if (angle_amounts>1):
                    for next_angle in ("a", "b", "c", "d"):
                        #if renpy.has_image(f"{tag}_{pos}_{angle}_{speed}"):
                #for next_angle in renpy.store.angle_variations:
                        if renpy.has_image(f"{tag}_{pos}_{next_angle}_slow"):
                            imagebutton auto f"gui/navigation/{next_angle}_slow_%s.png" action [
                                SetScreenVariable("angle", next_angle),  
                                renpy.scene,
                                Function(renpy.show,  name="{}_{}_{}_slow".format(tag, pos, next_angle)),
                                With(dissolve)
                            ]