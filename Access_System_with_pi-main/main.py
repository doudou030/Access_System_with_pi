import requests
import time
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import RPi.GPIO as GPIO
from deepface import DeepFace

#telegrambot def
def send_to_telegram(message):

    apiToken = ''#bot token放這
    chatID = ''#使用者的chat id
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)
#GPIO def
buzzer_pin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzer_pin,GPIO.OUT)
def buzz(pitch, duration) : 
	period = 1.0 / pitch 
	half_period = period / 2 
	cycles = int(duration * pitch) 
	for i in range(cycles) : 
		GPIO.output(buzzer_pin , GPIO.HIGH) 
		time.sleep(half_period) 
		GPIO.output(buzzer_pin , GPIO.LOW) 
		time.sleep(half_period) 

#face_recognition
recognizer = cv2.face.LBPHFaceRecognizer_create()         # 啟用訓練人臉模型方法
recognizer.read("face.yml")            # 讀取註冊過的人臉模型檔
cascade_path = "haarcascade_frontalface_default.xml"  # 載入人臉追蹤模型
face_cascade = cv2.CascadeClassifier(cascade_path)        # 啟用人臉追蹤

cap = cv2.VideoCapture(0)                                 # 開啟攝影機
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img,(540,300))              # 縮小尺寸，加快辨識效率
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # 轉換成黑白
    faces = face_cascade.detectMultiScale(gray)  # 追蹤人臉 ( 目的在於標記出外框 )

    # 建立姓名和 id 的對照表
    name = {
        '1':'Doudou'
    }

    # 依序判斷每張臉屬於哪個 id
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)            # 標記人臉外框
        idnum,confidence = recognizer.predict(gray[y:y+h,x:x+w])  # 取出 id 號碼以及信心指數 confidence
        try:
            analyze = DeepFace.analyze(img, actions=['emotion'])
            emotion = analyze['dominant_emotion']  # 取得情緒文字
            
        except:
            emotion = ''
        if confidence < 80:
            text = name[str(idnum)]           # 如果信心指數小於某個數值，取得對應的名字
            send_to_telegram(f"{text}進來了房間")
            send_to_telegram(f"他看起來很{emotion}")
            
        else:
            text = '???'                      # 不然名字就是 ???
            buzz(1000,5)                      # 響警報
            send_to_telegram("warning!!有不認識的人")
            send_to_telegram(f"他看起來很{emotion}")
            
        time.sleep(0.5)
        # 在人臉外框旁加上名字
        cv2.putText(img, text, (x,y-5),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)
        cv2.putText(img, emotion, (0,20),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)
        
    cv2.imshow('LSA-final project', img)
    if cv2.waitKey(5) == ord('q'):
        break    # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
