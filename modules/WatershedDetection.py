from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import filedialog
import cv2
import sys
import matplotlib.pyplot as plt
import numpy as np


class WatershedDetection:
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
                a = WatershedDetectAl(self.filename)
                images = a.watershedDetectionImg()

                # Eğer geri dönen görüntülerin sayısı 9 değilse veya hata oluşmuşsa işlem yapma
                if len(images) != 9:
                    print("Error in obtaining images.")
                    return

                # Sol tarafta orijinal resmi gösterecek olan Label widget'ı
                original_image = Image.open(self.filename)
                original_image = original_image.resize((450, 400))
                original_image = ImageTk.PhotoImage(original_image)

                original_label = Label(
                    self.root,
                    image=original_image,
                    bg="#2C073E",
                    fg="#ffffff",
                    width=450,
                    height=400,
                )
                original_label.image = original_image
                original_label.place(x=50, y=145)

                # Sağ tarafta beklenen 9 resmi gösterecek olan Frame widget'ı
                image_frame = Frame(self.root, bg="#3336be")
                image_frame.place(x=650, y=145)
                image_frame.grid_rowconfigure(0, weight=1)  # Satırları ölçeklendir
                image_frame.grid_columnconfigure(0, weight=1)  # Sütunları ölçeklendir

                # Her bir görüntüyü bir Label içinde göster
                for i, img in enumerate(images):
                    # Görüntüyü PIL formatına dönüştür
                    img = Image.fromarray(img)
                    img = img.resize((150, 133))  # Görüntü boyutlarını ayarla

                    # PIL formatındaki görüntüyü Tkinter formatına dönüştür
                    tk_img = ImageTk.PhotoImage(img)

                    # Label oluştur ve görüntüyü göster
                    label = Label(
                        image_frame,
                        image=tk_img,
                        bg="#2C073E",
                        fg="#ffffff",
                        width=150,
                        height=133,
                    )
                    label.image = tk_img  # Referansı tutması için
                    row = i // 3
                    col = i % 3
                    label.grid(row=row, column=col, padx=5, pady=5)

                self.root.mainloop()
            except Exception as e:
                print("Error in image detection:", e)

        # <---Form Ayarları--->

        self.root = Toplevel()
        self.root.wm_iconbitmap("img/image-processing.ico")
        self.root.geometry("1266x692+0+0")
        self.root.maxsize(1366, 768)
        self.root.title("Watershed Algoritması")
        self.root.configure(background="#3336be")

        # </---Form Ayarları--->

        # <---Resimlerin Eklenmesi--->
        mainmenu = ImageTk.PhotoImage(Image.open(os.getcwd() + "\\img\\home.png"))
        find = ImageTk.PhotoImage(Image.open(os.getcwd() + "\\img\\search.png"))
        noImage = ImageTk.PhotoImage(Image.open(os.getcwd() + "\\img\\noImage.png"))
        createImage = ImageTk.PhotoImage(
            Image.open(os.getcwd() + "\\img\\create_icon.png")
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

        createButton = Button(
            self.root,
            image=createImage,
            bd=0,
            highlightthickness=0,
            command=imgDetect,
            activeforeground="#7e7e7e",  # aktifken yazı rengi
            foreground="#7e7e7e",  # pasifken yazı rengi
            activebackground="white",  # aktifken arkaplan rengi
            background="#272727",  # pasifken arkaplan rengi
            text="Oluştur",
            font=("Arial 13 bold"),
            compound="top",
            width=100,
            height=90,
        )
        createButton.image = createImage
        createButton.place(x=525, y=300)

        # </---Butonların Oluşturulması--->

        # <---Labelların Oluşturulması--->

        title = Label(
            self.root,
            text="WATERSHED ALGORİTMASI",
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


class WatershedDetectAl:
    def __init__(self, filename):
        self.filename = filename

    def watershedDetectionImg(self):
        try:
            # Görüntüyü yükle
            imgOrj = cv2.imread(self.filename)
            imgBlr = cv2.medianBlur(imgOrj, 31)
            # Madeni para içindeki detayların sonucu etkilememesi için blurring yaptık
            imgGray = cv2.cvtColor(imgBlr, cv2.COLOR_BGR2GRAY)
            # Griye çevrilen resim THRESH_BINARY_INV ile arkaplan siyah, önplan beyaz yapılır
            ret, imgTH = cv2.threshold(
                imgGray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
            )

            kernel = np.ones((5, 5), np.uint8)
            # imgTH çıktısında ön plan nesneleri üzerinde kalan gürültüden kurtulmak için
            # morfoloji operatörlerden openning işlemi uygulanır.
            imgOPN = cv2.morphologyEx(imgTH, cv2.MORPH_OPEN, kernel, iterations=7)

            # Arkaplan alanı
            # dilate() fonksiyonu ile nesneler genişletebilir ve kesin emin olduğumuz arkaplan
            # kısımları elde edilir.
            sureBG = cv2.dilate(imgOPN, kernel, iterations=3)

            # Önplan Alanı
            # distanceTransform() ile her pikselin en yakın sıfır değerine sahip piksele
            # olan mesafesi hesaplanır. Nesnelerin merkez pikselleri yani sıfır piksellerine
            # en uzak nokta beyaz kalırken, siyah piksellere yaklaştıkça piksel değerleri
            # düşer. Böylece madeni para, yani emin olduğumuz ön plan piksellerin ortaya
            # çıkması sağlanmıştır.
            dist_transform = cv2.distanceTransform(imgOPN, cv2.DIST_L2, 5)

            # Eşikleme yap
            # Eşik değeri olarak hesaplanan maksimum mesafenin %70'den büyük olanlarının
            # piksel değeri 255 yapılarak sureFG elde edilmiştir.
            ret, sureFG = cv2.threshold(
                dist_transform, 0.7 * dist_transform.max(), 255, 0
            )

            # Bilinmeyen bölgeleri bul
            # Emin olduğumuz arkaplan ve ön plan arasında kalan alandır.
            sureFG = np.uint8(sureFG)
            unknown = cv2.subtract(sureBG, sureFG)

            # Etiketleme işlemi
            ret, markers = cv2.connectedComponents(sureFG, labels=5)

            # Bilinmeyen pikselleri etiketle
            markers = markers + 1
            markers[unknown == 255] = 0

            # Watershed algoritması uygula
            markers = cv2.watershed(imgOrj, markers)

            contours, hierarchy = cv2.findContours(
                markers, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE
            )

            imgCopy = imgOrj.copy()
            for i in range(len(contours)):
                if hierarchy[0][i][3] == -1:
                    cv2.drawContours(imgCopy, contours, i, (255, 0, 0), 5)

            # Görüntülerin her birini bir listeye ekle ve döndür
            images = [
                imgOrj,
                imgBlr,
                imgGray,
                imgTH,
                imgOPN,
                sureBG,
                dist_transform,
                sureFG,
                imgCopy,
            ]
            return images

        except Exception as e:
            print("Error in Watershed Detection:", e)
            return []
