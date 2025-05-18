from cv2 import VideoCapture,imshow,destroyAllWindows,waitKey,resize
class video_playback(VideoCapture):
    def __init__(self,path="sitting_avatar.mp4",height=1000,width=1000):
        super().__init__(path)
        self.width = width
        self.height = height
    def play(self):


        while(self.isOpened()):
            ret, frame = self.read()
            if ret == True:
                resize_frame = resize(frame,(self.width,self.height))
                imshow(winname="My video",mat=resize_frame)
                
                if waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                stop()
                break
        def stop(self):
            self.release()
            destroyAllWindows()

