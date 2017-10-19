#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 18 oct. 2017

@author: Andres Buelvas 13-10184
@author: Donato Bracuto 13-10173
'''

from datetime import date

#Clase creada para guardar los montos, fecha y identificador del establecimiento donde se haga una recarga o consumo
class nodo:
    
    def __init__(self):
        
        self.proximo = None
        self.idEstablecimiento = 0
        self.monto = 0
        self.fecha = None
        self.total = 0
        
    def imprimirValores(self):
        
        print("id del Establecimiento: " +str(self.idEstablecimiento)+ " ---- monto:" 
              +str(self.monto)+ " ---- fecha: " +str(self.fecha))
    
    #Metodo que sirve para registrar una operacion ya sea recarga o consumo       
    def appendRecargaConsumo(self, idEstablecimiento, monto, fecha):
        
        UltimoAppend = False
        buscando = self.proximo
        
        while not UltimoAppend:
            
            if buscando != None:
                buscando = self.proximo.proximo
        
            else:
                self.proximo = nodo()
                self.idEstablecimiento = idEstablecimiento
                self.fecha = fecha
                self.monto = monto
                self.total += monto
                self.imprimirValores()
                UltimoAppend  = True
                        
#Billetera electronica
class billeteraElectronica:
    
    def __init__(self, idd, nombres, apellidos, ci, pin):
        self.id = idd
        self.nombres = nombres
        self.apellidos = apellidos
        self.ci = ci
        self.creditoRecarga = nodo()
        self.debitoConsumo = nodo()
        self.pin = pin
    
    #Metodo qeu sirve para imprimir el saldo actual de la cuenta
    def saldo(self):
        
        dinero = self.creditoRecarga.total - self.debitoConsumo.total
        return dinero
    
    #Metodo qeu sirve para realizar una recarga a la cuenta
    def recargar(self, idEstablecimiento, monto, fecha):
        
        #Verificamos si los datos son validos
        if idEstablecimiento >= 0 and monto >= 0:
            self.creditoRecarga.appendRecargaConsumo(idEstablecimiento, monto, fecha)
            #print("Recarga Exitosa")
        else:
            pass
            
    #Metodo qeu sirve para realizar un consumo
    def consumir(self, idEstablecimiento, monto, fecha, pin):
        
        #Verificamos si los datos son validos
        if idEstablecimiento >= 0 and monto >= 0 and pin >= 0:
            if pin != self.pin:
                #print("Clave incorrecta")
                pass
                
            else:
                # Verificamos si el saldo actual de la cuenta es suficiente
                if self.saldo() < monto: 
                    #print("Saldo insuficiente") 
                    pass
                    
                else:
                    self.debitoConsumo.appendRecargaConsumo(idEstablecimiento, monto, fecha)
                    #print("Consumo Exitoso")  
        
        else:
            pass                 
        