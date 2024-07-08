init python:

    maxnumx = 3
    maxnumy = 3
    maxperpage = maxnumx * maxnumy
    gallery_page = 0

screen sceneGallery(movie = None):
    $start = gallery_page * maxperpage 
    $end = min(start + maxperpage - 1, len(gallery_scenes) -1)

    grid maxnumx maxnumy:
        xalign 0.5
        yalign 0.5
        spacing 150
 
        for i in range(start, end +1):
                    #for q in gallery_scenes:
            vbox:
                xalign 0.5
                yalign 0.5
                if renpy.seen_label(gallery_scenes[i].label):
                    imagebutton:
                        idle im.Scale(gallery_scenes[i].cover, 320, 180)
                        hover im.Scale(gallery_scenes[i].cover, 320, 180)
                        if renpy.seen_label(gallery_scenes[i].label):
                            action Replay(gallery_scenes[i].label, locked=False)
                        hovered Show("screenTextDisplay", displayText=gallery_scenes[i].hint)
                        unhovered Hide("screenTextDisplay")
                    text "[gallery_scenes[i].title]" size 20 xalign 0.5
                else:
                    $ sc= gallery_scenes[i].cover.split("_")[1]
                    imagebutton:
                        idle "gallery/replay_lock.jpg"
                        hover "gallery/hover_" + str(sc) + ".jpg"
                    #text "[]" 
        for i in range(end - start + 1, maxperpage):
            null

    if gallery_page > 0:
        textbutton "{color=#000}Previous{/color}":
            action SetVariable("gallery_page", gallery_page - 1)
            xalign 0
            yalign 0.5
            background "#fff8"
    if (gallery_page + 1) * maxperpage < len(gallery_scenes):
        textbutton "{color=#000}Next{/color}":
            action SetVariable("gallery_page", gallery_page + 1)
            xalign 0.99
            yalign 0.5
            background "#fff8"