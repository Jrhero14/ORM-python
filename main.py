import models
import CRUD
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)
SessionLogin = CRUD.SessionLogin()

while(1):
    print("PROGRAM INPUT USER")
    if not(SessionLogin.getStatusLogin()):
        print("Login admin dulu bro")
        userAdmin = input("Username: ")
        passAdmin = input("Password: ")
        resultLogin = CRUD.SessionLogging(usernameIn=userAdmin, passwordIn=passAdmin)
        SessionLogin.login(userObj=resultLogin)
    print("1. Tambah User\n"
          "2. Lihat Infomasi User\n"
          "3. Hapus User\n"
          "4. Ubah data user\n"
          "5. Exit\n"
          f"STATUS lOGIN [{SessionLogin.getUser()}]")
    myinput = int(input("Pilih menu:"))

    if (myinput == 1):
        usernameIn = input("Masukan username: ")
        umurIn = int(input("Umur: "))
        emailIn = input("Email: ")
        passwordIn = input("Masukan password: ")
        reIn = input("Masukan ulang password: ")
        while (passwordIn != reIn):
            reIn = input("Password tidak sama, ulangi: ")
        CRUD.tambahUser(username=usernameIn, password=passwordIn, age=umurIn, email=emailIn)

    elif (myinput == 2):
        usernameIn = input("Username: ")
        if (CRUD.cariUser(username=usernameIn)):
            CRUD.getInfoUser(username=usernameIn)
        else:
            print("Maaf User tidak ditemukan")

    elif (myinput == 3):
        userIn = input("Akun yang akan dihapus?: ")
        userObj = CRUD.cariUser(userIn)
        if (userObj):
            if(True if input(f"Yakin hapus akun {userObj.username} (y/n)?: ")=="y" else False):
                CRUD.deleteUser(userObj.username)
            else:
                print("Hapus data dibatalkan")
        else:
            print("Akun tidak ditemukan")

    elif (myinput == 4):
        userEdit = input("User yang akan didedit: ")
        getObj = CRUD.cariUser(username=userEdit)
        if (getObj):
            print(f"User yang diedit adalah [{getObj.username}]")
            usernameEdit = input("Username Baru: ")
            emailEdit = input("Email Baru: ")
            umur = int(input("Umur baru: "))
            CRUD.EditData(usernameIn=usernameEdit, emailIn=emailEdit, umurIn=umur, data=getObj)
            print("Edit data berhasil")

    elif(myinput == 5):
        exit(0)

    print("\n")



