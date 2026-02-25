import re 

class Validaciones:

    @staticmethod
    def validar_menu_principal(num): # Validar opción introducida del menú prinicpal (int)
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
    def validar_numero_en_rango(num, lim): # Validar que el número introducido es entero y dentro de un rango
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
    def validar_float(num): # Validar que el número introducido es un float
        try:
            float(num)
        except ValueError:
            return False
        else:
            return float(num)
        
        


    @staticmethod
    def validar_dni(dni): # Validar que se ha introducido un DNI de 8 números y una mayúscula
        patron_dni = r'^\d{8}[A-Z]$'
        
        if (re.match(patron_dni, dni)):
            return True
        else: 
            return False
        

    @staticmethod
    def validar_password(password): # Validar la contraseña, mínimo: 1 mayúscula, 1 minúscula y 1 número
        patron_password = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$"
        if (re.match(patron_password, password)):
            return True
        else: 
            return False

    @staticmethod
    def validar_fecha(fecha): # Validar que se ha introducido una fecha correcta
        pass