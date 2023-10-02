class Djur:
    def __init__(self, namn):
        self.namn = namn
    
    def tala(self):
        raise NotImplementedError("Subklasser måste implementera denna metod")

class Hund(Djur):
    def tala(self):
        return f"{self.namn} säger vov!"

# Skapa ett Hund-objekt
my_dog = Hund("Buddy")

# Anropa metoden tala
print(my_dog.tala())  # Output: Buddy säger vov!



class Katt(Djur):
    def tala(self):
        return f"{self.namn} säger mjau!"

    def spinna(self):
        return f"{self.namn} spinner!"

# Skapa ett Katt-objekt
my_cat = Katt("Whiskers")

# Anropa de överlagrade metoderna
print(my_cat.tala())  # Output: Whiskers säger mjau!
print(my_cat.spinna())  # Output: Whiskers spinner!


class Labrador(Hund):
    def __init__(self, namn, färg):
        super().__init__(namn)
        self.färg = färg

    def hälsa(self):
        return f"Jag är en {self.färg} Labrador och jag heter {self.namn}!"

# Skapa ett Labrador-objekt
my_lab = Labrador("Max", "gul")

# Anropa metoden hälsa
print(my_lab.hälsa())  # Output: Jag är en gul Labrador och jag heter Max!


def låt_djuret_tala(djur):
    return djur.tala()

# Anropa funktionen med olika djur
print(låt_djuret_tala(my_dog))  # Output: Buddy säger vov!
print(låt_djuret_tala(my_cat))  # Output: Whiskers säger mjau!
