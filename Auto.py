from abc import ABC, abstractmethod

class Auto(ABC):
    _autok = []
    
    def __init__(self, rendszam, marka, tipus, evjarat, ar):
        self.rendszam = rendszam
        self.marka = marka
        self.tipus = tipus
        self.evjarat = evjarat
        self.ar = ar
        Auto._autok.append(self)
    
    @abstractmethod
    def szamitsd_ki_napi_dij(self):
        pass
    
    @abstractmethod
    def get_auto_info(self):
        pass
    
    def __str__(self):
        return f"{self.marka} {self.tipus} ({self.evjarat}) - Rendszám: {self.rendszam}"
    
    @classmethod
    def autok_adatai(cls):
        return cls._autok