class Person:
    def __init__(self, namn, födelsedatum) -> None:
        self.namn = namn
        self._födelsedatum = födelsedatum

    def get_födelsedatum(self):
        return self._födelsedatum
    
class Barn(Person):
    def __init__(self, namn, födelsedatum, ålder) -> None:
        super().__init__(namn, födelsedatum)
        self.ålder = ålder

    def leka(self):
        pass

class Vuxen(Person):
    def __init__(self, namn, födelsedatum, vuxen_ålder) -> None:
        super().__init__(namn, födelsedatum)
        self.ålder = vuxen_ålder
        
    def arbeta(self):
        pass

class Förälder(Vuxen):
    def __init__(self, namn, födelsedatum, vuxen_ålder, lista_med_barn) -> None:
        super().__init__(namn, födelsedatum, vuxen_ålder)
        self._egna_barn = lista_med_barn

    def print_barn(self):
        for barn in self._egna_barn:
            print(barn)

p = Person('Sebastian', '19890704')
print(p.namn)

emil = Barn('Emil',19010503, 8) 
ida = Barn('Ida', 19030112, 4)


alma = Förälder('Alma', 18890315, 33, [emil, ida])
anton = Förälder('Anton', 18830312,50,[emil,ida])

alma.print_barn()
anton.print_barn()