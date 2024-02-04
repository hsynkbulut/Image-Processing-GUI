from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import filedialog
import cv2
import sys
import numpy as np


class ImageSmoothing:
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
                kernel_size = int(self.kernelEntry.get())
                a = ImageSmoothingAl(self.filename)
                a.imageSmoothingImg(kernel_size)

                myImage2.place_forget()
                if self.video == 1:
                    imgFirst = Image.open("img/noImage.png")
                else:
                    imgFirst = Image.open("img/dist/blur.png")
                imgLast = imgFirst.resize((450, 400))
                Myimg = ImageTk.PhotoImage(imgLast)
                myImageLast = Label(
                    self.root,
                    image=Myimg,
                    bg="#2C073E",
                    fg="#ffffff",
                    width=450,
                    height=400,
                )
                myImageLast.image = Myimg
                myImageLast.place(x=650, y=145)
            except:
                pass

        def imgGaussianDetect():
            try:
                kernel_size = int(self.kernelEntry.get())
                a = ImageSmoothingAl(self.filename)
                a.imageSmoothingGaussianImg(kernel_size)

                myImage2.place_forget()
                if self.video == 1:
                    imgFirst = Image.open("img/noImage.png")
                else:
                    imgFirst = Image.open("img/dist/gaussian.png")
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

        def imgMedianDetect():
            try:
                kernel_size = int(self.kernelEntry.get())
                a = ImageSmoothingAl(self.filename)
                a.imageSmoothingMedianImg(kernel_size)

                myImage2.place_forget()
                if self.video == 1:
                    imgFirst = Image.open("img/noImage.png")
                else:
                    imgFirst = Image.open("img/dist/median.png")
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

        def imgBoxFilterDetect():
            try:
                kernel_size = int(self.kernelEntry.get())
                a = ImageSmoothingAl(self.filename)
                a.imageSmoothingBoxFilterImg(kernel_size)

                myImage2.place_forget()
                if self.video == 1:
                    imgFirst = Image.open("img/noImage.png")
                else:
                    imgFirst = Image.open("img/dist/median.png")
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

        def imgBilateralFilterDetect():
            try:
                a = ImageSmoothingAl(self.filename)
                a.imageSmoothingBilateralFilterImg()

                myImage2.place_forget()
                if self.video == 1:
                    imgFirst = Image.open("img/noImage.png")
                else:
                    imgFirst = Image.open("img/dist/median.png")
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
        self.root.title("Görüntü Bulanıklaştırma (Görüntü Yumuşatma)")
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

        bulButton = Button(
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
        bulButton.image = find
        bulButton.place(x=980, y=100)

        imageButton = Button(
            self.root,
            # image=smooth,
            bd=0,
            highlightthickness=0,
            command=imgDetect,
            activeforeground="#272727",  # aktifken yazı rengi
            foreground="white",  # pasifken yazı rengi
            activebackground="white",  # aktifken arkaplan rengi
            background="#272727",  # pasifken arkaplan rengi
            text="Blur",
            font=("Verdana", 10, "bold"),
            width=14,
            height=2,
        )
        # imageButton.image = smooth
        imageButton.place(x=50, y=575)

        gaussianButton = Button(
            self.root,
            # image=gaussian,
            bd=0,
            highlightthickness=0,
            command=imgGaussianDetect,
            activeforeground="#272727",  # aktifken yazı rengi
            foreground="white",  # pasifken yazı rengi
            activebackground="white",  # aktifken arkaplan rengi
            background="#272727",  # pasifken arkaplan rengi
            text="Gaussian Blur",
            font=("Verdana", 10, "bold"),
            width=14,
            height=2,
        )
        # gaussianButton.image = gaussian
        gaussianButton.place(x=200, y=575)

        medianButton = Button(
            self.root,
            # image=median,
            bd=0,
            highlightthickness=0,
            command=imgMedianDetect,
            activeforeground="#272727",  # aktifken yazı rengi
            foreground="white",  # pasifken yazı rengi
            activebackground="white",  # aktifken arkaplan rengi
            background="#272727",  # pasifken arkaplan rengi
            text="Median Blur",
            font=("Verdana", 10, "bold"),
            width=14,
            height=2,
        )
        # medianButton.image = median
        medianButton.place(x=350, y=575)

        boxFilterButton = Button(
            self.root,
            # image=boxFilter,
            bd=0,
            highlightthickness=0,
            command=imgBoxFilterDetect,
            activeforeground="#272727",  # aktifken yazı rengi
            foreground="white",  # pasifken yazı rengi
            activebackground="white",  # aktifken arkaplan rengi
            background="#272727",  # pasifken arkaplan rengi
            text="Box Filter",
            font=("Verdana", 10, "bold"),
            width=14,
            height=2,
        )
        # boxFilterButton.image = boxFilter
        boxFilterButton.place(x=50, y=630)

        bilateralFilterButton = Button(
            self.root,
            # image=bilateralFilter,
            bd=0,
            highlightthickness=0,
            command=imgBilateralFilterDetect,
            activeforeground="#272727",  # aktifken yazı rengi
            foreground="white",  # pasifken yazı rengi
            activebackground="white",  # aktifken arkaplan rengi
            background="#272727",  # pasifken arkaplan rengi
            text="Bilateral Filter",
            font=("Verdana", 10, "bold"),
            width=14,
            height=2,
        )
        # bilateralFilterButton.image = bilateralFilter
        bilateralFilterButton.place(x=200, y=630)

        # </---Butonların Oluşturulması--->

        # <---Labelların Oluşturulması--->

        title = Label(
            self.root,
            text="GÖRÜNTÜ BULANIKLAŞTIRMA (GÖRÜNTÜ YUMUŞATMA)",
            font="Arial 15 bold ",
            bg="#3336be",
            fg="white",
        )
        title.place(x=370, y=30)

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

        kernelLabel = Label(self.root, text="Kernel Boyutu:", bg="#3336be", fg="white")
        kernelLabel.place(x=510, y=270)
        self.kernelEntry = Entry(self.root, width=5)
        self.kernelEntry.place(x=600, y=270)

        # </---Labellerın Oluşturulması--->

        self.root.mainloop()

    # <---Fonksiyonların Tanımlanması--->

    def Quit(self):
        self.root.destroy()

    # </---Fonksiyonların Tanımlanması--->


class ImageSmoothingAl:
    def __init__(self, filename):
        self.filename = filename

    def imageSmoothingImg(self, kernel_size):
        try:
            img = cv2.imread(self.filename)
            blur = cv2.blur(img, (kernel_size, kernel_size))
            cv2.imwrite("img/dist/blur.png", blur, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except:
            pass

    def imageSmoothingGaussianImg(self, kernel_size):
        try:
            img = cv2.imread(self.filename)
            blur = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
            cv2.imwrite("img/dist/gaussian.png", blur, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except:
            pass

    def imageSmoothingMedianImg(self, kernel_size):
        try:
            img = cv2.imread(self.filename)
            blur = cv2.medianBlur(img, kernel_size)
            cv2.imwrite("img/dist/median.png", blur, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except:
            pass

    def imageSmoothingBoxFilterImg(self, kernel_size):
        try:
            img = cv2.imread(self.filename)
            blur = cv2.boxFilter(img, -1, (kernel_size, kernel_size))
            cv2.imwrite("img/dist/blur.png", blur, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except:
            pass

    def imageSmoothingBilateralFilterImg(self):
        try:
            img = cv2.imread(self.filename)
            blur = cv2.bilateralFilter(img, 9, 75, 75)
            cv2.imwrite("img/dist/gaussian.png", blur, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except:
            pass
