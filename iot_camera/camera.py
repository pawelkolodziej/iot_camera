import time
import picamera
import datetime
import os
import io
from base_camera import BaseCamera



class Camera(BaseCamera):


    def getFileName(self):
        return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")

    def removeoldpics(self):
        os.remove(self.fileName)

    def makePreview(self, lengthInSec):
        self.fileName = self.getFileName()
        with picamera.PiCamera() as camera:
            camera.annotate_text = 'picture'
            camera.resolution = (640, 480)
            camera.framerate = 24
            camera = picamera.PiCamera()
            # cam.start_preview()
            camera.capture(self.fileName)
            # cam.stop_preview()

    
    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:
            camera.annotate_text = 'streaming'
            camera.resolution = (640, 480)
            camera.framerate = 24
            # let camera warm up
            time.sleep(2)
            
            
            stream = io.BytesIO()
            for foo in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # return current frame
                stream.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()
