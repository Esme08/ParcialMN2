from PySide6 import *
from PySide6.QtWidgets import *
import sys
from form import *

import sympy
from sympy import *
##holi

a=[]
b=[]
c=[]
d=[]
resultado=[]

class Operaciones (QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.bttn_calcularsuma.clicked.connect(self.Suma)
        self.ui.bttn_calcularresta.clicked.connect(self.Resta)
        self.ui.bttn_calcularmulti.clicked.connect(self.Multiplicacion)
        self.ui.bttn_trasponer.clicked.connect(self.traspuesta)
        self.ui.bttn_determinante.clicked.connect(self.determinante)
        self.ui.bttn_adjunta.clicked.connect(self.adjunta)
        self.ui.bttn_invertir.clicked.connect(self.inversa)
        self.ui.bttn_invertir_2.clicked.connect(self.matrizSE)
        self.ui.bttn_invertir_3.clicked.connect(self.cramerSE)
    
    def Suma(self):
        for i in range(3):
            for j in range(3):
                a.append([0]*3)
                b.append([0]*3)
                resultado.append([0]*3)

        a[0][0]=float(self.ui.txt_sa00.text())
        a[0][1]=float(self.ui.txt_sa01.text())
        a[0][2]=float(self.ui.txt_sa02.text())
        a[1][0]=float(self.ui.txt_sa10.text())
        a[1][1]=float(self.ui.txt_sa11.text())
        a[1][2]=float(self.ui.txt_sa12.text())
        a[2][0]=float(self.ui.txt_sa20.text())
        a[2][1]=float(self.ui.txt_sa21.text())
        a[2][2]=float(self.ui.txt_sa22.text())
        
        b[0][0]=float(self.ui.txt_sb00.text())
        b[0][1]=float(self.ui.txt_sb01.text())
        b[0][2]=float(self.ui.txt_sb02.text())
        b[1][0]=float(self.ui.txt_sb10.text())
        b[1][1]=float(self.ui.txt_sb11.text())
        b[1][2]=float(self.ui.txt_sb12.text())
        b[2][0]=float(self.ui.txt_sb20.text())
        b[2][1]=float(self.ui.txt_sb21.text())
        b[2][2]=float(self.ui.txt_sb22.text())

        resultado[0][0]=a[0][0]+b[0][0]
        resultado[0][1]=a[0][1]+b[0][1]
        resultado[0][2]=a[0][2]+b[0][2]
        resultado[1][0]=a[1][0]+b[1][0]
        resultado[1][1]=a[1][1]+b[1][1]
        resultado[1][2]=a[1][2]+b[1][2]
        resultado[2][0]=a[2][0]+b[2][0]
        resultado[2][1]=a[2][1]+b[2][1]
        resultado[2][2]=a[2][2]+b[2][2]

        self.ui.txt_sR00.setText(str(resultado[0][0]))
        self.ui.txt_sR01.setText(str(resultado[0][1]))
        self.ui.txt_sR02.setText(str(resultado[0][2]))
        self.ui.txt_sR10.setText(str(resultado[1][0]))
        self.ui.txt_sR11.setText(str(resultado[1][1]))
        self.ui.txt_sR12.setText(str(resultado[1][2]))
        self.ui.txt_sR20.setText(str(resultado[2][0]))
        self.ui.txt_sR21.setText(str(resultado[2][1]))
        self.ui.txt_sR22.setText(str(resultado[2][2]))
    
    def Resta(self):

        for i in range(3):
            for j in range(3):
                a.append([0]*3)
                b.append([0]*3)
                resultado.append([0]*3)

        a[0][0]=float(self.ui.txt_ra00.text())
        a[0][1]=float(self.ui.txt_ra01.text())
        a[0][2]=float(self.ui.txt_ra02.text())
        a[1][0]=float(self.ui.txt_ra10.text())
        a[1][1]=float(self.ui.txt_ra11.text())
        a[1][2]=float(self.ui.txt_ra12.text())
        a[2][0]=float(self.ui.txt_ra20.text())
        a[2][1]=float(self.ui.txt_ra21.text())
        a[2][2]=float(self.ui.txt_ra22.text())

        b[0][0]=float(self.ui.txt_rb00.text())*-1
        b[0][1]=float(self.ui.txt_rb01.text())*-1
        b[0][2]=float(self.ui.txt_rb02.text())*-1
        b[1][0]=float(self.ui.txt_rb10.text())*-1
        b[1][1]=float(self.ui.txt_rb11.text())*-1
        b[1][2]=float(self.ui.txt_rb12.text())*-1
        b[2][0]=float(self.ui.txt_rb20.text())*-1
        b[2][1]=float(self.ui.txt_rb21.text())*-1
        b[2][2]=float(self.ui.txt_rb22.text())*-1

        resultado[0][0]=a[0][0]+b[0][0]
        resultado[0][1]=a[0][1]+b[0][1]
        resultado[0][2]=a[0][2]+b[0][2]
        resultado[1][0]=a[1][0]+b[1][0]
        resultado[1][1]=a[1][1]+b[1][1]
        resultado[1][2]=a[1][2]+b[1][2]
        resultado[2][0]=a[2][0]+b[2][0]
        resultado[2][1]=a[2][1]+b[2][1]
        resultado[2][2]=a[2][2]+b[2][2]

        self.ui.txt_rR00.setText(str(resultado[0][0]))
        self.ui.txt_rR01.setText(str(resultado[0][1]))
        self.ui.txt_rR02.setText(str(resultado[0][2]))
        self.ui.txt_rR10.setText(str(resultado[1][0]))
        self.ui.txt_rR11.setText(str(resultado[1][1]))
        self.ui.txt_rR12.setText(str(resultado[1][2]))
        self.ui.txt_rR20.setText(str(resultado[2][0]))
        self.ui.txt_rR21.setText(str(resultado[2][1]))
        self.ui.txt_rR22.setText(str(resultado[2][2]))

    def Multiplicacion(self):

        for i in range(3):
            for j in range(3):
                a.append([0]*3)
                b.append([0]*3)
                resultado.append([0]*3)
        
        a[0][0]=float(self.ui.txt_ma00.text())
        a[0][1]=float(self.ui.txt_ma01.text())
        a[0][2]=float(self.ui.txt_ma02.text())
        a[1][0]=float(self.ui.txt_ma10.text())
        a[1][1]=float(self.ui.txt_ma11.text())
        a[1][2]=float(self.ui.txt_ma12.text())
        a[2][0]=float(self.ui.txt_ma20.text())
        a[2][1]=float(self.ui.txt_ma21.text())
        a[2][2]=float(self.ui.txt_ma22.text())

        b[0][0]=float(self.ui.txt_mb00.text())
        b[0][1]=float(self.ui.txt_mb01.text())
        b[0][2]=float(self.ui.txt_mb02.text())
        b[1][0]=float(self.ui.txt_mb10.text())
        b[1][1]=float(self.ui.txt_mb11.text())
        b[1][2]=float(self.ui.txt_mb12.text())
        b[2][0]=float(self.ui.txt_mb20.text())
        b[2][1]=float(self.ui.txt_mb21.text())
        b[2][2]=float(self.ui.txt_mb22.text())

        resultado[0][0]=a[0][0]*b[0][0]+a[0][1]*b[1][0]+a[0][2]*b[2][0]
        resultado[0][1]=a[0][0]*b[0][1]+a[0][1]*b[1][1]+a[0][2]*b[2][1]
        resultado[0][2]=a[0][0]*b[0][2]+a[0][1]*b[1][2]+a[0][2]*b[2][2]
        resultado[1][0]=a[1][0]*b[0][0]+a[1][1]*b[1][0]+a[1][2]*b[2][0]
        resultado[1][1]=a[1][0]*b[0][1]+a[1][1]*b[1][1]+a[1][2]*b[2][1]
        resultado[1][2]=a[1][0]*b[0][2]+a[1][1]*b[1][2]+a[1][2]*b[2][2]
        resultado[2][0]=a[2][0]*b[0][0]+a[2][1]*b[1][0]+a[2][2]*b[2][0]
        resultado[2][1]=a[2][0]*b[0][1]+a[2][1]*b[1][1]+a[2][2]*b[2][1]
        resultado[2][2]=a[2][0]*b[0][2]+a[2][1]*b[1][2]+a[2][2]*b[2][2]

        self.ui.txt_mR00.setText(str(resultado[0][0]))
        self.ui.txt_mR01.setText(str(resultado[0][1]))
        self.ui.txt_mR02.setText(str(resultado[0][2]))
        self.ui.txt_mR10.setText(str(resultado[1][0]))
        self.ui.txt_mR11.setText(str(resultado[1][1]))
        self.ui.txt_mR12.setText(str(resultado[1][2]))
        self.ui.txt_mR20.setText(str(resultado[2][0]))
        self.ui.txt_mR21.setText(str(resultado[2][1]))
        self.ui.txt_mR22.setText(str(resultado[2][2]))
        
    def traspuesta(self):
        for i in range(3):
            for j in range(3):
                a.append([0]*3)
                resultado.append([0]*3)
        
        a[0][0] = float(self.ui.txt_tras00.text())
        a[0][1] = float(self.ui.txt_tras01.text())
        a[0][2] = float(self.ui.txt_tras02.text())
        a[1][0] = float(self.ui.txt_tras10.text())
        a[1][1] = float(self.ui.txt_tras11.text())
        a[1][2] = float(self.ui.txt_tras12.text())
        a[2][0] = float(self.ui.txt_tras20.text())
        a[2][1] = float(self.ui.txt_tras21.text())
        a[2][2] = float(self.ui.txt_tras22.text())

        for i in range(3):
            for j in range(3):
                resultado[i][j] = a[j][i]

        self.ui.txt_tR00.setText(str(resultado[0][0]))
        self.ui.txt_tR01.setText(str(resultado[0][1]))
        self.ui.txt_tR02.setText(str(resultado[0][2]))
        self.ui.txt_tR10.setText(str(resultado[1][0]))
        self.ui.txt_tR11.setText(str(resultado[1][1]))
        self.ui.txt_tR12.setText(str(resultado[1][2]))
        self.ui.txt_tR20.setText(str(resultado[2][0]))
        self.ui.ttxt_tR21.setText(str(resultado[2][1]))
        self.ui.txt_tR22.setText(str(resultado[2][2]))

    def determinante(self):
        for i in range(3):
            for j in range(3):
                a.append([0]*3)

        a[0][0] = float(self.ui.txt_deter00.text())
        a[0][1] = float(self.ui.txt_deter02.text())
        a[0][2] = float(self.ui.txt_deter03.text())
        a[1][0] = float(self.ui.txt_deter10.text())
        a[1][1] = float(self.ui.txt_deter11.text())
        a[1][2] = float(self.ui.txt_deter12.text())
        a[2][0] = float(self.ui.txt_deter20.text())
        a[2][1] = float(self.ui.txt_deter21.text())
        a[2][2] = float(self.ui.txt_deter22.text())   

        dp = a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1]
        ds = a[2][0]*a[1][1]*a[0][2] + a[2][1]*a[1][2]*a[0][0] + a[2][2]*a[1][0]*a[0][1]

        deter= dp - ds

        self.ui.txt_resultadodeter.setText(str(deter))

    def adjunta(self):
        for i in range(3):
            for j in range(3):
                a.append([0]*3)
                b.append([0]*3)
                resultado.append([0]*3)

        a[0][0] = float(self.ui.txt_adj00.text())
        a[0][1] = float(self.ui.txt_adj01.text())
        a[0][2] = float(self.ui.txt_adj02.text())
        a[1][0] = float(self.ui.txt_adj10.text())
        a[1][1] = float(self.ui.txt_adj11.text())
        a[1][2] = float(self.ui.txt_adj12.text())
        a[2][0] = float(self.ui.txt_adj20.text())
        a[2][1] = float(self.ui.txt_adj21.text())
        a[2][2] = float(self.ui.txt_adj22.text()) 

        b[0][0] = a[1][1]*a[2][2]-a[1][2]*a[2][1]
        b[0][1] = -(a[1][0]*a[2][2]-a[2][0]*a[1][2])
        b[0][2] = a[1][0]*a[2][1]-a[1][1]*a[2][0]
        b[1][0] = -(a[0][1]*a[2][2]-a[2][1]*a[0][2])
        b[1][1] = a[0][0]*a[2][2]-a[0][2]*a[2][0]
        b[1][2] = -(a[0][0]*a[2][1]-a[2][0]*a[0][1])
        b[2][0] = a[0][1]*a[1][2]-a[0][2]*a[1][1]
        b[2][1] = -(a[0][0]*a[1][2]-a[0][2]*a[1][0])
        b[2][2] = a[0][0]*a[1][1]-a[0][1]*a[1][0]

        for i in range(3):
            for j in range(3):
                resultado[i][j] = b[j][i]

        self.ui.txt_adjR00.setText(str(resultado[0][0]))
        self.ui.txt_adjR01.setText(str(resultado[0][1]))
        self.ui.txt_adjR02.setText(str(resultado[0][2]))
        self.ui.txt_adjR10.setText(str(resultado[1][0]))
        self.ui.txt_adjR11.setText(str(resultado[1][1]))
        self.ui.txt_adjR12.setText(str(resultado[1][2]))
        self.ui.txt_adjR20.setText(str(resultado[2][0]))
        self.ui.txt_adjR21.setText(str(resultado[2][1]))
        self.ui.txt_adjR22.setText(str(resultado[2][2]))

    def inversa(self):
        for i in range(3):
            for j in range(3):
                a.append([0]*3)
                b.append([0]*3)
                resultado.append([0]*3)

        a[0][0] = float(self.ui.txt_inver00.text())
        a[0][1] = float(self.ui.txt_inver01.text())
        a[0][2] = float(self.ui.txt_inver02.text())
        a[1][0] = float(self.ui.txt_inver10.text())
        a[1][1] = float(self.ui.txt_inver11.text())
        a[1][2] = float(self.ui.txt_inver12.text())
        a[2][0] = float(self.ui.txt_inver20.text())
        a[2][1] = float(self.ui.txt_inver21.text())
        a[2][2] = float(self.ui.txt_inver22.text()) 

        dp = a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1]
        ds = a[2][0]*a[1][1]*a[0][2] + a[2][1]*a[1][2]*a[0][0] + a[2][2]*a[1][0]*a[0][1]

        deter= dp - ds

        b[0][0] = a[1][1]*a[2][2]-a[1][2]*a[2][1]
        b[0][1] = -(a[1][0]*a[2][2]-a[2][0]*a[1][2])
        b[0][2] = a[1][0]*a[2][1]-a[1][1]*a[2][0]
        b[1][0] = -(a[0][1]*a[2][2]-a[2][1]*a[0][2])
        b[1][1] = a[0][0]*a[2][2]-a[0][2]*a[2][0]
        b[1][2] = -(a[0][0]*a[2][1]-a[2][0]*a[0][1])
        b[2][0] = a[0][1]*a[1][2]-a[0][2]*a[1][1]
        b[2][1] = -(a[0][0]*a[1][2]-a[0][2]*a[1][0])
        b[2][2] = a[0][0]*a[1][1]-a[0][1]*a[1][0]

        for i in range(3):
            for j in range(3):
                resultado[i][j] = b[j][i]

        self.ui.txt_inverR00.setText(str(resultado[0][0]/deter))
        self.ui.txt_inverR01.setText(str(resultado[0][1]/deter))
        self.ui.txt_inverR02.setText(str(resultado[0][2]/deter))
        self.ui.txt_inverR10.setText(str(resultado[1][0]/deter))
        self.ui.txt_inverR11.setText(str(resultado[1][1]/deter))
        self.ui.txt_inverR12.setText(str(resultado[1][2]/deter))
        self.ui.txt_inverR20.setText(str(resultado[2][0]/deter))
        self.ui.txt_inverR21.setText(str(resultado[2][1]/deter))
        self.ui.txt_inverR22.setText(str(resultado[2][2]/deter))

    def matrizSE(self):
        for i in range(3):
            for j in range(3):
                a.append([0]*3)
                b.append([0]*3)
                resultado.append([0]*3)

        for i in range(3):
            for j in range(1):
                c.append([0]*3)
                d.append([0]*3)

        a[0][0] = float(self.ui.txt_ecua1Xadj.text())
        a[0][1] = float(self.ui.txt_ecua1Yadj.text())
        a[0][2] = float(self.ui.txt_ecua1Zadj.text())
        a[1][0] = float(self.ui.txt_ecua2Xadj.text())
        a[1][1] = float(self.ui.txt_ecua2Yadj.text())
        a[1][2] = float(self.ui.txt_ecua2Zadj.text())
        a[2][0] = float(self.ui.txt_ecua3Xadj.text())
        a[2][1] = float(self.ui.txt_ecua3Yadj.text())
        a[2][2] = float(self.ui.txt_ecua3Zadj.text()) 

        c[0][0] = float(self.ui.txt_independiente1adj.text()) 
        c[1][0] = float(self.ui.txt_independiente2adj.text()) 
        c[2][0] = float(self.ui.txt_independiente3adj.text()) 


        dp = a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1]
        ds = a[2][0]*a[1][1]*a[0][2] + a[2][1]*a[1][2]*a[0][0] + a[2][2]*a[1][0]*a[0][1]

        deter = dp - ds

        b[0][0] = a[1][1]*a[2][2]-a[1][2]*a[2][1]
        b[0][1] = -(a[1][0]*a[2][2]-a[2][0]*a[1][2])
        b[0][2] = a[1][0]*a[2][1]-a[1][1]*a[2][0]
        b[1][0] = -(a[0][1]*a[2][2]-a[2][1]*a[0][2])
        b[1][1] = a[0][0]*a[2][2]-a[0][2]*a[2][0]
        b[1][2] = -(a[0][0]*a[2][1]-a[2][0]*a[0][1])
        b[2][0] = a[0][1]*a[1][2]-a[0][2]*a[1][1]
        b[2][1] = -(a[0][0]*a[1][2]-a[0][2]*a[1][0])
        b[2][2] = a[0][0]*a[1][1]-a[0][1]*a[1][0]

        for i in range(3):
            for j in range(3):
                resultado[i][j] = b[j][i]
        
        d[0][0] = resultado[0][0]*c[0][0]+resultado[0][1]*c[1][0]+resultado[0][2]*c[2][0]
        d[1][0] = resultado[1][0]*c[0][0]+resultado[1][1]*c[1][0]+resultado[1][2]*c[2][0]
        d[2][0] = resultado[2][0]*c[0][0]+resultado[2][1]*c[1][0]+resultado[2][2]*c[2][0]

        self.ui.txt_respuestaXadj.setText(str(d[0][0]/deter))
        self.ui.txt_respuestaYadj.setText(str(d[1][0]/deter))
        self.ui.txt_respuestaZadj.setText(str(d[2][0]/deter))
    
    def cramerSE(self):
        for i in range(3):
            for j in range(3):
                a.append([0]*3)
                b.append([0]*3)
                c.append([0]*3)
                d.append([0]*3)

        a[0][0] = float(self.ui.txt_ecua1XCramer.text())
        a[0][1] = float(self.ui.txt_ecua1YCramer.text())
        a[0][2] = float(self.ui.txt_ecua1ZCramer.text())
        a[1][0] = float(self.ui.txt_ecua2XCramer.text())
        a[1][1] = float(self.ui.txt_ecua2YCramer.text())
        a[1][2] = float(self.ui.txt_ecua2ZCramer.text())
        a[2][0] = float(self.ui.txt_ecua3XCramer.text())
        a[2][1] = float(self.ui.txt_ecua3YCramer.text())
        a[2][2] = float(self.ui.txt_ecua3ZCramer.text())  

        dp = a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1]
        ds = a[2][0]*a[1][1]*a[0][2] + a[2][1]*a[1][2]*a[0][0] + a[2][2]*a[1][0]*a[0][1]

        deter= dp - ds

        b[0][0] = float(self.ui.txt_independiente1Cramer.text())
        b[0][1] = float(self.ui.txt_ecua1YCramer.text())
        b[0][2] = float(self.ui.txt_ecua1ZCramer.text())
        b[1][0] = float(self.ui.txt_independiente2Cramer.text())
        b[1][1] = float(self.ui.txt_ecua2YCramer.text())
        b[1][2] = float(self.ui.txt_ecua2ZCramer.text())
        b[2][0] = float(self.ui.txt_independiente3Cramer.text())  
        b[2][1] = float(self.ui.txt_ecua3YCramer.text())
        b[2][2] = float(self.ui.txt_ecua3ZCramer.text()) 

        dpX = b[0][0]*b[1][1]*b[2][2] + b[0][1]*b[1][2]*b[2][0] + b[0][2]*b[1][0]*b[2][1]
        dsX = b[2][0]*b[1][1]*b[0][2] + b[2][1]*b[1][2]*b[0][0] + b[2][2]*b[1][0]*b[0][1]

        deterX= dpX - dsX

        c[0][0] = float(self.ui.txt_ecua1XCramer.text())
        c[0][1] = float(self.ui.txt_independiente1Cramer.text())
        c[0][2] = float(self.ui.txt_ecua1ZCramer.text())
        c[1][0] = float(self.ui.txt_ecua2XCramer.text())
        c[1][1] = float(self.ui.txt_independiente2Cramer.text())
        c[1][2] = float(self.ui.txt_ecua2ZCramer.text())
        c[2][0] = float(self.ui.txt_ecua3XCramer.text())
        c[2][1] = float(self.ui.txt_independiente3Cramer.text())   
        c[2][2] = float(self.ui.txt_ecua3ZCramer.text()) 

        dpY = c[0][0]*c[1][1]*c[2][2] + c[0][1]*a[1][2]*c[2][0] + c[0][2]*c[1][0]*c[2][1]
        dsY = c[2][0]*c[1][1]*c[0][2] + c[2][1]*c[1][2]*c[0][0] + c[2][2]*c[1][0]*c[0][1]

        deterY= dpY - dsY

        d[0][0] = float(self.ui.txt_ecua1XCramer.text())
        d[0][1] = float(self.ui.txt_ecua1YCramer.text())
        d[0][2] = float(self.ui.txt_independiente1Cramer.text())
        d[1][0] = float(self.ui.txt_ecua2XCramer.text())
        d[1][1] = float(self.ui.txt_ecua2YCramer.text())
        d[1][2] = float(self.ui.txt_independiente2Cramer.text())
        d[2][0] = float(self.ui.txt_ecua3XCramer.text())
        d[2][1] = float(self.ui.txt_ecua3YCramer.text())
        d[2][2] = float(self.ui.txt_independiente3Cramer.text())

        dpZ = d[0][0]*d[1][1]*d[2][2] + d[0][1]*d[1][2]*d[2][0] + d[0][2]*d[1][0]*d[2][1]
        dsZ = d[2][0]*d[1][1]*d[0][2] + d[2][1]*d[1][2]*d[0][0] + d[2][2]*d[1][0]*d[0][1]

        deterZ= dpZ - dsZ   

        x = deterX/deter
        y = deterY/deter
        z = deterZ/deter

        self.ui.txt_respuestaXCramer.setText(str(x))
        self.ui.txt_respuestaYCramer.setText(str(y))
        self.ui.txt_respuestaZCramer.setText(str(z))

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = Operaciones()
    myapp.show()
    sys.exit(app.exec_())