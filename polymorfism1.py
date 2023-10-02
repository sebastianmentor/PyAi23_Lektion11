class Djur:
    def __init__(self, art) -> None:
        self._art = art

    def läte(self):
        raise NotImplementedError('Alla djur måste ha ett läte!')
    
class Hund(Djur):
    def __init__(self,ras) -> None:
        super().__init__('Hund')
        self._ras = ras

    def läte(self):
        print('Hunden Skäller!')

class Anka(Djur):
    def __init__(self,ras ) -> None:
        super().__init__('Anka')
        self._ras = ras

    def läte(self):
        print('Ankan kvackar!')


labrador = Hund('Labrador')
anka = Anka('Svensk blå anka')

def hur_låter_djuret(djur:Djur):
    djur.läte()

for djur in [labrador, anka]:
    hur_låter_djuret(djur)