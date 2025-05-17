class ketab:
    
    def __init__(self,nam_ketab,shomare_virayesh,nobat_chap,nam_nevisande,shomare_serial,vaziat):
        self.nam_ketab = nam_ketab
        self.shomare_virayesh = shomare_virayesh
        self.nobat_chap = nobat_chap
        self.nam_nevisande = nam_nevisande
        self.shomare_serial = shomare_serial
        self.vaziat = vaziat
        self.nam_girande = []
        self.tarikhche_amanat = []

    def gharz(self,nam_gharz_girande,tarikh_amanat):
        if self.vaziat == 'موجود':
            self.vaziat = 'امانت'
            self.nam_girande.append(nam_gharz_girande)
            self.tarikhche_amanat.append({
                'nam gharz girande': nam_gharz_girande,
                'tarikh_amanat': tarikh_amanat,
                'tarikh bargasht' : None})
        else:
            print('این کتاب امانت داده شده')
    
    def pas_dadan(self,nam_gharz_girande,tarikh_bargasht):
        for i in self.tarikhche_amanat:
            if i['nam gharz girande'] == nam_gharz_girande:
                i['tarikh bargasht'] = tarikh_bargasht
                self.vaziat = 'موجود'
                break
                
k1 = ketab("Python Basics", 1, 2, "Alireza", 12345, "موجود")
k1.gharz('reza','1404/1/1')
k1.pas_dadan('reza','1404/1/15')

print(k1.tarikhche_amanat)