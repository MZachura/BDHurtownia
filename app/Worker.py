import pymysql.cursors


class Worker:
    def __init__(self):
        self.conn = pymysql.connect(host='192.168.64.2',
                                    user='root',
                                    password='root',
                                    db='HurtowniaBaza2',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor,
                                    autocommit=True)

    # INSERT CATEGORY(1 OPT)
    def insert_category(self, name):
        with self.conn.cursor() as cursor:
            sql = '''INSERT INTO Kategoria (`nazwa`) VALUES (%s)'''
            cursor.execute(sql, (name))
            # self.conn.commit()

    # UPDATE CATEGORY NAME(1 OPT)
    def update_category(self, name, newName):
        with self.conn.cursor() as cursor:
            sql = '''UPDATE Kategoria
                   SET nazwa=%s
                   WHERE nazwa=%s'''
            cursor.execute(sql, (newName, name))

    # SELECT CLIENTS
    def select_clients(self):
        with self.conn.cursor() as cursor:
            sql = '''select nazwa, concat(imie, ' ', nazwisko) as "dane osobowe", nr_telefonu from Klient;'''
            cursor.execute(sql)
            results = cursor.fetchall()

            for result in results:
                print(result)

    # INSERT NEW CLIENT
    def insert_client(self, company_name, telephone, f_name, l_name):
        with self.conn.cursor() as cursor:
            sql = '''INSERT INTO Klient ( `nazwa`, `nr_telefonu`, `imie`, `nazwisko`) VALUES ( %s, %s, %s, %s)'''
            cursor.execute(sql, (company_name, telephone, f_name, l_name))

    # SELECT ORDERS(3 OPTS)

    def count_orders_by_status(self):
        with self.conn.cursor() as cursor:
            sql = '''select status, count(*) as liczba from Zamowienie group by status'''
            cursor.execute(sql)
            results = cursor.fetchall()

            for result in results:
                print(result)

    def select_orders_by_date(self):
        with self.conn.cursor() as cursor:
            sql = '''select Klient.nazwa, Zamowienie.ilosc, Zamowienie.data, Zamowienie.cena, Zamowienie.status from Zamowienie
                   inner join Klient
                   on Zamowienie.id_klienta=Klient.id
                   order by Zamowienie.data'''
            cursor.execute(sql)
            results = cursor.fetchall()

            for result in results:
                print(result)

    def select_order_by_client_id(self, client_id):
        with self.conn.cursor() as cursor:
            sql = '''select * from Zamowienie where id_klienta=%s;'''
            cursor.execute(sql, (client_id))
            result = cursor.fetchall()
            print(result)

    # DELETE PRODUCT(3 OPT)

    def delete_product_by_category(self, id):
        with self.conn.cursor() as cursor:
            sql = '''DELETE FROM Produkt WHERE id_kategorii=%s;'''
            cursor.execute(sql, (id))

    def delete_product_by_fullname(self, fullname):
        with self.conn.cursor() as cursor:
            sql = '''DELETE FROM Produkt WHERE nazwa=%s;'''
            cursor.execute(sql, (fullname))

    def delete_product_by_partname(self, partname):
        with self.conn.cursor() as cursor:
            sql = '''DELETE FROM Produkt WHERE nazwa LIKE partname;'''
            cursor.execute(sql, (partname))

    # UPDATE STATUS ORDER(1 OPT)

    def update_status_order(self, status, id):
        with self.conn.cursor() as cursor:
            sql = '''UPDATE  Zamowienie
                   SET status=%s
                   WHERE id=%s'''
            cursor.execute(sql, (status, id))

    # WORKER select
    def select_worker_by_postion(self, id_position):
        with self.conn.cursor() as cursor:
            sql = '''select concat(Pracownik.imie, ' ', Pracownik.nazwisko) as 'Dane osobowe', Pracownik.pensja, Pozycja.pozycja
            from Pracownik
            inner join Pozycja
            on Pracownik.id_pozycji=Pozycja.id
            where Pracownik.id_pozycji=%s'''
            cursor.execute(sql, (id_position))
            results = cursor.fetchall()

            for result in results:
                print(result)

    # WORKER UPDATE(2 OPT)

    def update_worker_position(self, position_id, id):
        with self.conn.cursor() as cursor:
            sql = '''UPDATE  Pracownik
                   SET id_pozycji=%s
                   WHERE id=%s;'''
            cursor.execute(sql, (position_id, id))

    def update_worker_salary(self, newSalary, id):
        with self.conn.cursor() as cursor:
            sql = '''UPDATE  Pracownik
                   SET pensja=%s
                   WHERE id=%s;'''
            cursor.execute(sql, (newSalary, id))

    # PRODUCT INSERT(1 OPT)
    def insert_produt(self, id_cat, quant, price, id_del, name):
        with self.conn.cursor() as cursor:
            sql = '''INSERT INTO Produkt(`id_kategorii`,`ilosc`,`cena`,`id_dostawcy`,`nazwa`) VALUES (%s,%s,%s,%s,%s);  '''
            cursor.execute(sql, (id_cat, quant, price, id_del, name))

    # PRODUCT UPDATE(4 OPT)
    # cena
    def update_product_price(self, newPrice, id):
        with self.conn.cursor() as cursor:
            sql = '''UPDATE  Produkt
                   SET cena=%s
                   WHERE id=%s;'''
            cursor.execute(sql, (newPrice, id))

    # id_dostawcy
    def update_product_delivery_id(self, newIDDostawcy, id):
        with self.conn.cursor() as cursor:
            sql = '''UPDATE  Produkt
                   SET id_dostawcy=%s
                   WHERE id=%s;'''
            cursor.execute(sql, (newIDDostawcy, id))

    # zmiana ilości
    def update_product_quantity(self, newQuant, id):
        with self.conn.cursor() as cursor:
            sql = '''UPDATE  Produkt
                   SET ilosc=%s
                   WHERE id=%s;'''
            cursor.execute(sql, (newQuant, id))

    # zmiana nazwy
    def update_product_name(self, newName, id):
        with self.conn.cursor() as cursor:
            sql = '''UPDATE  Produkt
                   SET nazwa=%s
                   WHERE id=%s;'''
            cursor.execute(sql, (newName, id))

    # INSERT Worker
    def insert_worker(self, id_pos, sallary, name, surname):
        with self.conn.cursor() as cursor:
            sql = '''INSERT INTO `Pracownik` (`id_pozycji`, `pensja`, `imie`, `nazwisko`) VALUES ( %s, %s, %s, %s);'''
            cursor.execute(sql, (id_pos, sallary, name, surname))

    # DELETE WORKER(2 OPT)

    def delete_worker_by_id(self, idset):
        with self.conn.cursor() as cursor:
            sql = '''DELETE FROM Pracownik WHERE id LIKE idset;'''
            cursor.execute(sql, (idset))

    def delete_worker_by_name(self, workname):
        with self.conn.cursor() as cursor:
            sql = '''DELETE FROM Pracownik WHERE nazwa LIKE workname;'''
            cursor.execute(sql, (workname))

    # POSITION UPDATE(1 OPT)

    def update_position(self, newpos, position):
        with self.conn.cursor() as cursor:
            sql = '''UPDATE  Pozycja
                   SET pozycja=%s
                   WHERE pozycja=%s;'''
            cursor.execute(sql, (newpos, position))

    # POSITION INSERT
    def insert_position(self, position):
        with self.conn.cursor() as cursor:
            sql = '''INSERT INTO Pozycja ( `position`) VALUES ( %s);'''
            cursor.execute(sql, (position))

    # LOCALIZATION INSERT(1 OPT)
    def insert_localization(self, id_cat, name):
        with self.conn.cursor() as cursor:
            sql = '''INSERT INTO Lokalizacja ( `id_kategorii`,`nazwa`) VALUES ( %s, %s);'''
            cursor.execute(sql, (id_cat, name))

    # LOCALIZATION UPDATE(1 OPT)
    def update_localization(self, id, newloc):
        with self.conn.cursor() as cursor:
            sql = '''UPDATE  Lokalizacja
                   SET nazwa=%s
                   WHERE id=%s;'''
            cursor.execute(sql, (newloc, id))

    # select delivery
    def select_delivery(self):
        with self.conn.cursor() as cursor:
            sql = '''select * from Dostawca;'''
            cursor.execute(sql)
            results = cursor.fetchall()

            for result in results:
                print(result)

    # insert delivery
    def insert_delivery(self, name, address, telephone):
        with self.conn.cursor() as cursor:
            sql = '''INSERT INTO `Dostawca` (`nazwa`, `adres`, `nr_telefonu`) VALUES (%s, %s, %s);'''
            cursor.execute(sql, (name, address, telephone))

    # update delivery
    def update_delivery(self, name, newname, newadrr, newphone):
        with self.conn.cursor() as cursor:
            sql = '''UPDATE  Dostawca
                   SET nazwa=%s, adres=%s, nr_telefonu=%s
                   WHERE name=%s;'''
            cursor.execute(sql, (newname, newadrr, newphone, name))

    def __exit__(self, ):
        self.conn.close()
