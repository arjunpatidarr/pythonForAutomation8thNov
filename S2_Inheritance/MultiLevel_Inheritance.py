class  WhatsApp1:

    def  text(self):
        print("text message feature")

class WhatsApp2(WhatsApp1):

    def  audioCalling(self):
        print("audio calling feature")


class WhatsApp3(WhatsApp2):

    def  videoCalling(self):
        print("Video calling feature")



obj = WhatsApp3()
obj.videoCalling()
obj.text()
obj.audioCalling()
