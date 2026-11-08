import random
from character import calculate_stats

def run_battle(character):
#Simulate a turn-based combat against a random monster
    if not character:
        print("\n[!] No active character to fight with!")
        return

    char_hp, char_atk, char_def = calculate_stats(character)
    
    monster_names = ["Goblin", "Orc", "Skeleton Archer", "Dark Slime", "Cave Troll"]
    monster_name = random.choice(monster_names)
    
    monster_hp = random.randint(40, 70) + (character["level"] * 5)
    monster_atk = random.randint(8, 14) + (character["level"] * 2)
    monster_def = random.randint(2, 6) + character["level"]
    
    print("\n=== BATTLE START ===")
    print(f"A wild {monster_name} appears!")
    print(f"Monster Stats -> HP: {monster_hp}, ATK: {monster_atk}, DEF: {monster_def}")
    print(f"Your Stats    -> HP: {char_hp}, ATK: {char_atk}, DEF: {char_def}")
    print("="*20)
    
    turn = 1
    while char_hp > 0 and monster_hp > 0:
        print(f"\n--- Turn {turn} ---")
        input("Press Enter to roll dice and attack... ")
        
        hero_roll = random.randint(1, 6)
        hero_damage = max(1, (char_atk + hero_roll) - monster_def)
        monster_hp -= hero_damage
        print(f"[!] You rolled a {hero_roll}! You hit the {monster_name} for {hero_damage} damage.")
        
        if monster_hp <= 0:
            print(f"\n[+] VICTORY! You defeated the {monster_name}!")
            break
            
        monster_roll = random.randint(1, 6)
        monster_damage = max(1, (monster_atk + monster_roll) - char_def)
        char_hp -= monster_damage
        print(f"[-] The {monster_name} rolled a {monster_roll} and hits you for {monster_damage} damage. (Your HP: {max(0, char_hp)})")
        
        if char_hp <= 0:
            print(f"\n[-] DEFEAT! You were defeated by the {monster_name}...")
            
        turn += 1
    print("=== BATTLE END ===\n")
