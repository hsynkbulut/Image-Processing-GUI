from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import filedialog
import cv2
import sys


class Thresholding:
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

        def adaptiveThresholdingDetect():
            try:
                block_size = int(self.blockEntry.get())
                C = int(self.cEntry.get())

                a = ThresholdingDetectAl(self.filename)
                a.adaptiveThresholdingImg(block_size, C)

                myImage2.place_forget()
                if self.video == 1:
                    imgFirst = Image.open("img/noImage.png")
                else:
                    imgFirst = Image.open("img/dist/adaptive_threshold.png")
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

        def otsuThresholdingDetect():
            try:
                a = ThresholdingDetectAl(self.filename)
                a.otsuThresholdingImg()

                myImage2.place_forget()
                if self.video == 1:
                    imgFirst = Image.open("img/noImage.png")
                else:
                    imgFirst = Image.open("img/dist/otsu_threshold.png")
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
        self.root.title("Thresholding")
        self.root.configure(background="#3336be")

        # </---Form Ayarları--->

        # <---Resimlerin Eklenmesi--->

        mainmenu = ImageTk.PhotoImage(Image.open(os.getcwd() + "\\img\\home.png"))
        find = ImageTk.PhotoImage(Image.open(os.getcwd() + "\\img\\search.png"))
        noImage = ImageTk.PhotoImage(Image.open(os.getcwd() + "\\img\\noImage.png"))

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

        adaptiveThresholdButton = Button(
            self.root,
            bd=0,
            highlightthickness=0,
            command=adaptiveThresholdingDetect,
            activeforeground="#272727",  # aktifken yazı rengi
            foreground="white",  # pasifken yazı rengi
            activebackground="white",  # aktifken arkaplan rengi
            background="#272727",  # pasifken arkaplan rengi
            text="Adaptive Thresholding",
            font=("Verdana", 10, "bold"),
            width=20,
            height=3,
        )
        adaptiveThresholdButton.place(x=70, y=605)

        otsuThresholdButton = Button(
            self.root,
            bd=0,
            highlightthickness=0,
            command=otsuThresholdingDetect,
            activeforeground="#272727",  # aktifken yazı rengi
            foreground="white",  # pasifken yazı rengi
            activebackground="white",  # aktifken arkaplan rengi
            background="#272727",  # pasifken arkaplan rengi
            text="Otsu Thresholding",
            font=("Verdana", 10, "bold"),
            width=20,
            height=3,
        )
        otsuThresholdButton.place(x=290, y=605)

        # </---Butonların Oluşturulması--->

        # <---Labelların Oluşturulması--->

        title = Label(
            self.root,
            text="THRESHOLDING ",
            font="Arial 15 bold ",
            bg="#3336be",
            fg="white",
        )
        title.place(x=463, y=30)

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

        blockLabel = Label(self.root, text="Blok Boyutu:", bg="#3336be", fg="white")
        blockLabel.place(x=70, y=570)
        self.blockEntry = Entry(self.root, width=5)
        self.blockEntry.place(x=144, y=570)

        cLabel = Label(self.root, text="C:", bg="#3336be", fg="white")
        cLabel.place(x=188, y=570)
        self.cEntry = Entry(self.root, width=5)
        self.cEntry.place(x=206, y=570)

        # </---Labellerın Oluşturulması--->

        self.root.mainloop()

    # <---Fonksiyonların Tanımlanması--->

    def Quit(self):
        self.root.destroy()

    # </---Fonksiyonların Tanımlanması--->


class ThresholdingDetectAl:
    def __init__(self, filename):
        self.filename = filename

    def adaptiveThresholdingImg(self, block_size, C):
        try:
            image = cv2.imread(self.filename, cv2.IMREAD_GRAYSCALE)
            # block_size = 11
            # C = 2
            adaptive_threshold = cv2.adaptiveThreshold(
                image,
                255,
                cv2.ADAPTIVE_THRESH_MEAN_C,
                cv2.THRESH_BINARY,
                block_size,
                C,
            )
            cv2.imwrite(
                "img/dist/adaptive_threshold.png",
                adaptive_threshold,
                [cv2.IMWRITE_JPEG_QUALITY, 100],
            )
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except Exception as e:
            print(f"Hata: {e}")

    def otsuThresholdingImg(self):
        try:
            image = cv2.imread(self.filename, cv2.IMREAD_GRAYSCALE)
            _, otsu_threshold = cv2.threshold(
                image, 0, 255, cv2.THRESH_BINARY + +cv2.THRESH_OTSU
            )
            cv2.imwrite(
                "img/dist/otsu_threshold.png",
                otsu_threshold,
                [cv2.IMWRITE_JPEG_QUALITY, 100],
            )
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except Exception as e:
            print(f"Hata: {e}")
