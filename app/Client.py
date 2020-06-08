import pymysql.cursors


class Client:
    def __init__(self):
        self.conn = pymysql.connect(host='192.168.64.2',
                                    user='root',
                                    password='root',
                                    db='HurtowniaBaza2',
                                    charset='utf8mb4',
                                    port=8080,
                                    cursorclass=pymysql.cursors.DictCursor
                                    )

    # PRODUCT SELECT
    def select_product_by_name(self, keyword):
        # try:
        with self.conn.cursor() as cursor:
            sql = ''' select Produkt.nazwa as "Nazwa Produktu", Produkt.ilosc as "Ilosc produktow", Produkt.cena as "Cena produktu", Kategoria.nazwa as "Nazwa Kategorii"
             from Produkt inner join Kategoria
             on Produkt.id_kategorii=Kategoria.id
             where Kategoria.nazwa=%s'''
            cursor.execute(sql, (keyword))
            results = cursor.fetchall()

            # print(results[0]['Nazwa Produktu'])

            for result in results:
                print(result)
        # finally:
        #     connection.close()

    # ORDER
    def order(self,id_prod, id_client, quant):
        with self.conn.cursor() as cursor:
            sql='''select * from Produkt where id_produktu=%s '''
            cursor.execute(sql,(id_prod))
            results = cursor.fetchall()
            if(int(results['ilosc'])-quant>=0):
                price=int(results['cena'])*quant
                sql=''' INSERT INTO Zamowienie (`id_produktu`, `id_klienta`,`ilosc`,`cena`) VALUES (%s, %s, %s, %s)'''
                cursor.execute(sql,(id_prod,id_client,quant,price))
            else:
                print("brak wystarczającej ilości produktów")

# CHECK ORDER STATUS
    def check_order_status(self, id_order):
        with self.conn.cursor() as cursor:
            sql = '''select Zamowienie.id as 'ID zamowienia', Produkt.nazwa, Zamowienie.ilosc, Zamowienie.status
                        from Zamowienie
                        inner join Produkt
                        on Zamowienie.id_produktu=Produkt.id
                        where Zamowienie.Id=%s '''
            cursor.execute(sql, (id_order))
            result = cursor.fetchone()
            print(result)

    def __exit__(self, ):
        self.conn.close()
