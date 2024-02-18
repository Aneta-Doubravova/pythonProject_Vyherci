from vyber_vyhercu import VyberVyhercu  # Import třídy VyberVyhercu

# Vytvoření instance třídy se 100 účastníky.
vyber = VyberVyhercu(100)

# Simulace 5 kol s 10 výherci v každém kole.
matice_vyher = vyber.simulace_vic_kol(5, 10)

# Vypsání jmen výherců v jednotlivých kolech.
print("Jména výherců v jednotlivých kolech:")
for kolo in range(len(matice_vyher)):  # Procházíme každé kolo.
    vyherni_indexy = [i for i, val in enumerate(matice_vyher[kolo]) if val > 0]  # Najdeme indexy výherců v tomto kole.
    vyherni_jmena = [vyber.ucastnici[index] for index in vyherni_indexy]  # Převedeme indexy na jména.
    print(f"Kolo {kolo + 1}: {', '.join(vyherni_jmena)}")  # Vypíšeme jména výherců.

# Gratulace výhercům.
print("Gratulujeme všem výhercům soutěže!")
