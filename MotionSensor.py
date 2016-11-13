from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime

camera = PiCamera()
pir = MotionSensor(18)
while True:
    pir.wait_for_motion()
    filename = datetime.now().strftime("/home/pi/Desktop/Projects/SecurityCamera/SecurityVideos/capture.h264")#%Y-%m-%d_%H.%M.%S.h264")
    camera.start_recording(filename)
    pir.wait_for_no_motion()
    camera.stop_recording()
