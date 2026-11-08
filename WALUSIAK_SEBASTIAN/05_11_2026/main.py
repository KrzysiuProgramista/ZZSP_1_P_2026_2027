from character import create_character, calculate_stats, level_up, BASE_STATS
from inventory import add_item, remove_item

def show_character_sheet(character):
    """Wyświetla pełne podsumowanie postaci w konsoli."""
    if not character:
        print("\n[!] Najpierw musisz stworzyć postać!")
        return

    hp, attack, defense = calculate_stats(character)

    print("\n--- KARTA POSTACI ---")
    print(f"Imię: {character['name']}")
    print(f"Klasa: {character['class']}")
    print(f"Poziom: {character['level']}")
    print(f"HP: {hp} | Atak: {attack} | Obrona: {defense}")
    
    print("Ekwipunek:")
    if not character["inventory"]:
        print("  (pusty)")
    else:
        for item in character["inventory"]:
            print(f"  - {item['name']} (typ: {item['type']}, bonus: {item['bonus']})")
    print("----------------------")

def main():
    active_hero = None

    while True:
        print("\n=== RPG CHARACTER MANAGER ===")
        print("1. Stwórz postać")
        print("2. Dodaj przedmiot do ekwipunku")
        print("3. Usuń przedmiot z ekwipunku")
        print("4. Awansuj postać (Level Up)")
        print("5. Pokaż kartę postaci")
        print("0. Wyjdź")
        
        choice = input("Wybierz opcję: ").strip()

        if choice == "1":
            name = input("Podaj imię bohatera: ").strip()
            while not name:
                print("Imię nie może być puste!")
                name = input("Podaj imię bohatera: ").strip()

            print("Dostępne klasy: Warrior, Mage, Ranger")
            cls = input("Wybierz klasę (domyślnie Warrior): ").strip().capitalize()
            if cls not in BASE_STATS:
                cls = "Warrior"

            active_hero = create_character(name=name, character_class=cls)
            print(f"\n[+] Stworzono bohatera: {active_hero['name']} ({active_hero['class']})!")

        elif choice == "2":
            if not active_hero:
                print("\n[!] Najpierw stwórz postać!")
                continue
            item_name = input("Nazwa przedmiotu: ").strip()
            item_type = input("Typ przedmiotu (weapon/consumable/misc): ").strip().lower()
            
            try:
                bonus = int(input("Bonus do ataku (np. 3, dla mikstur/reszt: 0): "))
            except ValueError:
                bonus = 0

            add_item(active_hero, item_name, item_type, bonus)
            print(f"\n[+] Dodano przedmiot: {item_name}")

        elif choice == "3":
            if not active_hero:
                print("\n[!] Najpierw stwórz postać!")
                continue
            item_name = input("Nazwa przedmiotu do usunięcia: ").strip()
            if remove_item(active_hero, item_name):
                print(f"\n[-] Usunięto przedmiot: {item_name}")
            else:
                print(f"\n[!] Nie znaleziono przedmiotu o nazwie: {item_name}")

        elif choice == "4":
            if not active_hero:
                print("\n[!] Najpierw stwórz postać!")
                continue
            level_up(active_hero)
            print(f"\n[^] {active_hero['name']} awansował na poziom {active_hero['level']}!")

        elif choice == "5":
            show_character_sheet(active_hero)

        elif choice == "0":
            print("\nSiema! Do zobaczenia w dungeonie")
            break

        else:
            print("\n[!] Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()
