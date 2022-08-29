# soyut sınıflar nesne üretemez. Şablon sınıf olarak nitelendirilir.
# Sınıfar hafızada yer tutmaz. Ama referans oluşturulduğu zaman yer tutarlar.
# Abstract sınıfların nesnesi oluşturulmadığı için hiçbir zaman hafızada yer tutmazlar
# Getter setter fonksiyonları olusturulduğu zaman değerine ulaşmak istersek getter fonksiyon ismini kullanmalıyız
# private bir metodu abstract class içerisinde kullanamazsın.Ya public yada protected
# Abstract classlar en az bir tane abstract metod almak zorundadır.
# Abstract metodu miras alan sınıf abstract classtaki metodların hepsini almak sorundadır.
# abstract sınıf içerisinde abstract metodla tanımlanan her metod miras alan sınıfta kullanılmalıdır.

from abc import ABC, abstractmethod  # abc kütüphanesinden ABC ve abstract metodu import edilir.


class Coin(ABC):

    @abstractmethod
    def add_list(self):
        pass

    def info(self):  # abstract metodlarda kendine özgü metodlara sahip olabilir. Ama !!!!
        # bu durumda @abstractmetod ibaresi kullanılmamalıdır. abstractmetod sadece miras verilen
        # metodları tanımlar
        pass


class User(Coin):
    user_list = []

    def __init__(self, u_id, username, password, budget):
        self.__u_id = u_id
        self.__username = username
        self.__password = password
        self.__budget = budget

    def __user_info(self):
        o = f' {self.__u_id} {self.__username} {self.__password} {self.__budget}'
        return o

    @property
    def user_info(self):
        return self.__user_info()

    @property
    def u_id(self):
        return self.__u_id

    @u_id.setter
    def u_id(self, value):
        self.__u_id = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        self.__budget = value

    def add_list(self):
        temp_list = [self.__u_id, self.username, self.__budget]
        self.user_list.append(temp_list)
        return list


class CoinList:

    def __init__(self, coin_id, name, value):
        self.__coin_id = coin_id
        self.__name = name
        self.__value = value

    @property
    def coin_id(self):
        return self.__coin_id

    @coin_id.setter
    def coin_id(self, value):
        self.__coin_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def valuex(self):
        return self.__value

    @valuex.setter
    def valuex(self, value):
        self.__value = value

    def __info(self):  # Metodlarla da getter setter işlemi gerçekleştirilebilir.
        kxs = f'ID: {self.coin_id} NAME: {self.name} VALUE: {self.valuex}'
        return kxs

    @property
    def info(self):
        return self.__info()


c1 = CoinList(None, None, None)
c1.coin_id = 247
c1.name = 'ENS'
c1.valuex = 224.80
print(c1.info)

u1 = User(None, None, None, None)
u1.u_id = 123
u1.username = 'user1'
u1.password = '5165sda'
u1.budget = 2750
k = u1.user_info
print(k)
u1.add_list()
print(u1.user_list)
