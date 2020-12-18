import cv2, pyautogui, keyboard, win32api, win32con, time
import numpy as np

tarkkuus = 1
ruudun_alku_x = 100
ruudun_alku_y = 160
musta_filtteri = 260 #mitä suurempi luku, sitä enemmän mustaa
valkoinen_filtteri = 200 #mitä pienempi luku, sitä enemmän valkoista
harmaa_filtteri = 200 #mitä pienempi luku, sitä enemmän tumman harmaata

x = 0
i = 1
img = cv2.imread("____.jpg") #image name here

korkeus , leveys, _ = img.shape

for y in range(korkeus):
    for x in range(leveys):
        #valkoinen
        if sum(img[y,x]) > int((255*3)/2)+valkoinen_filtteri:
            for i in range(3):
                img[y,x][i] = 255
        #vaalean harmaa
        elif harmaa_filtteri + valkoinen_filtteri < sum(img[y,x]) <((255*3)/2)+valkoinen_filtteri:
            for i in range(3):
                img[y,x][i] = 75
        #tumman harmaa
        elif musta_filtteri < sum(img[y,x]) < valkoinen_filtteri+harmaa_filtteri:
            for i in range(3):
                img[y,x][i] = 175
        #musta
        else:
            for i in range(3):
                img[y,x][i] = 0

#kernel = np.ones((2,2), np.uint8) 
#img = cv2.erode(img, kernel, iterations=1)

cv2.imshow("piirros", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

while True:
    if keyboard.is_pressed('q'):
        for y in range(0,korkeus-2, tarkkuus):
            if keyboard.is_pressed('l'):
                break
            x = 0
            while x < leveys-2:
                i = 0
                if sum(img[y,x]) == 0:
                    win32api.SetCursorPos((ruudun_alku_x+x, ruudun_alku_y+y))
                    while True:
                        try:
                            if sum(img[y,x+i]) == 0:
                                i += 1
                            else:
                                break
                        except:
                            i += 1
                            break
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,ruudun_alku_x+x,ruudun_alku_y+y,0,0)
                    win32api.SetCursorPos((ruudun_alku_x+x+i, ruudun_alku_y+y))
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,ruudun_alku_x+x+i,ruudun_alku_y+y,0,0)
                    time.sleep(0.000001)
                    x = x+i

                x += tarkkuus

    if keyboard.is_pressed('e'):
        for y in range(0,korkeus-2, tarkkuus):
            if keyboard.is_pressed('l'):
                break
            x = 0
            while x < leveys-2:
                i = 0
                if sum(img[y,x]) == 225:
                    win32api.SetCursorPos((ruudun_alku_x+x, ruudun_alku_y+y))
                    while True:
                        try:
                            if sum(img[y,x+i]) == 225:
                                i += 1
                            else:
                                break
                        except:
                            i += 1
                            break
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,ruudun_alku_x+x,ruudun_alku_y+y,0,0)
                    win32api.SetCursorPos((ruudun_alku_x+x+i, ruudun_alku_y+y))
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,ruudun_alku_x+x+i,ruudun_alku_y+y,0,0)
                    time.sleep(0.000001)
                    x = x+i

                x += tarkkuus

    if keyboard.is_pressed('w'):
        for y in range(0,korkeus-2, tarkkuus):
            if keyboard.is_pressed('l'):
                break
            x = 0
            while x < leveys-2:
                i = 0
                if sum(img[y,x]) == 525:
                    win32api.SetCursorPos((ruudun_alku_x+x, ruudun_alku_y+y))
                    while True:
                        try:
                            if sum(img[y,x+i]) == 525:
                                i += 1
                            else:
                                break
                        except:
                            i += 1
                            break
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,ruudun_alku_x+x,ruudun_alku_y+y,0,0)
                    win32api.SetCursorPos((ruudun_alku_x+x+i, ruudun_alku_y+y))
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,ruudun_alku_x+x+i,ruudun_alku_y+y,0,0)
                    time.sleep(0.000001)
                    x = x+i

                x += tarkkuus
             
            
