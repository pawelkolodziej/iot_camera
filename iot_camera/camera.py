import time
import picamera
import datetime
import os
from base_camera import BaseCamera



class Camera(BaseCamera):

    def __init__(self):
        self.fileName = None

    def getFileName(self):
        return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")

    def removeoldpics(self):
        os.remove(self.fileName)

    def makePreview(self, lengthInSec):
        self.fileName = self.getFileName()
        cam = picamera.PiCamera()
        # cam.start_preview()
        cam.capture(self.fileName)
        # cam.stop_preview()

    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:
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
