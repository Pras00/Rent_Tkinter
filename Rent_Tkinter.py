from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv

file = 'user.csv'

# Fungsi menjalankan halaman rental
def rental():
    pilihan = ["Assassin's Creed III", "Assassin's Creed IV : Black Flag", 
    "Call of Duty : Ghost", "Call of Duty : Modern Warfare",
    "Call of Duty : Black Ops III", "Battlefield I",
    "Battlefield IV", "Battlefield V", "Point Blank",
    "GOD OF WAR 4", "Valorant", "PUBG", "PES 2021", "PES 2022", 
    "FIFA 21", "FIFA 22", "THE SIMS 4", "Stumble Guy",
    "Far Cry 5","Red Dead Redamption II", "CS: Global Offensive",
    "Cyberpunk 2077", "GTA IV", "GTA V"
    ]

    duration = ["1","2","3","4","5","6","7","8","9","10",
    "11","12","13","14","15","16","17","18","19","20",
    "21","22","23","24",
    ]

    window = Tk()
    cnv = Canvas(window, width=300, height=450)
    cnv.pack()

    cnv.create_line(0,450,105,350)
    cnv.create_line(300,450,190,390)
    cnv.create_line(0,320,105,350)
    cnv.create_line(300,320,190,390)

    judul = Label(window, text="DVD GAME RENTAL", font=("georgia", 18, "bold")).place(x=17, y=10)

    nama = Label(window, text="Nama").place(x=20, y=50)
    umur = Label(window, text="Umur").place(x=20, y=90)
    gender = Label(window, text="Jenis Kelamin").place(x=20, y=130)
    alamat = Label(window, text="Alamat").place(x=20, y=170)
    no_hp = Label(window, text="No. Handphone").place(x=110, y=210)
    durasi = Label(window, text="Durasi/jam").place(x=20, y=210)
    game = Label(window, text="Game").place(x=20, y=250)

    e1 = Entry(window, width=40)
    e1.place(x=20, y=70)
    e2 = Entry(window, width=40)
    e2.place(x=20, y=110)
    e3 = Entry(window, width=40)
    e3.place(x=20, y=190)
    e4 = ttk.Combobox(window, values=duration, width=7)
    e4.place(x=20, y=230)
    e4.current(0)
    e5 = Entry(window, width=20)
    e5.place(x=110, y=230)
    e6 = ttk.Combobox(window, values=pilihan, width=30)
    e6.place(x=20, y=270)
    e6.current(0)

    r = StringVar()
    r.set("Laki-laki")
    rb = Radiobutton(window, text="Laki-laki", variable=r, value="Laki-laki").place(x=20, y=150)
    rb2 = Radiobutton(window, text="Perempuan", variable=r, value="Perempuan").place(x=80, y=150)

    # Fungsi menjalankan halaman hasil
    def halaman_hasil():
        root = Tk()
        cnv = Canvas(root, width=400, height=300)
        cnv.pack()

        labelfr = LabelFrame(root,text = "Note",padx=20,pady=20)
        labelfr.place(x = 50,y = 30)

        # Menyimpan nilai inputan user
        def hasil():
            nama = e1.get()
            umur = e2.get()
            gender = r.get()
            alamat = e3.get()
            durasi = e4.get()
            nomor = e5.get()
            game = e6.get()
            harga = int(durasi) * 10000

            Label(labelfr,
            text=(f"Nama : {nama}"
            f"\nUmur  : {umur} Tahun"
            f"\nGender : {gender}"
            f"\nAlamat : {alamat}"
            f"\nNo. HP : {nomor}"
            f"\nDurasi : {durasi} Jam"
            f"\nGame : {game}"
            f"\nHarga : {harga}"), 
            font=("arial")
            ).grid()
        # Memanggil fungsi hasil
        hasil()
        # Menghapus Inputan setelah dijalankan
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)

    Button(window, text="Pesan", command=halaman_hasil, height=2, width=11).place(x=105,y=350)

    window.mainloop()


# Halaman awal login
# User diminta menginputkan Username dan Password
def Halaman_login():
    window = Tk()
    window.title("Login")
    cnv = Canvas(window, width=300, height=200)
    cnv.pack()

    # Halaman daftar
    def halaman_daftar():
        window.destroy()
        root = Tk()
        root.title("Daftar")
        root.geometry("300x240")

        # Mengisi username dan password
        def daftar():
            username = e1.get()
            password = e2.get()
            re_password = e3.get()
            # Cek password
            if username == "" and password == "" and re_password == "":
                messagebox.showwarning("", "Tidak boleh kosong..!")
            elif password != re_password:
                messagebox.showwarning("", "Password tidak sesuai..!")
            elif password == re_password:
                try :
                    with open(file, mode='a', newline='') as csv_file:
                        writer = csv.writer(csv_file, delimiter=',')
                        writer.writerow([username, password])
                except FileNotFoundError:
                    with open(file, mode='w', newline="") as csv_file:
                        csv.writer(csv_file, delimiter=',')
            
                messagebox.showinfo("", "Berhasil Daftar..!")
                root.destroy()
                Halaman_login()

        judul = Label(root, text="DAFTAR", font=("georgia", 12, "bold")).place(x=115, y=10)
        Label(root, text="Username").place(x=10, y=50)
        Label(root, text="Password").place(x=10, y=80)
        Label(root, text="Re-type Password").place(x=10, y=110)

        e1 = Entry(root, width=25)
        e1.place(x=120, y=50)

        e2 = Entry(root, width=25)
        e2.place(x=120, y=80)
        e2.config(show="*")

        e3 = Entry(root, width=25)
        e3.place(x=120, y=110)
        e3.config(show="*")

        Button(root, text="Daftar", command=daftar, height=2, width=11).place(x=10, y=160)

        root.mainloop()

    # Fungsi login
    def login():
        username = e1.get()
        password = e2.get()
        # Mengakses file CSV
        data = []
        try :
            with open(file, mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    data.append(row)
        except FileNotFoundError:
                with open(file, mode='w', newline="") as csv_file:
                    csv.writer(csv_file, delimiter=',')

        # Cek username dan password
        if([username, password] in data):
            messagebox.showinfo("", "Berhasil Login..!")
            window.destroy()
            rental()
        elif([username, password] not in data):
            messagebox.showwarning("", "Username / Password salah..!")

    judul = Label(window, text="LOGIN", font=("georgia", 12, "bold") ).place(x=120, y=10)
    Label(window, text="Username").place(x=10, y=50)
    Label(window, text="Password").place(x=10, y=80)

    e1 = Entry(window, width=25)
    e1.place(x=120, y=50)

    e2 = Entry(window, width=25)
    e2.place(x=120, y=80)
    e2.config(show="*")

    Button(window, text="Login", command=login, height=2, width=11).place(x=10, y=130)
    Button(window, text="Daftar",command=halaman_daftar, height=2, width=11).place(x=120, y=130)

    window.mainloop()


# Menjalankan fungsi
Halaman_login()