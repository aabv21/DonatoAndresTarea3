'''
Created on 17 oct. 2017

@author: aabv
'''



from datetime import date

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
                        

class billeteraElectronica:
    
    def __init__(self, idd, nombres, apellidos, ci, pin):
        
        self.id = idd
        self.nombres = nombres
        self.apellidos = apellidos
        self.ci = ci
        self.creditoRecarga = nodo()
        self.debitoConsumo = nodo()
        self.pin = pin
        
    def saldo(self):
        
        dinero = self.creditoRecarga.total - self.debitoConsumo.total
        return dinero
    
    def recargar(self, idEstablecimiento, monto, fecha):
        
        if idEstablecimiento < 0 and monto < 0:
            pass
        
        else:
            self.creditoRecarga.appendRecargaConsumo(idEstablecimiento, monto, fecha)
            #print("Recarga Exitosa")
    
    def consumir(self, idEstablecimiento, monto, fecha, pin):
        
        if idEstablecimiento < 0 and monto < 0 and pin < 0:
            pass
        
        else:
        
            if pin != self.pin:
                #print("Clave incorrecta")
                pass
                
            else:
                if self.saldo() < monto:
                    #print("Saldo insuficiente") 
                    pass
                    
                else:
                    self.debitoConsumo.appendRecargaConsumo(idEstablecimiento, monto, fecha)
                    #print("Consumo Exitoso")
            
##############################
######### Programa
##############################
'''
miBilletera = billeteraElectronica(1, "Andres Alejandro", "Buelvas Vergara", 24222622, 1111)
print("Mi saldo actual:" + str(miBilletera.saldo())+"\n")
fecha = date(2017, 1, 12) #Anyo - mes - dia
miBilletera.recargar(1, 1000, fecha)
print("Mi saldo actual:" + str(miBilletera.saldo())+"\n")
miBilletera.recargar(2, 500, fecha)
print("Mi saldo actual:" + str(miBilletera.saldo())+"\n")
miBilletera.consumir(1, 300, fecha, 1111)
print("Mi saldo actual:" + str(miBilletera.saldo())+"\n")
miBilletera.consumir(1, 600, fecha, 1111)
miBilletera.consumir(1, 400, fecha, 1111)
miBilletera.recargar(1, 1000, fecha)
miBilletera.recargar(1, 300, fecha)
miBilletera.recargar(1, 2000, fecha)
miBilletera.recargar(1, 200, fecha)
print("Mi saldo actual:" + str(miBilletera.saldo())+"\n")
miBilletera.consumir(1, 400, fecha, 2222)
print("Mi saldo actual:" + str(miBilletera.saldo())+"\n")
miBilletera.consumir(1, 3400, fecha, 1111)
print("Mi saldo actual:" + str(miBilletera.saldo())+"\n")
miBilletera.consumir(1, 400, fecha, 1111)
print("Mi saldo actual:" + str(miBilletera.saldo())+"\n")
'''

      
              
        