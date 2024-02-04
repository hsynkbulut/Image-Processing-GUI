from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import filedialog
import cv2
import sys


class CopyMakeBorder:
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

        def copyMakeBorderDetect():
            try:
                border_width = int(self.borderWidth.get())
                a = CopyMakeBorderDetectAl(self.filename)
                a.CopyMakeBorderImg(border_width)

                myImage2.place_forget()
                if self.video == 1:
                    imgFirst = Image.open("img/noImage.png")
                else:
                    imgFirst = Image.open("img/dist/copy_make_border.png")
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
        self.root.title("Resim Dışına Kenarlık Ekleme")
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
            command=copyMakeBorderDetect,
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
        createButton.place(x=525, y=310)

        # </---Butonların Oluşturulması--->

        # <---Labelların Oluşturulması--->

        title = Label(
            self.root,
            text="RESİM DIŞINA KENARLIK EKLEME ",
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

        borderWidthLabel = Label(
            self.root, text="Kenar Kalınlığı:", bg="#3336be", fg="white"
        )
        borderWidthLabel.place(x=510, y=270)
        self.borderWidth = Entry(self.root, width=5)
        self.borderWidth.place(x=600, y=270)

        # </---Labellerın Oluşturulması--->

        self.root.mainloop()

    # <---Fonksiyonların Tanımlanması--->

    def Quit(self):
        self.root.destroy()

    # </---Fonksiyonların Tanımlanması--->


class CopyMakeBorderDetectAl:
    def __init__(self, filename):
        self.filename = filename

    def CopyMakeBorderImg(self, border_width):
        try:
            image = cv2.imread(self.filename)
            # border_color = (0, 0, 0)
            border_color = (120, 12, 240)
            # border_width = 10
            image_with_border = cv2.copyMakeBorder(
                image,
                border_width,
                border_width,
                border_width,
                border_width,
                borderType=cv2.BORDER_CONSTANT,
                value=border_color,
            )
            cv2.imwrite(
                "img/dist/copy_make_border.png",
                image_with_border,
                [cv2.IMWRITE_JPEG_QUALITY, 100],
            )
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except Exception as e:
            print(f"Hata: {e}")
