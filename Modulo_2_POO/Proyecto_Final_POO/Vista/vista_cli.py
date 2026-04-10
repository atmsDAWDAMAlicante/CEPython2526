# Vista CLI - para la versión CLI... empezamos por aquí

from Modelo.validaciones import Validaciones


class Menus:
  
  menu_interfaz = {"texto": "Elige: 1-CLI / 2-GUI / 0-Salir", "lim": 2} # tipo de menu
  menu_iniciar_juego = {"texto": "Elige: 1-Iniciar juego / 2-Cargar partida / 0 - Salir", "lim": 2} # Controlador 
  menu_guardar_cargar = {"texto": "Elige: 1-Guardar / 2-Cargar", "lim": 2} # Guardar/Cargar - JSON



  @staticmethod
  def menu(menu_activo):

    sufijo = ": "

    opcion_menu = input(f'{menu_activo['texto']}{sufijo}')
    sufijo = ": "
    tipo_validado = Validaciones.validar_menu_en_rango(opcion_menu, menu_activo['lim'])
    while (tipo_validado == False):
      sufijo = ", otra vez: "
      opcion_menu = input(f'{menu_activo['texto']}{sufijo}')
      tipo_validado = Validaciones.validar_menu_en_rango(opcion_menu, menu_activo['lim'])
    return int(opcion_menu)
