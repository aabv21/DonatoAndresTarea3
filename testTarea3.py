#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

@author: Andres Buelvas 13-10184
@author: Donato Bracuto 13-10173

'''

import unittest
from tarea3 import *

class testTarea3(unittest.TestCase):
    
    #Probamos una billetera cualquiera
    def setUp(self):
        self.bille = billeteraElectronica(0, "Donato", "Andres", 0, 0)
        self.bille2 = billeteraElectronica(0, "eáiu", "aeiou", 0, 0)
        self.fecha = date(1, 1, 1)
        self.fecha2 = date(2012, 12, 12)
        self.fecha3 = "2012/12/12"
    
    #[CASO FRONTERA] Verificamos que la billetera realmente existe [CASO FRONTERA]
    def testBilleteraExiste(self):
        self.assertTrue(self.bille, 'la billetera sin caracteres especiales no ha sido creada')
        self.assertTrue(self.bille2, 'la billetera con caracteres especiales no ha sido creada')
    
    #[CASO INTERNO] Verificamos que existe un metodo que nos permita consultar el saldo de nuestra billetera
    def testExisteMetodoSaldo(self):
        self.assertEqual(0, self.bille.saldo(), 'El saldo de la billetera deberia ser 0')
    
    #[CASO INTERNO] Verificamos funcionalidad del Saldo Nulo    
    def testSaldoNulo(self):
        self.assertEqual(0, self.bille.saldo(), 'El saldo de la billetera deberia ser 0')
    
    #[CASO FRONTERA] Verificamos recargas positivas    
    def testFuncionalidadMetodoRecargar(self):
        self.bille.recargar(1, 5000, self.fecha2)
        self.assertEqual(self.bille.saldo(), 5000, 'Error en las operaciones de recarga')
    
    #[CASO FRONTERA] Verificamos recargas negativas    
    def testFuncionalidadMetodoRecargarNeg(self):
        self.bille.recargar(1, -5000, self.fecha2)
        self.assertEqual(self.bille.saldo(), 0, 'En las recargas no se pueden poner montos negativos')
    
    #[CASO FROTENRA] Verificamos que funcione el metodo consumo con montos menores al saldo de la cuenta
    def testExisteMetodoConsumoNeg(self):
        self.bille.consumir(0, 100, self.fecha, 1)
        self.assertEqual(self.bille.saldo(), 0, 'Los consumos qeu superan el saldo deben ser rechazados')
    
    #[CASO FROTENRA] Verificamos que funcione el metodo consumo con montos negativos
    def testExisteMetodoConsumoNeg(self):
        self.bille.consumir(0, -150, self.fecha, 1)
        self.assertEqual(self.bille.saldo(), 0, 'En los consumos no se pueden poner montos negativos')
        
    #[CASO FRONTERA] Verificamos restriccion del pin introducido es el mismo pin de la billetera
    def testMismoPin(self):
        self.bille.recargar(1, 5000, self.fecha2)
        self.bille.consumir(1, 0, self.fecha2, 0)
        self.assertEqual(self.bille.saldo(), 5000, 'Error en la verificacion de pines')                                 
        
    #[CASO ESQUINA] Verificamos funcionalidad del metodo consumo al descontar al saldo actual con mismo pin
    def testBalancePositivoPermiteConsumo(self):
        self.bille.recargar(1, 5000, self.fecha2)
        self.bille.consumir(1, 3000, self.fecha2, 0)
        self.assertEqual(self.bille.saldo(), 2000, 'Error en la verificacion de pines iguales')
        
    #[CASO ESQUINA] Verificamos funcionalidad consumo aceptado con pines distinto
    def testConsumoNoExistoso(self):
        self.bille.recargar(1, 5000, self.fecha2)
        self.bille.consumir(1, 3000, self.fecha2, 1)
        self.assertEqual(self.bille.saldo(), 5000, 'Error en la verificacion de pines distintos')
        
    #[CASO ESQUINA] Verificamos consumo no aceptado con pines iguales        
    def testBalanceNegativo(self):
        self.bille.recargar(1, 5000, self.fecha2)
        saldo_viejo = self.bille.saldo()
        self.bille.consumir(1, 5001, self.fecha2, 0)
        saldo_actual = self.bille.saldo()
        self.assertEqual(saldo_viejo, saldo_actual, 'Error en la operacion de consumo el verificar los pines') 
           
    #[CASO FRONTERA] Verificamos que el consumo es igual al saldo de la billetera
    def testBalanceNulo(self):
        self.bille.recargar(1, 5000, self.fecha2)
        self.bille.consumir(1, 5000, self.fecha2, 0)
        self.assertEqual(self.bille.saldo(), 0, 'Error en  las operaciones de recarga y consumo')
        
    #[CASO MALICIA] Verificamos que se permita todo tipo de letra del castellano  
    def testTodoTipoDeLetra(self):
        mi_billetera = self.bille2
        self.assertTrue(mi_billetera, 'Error al leer caracteres especiales del Castellano')
    
    #[CASO MALICIA] Verificamos Formato de fecha valida (solo formato date)   
    def testFechaValida(self):
        self.assertFalse(self.bille.recargar(1, 5000, self.fecha3), 'Formato de fecha no reconocido')
        
    #[CASO MALICIA] Verificamos monto e id negativos de recarga:
    def testNoRecargaValoresNagativos(self):
        self.assertFalse(self.bille.recargar(-1, -1, self.fecha2), 'No se puede recargar valores negativos')
        
    #[CASO MALICIA] Verificamos monto, id, y pin negativos de consumo
    def testNoConsumoValoresNegativos(self):
        self.assertFalse(self.bille.consumir(-1, -1, self.fecha2, -1), 'No se puede consumir valores negativos')
                  
 
        
           
        