class Ämne:
    def __init__(self, ämne) -> None:
        self._ämne = ämne

    def __str__(self) -> str:
        return self._ämne

class Betyg:

    lista_med_giltliga_betyg = ['A','B','C','D','E','F']

    @classmethod
    def kontrollera_giltligt_betyg(cls,betyg):
        return betyg in cls.lista_med_giltliga_betyg
    
    def __init__(self, ämne, betyg) -> None:
        if not Betyg.kontrollera_giltligt_betyg(betyg):
            raise ValueError
        
        if not isinstance(ämne,Ämne):
            raise ValueError
        
        self._ämne = ämne
        self._betyg = betyg

    def __str__(self) -> str:
        return f'{self._ämne} med betyg {self._betyg}'
        

class Skola:
    def __init__(self,namn) -> None:
        self.namn = namn

class Student:
    def __init__(self, skola) -> None:
        self.skola = skola
        self.lista_med_betyg = []

    def sätt_betyg(self, betyg):
        if isinstance(betyg,Betyg):
            self.lista_med_betyg.append(betyg)
    
    def print_betyg(self):
        for betyg in self.lista_med_betyg:
            print(betyg)

skola = Skola('Teknikhögskolan')

kalle = Student(skola)

programmering = Ämne('Programmering')
matteA = Ämne('MatteA')

kalle.sätt_betyg(Betyg(programmering,'F'))
kalle.sätt_betyg(Betyg(matteA,'C'))

kalle.print_betyg()