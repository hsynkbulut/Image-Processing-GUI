from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import filedialog
import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt


class CannyEdgeDetection:
    def __init__(self, master):
        def MainmenuFonk():
            master.update()
            master.deiconify()
            self.Quit()

        def openFileImg():
            try:
                filename = filedialog.askopenfilename(
                    initialdir="/img/",
                    title="Lütfen Bir Resim veya Video Dosyası Seçin",
                    filetypes=(
                        ("JPG File", "*.jpg"),
                        ("PNG File", "*.png"),
                        ("MP4 File", "*.mp4"),
                        ("AVI File", "*.avi"),
                    ),
                )
                myImage.place_forget()
                imgFirst = Image.open(filename)
                imgLast = imgFirst.resize((450, 400))
                myImg = ImageTk.PhotoImage(imgLast)
                myImageLast = Label(
                    self.root,
                    image=myImg,
                    bg="#2C073E",
                    fg="#ffffff",
                    width=450,
                    height=400,
                )
                myImageLast.image = myImg
                myImageLast.place(x=50, y=145)
                Path.config(text=filename)
                self.video = 0
                self.filename = filename
            except:
                noImage = ImageTk.PhotoImage(
                    Image.open(os.getcwd() + "\\img\\noImage.png")
                )
                myImageLast = Label(
                    self.root,
                    image=noImage,
                    bg="#2C073E",
                    fg="#ffffff",
                    width=450,
                    height=400,
                )
                myImageLast.image = noImage
                myImageLast.place(x=50, y=145)
                Path.config(text=filename)
                myImage2.place_forget()
                myImage2Last = Label(
                    self.root,
                    image=noImage,
                    bg="#2C073E",
                    fg="#ffffff",
                    width=450,
                    height=400,
                )
                myImage2Last.image = noImage
                myImage2Last.place(x=650, y=145)
                self.video = 1
                self.filename = filename

        def imgDetect():
            try:
                low_threshold = int(self.lowThreshold.get())
                high_threshold = int(self.highThreshold.get())
                a = EdgeDetectAI(self.filename)
                a.edgeDetectionImg(low_threshold, high_threshold)

                myImage2.place_forget()
                if self.video == 1:
                    imgFirst = Image.open("img/noImage.png")
                else:
                    imgFirst = Image.open("img/dist/testEdge.jpg")
                imgLast = imgFirst.resize((450, 400))
                myImg = ImageTk.PhotoImage(imgLast)
                myImageLast = Label(
                    self.root,
                    image=myImg,
                    bg="#2C073E",
                    fg="#ffffff",
                    width=450,
                    height=400,
                )
                myImageLast.image = myImg
                myImageLast.place(x=650, y=145)
            except:
                pass

        # <---Form Ayarları--->

        self.root = Toplevel()
        self.root.wm_iconbitmap("img/image-processing.ico")
        self.root.geometry("1266x692+0+0")
        self.root.maxsize(1366, 768)
        self.root.title("Kenar Algılama")
        self.root.configure(background="#3336be")

        # </---Form Ayarları--->

        # <---Resimlerin Eklenmesi--->

        mainmenu = ImageTk.PhotoImage(Image.open(os.getcwd() + "\\img\\home.png"))
        find = ImageTk.PhotoImage(Image.open(os.getcwd() + "\\img\\search.png"))
        noImage = ImageTk.PhotoImage(Image.open(os.getcwd() + "\\img\\noImage.png"))
        fotoImage = ImageTk.PhotoImage(
            Image.open(os.getcwd() + "\\img\\camera_icon.png")
        )
        videoImage = ImageTk.PhotoImage(
            Image.open(os.getcwd() + "\\img\\video_icon.png")
        )
        camImage = ImageTk.PhotoImage(
            Image.open(os.getcwd() + "\\img\\webcam_icon.png")
        )

        # </---Resimlerin Eklenmesi--->

        # <---Butonların Oluşturulması--->

        menu = Button(
            self.root,
            image=mainmenu,
            bd=0,
            highlightthickness=0,
            command=MainmenuFonk,
            width=150,
            height=50,
            activeforeground="white",  # aktifken yazı rengi
            foreground="white",  # pasifken yazı rengi
            activebackground="#272727",  # aktifken arkaplan rengi
            background="#3336be",  # pasifken arkaplan rengi
            text=" Anasayfa",
            font=("Arial 14 bold"),
            compound="left",
        )
        menu.image = mainmenu
        menu.place(x=10, y=20)

        findButton = Button(
            self.root,
            image=find,
            bd=0,
            highlightthickness=0,
            command=openFileImg,
            width=24,
            height=24,
            activebackground="white",  # aktifken arkaplan rengi
            background="#3336be",  # pasifken arkaplan rengi
        )
        findButton.image = find
        findButton.place(x=980, y=100)

        imageButton = Button(
            self.root,
            image=fotoImage,
            bd=0,
            highlightthickness=0,
            command=imgDetect,
            activeforeground="#7e7e7e",  # aktifken yazı rengi
            foreground="#7e7e7e",  # pasifken yazı rengi
            activebackground="white",  # aktifken arkaplan rengi
            background="#272727",  # pasifken arkaplan rengi
            text="Kamera",
            font=("Arial 13 bold"),
            compound="top",
            width=100,
            height=90,
        )
        imageButton.image = fotoImage
        imageButton.place(x=80, y=575)

        videoButton = Button(
            self.root,
            image=videoImage,
            bd=0,
            highlightthickness=0,
            command=self.edgeVideo,
            activeforeground="#7e7e7e",  # aktifken yazı rengi
            foreground="#7e7e7e",  # pasifken yazı rengi
            activebackground="white",  # aktifken arkaplan rengi
            background="#272727",  # pasifken arkaplan rengi
            text="Video",
            font=("Arial 13 bold"),
            compound="top",
            width=100,
            height=90,
        )
        videoButton.image = videoImage
        videoButton.place(x=220, y=575)

        streamButton = Button(
            self.root,
            image=camImage,
            bd=0,
            highlightthickness=0,
            command=self.edgeWeb,
            activeforeground="#7e7e7e",  # aktifken yazı rengi
            foreground="#7e7e7e",  # pasifken yazı rengi
            activebackground="white",  # aktifken arkaplan rengi
            background="#272727",  # pasifken arkaplan rengi
            text="Webcam",
            font=("Arial 13 bold"),
            compound="top",
            width=100,
            height=90,
        )
        streamButton.image = camImage
        streamButton.place(x=360, y=575)

        # </---Butonların Oluşturulması--->

        # <---Labelların Oluşturulması--->

        title = Label(
            self.root,
            text="KENAR ALGILAMA",
            font="Arial 15 bold ",
            bg="#3336be",
            fg="white",
        )
        title.place(x=490, y=30)

        fileLbl = Label(self.root, text="Dosya yolu :", bg="#3336be", fg="white")
        fileLbl.place(x=55, y=100)

        Path = Label(
            self.root, text="Lütfen Bir Dosya Seçiniz ...", bg="#3336be", fg="white"
        )
        Path.place(x=160, y=100)

        myImage = Label(
            self.root, image=noImage, bg="#2C073E", fg="#ffffff", width=450, height=400
        )
        myImage.place(x=50, y=145)

        myImage2 = Label(
            self.root, image=noImage, bg="#2C073E", fg="#ffffff", width=450, height=400
        )
        myImage2.place(x=650, y=145)

        description = Label(
            self.root,
            text="Kamerayı kapatmak için lütfen ESC tuşuna basın",
            bg="#3336be",
            fg="white",
        )
        description.place(x=720, y=570)

        lowThresholdLabel = Label(
            self.root, text="Düşük Eşik Değeri:", bg="#3336be", fg="white"
        )
        lowThresholdLabel.place(x=505, y=270)
        self.lowThreshold = Entry(self.root, width=5)
        self.lowThreshold.place(x=610, y=270)

        highThresholdLabel = Label(
            self.root, text="Yüksek Eşik Değeri:", bg="#3336be", fg="white"
        )
        highThresholdLabel.place(x=505, y=320)
        self.highThreshold = Entry(self.root, width=5)
        self.highThreshold.place(x=610, y=320)

        # </---Labellerın Oluşturulması--->

        self.root.mainloop()

    # <---Fonksiyonların Tanımlanması--->

    def edgeVideo(self):
        try:
            a = EdgeDetectAI(self.filename)
            a.edgeDetectionVideo()
        except:
            pass

    def edgeWeb(self):
        a = EdgeDetectAI(" ")
        a.edgeDetectionWebcam()

    def Quit(self):
        self.root.destroy()

    # </---Fonksiyonların Tanımlanması--->


