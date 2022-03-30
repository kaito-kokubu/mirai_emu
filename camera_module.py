import cv2
import time

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        break
    #cv2.imshow("Frame", frame)
    cv2.imwrite('test.jpg', frame)
    '''
    key = cv2.waitkey(1)
    if key == 27:
        break
    '''
    time.sleep(1)

camera.release()
cv2.destroyAllWindows()

'''
55dd2c7b-4911-4ac2-a11a-b8d9fbca0ec2
'''