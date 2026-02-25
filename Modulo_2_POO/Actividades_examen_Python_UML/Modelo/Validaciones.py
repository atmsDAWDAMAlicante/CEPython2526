import re 

class Validaciones:

    @staticmethod
    def validar_menu_principal(num):
        try:
            int(num)
        except ValueError:
            return -1
        else:
            if ((int(num) < 0) or (int(num) > 10)):
                return -1
            else:
                return int(num)
            
    @staticmethod
    def validar_numero_en_rango(num, lim):
        try:
            int(num)
        except ValueError:
            return -1
        else:
            if ((int(num) > 0 ) and (int(num) <= lim)):
                return int(num)
            else:
                return -1
        

    @staticmethod
    def validar_dni(dni):
        patron_dni = r'^\d{8}[A-Z]$'
        
        if (re.match(patron_dni, dni)):
            return True
        else: 
            return False
        
    @staticmethod
    def validar_password(password):
        patron_password = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$"
        if (re.match(patron_password, password)):
            return True
        else: 
            return False

    @staticmethod
    def validar_fecha(fecha):
        pass