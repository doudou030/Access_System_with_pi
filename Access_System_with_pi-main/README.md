# Access Control System with pi

## Concept Development 動機發想

<!-- Why does your team want to build this idea/project?  -->
有些資料與物品具有非常高的價值，以防內鬼誕生之後沒有人能守護，因此做一個以rasberry-pi執行的門禁系統，以USB camera讀入影像辨識人臉，先以opencv進行訓練並註冊，如果是註冊過的就可以亮led燈表示通過，並透過telegram bot會傳送他的名子說他來了，若是沒有註冊過的則會使蜂鳴器叫並且透過telegram提醒說這是沒註冊的人，並且會顯示畫面裡的人的情緒。
## Implementation Resources 硬體設備

<!-- e.g., How many Raspberry Pi? How much you spent on these resources? -->
- 1塊Raspberry Pi Model 3B
- 1台webcam
- 1塊麵包版
- 1個蜂鳴器
- 杜邦線至少4條
- 1個LED
- 1個電阻(防LED燒壞)

   
## Existing Library/Software 軟體架構

<!-- Which libraries do you use while you implement the project -->
- python3.9.2
- GPIO module(樹梅派內建就有)
- python-telegram-bot(為了通知在遠端的使用者用telegram做interface)
- opencv(影像辨識)
- tensorflow2.9.1
- deepface(辨識人臉情緒、年齡、人種)

## Implementation Process

<!-- What kind of problems you encounter, and how did you resolve the issue? -->
- 因為樹梅派跑不太動深度學習的人臉辨識，因此使用了cv2取代做人臉辨識與偵測，其實可以先sever端訓練好之後再把model丟到樹梅派裡就好

- 直接`pip install tensorflow`會使樹梅派當機
因此用其他方式代替
>原本想要載tensorflow-lite，使用到的deepface好像只吃tensorflow，因此載tensorflow lite需要完全改寫，不然就是要載專門給樹梅派(arm架構)的tensorflow
## Knowledge from Lecture

<!-- What kind of knowledge did you use on this project? -->

- linux系統基本指令
## Installation 預先下載

<!-- How do the user install with your project? -->

- 更新/取得最新版本的軟體資訊及下載文字編輯器vim
```
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install vim
```


- 去telegram找`@BotFather`申請一個機器人記好api token

![](https://github.com/doudou030/Access_Control_System_with_pi/blob/main/img/creatbot.jpg?raw=true)



- 下載人臉追蹤模型(要記好位置)
```
$ wget https://github.com/kipr/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml
```
- 下載樹梅派專用tensorflow2.9.1
    - `https://drive.google.com/file/d/1xP6ErBK85SMFnQamUh4ro3jRmdCV_qDU/view`
    - 從上面的連結下載whl檔
    - 之後執行`$ sudo -H pip install tensorflow-2.9.1-cp39-cp39-linux_aarch64.whl`

- 下載python專屬套件(使用pip)
```
$ pip install opencv_python
$ pip install opencv_contrib_python
$ pip install deepface 
```
## Usage 使用方法
<!-- How to use your project -->

- GPIO接線

![](https://github.com/doudou030/Access_Control_System_with_pi/blob/main/img/pin.jpg?raw=true)

- 下載程式碼並增加使用權限
```
$ git clone https://github.com/doudou030/Access_Control_System_with_pi.git
$ cd Access_Control_System_with_pi
$ chmod +755 run
```
- 註冊自己的臉
    - 先多自拍幾張存好並命名成{number}.jpeg 例: 1.jpeg、2.jpeg
    - 並存在**自己知道位置**的資料夾
    - 並取名叫做face01`$ mkdir face01`
```
$ vim train.py
```
![](https://github.com/doudou030/Access_Control_System_with_pi/blob/main/img/train.jpg?raw=true)

- 改成自己bot的token與chat id
```
$ vim main.py
```
- chat id找法 
>去尋找`@GreenTracksBot`並`/start`他就會回傳你的chat id

![](https://github.com/doudou030/Access_Control_System_with_pi/blob/main/img/chatid_with_token.png?raw=true)
- 執行
```
$ ./run
```
- Demo成果

![](https://github.com/doudou030/Access_Control_System_with_pi/blob/main/img/Demo1.jpg?raw=true)

![](https://github.com/doudou030/Access_Control_System_with_pi/blob/main/img/Demo2.jpg?raw=true)

## Job Assignment 工作分配
- 歐丞言
    - 寫github
    - 建立telegram bot
    - python programming
- 郝健皓
    - python debugging
    - demo錄影
- 陳奕宏
    - demo錄影
- 陳俊維
    - telegram bot programming
    

## References

- [Python Telegram Bot  gtihub](https://github.com/python-telegram-bot/python-telegram-bot)
- [Python Telegram Bot Document](https://docs.python-telegram-bot.org/en/stable/index.html)
- [取得telegram chat ID ](https://greentracks.app/index.php/2022/04/08/telegram/)
- [GPIO教學 github](https://github.com/piepie-tw/gpio-game-console)
- [Opencv辨識人臉教學](https://steam.oxxostudio.tw/category/python/ai/ai-face-recognizer.html)
- [deepface情緒辨識](https://steam.oxxostudio.tw/category/python/ai/ai-emotion.html)
- [電路模擬圖tinkercad](https://www.tinkercad.com/dashboard)
- [rasberry pi tensorflow github](https://github.com/Qengineering/TensorFlow-Raspberry-Pi_64-bit)
