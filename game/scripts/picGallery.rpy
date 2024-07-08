init python:

    maxnumx = 3
    maxnumy = 3
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy
    gallery_page = 0

    g= Gallery()
    
    g.button("locked")
    g.image("replay_lock")

    g.locked_button= "gallery/replay_lock.jpg"
    g.navigation= True

    g.button("gallery_1")
    g.unlock_image("gallery_1_1")
    g.unlock_image("gallery_1_2")

    g.button("gallery_2")
    g.unlock_image("gallery_2")

    g.button("gallery_3")
    g.unlock_image("gallery_3_1")
    g.image("gallery_3_2")
    g.condition("persistent.bonus_gallery_1")

    g.button("gallery_4")
    g.image("gallery_4")
    g.condition("persistent.bonus_gallery_2")

    g.button("gallery_5")
    g.unlock_image("gallery_5")
    
    g.button("gallery_6")
    g.unlock_image("gallery_6")

    g.button("gallery_7")
    g.unlock_image("gallery_7")

    g.button("gallery_8")
    g.unlock_image("gallery_8")
    
    g.button("gallery_9")
    g.unlock_image("gallery_9")
    
    g.button("gallery_10")
    g.unlock_image("gallery_10")
    

screen picGallery(movie = None):
    $start = gallery_page * maxperpage 
    $end = min(start + maxperpage - 1, len(gallery_pics) -1)

    grid maxnumx maxnumy:
        xfill True
        yfill True
 
        for i in range(start, end +1):
            $gallery_pics[i].refresh_lock()  
            vbox:
                xalign 0.5
                yalign 0.5
                add g.make_button("gallery_" +str(i+1), unlocked="gallery/hover_" + str(i+1) + ".jpg" , hover_border="gallery/thumb_" + str(i+1) + ".jpg", xalign=0.5, yalign=0.5)
                text "[gallery_pics[i].title]" xalign 0.5 size 35

        for i in range(end - start + 1, maxperpage):
            null

    if gallery_page > 0:
        textbutton "{color=#000}Previous{/color}":
            action SetVariable("gallery_page", gallery_page - 1)
            xalign 0
            yalign 0.5
            background "#fff8"
    if (gallery_page + 1) * maxperpage < len(gallery_pics):
        textbutton "{color=#000}Next{/color}":
            action SetVariable("gallery_page", gallery_page + 1)
            xalign 0.99
            yalign 0.5
            background "#fff8"