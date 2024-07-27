import cv2
import threading
def display_image():
    imglink = 'test3.jpeg'
    cv2.namedWindow('image', cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_EXPANDED)
    img = cv2.imread(imglink)
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    display_image()
