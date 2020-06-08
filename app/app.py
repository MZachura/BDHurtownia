from getpass import getpass
from Worker import Worker
from Client import Client
from WorkerMenu import *


class Control:

    def __init__(self):
        self.option = 0
        self.clientObj = Client()
        # self.worker = Worker()

    def switch(self, usr):
        if usr == 1:
            print("1. przeglądaj produkty: ")
            print("2. złóż zamówienie: ")
            print("3. sprawdź stan zamówienia: ")
            self.option = input("Opcja nr: ")
            if int(self.option) <= 3:
                self.client()
            else:
                print("niepoprawna opcja")
        elif usr == 2:
            print("1. produkty: ")
            print("2. klienci: ")
            print("3. zamówienia: ")
            print("4. dostawcy: ")
            print("5. pracownicy: ")
            print("6. lokalizacje: ")
            print("7. kategoria: ")
            self.option = input("Opcja nr: ")
            if int(self.option) <= 7:
                worker_menu = WorkerMenu()
                worker_menu.select_option(str(self.option))
            else:
                print("niepoprawna opcja")

    def client(self):
        if self.option is '1':
            print("Wódki")
            print("Piwa")
            print("Cydr")
            print("Wino")
            keyword = input("podaj katerorie ")
            self.clientObj.select_product_by_name(keyword)
        elif self.option is '2':
            id_prod = input("podaj id produktu który chcesz zamówić: ")
            id_client = input("podaj id klienta (w przypadku braku, skontaktuj się z działem obsługi klienta): ")
            quant = input("podaj ilość produktów: ")
            self.clientObj.order(id_prod, id_client, quant)
        elif self.option is '3':
            id_zamowienia = input("podaj id zamówienia: ")
            self.clientObj.check_order_status(id_zamowienia)
        else:
            print("Brak operacji")


control = Control()
hell = 0

while int(hell) != 3:
    hell = int(input("czy chcesz wejść do sklepu jako klient (1), użytkownik (2), czy opuścic aplikacje (3)?"))

    if hell == 1:
        print("logowanie jako klient")
        usr = 1
        control.switch(usr)
    elif hell == 2:
        print("logowanie jako pracownik")
        print("podaj login i haslo")
        username = input("podaj login: ")
        password = getpass("hasło: ")
        if (username == "admin" and password == "1234"):
            print("zalogowano")
            usr = 2
            control.switch(usr)
        else:
            print("error")
    else:
        print("Opuszczenie aplikacji!")
        break
