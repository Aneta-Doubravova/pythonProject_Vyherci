# Projekt Výběr Výherců

Jednoduchá aplikace pro simulaci výběru náhodných výherců z předem definovaného počtu účastníků pomocí Pythonu. Umožňuje provádět simulace více kol výběru, přičemž každé kolo může mít různé výherce.

## Instalace

1. Nainstalujte Python (pokud ještě nemáte nainstalovaný).
2. Stáhněte si zdrojové kódy z tohoto repozitáře.

## Použití

1. Spusťte aplikaci.
2. Aplikace automaticky simuluje výběr výherců podle nastavení.
3. Výsledky jednotlivých kol jsou vypsány na obrazovku.

## Funkce

- **Náhodný Výběr**: Vybere náhodné výherce z listu účastníků.
- **Simulace Kol**: Umožňuje simulovat více kol výběru, každé s možností mít odlišné výherce.
- **Flexibilní Počet Účastníků**: Počet účastníků je konfigurovatelný při inicializaci instance třídy.
- **Reprezentace Výsledků**: Výsledky jednotlivých kol jsou zaznamenány a mohou být snadno zobrazeny.


```python
from vyber_vyhercu import VyberVyhercu

# Vytvoření instance třídy VyberVyhercu pro 100 účastníků
vyber = VyberVyhercu(100)

# Simulace 5 kol výběru s 10 výherci v každém kole
matice_vyher = vyber.simulace_vic_kol(5, 10)

# Vypsání výsledků
print("Výherní ID v jednotlivých kolech:")
for kolo, vyhry in enumerate(matice_vyher, start=1):
    # Získání indexů výherců v aktuálním kole
    vyherni_indexy = [i for i, val in enumerate(vyhry) if val > 0]
    # Převedení indexů na výherní ID
    vyherni_ID = [vyber.ucastnici[index] for index in vyherni_indexy]
    # Vypsání výherních ID pro dané kolo
    print(f"Kolo {kolo}: {', '.join(vyherni_ID)}")
