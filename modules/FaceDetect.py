from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import filedialog
import cv2
import sys


class FaceDetection:
    def __init__(self, master):
        def MainmenuFonk():
            master.update()
            master.deiconify()
            self.Quit()

        def openFileVideo():
            try:
                filename = filedialog.askopenfilename(
                    initialdir="/videos/",
                    title="Please Select a Video File",
                    filetypes=(
                        ("MP4 File", "*.mp4"),
                        ("AVI File", "*.avi"),
                        ("All Files", "*.*"),
                    ),
                )
                self.filename = filename
                self.faceDetectionVideo()
            except Exception as e:
                print("Error:", e)

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
            except Exception as e:
                print("Hata:", e)

        def imgDetect():
            try:
                a = FaceDetectAl(self.filename)
                success = a.faceDetectionImg()

                myImage2.place_forget()
                if (
                    self.video == 1 or not success
                ):  # Eğer video varsa veya işlem başarısızsa
                    imgFirst = Image.open("img/noImage.png")
                else:
                    imgFirst = Image.open("img/dist/test.jpg")
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
            except Exception as e:
                print("Hata:", e)

        # <---Form Ayarları--->

        self.root = Toplevel()
        self.root.wm_iconbitmap("img/image-processing.ico")
        self.root.geometry("1266x692+0+0")
        self.root.maxsize(1366, 768)
        self.root.title("Yüz Algılama")
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
            command=openFileVideo,
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
            command=self.faceWeb,
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
            text="YÜZ ALGILAMA",
            font="Arial 15 bold ",
            bg="#3336be",
            fg="white",
        )
        title.place(x=500, y=30)

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

        # </---Labellerın Oluşturulması--->

        self.root.mainloop()

    # <---Fonksiyonların Tanımlanması--->

    def faceDetectionVideo(self):
        try:
            face_cascade = cv2.CascadeClassifier(
                "data/haarcascade_frontalface_default.xml"
            )
            cap = cv2.VideoCapture(self.filename)
            while True:
                ret, img = cap.read()
                if not ret:
                    break

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.1, 4)
                for x, y, w, h in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 3)

                cv2.imshow("Face Detection from Video", img)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

            cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            print("Error:", e)

    def faceWeb(self):
        a = FaceDetectAl(" ")
        a.faceDetectionWebcam()

    def Quit(self):
        self.root.destroy()

    # </---Fonksiyonların Tanımlanması--->


class FaceDetectAl:
    def __init__(self, filename):
        self.filename = filename

    def faceDetectionImg(self):
        try:
            faceCascade = cv2.CascadeClassifier(
                "data/haarcascade_frontalface_default.xml"
            )
            conf_1 = cv2.imread(self.filename)
            conf_2 = conf_1.copy()
            faces_1 = faceCascade.detectMultiScale(conf_1)
            for x, y, w, h in faces_1:
                cv2.rectangle(conf_1, (x, y), (x + w, y + h), (0, 255, 255), 10)
            faces_2 = faceCascade.detectMultiScale(
                conf_2, scaleFactor=1.3, minNeighbors=6
            )
            for x, y, w, h in faces_2:
                cv2.rectangle(conf_2, (x, y), (x + w, y + h), (0, 255, 255), 10)

            cv2.imwrite("img/dist/test.jpg", conf_2, [cv2.IMWRITE_JPEG_QUALITY, 100])
            return True  # İşlem başarılıysa True döner
            # cv2.waitKey()
        except Exception as e:
            print("Hata:", e)
            return False  # İşlem başarısızsa False döner

    def faceDetectionVideo(self):
        try:
            faceCascade = cv2.CascadeClassifier(
                "data/haarcascade_frontalface_default.xml"
            )
            cap = cv2.VideoCapture(self.filename)
            while True:
                _, conf_1 = cap.read()
                conf_2 = conf_1.copy()
                faces_1 = faceCascade.detectMultiScale(conf_1)
                for x, y, w, h in faces_1:
                    cv2.rectangle(conf_1, (x, y), (x + w, y + h), (0, 255, 255), 3)
                faces_2 = faceCascade.detectMultiScale(
                    conf_2, scaleFactor=1.3, minNeighbors=6
                )
                for x, y, w, h in faces_2:
                    cv2.rectangle(conf_2, (x, y), (x + w, y + h), (0, 255, 255), 3)
                cv2.imshow("Videodan Yuz Algilama", conf_2)
                k = cv2.waitKey(30) & 0xFF
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        except:
            pass

    def faceDetectionWebcam(self):
        try:
            faceCascade = cv2.CascadeClassifier(
                "data/haarcascade_frontalface_default.xml"
            )
            cap = cv2.VideoCapture(0)
            while True:
                _, conf_1 = cap.read()
                conf_2 = conf_1.copy()
                faces_1 = faceCascade.detectMultiScale(conf_1)
                for x, y, w, h in faces_1:
                    cv2.rectangle(conf_1, (x, y), (x + w, y + h), (0, 255, 255), 3)
                faces_2 = faceCascade.detectMultiScale(
                    conf_2, scaleFactor=1.3, minNeighbors=6
                )
                for x, y, w, h in faces_2:
                    cv2.rectangle(conf_2, (x, y), (x + w, y + h), (0, 255, 255), 3)
                cv2.imshow("Web Kamerasindan Yuz Algilama", conf_2)
                k = cv2.waitKey(30) & 0xFF
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        except:
            pass
