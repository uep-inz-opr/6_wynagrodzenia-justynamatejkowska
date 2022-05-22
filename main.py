class Pracownik:
  suma=0
  def __init__(self,imie,brutto):
    self.imie=imie
    self.brutto=int(brutto)

  def wynagrodzenienetto(self):
    if self.brutto > 1599:
      #składki pracownika
      e1=0.0976 #składka emerytalna
      r=0.015 #składka rentowa
      ch=0.0245 #składka chorobowa
      zd=0.09 #cała składka zdrowotna
      z=0.0775 #zdrowotna do odliczenia
      pd=0.18 #zaliczka na podatek
        

      skl_spol=round(round(self.brutto*e1,2)+round(self.brutto*r,2)+round(self.brutto*ch,2),2) #suma składek społecznych
      podst_zdrow=round(self.brutto-skl_spol,2) #podstawa zdrowotnego
      skl_zdr=round(podst_zdrow*zd,2) #cała składka zdrowotna
      dop=round(podst_zdrow*z,2) #zdrowotna do odliczenia
      podst_zp=round(self.brutto-111.25-skl_spol,0) #podstawa ddo obliczenia podatku
      zpdpo=round((podst_zp*0.18)-46.33,2) #składka na podatek pomniejszona o kup
      zpddp=round(zpdpo-dop,0) #zaliczka na podatek pomniejszona o zdrowotna do odliczenia
      w=round(self.brutto-skl_spol-skl_zdr-zpddp,2) #wynagrodzenie netto

      netto='%.2f' %w #zokrąglenie wyn

      sp=round(self.brutto*0.0976,2)+round(self.brutto*0.065,2)+round(self.brutto*0.0193,2)+round(self.brutto*0.0245,2)+round(self.brutto*0.001,2) #narzut na wynagrodzenia
      lkp=round(self.brutto+sp,2) #wyn brutto + narzut
      skl_prac='%.2f' %sp 
      kosztypracodawcy='%.2f' %lkp
      
      self.suma=self.suma+lkp
      print(self.imie,netto,skl_prac,kosztypracodawcy)
    else:
      print(self.imie,0)

liczba_pracownikow=int(input())
k=[]
for i in range(liczba_pracownikow): #input
  pracownik=input().split()
  k.append(pracownik)
  suma_kosztów=0
for j in k:
    liczba=Pracownik(j[0],int(j[1])) 
    liczba.wynagrodzenienetto()
    suma_kosztów=(suma_kosztów+liczba.suma)
    sko='%.2f' %suma_kosztów

print(sko)

