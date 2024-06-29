import cv2
import time
import pygame.mixer
from PIL import ImageGrab

def Judge_Matching(num):
    if 0.90 < num:
        return True
    else:
        return False


template = cv2.imread('./persona.png') #検索元画像ファイルパスを指定
pygame.mixer.init(frequency = 44100)
pygame.mixer.music.load('LastSurprise.mp3')

while(True):
    ImageGrab.grab().save('./persona2.png')
    image = cv2.imread('./persona2.png') #検索先画像のファイルパスを指定
    #OpenCVで画像部分一致を検索
    result = cv2.matchTemplate(image, template, cv2.TM_CCORR_NORMED)

    # 最も類似度が高い位置と低い位置を取得
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)

    #類似度が閾値を超えているか判定（上で作った関数を使用）
    Judg = Judge_Matching(maxVal)
    print(maxVal)
    #結果を出力
    if Judg:
        print("true")
        pygame.mixer.music.play(20)
    else:
        print("false")
        pygame.mixer.music.stop()
    # （実行結果→）True or False
    time.sleep(1)
