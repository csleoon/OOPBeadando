from Auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam, marka, tipus, evjarat, ar, teherbiras, plato_hossz):
        super().__init__(rendszam, marka, tipus, evjarat, ar)
        self.teherbiras = teherbiras  # kg-ban
        self.plato_hossz = plato_hossz  # méterben
    
    def szamitsd_ki_napi_dij(self):
        return (self.ar * 0.003) + (((self.teherbiras - 1) // 1000 + 1) * 5000)
    
    def get_auto_info(self):
        return {
            'rendszam': self.rendszam,
            'marka': self.marka,
            'tipus': self.tipus,
            'evjarat': self.evjarat,
            'ar': self.ar,
            'teherbiras': self.teherbiras,
            'plato_hossz': self.plato_hossz,
            'napi_dij': self.szamitsd_ki_napi_dij()
        }
    
    def __str__(self):
        return f"{super().__str__()} - Teherbírás: {self.teherbiras}kg, Plató: {self.plato_hossz}m"