'''

@author: aabv
'''

import unittest
from tarea3 import *

class testTarea3(unittest.TestCase):
    
    #Probamos una billetera cualquiera
    def setUp(self):
        self.bille = billeteraElectronica(0, "", "", 0, 0)
        self.bille2 = billeteraElectronica(0, "Aünuáñ", "Aünuáñ", 0, 0)
        self.bille3 = billeteraElectronica(-1, "", "", -1, -1)
        self.bille4 = billeteraElectronica(0, 0, 0, 0, 0)
        self.fecha = date(1, 1, 1)
        self.fecha2 = date(2012, 12, 12)
        self.fecha3 = "2012/12/12"
    
    #Verificamos que la billetera realmente existe    
    def testBilleteraExiste(self):
        self.bille
    
    #Verificamos que existe un metodo que nos permita consultar el saldo de nuestra billetera
    def testExisteMetodoSaldo(self):
        self.bille.saldo()
    
    #Verificamos funcionalidad del Saldo Nulo    
    def testSaldoNulo(self):
        self.assertEqual(self.bille.saldo(), 0)
     
    #Verificamos que existe un metodo recargar
    def testExisteMetodoRecargar(self):
        self.bille.recargar(0, 0, self.fecha)
    
    #Verificamos funcionalidad del metodo recargar    
    def testFuncionalidadMetodoRecargar(self):
        self.bille.recargar(1, 5000, self.fecha2)
        self.assertEqual(self.bille.saldo(), 5000)
        
    #Verificamos que existe el metodo consumo
    def testExisteMetodoConsumo(self):
        self.bille.consumir(0, 0, self.fecha, 1)
        
    #Verificamos restriccion del pin introducido es el mismo pin de la billetera
    def testMismoPin(self):
        self.bille.recargar(1, 5000, self.fecha2)
        self.bille.consumir(1, 0, self.fecha2, 0)
        self.assertEqual(self.bille.saldo(), 5000)                                 
        
    #Verificamos funcionalidad del metodo consumo al descontar al saldo actual con mismo pin
    def testBalancePositivoPermiteConsumo(self):
        self.bille.recargar(1, 5000, self.fecha2)
        self.bille.consumir(1, 3000, self.fecha2, 0)
        self.assertEqual(self.bille.saldo(), 2000)
        
    #Verificamos funcionalidad consumo aceptado con pines distinto
    def testConsumoNoExistoso(self):
        self.bille.recargar(1, 5000, self.fecha2)
        self.bille.consumir(1, 3000, self.fecha2, 1)
        self.assertEqual(self.bille.saldo(), 5000)
        
    #Verificamos consumo no aceptado con pines iguales        
    def testBalanceNegativo(self):
        self.bille.recargar(1, 5000, self.fecha2)
        saldo_viejo = self.bille.saldo()
        self.bille.consumir(1, 5001, self.fecha2, 0)
        saldo_actual = self.bille.saldo()
        self.assertEqual(saldo_viejo, saldo_actual) 
           
    #Verificamos caso borde donde el consumo es igual al saldo de la billetera
    def testBalanceNulo(self):
        self.bille.recargar(1, 5000, self.fecha2)
        self.bille.consumir(1, 5000, self.fecha2, 0)
        self.assertEqual(self.bille.saldo(), 0)
        
    #Verificamos caso malicioso donde se permita todo tipo de letra del castellano  
    def testTodoTipoDeLetra(self):
        mi_billetera = self.bille2
        assert (mi_billetera)
    
    #Verificamos caso malicioso de Formato de fecha valida (solo formato date)   
    def testFechaValida(self):
        assert not (self.bille.recargar(1, 5000, self.fecha3))
        
    #Verificamos caso malicioso de monto e id negativos de recarga:
    def testNoRecargaValoresNagativos(self):
        assert not (self.bille.recargar(-1, -1, self.fecha2))
        
    #Verificamos caso malicioso de monto, id, y pin negativos de consumo
    def testNoConsumoValoresNegativos(self):
        assert not (self.bille.consumir(-1, -1, self.fecha2, -1))
                  
 
        
           
        