from Worker import *

class WorkerMenu:

    def __init__(self):
        self.worker = Worker2()

    def select_option(self, opt):
        if opt is '1':
            self.products_options()
        elif opt is '2':
            self.clients_options()
        elif opt is '3':
            self.orders_options()
        elif opt is '4':
            self.delivery_options()
        elif opt is '5':
            self.workers_options()
        elif opt is '6':
            self.localization_options()
        elif opt is '7':
            self.categories_options()
        else:
            print("Nie ma takiej opcji")

    def products_options(self):
        print("1. Dodaj nowy produkt:")
        print("2. Aktualizacja ceny produktu:")
        print("3. Aktualizacja dostawcy produktu:")
        print("4. Aktualizacja ilości produktu:")
        print("5. Aktualizacja nazwy produktu:")
        print("6. Usunięcie produktu po całej nazwie:")
        print("7. Usunięcie produktu po czesci nazwy:")
        print("8. Usunięcie produktu po kategorii:")

        opt = int(input("Opcja nr:"))
        if opt is 1:
            id_cat = input("ID kategorii produktu: ")
            quant = input("Ilosc sztuk produktu: ")
            price = input("Cena sztuki: ")
            id_del = input("ID dostawcy: ")
            name = input("Nazwa produktu: ")
            self.worker.insert_produt(id_cat, quant, price, id_del, name)
        elif opt is 2:
            newPrice = input("Nowa cena: ")
            id = input("ID produktu do aktualizacji: ")
            self.worker.update_product_price(newPrice, id)
        elif opt is 3:
            newDeliveryId = input("ID nowego dostawcy: ")
            id = input("ID produktu do aktualizacji: ")
            self.worker.update_product_delivery_id(newDeliveryId, id)
        elif opt is 4:
            newQuant = input("Nowa ilosc produktu: ")
            id = input("ID produktu do aktualizacji: ")
            self.worker.update_product_quantity(newQuant, id)
        elif opt is 5:
            newName = input("Nowa nazwa produktu: ")
            id = input("ID produktu do aktualizacji: ")
            self.worker.update_product_name(newName, id)
        elif opt is 6:
            fullname = input("Podaj cala nazwe produktu do usuniecia: ")
            self.worker.delete_product_by_fullname(fullname)
        elif opt is 7:
            partname = input("Podaj czesc nazwy do usuniecia(OSTROŻNIE): ")
            self.worker.delete_product_by_partname(partname)
        elif opt is 8:
            id_cat = input("Podaj id kategorii do usunięcia: ")
            self.worker.delete_product_by_category(id_cat)
        else:
            print("Brak takiej operacji")

    def clients_options(self):
        print("1. Wyswietl klientow:")
        print("2. Dodaj nowego klienta:")

        opt = int(input("Opcja nr:"))
        if opt is 1:
            self.worker.select_clients()
        elif opt is 2:
            company_name = input("Podaj nazwe firmy: ")
            telephone = input("Podaj nr. telefonu firmy: ")
            fname = input("Podaj imie odpowiedzialnego pracownika: ")
            lname = input("Podaj nazwisko odpowiedzialnego pracownika: ")
            self.worker.insert_client(company_name, telephone, fname, lname)
        else:
            print("Brak takiej operacji")


    def orders_options(self):
        print("1. Zlicz zamowienia o danym statusie:")
        print("2. Wyswietl zamowienia wg. daty:")
        print("3. Wyswietl zamowienia po id klienta:")
        print("4. Zmien status zamowienia:")

        opt = int(input("Opcja nr:"))
        if opt is 1:
            self.worker.count_orders_by_status()
        elif opt is 2:
            self.worker.select_orders_by_date()
        elif opt is 3:
            client_id = input("Podaj id klienta: ")
            self.worker.select_order_by_client_id(client_id)
        elif opt is 4:
            new_status = input("Podaj nowy status zamowienia: ")
            id_order = input("Podaj ID zamowienia: ")
            self.worker.update_status_order(new_status, id_order)
        else:
            print("Brak takiej operacji")

    def delivery_options(self):
        print("1. Wyświetl dostawców: ")
        print("2. Dodaj dostawcę: ")
        print("3. Modyfikuj dostawcę: ")
        opt = int(input("Opcja nr:"))
        if opt is 1:
            self.worker.select_delivery()
        elif opt is 2:
            # name,adress,telephone
            name = input("Nazwa: ")
            adress = input("Adres: ")
            telephone = input("Telefon: ")
            self.worker.insert_delivery(name, address, telephone)
        elif opt is 3:
            # name,newname,newadrr,newphone
            name = input("Nazwa: ")
            newname = input("Nowa nazwa: ")
            newadrr = input("Nowy adres: ")
            newphone = input("Nowy nr.telefonu: ")
            self.worker.update_delivery(name, newname, newadrr, newphone)

    def workers_options(self):
        print("1. Wyświetl pracowników po pozycji: ")
        print("2. Awansuj/degraduj pracownika: ")
        print("3. Edycja wypłaty pracownika: ")
        print("4. Dodaj pracownika: ")
        print("5. Usuń pracownika poprzez id pracownika: ")
        print("6. Usuń pracownika poprzez imie i nazwisko: ")
        opt = int(input("Opcja nr:"))
        if opt is 1:
            id_position = input("ID pozycji do wyświetlenia: ")
            self.worker.select_worker_by_postion(id_position)
        elif opt is 2:
            # id_pozycji,id_pracownika
            id_pracownika = input("ID pracownika: ")
            id_pozycji = input("ID nowej pozycji: ")
            self.worker.update_worker_position(id_pozycji, id_pracownika)
        elif opt is 3:
            # newSalary,id_pracownika
            id_pracownika = input("ID pracownika: ")
            newSalary = input("Nowa wypłata: ")
            self.worker.update_worker_salary(newSalary, id_pracownika)
        elif opt is 4:
            # id_pos,sallary,name,surname
            name = input("Imie: ")
            surname = input("Nazwisko: ")
            id_pos = input("ID pozycji: ")
            sallary = input("Wypłata: ")
            self.worker.insert_worker(id_pos, sallary, name, surname)
        elif opt is 5:
            # idset
            idset = input("ID pracownika: ")
            self.worker.delete_worker_by_id(idset)
        elif opt is 6:
            # workname
            workname = input("Nazwa: ")
            self.worker.delete_worker_by_name(workname)

    def localization_options(self):
        print("1. Dodaj kategorię produktów do lokalizacji: ")
        print("2. Zmień nazwę lokalizacji: ")
        opt = int(input("Opcja nr:"))
        if opt is 1:
            # id_cat, name
            id_cat = input("ID kategori: ")
            name = input("Nazwa lokalizacji: ")
            self.worker.insert_localization(id_cat, name)
        elif opt is 2:
            # id,newloc
            id = input("ID lokalizacji: ")
            newloc = input("Nowa nazwa lokalizacji: ")
            self.worker.insert_localization(id, newloc)

    def categories_options(self):
        print("1. Dodaj kategorię: ")
        print("2. Modyfikuj kategorię: ")
        opt = int(input("Opcja nr:"))
        if opt is 1:
            # name
            name = input("Nazwa kategori: ")
            self.worker.insert_category(name)
        elif opt is 2:
            # name,newname
            name = input("Stara nazwa kategorii: ")
            newname = input("Nowa nazwa kategorii: ")
            self.worker.update_category(name, newname)
