from picamera2 import Picamera2
import cv2

picam2 = Picamera2()
picam2.start()

while True:
    frame = picam2.capture_array()
    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

    cv2.imshow("Pi Camera Stream", frame_bgr)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
picam2.close()