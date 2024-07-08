screen PopUp(PopUpMessage):
    frame:
        xalign 0.5
        yalign 0.5
        xsize 500
        vbox:
            text PopUpMessage
            text ""
            button:
                text "Close"
                action Return()