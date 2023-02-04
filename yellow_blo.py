# import cv2 as cv

# import numpy as np

# def find_coord(event,x,y,flags,params):

#     if event==cv.EVENT_FLAG_LBUTTON:
#         print(x,',',y)
#         font=cv.FONT_HERSHEY_PLAIN
#         cv.putText(img,str(x) +','+ str(y),(x,y), font,1(255,0,0))
#         cv.imshow("image",img)

# if __name__=="__main__":
#     img = cv.imread("yellow_detect (1).jpeg")

#     cv.imshow("image",img)

#     cv.setMouseCallback("image", find_coord)

#     cv.waitKey(0)

#     cv.destroyAllWindows()  


import cv2 as cv
import numpy as np
import pyautogui as pg

yell = pg.yell()

yell = cv.cvtColor(np.array(yell), cv.COLOR_RGB2BGR)

block = pg.locateAllOnScreen('')

cv.imshow('yell', yell)

cv.waitKey(0)

cv.destroyAllWindows()