class EdgeDetectAI:
    def __init__(self, filename):
        self.filename = filename

    def edgeDetectionImg(self, low_threshold, high_threshold):
        try:
            img = cv2.imread(self.filename, cv2.IMREAD_GRAYSCALE)
            # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # edges = cv2.Canny(gray, 20, 30)
            # edges_high_thresh = cv2.Canny(gray, 60, 120)
            # images = np.hstack((edges, edges_high_thresh))
            sonuc1 = cv2.Canny(img, low_threshold, high_threshold, L2gradient=True)
            cv2.imwrite(
                "img/dist/testEdge.jpg", sonuc1, [cv2.IMWRITE_JPEG_QUALITY, 100]
            )
            cv2.waitKey()
        except:
            pass

    def edgeDetectionVideo(self):
        try:
            cap = cv2.VideoCapture(self.filename)
            while cap.isOpened():
                ret, frame = cap.read()
                if ret == True:
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    edges = cv2.Canny(gray, 20, 30)
                    edges_high_thresh = cv2.Canny(gray, 60, 120)
                    images = np.hstack((edges, edges_high_thresh))
                    cv2.imshow("Videodan Kenar Algilama", images)
                    k = cv2.waitKey(30) & 0xFF
                    if k == 27:
                        break
                else:
                    break
            cap.release()
            cv2.destroyAllWindows()
        except:
            pass

    def edgeDetectionWebcam(self):
        try:
            cap = cv2.VideoCapture(0)
            while cap.isOpened():
                ret, frame = cap.read()
                if ret == True:
                    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    # edges = cv2.Canny(gray, 20, 30)
                    # edges_high_thresh = cv2.Canny(gray, 60, 120)
                    # images = np.hstack((edges, edges_high_thresh))
                    low_threshold = 50
                    high_threshold = 150
                    sonuc1 = cv2.Canny(
                        frame, low_threshold, high_threshold, L2gradient=True
                    )
                    cv2.imshow("Web Kamerasindan Kenar Algilama", sonuc1)
                    k = cv2.waitKey(30) & 0xFF
                    if k == 27:
                        break
                else:
                    break
            cap.release()
            cv2.destroyAllWindows()
        except:
            pass
