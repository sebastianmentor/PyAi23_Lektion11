class NyStudent:
    klass_variabel = 'Tillhör klassen och inte instanser'
    grundkrav = 'Matte3'

    @classmethod
    def validera_student(cls, betyg):
        return betyg == cls.grundkrav

    def __init__(self,namn, betyg) -> None:
        if NyStudent.validera_student(betyg):
            self.namn = namn
            self._avklarade_poäng = 0
            print(self.grundkrav)
        else:
            raise ValueError

class PythonUtvecklare:
    def __init__(self, namn) -> None:
        self.namn = namn
        self.kaffe = 1

ny_student = NyStudent('Sebastian','Matte3')
print(ny_student.namn)
print(NyStudent.klass_variabel)