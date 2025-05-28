from Auto import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam, marka, tipus, evjarat, ar, ulesek_szama):
        super().__init__(rendszam, marka, tipus, evjarat, ar)
        self.ulesek_szama = ulesek_szama
    
    def szamitsd_ki_napi_dij(self):
        """
        Személyautók esetében a napi díj az ár 0.5%-a + ülések száma * 1000 Ft
        """
        return (self.ar * 0.005) + (self.ulesek_szama * 1000)
    
    def get_auto_info(self):
        """
        Visszaadja a személyautó részletes információit
        """
        return {
            'rendszam': self.rendszam,
            'marka': self.marka,
            'tipus': self.tipus,
            'evjarat': self.evjarat,
            'ar': self.ar,
            'ulesek_szama': self.ulesek_szama,
            'napi_dij': self.szamitsd_ki_napi_dij()
        }