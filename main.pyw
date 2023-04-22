from PySide6 import *
from PySide6.QtWidgets import *
import sys
from form import *

import sympy
from sympy import *
##holi

a=[]
b=[]
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



    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = Operaciones()
    myapp.show()
    sys.exit(app.exec_())