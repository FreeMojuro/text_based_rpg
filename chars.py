class Karakter:
    def __init__(self, isim, hp, attack, mana):
        self.isim = isim
        self.max_hp = hp
        self.base_hp = hp
        self.base_attack = attack
        self.base_mana = mana
        self.passive_used = False
        self.special_used = False
        self.gold = 0
        self.potions = 0

    def passive_skill(self):
        pass

    def __str__(self):
        return f"[{self.isim}] Can: {self.base_hp}/{self.max_hp} | Atak: {self.base_attack} | Mana: {self.base_mana}"


class Human(Karakter):
    def __init__(self, isim):
        super().__init__(isim, hp=200, attack=10, mana=100)

    def passive_skill(self):
        if not self.passive_used and self.base_hp <= 40:
            self.base_attack = int(self.base_attack * 1.5)
            self.passive_used = True
            print(f"\n⚡ {self.isim} pasif yeteneği (Ölümcül Öfke) tetiklendi! Saldırı gücü arttı!")


class Knight(Human):
    def __init__(self, isim):
        super().__init__(isim)
        self.max_hp += 40
        self.base_hp = self.max_hp
        self.base_attack += 10
        self.base_mana -= 50

    def special_skill(self, enemy):
        if self.special_used:
            print(" Bu yetenek savaşta zaten kullanıldı!")
            return False
        if self.base_hp <= 20:
            print(" Yeteneği kullanmak için yeterli canın yok!")
            return False
        
        self.base_hp -= 20
        enemy.base_hp -= 50
        self.special_used = True
        print(f"\n {self.isim} 'Kutsal Darbe' kullandı! Kendinden 20 HP feda ederek düşmana 50 hasar verdi!")
        return True


class Dwarf(Human):
    def __init__(self, isim):
        super().__init__(isim)
        self.max_hp += 150
        self.base_hp = self.max_hp
        self.base_mana -= 60

    def special_skill(self, enemy=None):
        if self.special_used:
            print(" Bu yetenek zaten kullanıldı!")
            return False
        
        self.base_hp = min(self.max_hp, self.base_hp + 50)
        self.special_used = True
        print(f"\n {self.isim} 'Taş Deri' kullandı ve 50 HP iyileşti!")
        return True


# --- ELF SOYLARI ---
class Elf(Karakter):
    def __init__(self, isim):
        super().__init__(isim, hp=150, attack=15, mana=200)

    def passive_skill(self):
        if not self.passive_used and self.base_hp <= 40:
            self.base_attack = int(self.base_attack * 1.2)
            self.passive_used = True
            print(f"\n {self.isim} pasif yeteneği (Doğanın Çevikliği) tetiklendi!")

    def special_skill(self, enemy):
        if self.special_used:
            print(" Bu yetenek zaten kullanıldı!")
            return False
        if self.base_mana >= 100:
            self.base_mana -= 100
            enemy.base_hp -= 100
            self.special_used = True
            print(f"\n {self.isim} 'Ay Işığı Patlaması' kullandı! Düşmana 100 hasar verdi!")
            return True
        else:
            print("Yetersiz mana!")
            return False


class DarkElf(Elf):
    def __init__(self, isim):
        super().__init__(isim)
        self.max_hp += 125
        self.base_hp = self.max_hp
        self.base_attack += 40
        self.base_mana -= 25



class Demon(Karakter):
    def __init__(self, isim="Karanlık İblis"):
        super().__init__(isim, hp=65, attack=15, mana=100)
        self.skill_chance = 0.4

    def passive_skill(self):
        if not self.passive_used and self.base_hp <= 40:
            self.base_attack = int(self.base_attack * 2)
            self.passive_used = True
            print(f"\n {self.isim} pasif yeteneği (Cehennem Öfkesi) tetiklendi! Atak gücü ikiye katlandı!")

    def special_skill(self, enemy):
        if self.base_mana >= 75:
            self.base_mana -= 75
            enemy.base_hp -= 30
            print(f"\n {self.isim} 'Karanlık Ateş' kullandı ve {enemy.isim}'e 30 hasar verdi!")
            return True
        return False

class Boss(Demon):
    def __init__(self,isim = "Boss"):
        super().__init__(isim)
        self.max_hp = 350
        self.base_hp = 350
        self.base_attack = 45
        self.base_mana = 200
        self.skill_chance = 0.4
        
    def passive_skill(self):
        if not self.passive_used and self.base_hp <= 125:
            self.base_attack = int(self.base_attack * 1.5)
            self.passive_used = True
            print(f"\n {self.isim} pasif yeteneği (Cehennem Öfkesi) tetiklendi! Atak gücü %50 arttı!")
    
    def special_skill(self, enemy):
        if self.base_mana >= 75:
            self.base_mana -= 75
            enemy.base_hp -= 70
            print(f"\n {self.isim} 'Karanlık Ateş' kullandı ve {enemy.isim}'e 70 hasar verdi!")
            return True
        return False
        