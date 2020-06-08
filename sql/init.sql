CREATE DATABASE IF NOT EXISTS HurtowniaBaza2;

USE HurtowniaBaza2;

CREATE USER IF NOT EXISTS hurtownia@localhost IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON hotel.* TO hurtownia@localhost;

FLUSH privileges;

CREATE TABLE Kategoria (
    id INT NOT NULL AUTO_INCREMENT,
    nazwa VARCHAR(100) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE Dostawca(
    id INT NOT NULL AUTO_INCREMENT,
    nazwa VARCHAR(200) NOT NULL,
    adres VARCHAR(200),
    nr_telefonu INT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE Produkt (
    id INT NOT NULL AUTO_INCREMENT,
    id_kategorii INT NOT NULL,
    ilosc INT DEFAULT 0,
    cena DECIMAL DEFAULT 0,
    id_dostawcy INT NOT NULL,
    nazwa VARCHAR(200) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(id_kategorii) REFERENCES Kategoria(id),
    FOREIGN KEY(id_dostawcy) REFERENCES Dostawca(id)
);

CREATE TABLE Lokalizacja (
    id INT NOT NULL AUTO_INCREMENT,
    id_kategorii INT NOT NULL,
    nazwa VARCHAR(30),
    PRIMARY KEY(id),
    FOREIGN KEY(id_kategorii) REFERENCES Kategoria(id)
);

CREATE TABLE Klient(
    id INT NOT NULL AUTO_INCREMENT,
    nazwa VARCHAR(70) NOT NULL,
    nr_telefonu INT NOT NULL,
    imie VARCHAR(50),
    nazwisko VARCHAR(50),
    PRIMARY KEY(id)
);

CREATE TABLE Pozycja(
    id INT NOT NULL AUTO_INCREMENT,
    pozycja VARCHAR(50),
    PRIMARY KEY(id)
);

CREATE TABLE Pracownik(
    id INT NOT NULL AUTO_INCREMENT,
    id_pozycji INT NOT NULL,
    pensja DECIMAL NOT NULL,
    imie VARCHAR(50),
    nazwisko VARCHAR(50),
    PRIMARY KEY(id),
    FOREIGN KEY(id_pozycji) REFERENCES Pozycja(id)
);

CREATE TABLE Zamowienie(
    id INT NOT NULL AUTO_INCREMENT,
    id_produktu INT NOT NULL,
    id_klienta INT NOT NULL DEFAULT 2,
    id_pracownika INT NOT NULL,
    ilosc INT NOT NULL DEFAULT 0,
    cena DECIMAL DEFAULT 0,
    data DATETIME DEFAULT CURRENT_TIMESTAMP;,
    status VARCHAR(50) NOT NULL DEFAULT "in progress",
    FOREIGN KEY(id_produktu) REFERENCES Produkt(id),
    FOREIGN KEY(id_klienta) REFERENCES Klient(id),
    FOREIGN KEY(id_pracownika) REFERENCES Pracownik(id),
    PRIMARY KEY(id)
);

INSERT INTO `Dostawca` (`id`, `nazwa`, `adres`, `nr_telefonu`) VALUES
(1, 'Wyborowa.SA', 'Komandoria 5, 61-131 Poznań', 618770081),
(2, 'Tyskie Browary Książęce', 'Mikołowska 5, 43-100 Tychy', 323278203),
(3, 'Wielkopolska Wytwórnia Wódek Polanin', 'Karola Libelta 6, 63-000 Środa Wielkopolska', 612853441),
(4, 'Żywiec. Sprzedaż i dystrybucja', '27, Podkolejowa 25, 42-202 Częstochowa', 800610000),
(5, 'Tłocznia Naturalnych Soków i Cydru', 'Kolonia Świdnik Mały 28A, 20-258 Lublin', 663728003),
(6, 'Winnica ZAGRABIE', 'Miodowa 4, 32-061 Rybna', 691404747);



INSERT INTO `Kategoria` (`id`, `nazwa`) VALUES
(1, 'Wódki'),
(2, 'Piwa'),
(3, 'Cydr'),
(4, 'Wino');



INSERT INTO `Klient` (`id`, `nazwa`, `nr_telefonu`, `imie`, `nazwisko`) VALUES
(1, 'Lewiatan', 544127821, 'Ob', 'kl'),
(2, 'Sklep Alkoholowy Kraków', 444333121, 'Janusz', 'Januszewski'),
(3, 'Dom Weselny \"Jaworzynka\"', 123321222, 'Dariusz', 'Awent'),
(4, 'Bar \"Pod zgryźliwym Jankiem\"', 12333323, 'Mariusz', 'Witkac'),
(5, 'Dom Weselny \"Arkadia\"', 666363122, 'Roman', 'Polak');


INSERT INTO `Lokalizacja` (`id`, `id_kategorii`, `nazwa`) VALUES
(1, 3, 'Blok:A'),
(2, 2, 'Blok:B'),
(3, 1, 'Blok:C'),
(4, 4, 'Blok:A');



INSERT INTO `Pozycja` (`id`, `pozycja`) VALUES
(1, 'Właściciel'),
(2, 'Obsługa klienta'),
(3, 'Pracownik magazynu'),
(4, 'Dyrektor do spraw logistyki'),
(5, 'Kierownik magazynu ');



INSERT INTO `Pracownik` (`id`, `id_pozycji`, `pensja`, `imie`, `nazwisko`) VALUES
(1, 1, '8000', 'Marian', 'Zawiercki'),
(2, 2, '3400', 'Karolina', 'Czarnecka'),
(3, 4, '5200', 'Radosław', 'Racławicki'),
(4, 5, '4200', 'Czesław', 'Adamiuk'),
(5, 3, '2600', 'Adam', 'Adamowicz'),
(6, 3, '2400', 'Adrian', 'Leszek'),
(7, 3, '2450', 'Anna', 'Wacławik'),
(8, 3, '2500', 'Bartłomiej', 'Opolski'),
(9, 3, '2300', 'Jarosław', 'Jaroszewski'),
(10, 3, '2700', 'Mariusz', 'Pudz'),
(11, 3, '2400', 'Piotr', 'Mikołowski'),
(12, 3, '2450', 'Karol', 'Karolak'),
(13, 2, '3600', 'Damian', 'Rzepka');


INSERT INTO `Produkt` (`id`, `id_kategorii`, `ilosc`, `cena`, `id_dostawcy`, `nazwa`) VALUES
(1, 2, 500, '12', 4, 'PIWO ŻYWIEC 0.5L 4-PACK PUSZKA'),
(2, 2, 500, '3', 4, 'PIWO ŻYWIEC 0.5, PUSZKA'),
(3, 3, 429, '11', 5, 'Cydr Lubelski 1L'),
(4, 3, 240, '10', 5, 'Dobroński Jabłkowy 0,75L '),
(5, 4, 20, '251', 6, 'WINO PORTO KOPKE TAWNY 20YO 0,75L 20% DREWNIANA SKRZYNKA'),
(6, 4, 50, '290', 6, 'WINO BAROLO RISERVA MILENIUM DOCG 0,75L CZ/W WŁOCHY'),
(7, 4, 500, '17', 6, 'WINO CASA ITALIA BIANCO B/PS 0,75L'),
(8, 4, 12, '19', 6, 'WINO BARDOLINO CHIARETTO R/W 0.75L'),
(9, 4, 0, '20', 6, 'WINO VILLA BRUCCIO PRIMITIVO CZ/W 0.75L'),
(10, 4, 12, '22', 6, 'WINO AFRICAN HORIZON CABERN.SAUV.-SHIRAZ0.75L CZ/PW RPA'),
(11, 4, 420, '23', 6, 'WINO PRINCESSE MARIE VDF CZ/PS 0.75L'),
(12, 4, 33, '25', 6, 'WINO PRIMITIVO DI PUGLIA 0,75L CZ/PS ITALIA'),
(53, 2, 320, '2', 2, 'PIWO HARNAŚ 0.5L BUTELKA ZWROTNA'),
(54, 2, 333, '4', 2, 'PIWO HEINEKEN 0.5L BUTELKA BEZZWROTNA'),
(55, 2, 122, '3', 2, 'PIWO ZATECKY SVETLY LEZAK 0.5L BUTELKA'),
(56, 2, 200, '6', 2, 'PIWO PILSNER URQUELL 0.5L BUTELKA BEZZWROTNA'),
(57, 2, 540, '3', 2, 'PIWO HARNAŚ 0.5L PUSZKA'),
(58, 2, 231, '6', 2, 'PIWO HEINEKEN 0,65L BUTELKA BEZZWROTNA'),
(59, 2, 111, '3', 4, 'PIWO KASZTELAN NIEPASTERYZOWANE 05L BUTELKA ZWROTNA'),
(60, 2, 531, '3', 4, 'PIWO KASZTELAN 0,5L PUSZKA'),
(61, 2, 259, '2', 4, 'PIWO KSIĄŻ JASNE PEŁNE 0.5L BUTELKA ZWROTNA '),
(62, 2, 469, '5', 4, 'PIWO KSIĄŻĘCE IPA 0.5L BUTELKA ZWROTNA '),
(63, 2, 421, '4', 4, 'PIWO KSIĄŻĘCE ZŁOTE PSZENICZNE 0.5L BUTELKA ZWROTNA'),
(64, 2, 343, '5', 4, 'PIWO KSIĄŻĘCE PORTER 0.5L BUTELKA ZWROTNA'),
(65, 2, 544, '5', 4, 'PIWO KSIĄŻĘCE WEIZEN 0.5L BUTELKA ZWROTNA'),
(66, 2, 611, '3', 4, 'PIWO ŻYWIEC 0.5L BUTELKA ZWROTNA'),
(67, 2, 51, '5', 4, 'PIWO ŻYWIEC BIAŁE 0.5L BUTELKA ZWROTNA'),
(68, 2, 0, '3', 4, 'PIWO ŻYWIEC BEZALKOHOLOWE 0.5L BUTELKA ZWROTNA'),
(69, 2, 2, '5', 4, 'PIWO ŻYWIEC APA 0.5L BUTELKA ZWROTNA'),
(70, 2, 90, '5', 4, 'PIWO ŻYWIEC PORTER 0.5L BUTELKA ZWROTNA'),
(73, 1, 90, '40', 3, 'CZARNY BOCIAN 0.5L'),
(74, 1, 150, '60', 3, 'AMUNDSEN VODKA 0.7L'),
(75, 1, 250, '40', 1, 'ABSOLUT VODKA 0.5L'),
(76, 1, 500, '29', 1, 'WYBOROWA WÓDKA 0.5L'),
(77, 1, 340, '42', 1, 'WYBOROWA WÓDKA 0.7L'),
(78, 1, 400, '26', 3, 'ŻOŁĄDKOWA DE LUXE 0.5L'),
(79, 1, 220, '36', 3, 'ŻOŁĄDKOWA DE LUXE 0.7L'),
(80, 1, 120, '55', 3, 'ŻOŁĄDKOWA DE LUXE 1L'),
(81, 1, 90, '40', 1, 'CZARNY BOCIAN 0.5L'),
(82, 1, 150, '60', 1, 'AMUNDSEN VODKA 0.7L'),
(83, 1, 250, '40', 1, 'ABSOLUT VODKA 0.5L'),
(84, 1, 500, '29', 1, 'WYBOROWA WÓDKA 0.5L'),
(85, 1, 340, '42', 1, 'WYBOROWA WÓDKA 0.7L'),
(86, 1, 400, '26', 3, 'ŻOŁĄDKOWA DE LUXE 0.5L'),
(87, 1, 220, '36', 3, 'ŻOŁĄDKOWA DE LUXE 0.7L');

INSERT INTO `Zamowienie` (`id`, `id_produktu`, `id_klienta`, `id_pracownika`, `ilosc`, `cena`, `data`, `status`) VALUES
(1, 3, 1, 2, 20, '150','12-02-20', 'w trakcie'),
(2, 2, 4, 2, 20, '150', '22-03-20', 'w trakcie'),
(3, 5, 2, 2, 20, '150', '19-04-20', 'dostarczone');
