from database import SessionLocal
from typing import Optional
from models import user
import hashlib

def hashed(some: str):
    hash =  hashlib.sha256(bytes(some, 'utf-8')).hexdigest()
    return hash

def tambahUser(username: str, password: str, age: int, email: str):
    hash = hashed(some=password)
    session = SessionLocal()
    newUser = user(username=username, hashed_password=hash, age=age, email=email)
    session.add(newUser)
    session.commit()
    print("Sukses commit data ke database")
    SessionLocal.close_all()

def cariUser(username: Optional[str] = None):
    Session = SessionLocal()
    users = Session.query(user).filter(user.username == username).first()
    SessionLocal.close_all()
    return users

def getInfoUser(username: str):
    Session = SessionLocal()
    passIn = input("Masukan Password Akun: ")
    hashResult = hashed(some=passIn)
    userObj = Session.query(user).filter(user.hashed_password == hashResult).first()
    if (userObj and userObj.username == username):
        infoUser = f'''
            Nama: {userObj.username}
            Umur: {userObj.age}
            Email: {userObj.email}
            '''
        print(infoUser)
    else:
        print("Maaf Password Salah")
    SessionLocal.close_all()

def deleteUser(username):
    Session = SessionLocal()
    userObj = Session.query(user).filter(user.username == username).first()
    Session.delete(userObj)
    Session.commit()
    print("Hapus Data Complete")
    SessionLocal.close_all()

class SessionLogin():
    def __init__(self):
        self._logging = False
        self._user = None

    def _setLogging(self, value: bool):
        self._logging = value

    def _setUserLogging(self, value: str):
        self._user = value

    def getUser(self):
        return self._user

    def getStatusLogin(self):
        return self._logging

    def login(self, userObj):
        self._setLogging(value=True)
        self._setUserLogging(value=userObj.username)

def SessionLogging(usernameIn: str, passwordIn: str):
    Session = SessionLocal()
    getUser = Session.query(user).filter(user.username == usernameIn).first()
    if (getUser and getUser.is_admin):
        if (getUser.hashed_password != hashed(some=passwordIn)):
            print("Username atau password salah")
            exit()
        print("Anda berhasil login sebagai ADMIN")
        SessionLocal.close_all()
        return getUser
    else:
        print("Username atau password salah")
        exit()

def EditData(usernameIn: str, emailIn: str, umurIn:int, data):
    Session = SessionLocal()
    getObj = Session.query(user).filter(user.username == data.username).first()
    getObj.username = usernameIn
    getObj.email = emailIn
    getObj.age = umurIn
    Session.commit()
    Session.refresh(getObj)
    SessionLocal.close_all()