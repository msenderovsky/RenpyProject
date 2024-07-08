init python:
    class ReplayScene(object):
        def __init__(self, title, cover, label, parent = [], category = [], unlocked = False, filename="", arguments = {}, hint = ''):
            self.parent = parent
            self.category = category
            self.title = title
            self.cover = cover
            self.label = label
            self.arguments = arguments
            self.filename=filename
            self.hint = hint
            self.unlocked = unlocked
            gallery_scenes.append(self)
        
        
    class GalleryItem:
        def __init__(self, title, source, images, thumb, locked="replay_lock"):
            self.title = title
            self.source = source
            self.images = images
            self.thumb = thumb
            self.locked = locked
            self.refresh_lock()    
             
        def num_images(self):
            return len(self.images)

        def refresh_lock(self):
            self.num_unlocked = 0
            lockme = False
            #for img in self.source:
            if not renpy.seen_image(self.source):
                lockme = True
            else:
                self.num_unlocked += 1
            self.is_locked = lockme


define gallery_scenes = []
define gallery_pics = []
init python:
    gallery_pics.append(GalleryItem("{color=#fff}Image 1{/color}", "image1", ["image1","image1_2"], "thumb1"))
    gallery_pics.append(GalleryItem("{color=#fff}Image 2{/color}", "image3", ["image2"], "thumb2"))
    gallery_pics.append(GalleryItem("{color=#fff}Image 3{/color}", "image7", ["image3","image3_2"], "thumb3"))
    gallery_pics.append(GalleryItem("{color=#fff}Image 4{/color}", "image4", ["image4"], "thumb4"))
    gallery_pics.append(GalleryItem("{color=#fff}Image 5{/color}", "image5", ["image5"], "thumb5"))
    gallery_pics.append(GalleryItem("{color=#fff}Image 6{/color}", "image6", ["image6"], "thumb6"))
    gallery_pics.append(GalleryItem("{color=#fff}Image 7{/color}", "image7", ["image6"], "thumb7"))
    gallery_pics.append(GalleryItem("{color=#fff}Image 8{/color}", "image8", ["image8"], "thumb8"))
    gallery_pics.append(GalleryItem("{color=#fff}Image 9{/color}", "image6", ["image9"], "thumb9"))
    gallery_pics.append(GalleryItem("{color=#fff}Image 10{/color}", "image6", ["image10"], "thumb10"))

define replay13 = ReplayScene(parent= ['Yoga'], category= ['Instructor'], title = _('Yoga class'), cover = 'gallery/cover_1.jpg', label = 'yoga', hint = _('Yoga excercises'), arguments = {})
#define replay3 = ReplayScene(title = _('Scene3'), cover = 'gallery/gallery04.jpg', label = 'movie6', hint = _(''), arguments = {})
#define replay4 = ReplayScene(title = _('Scene4'), cover = 'gallery/gallery05.jpg', label = 'movie7', hint = _(''), arguments = {})