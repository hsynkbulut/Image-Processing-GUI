from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import filedialog
import cv2
import sys

import numpy as np


class HistogramDetection:
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

        def histogramCalcHistDetect():
            try:
                a = HistogramDetectAl(self.filename)
                a.histogramCalcHistImg()

                myImage2.place_forget()
                if self.video == 1:
                    imgFirst = Image.open("img/noImage.png")
                else:
                    imgFirst = Image.open("img/dist/histogram_calc_hist.png")
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

        def histogramEqualizeHistDetect():
            try:
                a = HistogramDetectAl(self.filename)
                a.histogramEqualizeHistImg()

                myImage2.place_forget()
                if self.video == 1:
                    imgFirst = Image.open("img/noImage.png")
                else:
                    imgFirst = Image.open("img/dist/histogram_equalize_hist.png")
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
        self.root.title("Histogram")
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

        calcHistButton = Button(
            self.root,
            bd=0,
            highlightthickness=0,
            command=histogramCalcHistDetect,
            activeforeground="#272727",  # aktifken yazı rengi
            foreground="white",  # pasifken yazı rengi
            activebackground="white",  # aktifken arkaplan rengi
            background="#272727",  # pasifken arkaplan rengi
            text="Calc Histogram",
            font=("Verdana", 10, "bold"),
            width=20,
            height=3,
        )
        calcHistButton.place(x=70, y=575)

        equalizeHistButton = Button(
            self.root,
            bd=0,
            highlightthickness=0,
            command=histogramEqualizeHistDetect,
            activeforeground="#272727",  # aktifken yazı rengi
            foreground="white",  # pasifken yazı rengi
            activebackground="white",  # aktifken arkaplan rengi
            background="#272727",  # pasifken arkaplan rengi
            text="Equalize Histogram",
            font=("Verdana", 10, "bold"),
            width=20,
            height=3,
        )
        equalizeHistButton.place(x=290, y=575)

        # </---Butonların Oluşturulması--->

        # <---Labelların Oluşturulması--->

        title = Label(
            self.root,
            text="HİSTOGRAM ",
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

        # </---Labellerın Oluşturulması--->

        self.root.mainloop()

    # <---Fonksiyonların Tanımlanması--->

    def Quit(self):
        self.root.destroy()

    # </---Fonksiyonların Tanımlanması--->


class HistogramDetectAl:
    def __init__(self, filename):
        self.filename = filename

    def histogramCalcHistImg(self):
        try:
            image = cv2.imread(self.filename, cv2.IMREAD_GRAYSCALE)
            hist = cv2.calcHist([image], [0], None, [256], [0, 256])
            cv2.imwrite(
                "img/dist/histogram_calc_hist.png",
                hist,
                [cv2.IMWRITE_JPEG_QUALITY, 100],
            )
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except Exception as e:
            print(f"Hata: {e}")

    def histogramEqualizeHistImg(self):
        try:
            image = cv2.imread(self.filename, cv2.IMREAD_GRAYSCALE)
            equalized_image = cv2.equalizeHist(image)
            cv2.imwrite(
                "img/dist/histogram_equalize_hist.png",
                equalized_image,
                [cv2.IMWRITE_JPEG_QUALITY, 100],
            )
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except Exception as e:
            print(f"Hata: {e}")
