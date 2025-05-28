from Auto import Auto
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto
from Berles import Berles


class Berloprogram:
    def __init__(self):
        self.berlesek = []
        Szemelyauto("IUH261", "Volkswagen", "Passat", 2020, 8500000, 5)
        Szemelyauto("K400", "BMW", "530i", 2021, 12500000, 5)
        Szemelyauto("GSM579", "Audi", "A6", 2019, 9800000, 5)
        
        Teherauto("THR001", "Ford", "Transit", 2021, 12000000, 1200, 3.5)
        Teherauto("THR002", "Mercedes", "Sprinter", 2022, 15000000, 1500, 4.0)

    def berelheto_autok_listazasa(self):
        print("Jelenleg berelheto autoink:")
        foglalt_rendszamok = []

        for berles in self.berlesek:
            foglalt_rendszam = berles[1]
            if foglalt_rendszam not in foglalt_rendszamok:
                foglalt_rendszamok.append(foglalt_rendszam)

        van_berelheto = False
        for auto in Auto.autok_adatai():
            if auto.rendszam not in foglalt_rendszamok:
                van_berelheto = True
                auto_info = auto.get_auto_info()
                print(f"\nRendszám: {auto_info['rendszam']}")
                print(f"Márka: {auto_info['marka']}")
                print(f"Típus: {auto_info['tipus']}")
                print(f"Évjárat: {auto_info['evjarat']}")
                print(f"Napi bérleti díj: {int(auto_info['napi_dij']):,} Ft")
                if isinstance(auto, Szemelyauto):
                    print(f"Ülések száma: {auto_info['ulesek_szama']}")
                elif isinstance(auto, Teherauto):
                    print(f"Teherbírás: {auto_info['teherbiras']} kg")
                    print(f"Plató hossza: {auto_info['plato_hossz']} m")
                print("-" * 40)

        if not van_berelheto:
            print("Jelenleg minden autónk foglalt!")

    def auto_berlese(self, rendszam, berlo_neve, datum):
        for auto in Auto.autok_adatai():
            if auto.rendszam == rendszam:
                self.berlesek.append([berlo_neve, rendszam, datum])
                auto_info = auto.get_auto_info()
                
                print("\n=== Sikeres foglalás részletei ===")
                print(f"Bérlő neve: {berlo_neve}")
                print(f"Foglalás dátuma: {datum}")
                print("\nAutó adatai:")
                print(f"Márka: {auto_info['marka']}")
                print(f"Típus: {auto_info['tipus']}")
                print(f"Évjárat: {auto_info['evjarat']}")
                print(f"Rendszám: {auto_info['rendszam']}")
                
                if isinstance(auto, Szemelyauto):
                    print(f"Ülések száma: {auto_info['ulesek_szama']}")
                elif isinstance(auto, Teherauto):
                    print(f"Teherbírás: {auto_info['teherbiras']} kg")
                    print(f"Plató hossza: {auto_info['plato_hossz']} m")
                
                print(f"Napi bérleti díj: {int(auto_info['napi_dij']):,} Ft")
                print("=" * 35)
                return

    def berles_lemondasa(self, rendszam, berlo_neve):
        felhasznalo_berlesei = []
        for index, berles in enumerate(self.berlesek):
            if berles[0] == berlo_neve:
                felhasznalo_berlesei.append((index, berles))

        if not felhasznalo_berlesei:
            print(f"Nem található foglalás {berlo_neve} névvel!")
            return False

        if len(felhasznalo_berlesei) == 1:
            self.berlesek.pop(felhasznalo_berlesei[0][0])
            print(f"A foglalás sikeresen törölve!")
            return True

        print(f"\n{berlo_neve} foglalásai:")
        for i, (index, berles) in enumerate(felhasznalo_berlesei, 1):
            print(f"{i}. Autó rendszáma: {berles[1]}, Dátum: {berles[2]}")

        while True:
            try:
                valasztas = int(input("\nMelyik foglalást szeretné törölni? (Írja be a számot): "))
                if 1 <= valasztas <= len(felhasznalo_berlesei):
                    torlendo_index = felhasznalo_berlesei[valasztas-1][0]
                    torolt_berles = self.berlesek.pop(torlendo_index)
                    print(f"\nA foglalás sikeresen törölve:")
                    print(f"Rendszám: {torolt_berles[1]}")
                    print(f"Dátum: {torolt_berles[2]}")
                    return True
                else:
                    print("Érvénytelen választás! Kérem, válasszon a listából!")
            except ValueError:
                print("Kérem, számot adjon meg!")

    def berles_listazasa(self):
        print("Jelenlegi foglalasok: ")
        print(self.berlesek)

    def ellenorizze_foglalast(self, rendszam, datum):
        foglalt_datumok = []
        for berles in self.berlesek:
            if berles[1] == rendszam:
                foglalt_datumok.append(berles[2])

        return datum not in foglalt_datumok

berlo_program = Berloprogram()

berlo_program.auto_berlese("IUH261", "Kovacs Bela", "2025.05.31")
berlo_program.auto_berlese("K400", "Kovacs Jozsef", "2025.06.04")
berlo_program.auto_berlese("IUH261", "Kovacs Bela", "2025.07.29")
berlo_program.auto_berlese("GSM579", "Kovacs Peter", "2025.09.22")

while True:
    print("\n--- Auto foglalási Rendszer ---")
    print("1. Auto foglalás")
    print("2. Auto berlesenek lemondása")
    print("3. Foglalhato autok listázása")
    print("4. Foglalasok listazasa")
    print("5. Kilépés")

    choice = input("Válasszon egy lehetőséget (1-5): ")

    if choice == "1":
        foglalt_rendszam = input("Adja meg a foglalando rendszamot: ")
        foglalo_neve = input("Adja meg a foglalo nevét: ")
        foglalando_datum = input("Adja meg a foglalas datumat! Csak egy napra tud foglalni.")
        autok = Auto.autok_adatai()
        rendszamok = [auto.rendszam for auto in autok]

        if foglalt_rendszam in rendszamok and berlo_program.ellenorizze_foglalast(foglalt_rendszam, foglalando_datum):
            berlo_program.auto_berlese(foglalt_rendszam, foglalo_neve, foglalando_datum)
        else:
            print("Sikertelen - A megadott rendszámú autó nem található vagy már foglalt erre a dátumra!")

    elif choice == "2":
        rendszam = input("Adja meg a rendszamot: ")
        berlo_neve = input("Adja meg a berlo nevét: ")
        berlo_program.berles_lemondasa(rendszam, berlo_neve)

    elif choice == "3":
        print("Jelenlegi foglalhato autoink: ")
        autok = Auto.autok_adatai()
        for auto in autok:
            print(auto)

    elif choice == "4":
        berlo_program.berles_listazasa()

    elif choice == "5":
        break

    else:
        print("Érvénytelen választás. Kérjük, válasszon egy lehetőséget (1-5).")