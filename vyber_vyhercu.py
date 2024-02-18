import random  # Importuje modul pro generování náhodných čísel.


class VyberVyhercu:
    def __init__(self, pocet_ucastniku):
        # Konstruktor třídy, vytváří seznam účastníků na základě počtu účastníků.
        # Každý účastník je označen jako "Účastník X", kde X je jeho pořadové číslo.
        self.ucastnici = ["Účastník " + str(i) for i in range(1, pocet_ucastniku + 1)]

    def vyber_nahodne_vyherce(self, pocet_vyhercu):
        # Vybere náhodně zadaný počet účastníků (vyherní ID) bez opakování z listu účastníků.
        # Používá modul random a jeho funkci sample pro tento účel.
        return random.sample(self.ucastnici, pocet_vyhercu)

    def simulace_vic_kol(self, pocet_kol, pocet_vyhercu_na_kolo):
        # Metoda pro simulaci více kol losování. Pro každé kolo vybere náhodné výherce.
        # Výsledky každého kola jsou zaznamenány v dvourozměrném seznamu (matice).
        vysledky = [[0 for _ in range(len(self.ucastnici))] for _ in range(pocet_kol)]  # Vytváří matici výher.
        for kolo in range(pocet_kol):  # Iteruje přes počet kol.
            vyherni = self.vyber_nahodne_vyherce(pocet_vyhercu_na_kolo)  # Vybere výherce pro aktuální kolo.
            for vyherce in vyherni:  # Iteruje přes seznam vybraných výherců.
                index = self.ucastnici.index(vyherce)  # Najde index vyherce v seznamu účastníků.
                vysledky[kolo][index] = 1  # Označí vyherce v matici výher pro dané kolo.
        return vysledky  # Vrátí matici výher po dokončení simulace.
