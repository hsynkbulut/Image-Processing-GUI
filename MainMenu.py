from tkinter import *
from modules.ContourDetection import ContourDetection
from modules.CopyMakeBorder import CopyMakeBorder
from modules.FaceDetect import FaceDetection
from modules.GammaFilterDetect import GammaFilterDetection
from modules.HistogramDetect import HistogramDetection
from modules.KernelBasedDetect import KernelBasedDetection
from modules.CannyEdgeDetect import CannyEdgeDetection
from modules.EdgeDetectionAlgorithms import EdgeDetectionAlgorithms
from modules.BlurImage import ImageSmoothing
from modules.HarrisCornerFilterDetection import HarrisCornerFilterDetection
from modules.Thresholding import Thresholding
from modules.WatershedDetection import WatershedDetection


class MainMenu:
    def __init__(self):
        self.window = Tk()
        self.window.wm_iconbitmap("img/image-processing.ico")
        self.window.geometry("1366x700+1+1")
        self.window.maxsize(1366, 768)
        self.window.title("Görüntü İşleme Uygulaması")
        self.window.configure(background="#3336be")  # arkaplan rengi

        avatar = PhotoImage(file="img/background_image.png")

        title = Label(
            self.window,
            text="Görüntü İşleme Modülleri",
            font="Arial 15 bold ",
            bg="#3336be",
            fg="white",
        )
        title.place(x=900, y=30)

        thresholdingButton = Button(
            self.window,
            cursor="circle",
            borderwidth=3,
            relief="flat",
            text="Thresholding",
            command=self.GoThresholding,
            font=("Verdana", 12, "bold"),
            activeforeground="white",  # aktifken yazı rengi
            foreground="#272727",  # pasifken yazı rengi
            activebackground="#272727",  # aktifken arkaplan rengi
            background="white",  # pasifken arkaplan rengi
            width=25,
            height=2,
        )
        thresholdingButton.pack()
        thresholdingButton.place(x=740, y=80)  # (x=1050, y=80)

        imageBorderButton = Button(
            self.window,
            cursor="circle",
            borderwidth=3,
            relief="flat",
            text="Resim Dışına Kenarlık Ekleme",
            command=self.GoCopyMakeBorder,
            font=("Verdana", 12, "bold"),
            activeforeground="white",  # aktifken yazı rengi
            foreground="#272727",  # pasifken yazı rengi
            activebackground="#272727",  # aktifken arkaplan rengi
            background="white",  # pasifken arkaplan rengi
            width=25,
            height=2,
        )
        imageBorderButton.pack()
        imageBorderButton.place(x=1050, y=80)  # (x=1050, y=150)

        blurButton = Button(
            self.window,
            cursor="circle",
            borderwidth=3,
            relief="flat",
            text="Görüntü Bulanıklaştırma",
            command=self.GoBlurImage,
            font=("Verdana", 12, "bold"),
            activeforeground="white",  # aktifken yazı rengi
            foreground="#272727",  # pasifken yazı rengi
            activebackground="#272727",  # aktifken arkaplan rengi
            background="white",  # pasifken arkaplan rengi
            width=25,
            height=2,
        )
        blurButton.pack()
        blurButton.place(x=740, y=150)  # (x=740, y=220)

        kernelBasedButton = Button(
            self.window,
            cursor="circle",
            borderwidth=3,
            relief="flat",
            text="Kernel Tabanlı Filtreleme",
            command=self.GoKernelBasedDetection,
            font=("Verdana", 12, "bold"),
            activeforeground="white",  # aktifken yazı rengi
            foreground="#272727",  # pasifken yazı rengi
            activebackground="#272727",  # aktifken arkaplan rengi
            background="white",  # pasifken arkaplan rengi
            width=25,
            height=2,
        )
        kernelBasedButton.pack()
        kernelBasedButton.place(x=1050, y=150)  # (x=1050, y=220)

        gammaFilterButton = Button(
            self.window,
            cursor="circle",
            borderwidth=3,
            relief="flat",
            text="Gamma Filtreleme",
            command=self.GoGammaFilterDetection,
            font=("Verdana", 12, "bold"),
            activeforeground="white",  # aktifken yazı rengi
            foreground="#272727",  # pasifken yazı rengi
            activebackground="#272727",  # aktifken arkaplan rengi
            background="white",  # pasifken arkaplan rengi
            width=25,
            height=2,
        )
        gammaFilterButton.pack()
        gammaFilterButton.place(x=740, y=220)  # (x=1050, y=290)

        histogramButton = Button(
            self.window,
            cursor="circle",
            borderwidth=3,
            relief="flat",
            text="Histogram",
            command=self.GoHistogramDetection,
            font=("Verdana", 12, "bold"),
            activeforeground="white",  # aktifken yazı rengi
            foreground="#272727",  # pasifken yazı rengi
            activebackground="#272727",  # aktifken arkaplan rengi
            background="white",  # pasifken arkaplan rengi
            width=25,
            height=2,
        )
        histogramButton.pack()
        histogramButton.place(x=1050, y=220)  # (x=1050, y=360)

        edgeDetectionButton = Button(
            self.window,
            cursor="circle",
            borderwidth=3,
            relief="flat",
            text="Kenar Tespit Algoritmaları",
            command=self.GoEdgeDetectionAlgorithms,
            font=("Verdana", 12, "bold"),
            activeforeground="white",  # aktifken yazı rengi
            foreground="#272727",  # pasifken yazı rengi
            activebackground="#272727",  # aktifken arkaplan rengi
            background="white",  # pasifken arkaplan rengi
            width=25,
            height=2,
        )
        edgeDetectionButton.pack()
        edgeDetectionButton.place(x=740, y=290)  # (x=740, y=360)

        cannyEdgeButton = Button(
            self.window,
            cursor="circle",
            borderwidth=3,
            relief="flat",
            text="Canny Kenar Algılama",
            command=self.GoCannyEdgeDetection,
            font=("Verdana", 12, "bold"),
            activeforeground="white",  # aktifken yazı rengi
            foreground="#272727",  # pasifken yazı rengi
            activebackground="#272727",  # aktifken arkaplan rengi
            background="white",  # pasifken arkaplan rengi
            width=25,
            height=2,
        )
        cannyEdgeButton.pack()
        cannyEdgeButton.place(x=1050, y=290)  # (x=740, y=150)

        harrisCornerFilterButton = Button(
            self.window,
            cursor="circle",
            borderwidth=3,
            relief="flat",
            text="Harris Filtresi",
            command=self.GoHarrisCornerFilterDetection,
            font=("Verdana", 12, "bold"),
            activeforeground="white",  # aktifken yazı rengi
            foreground="#272727",  # pasifken yazı rengi
            activebackground="#272727",  # aktifken arkaplan rengi
            background="white",  # pasifken arkaplan rengi
            width=25,
            height=2,
        )
        harrisCornerFilterButton.pack()
        harrisCornerFilterButton.place(x=740, y=360)  # (x=1050, y=430)

        faceButton = Button(
            self.window,
            cursor="circle",
            borderwidth=3,
            relief="flat",
            text="Yüz Algılama (Haarcascade)",
            command=self.GoFaceDetection,
            font=("Verdana", 12, "bold"),
            activeforeground="white",  # aktifken yazı rengi
            foreground="#272727",  # pasifken yazı rengi
            activebackground="#272727",  # aktifken arkaplan rengi
            background="white",  # pasifken arkaplan rengi
            width=25,
            height=2,
        )
        faceButton.pack()
        faceButton.place(x=1050, y=360)  # (x=740, y=80)

        contourDetectButton = Button(
            self.window,
            cursor="circle",
            borderwidth=3,
            relief="flat",
            text="Kontur Tespit Algoritması",
            command=self.GoContourDetection,
            font=("Verdana", 12, "bold"),
            activeforeground="white",  # aktifken yazı rengi
            foreground="#272727",  # pasifken yazı rengi
            activebackground="#272727",  # aktifken arkaplan rengi
            background="white",  # pasifken arkaplan rengi
            width=25,
            height=2,
        )
        contourDetectButton.pack()
        contourDetectButton.place(x=740, y=430)

        watershedButton = Button(
            self.window,
            cursor="circle",
            borderwidth=3,
            relief="flat",
            text="Watershed Algoritması",
            command=self.GoWatershedDetection,
            font=("Verdana", 12, "bold"),
            activeforeground="white",  # aktifken yazı rengi
            foreground="#272727",  # pasifken yazı rengi
            activebackground="#272727",  # aktifken arkaplan rengi
            background="white",  # pasifken arkaplan rengi
            width=25,
            height=2,
        )
        watershedButton.pack()
        watershedButton.place(x=1050, y=430)

        view = Label(self.window, image=avatar)
        view.place(x=40, y=80, width=650, height=500)

        self.window.mainloop()

    def GoThresholding(self):
        self.Quit()
        Thresholding(self.window)

    def GoCopyMakeBorder(self):
        self.Quit()
        CopyMakeBorder(self.window)

    def GoBlurImage(self):
        self.Quit()
        ImageSmoothing(self.window)

    def GoKernelBasedDetection(self):
        self.Quit()
        KernelBasedDetection(self.window)

    def GoGammaFilterDetection(self):
        self.Quit()
        GammaFilterDetection(self.window)

    def GoHistogramDetection(self):
        self.Quit()
        HistogramDetection(self.window)

    def GoEdgeDetectionAlgorithms(self):
        self.Quit()
        EdgeDetectionAlgorithms(self.window)

    def GoCannyEdgeDetection(self):
        self.Quit()
        CannyEdgeDetection(self.window)

    def GoHarrisCornerFilterDetection(self):
        self.Quit()
        HarrisCornerFilterDetection(self.window)

    def GoFaceDetection(self):
        self.Quit()
        FaceDetection(self.window)

    def GoContourDetection(self):
        self.Quit()
        ContourDetection(self.window)

    def GoWatershedDetection(self):
        self.Quit()
        WatershedDetection(self.window)

    def Quit(self):
        self.window.withdraw()

    # </---Anamenü Fonksiyonunun Tanımlanması--->
