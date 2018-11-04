import time

from CONSTANTS import IS_RASPBERRY_PI, CAMERA_PORT, RESOLUTION_H, RESOLUTION_W
from camera.camera_utils import preview_image
import cv2

class Camera:

    def __init__(self, height=RESOLUTION_H, width=RESOLUTION_W):
        self.current_frame = None
        self.height = height
        self.width = width
        self.camera = None

    def start_capture(self, height=None, width=None, usingPiCamera=IS_RASPBERRY_PI, ):
        import imutils
        from imutils.video import VideoStream
        resolution = (self.height, self.width)
        if height:
            if width:
                resolution = (height, width)
        print("Camera Resolution:", resolution)
        cf = VideoStream(usePiCamera=usingPiCamera,
                         resolution=resolution,
                         framerate=60).start()
        self.current_frame = cf
        time.sleep(2)

        if not usingPiCamera:
            frame = imutils.resize(self.current_frame.read(), width=resolution[0])
        # Stream started, call current_frame.read() to get current frame

    def stop_capture(self):
        print("Stopping Capture")
        self.current_frame.stop()

    def capture_image(self):

        # Number of frames to throw away while the camera adjusts to light levels
        ramp_frames = 1

        self.camera = cv2.VideoCapture(CAMERA_PORT)
        _, im = self.camera.read()
        [self.camera.read() for _ in range(ramp_frames)]
        # print("Taking image...")
        _, camera_capture = self.camera.read()
        del self.camera
        return camera_capture


if __name__ == '__main__':
    # Capture and Display Image
    camera = Camera()
    image = camera.capture_image()
    preview_image(image)

    # Stream Video
    camera = Camera()
    camera.start_capture()
    import cv2

    while True:
        cv2.imshow("Camera Stream", camera.current_frame.read())
        cv2.waitKey(10)
