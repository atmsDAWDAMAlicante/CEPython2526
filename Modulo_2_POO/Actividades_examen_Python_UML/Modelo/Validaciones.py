import re 

class Validaciones:
    @staticmethod
    def validar_dni(dni):
        patron_dni = r'^\d{8}[A-Z]$'
        
        if (re.match(patron_dni, dni)):
            return True
        else: 
            return False
