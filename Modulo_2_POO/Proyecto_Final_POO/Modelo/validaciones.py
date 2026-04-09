# Validar

class Validaciones:
  @staticmethod
  def validar_menu_en_rango(opcion_menu, lim):
    try:
      menu_validado = int(opcion_menu)
    except ValueError:
      print(f'Introduce un número entero dentro del 1 al {lim}')
      return False
    else:
      if (menu_validado > lim):
        print(f'Introduce un número entero dentro entre 1 y {lim}')
        return False
      else:
        return True