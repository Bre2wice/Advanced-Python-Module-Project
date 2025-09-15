import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    # Changed: attack deals randomized damage
    def attack(self, opponent):
        # random damage within a range (80%-120% of attack_power)
        damage = random.randint(int(self.attack_power * 0.8), int(self.attack_power * 1.2))
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Added: heal method
    def heal(self):
        heal_amount = random.randint(15, 30)  # random healing
        self.health = min(self.max_health, self.health + heal_amount)
        print(f"{self.name} heals for {heal_amount}! Current health: {self.health}/{self.max_health}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    # Added: Warrior special abilities
    def ability_one(self, opponent):
        print(f"{self.name} uses Power Strike!")
        damage = self.attack_power + 15
        opponent.health -= damage
        print(f"{self.name} deals {damage} damage with Power Strike!")

    def ability_two(self):
        print(f"{self.name} uses Battle Cry! Attack power increases by 10.")
        self.attack_power += 10

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    # Added: Mage special abilities
    def ability_one(self, opponent):
        print(f"{self.name} casts Fireball!")
        damage = self.attack_power + random.randint(10, 20)
        opponent.health -= damage
        print(f"{self.name} deals {damage} fire damage!")

    def ability_two(self):
        print(f"{self.name} uses Mana Shield! Restores 20 health.")
        self.health = min(self.max_health, self.health + 20)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)

    # Added: Archer special abilities
    def ability_one(self, opponent):
        print(f"{self.name} uses Quick Shot! Double arrow fired!")
        for _ in range(2):
            damage = random.randint(int(self.attack_power * 0.7), int(self.attack_power * 1.1))
            opponent.health -= damage
            print(f"{self.name} deals {damage} damage with Quick Shot!")

    def ability_two(self):
        print(f"{self.name} uses Evade! Next enemy attack will be dodged.")
        self.evade_next = True

# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)
        self.shield_active = False

    # Added: Paladin special abilities
    def ability_one(self, opponent):
        print(f"{self.name} uses Holy Strike!")
        damage = self.attack_power + 20
        opponent.health -= damage
        print(f"{self.name} deals {damage} holy damage!")

    def ability_two(self):
        print(f"{self.name} activates Divine Shield! Blocks the next attack.")
        self.shield_active = True

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)  # Implement Archer class
    elif class_choice == '4':
        return Paladin(name)  # Implement Paladin class
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability 1")
        print("3. Use Special Ability 2")
        print("4. Heal")
        print("5. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.ability_one(wizard)
        elif choice == '3':
            player.ability_two()
        elif choice == '4':
            player.heal()
        elif choice == '5':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            # Wizard attacks unless blocked/evaded
            if isinstance(player, Paladin) and player.shield_active:
                print(f"{player.name}'s Divine Shield blocks the attack!")
                player.shield_active = False
            elif isinstance(player, Archer) and getattr(player, "evade_next", False):
                print(f"{player.name} evades the attack!")
                player.evade_next = False
            else:
                wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated! The Evil Wizard triumphs...")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}! Victory is yours!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()