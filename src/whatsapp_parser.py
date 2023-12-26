"""Módulo para convertir los mensajes de Whatsapp. Es importante ver que los chats
de Android y los de iPhone no son iguales"""

def android_parser(mensaje: str) -> tuple[str, str, str]:
    """Función que a partir de un mensaje de WhatsApp me devuelve
    la fecha, la hora y la nombre que escribió el mensaje.
    
    :param mensaje: mensaje de WhatsApp del exportado. Un renglón del txt.
    :return: tupla de fecha, hora y nombre.
    """
    # limpiamos el caracter raro
    mensaje = mensaje.replace('\u202f', '')

    # obtener fecha
    fecha = mensaje.split(", ")[0]

    # obtener hora
    hora = mensaje.split(", ") # hago [String] de dos elementos separando por la coma
    hora = hora[1] # elijo el elemento 1 (donde está la hora)
    hora = hora.split(" - ") # separo por el - que siempre está
    hora = hora[0]

    # obtener nombre
    nombre = mensaje.split(" - ")
    nombre = nombre[1].split(":")[0]
    
    return (fecha, hora, nombre)


def es_mensaje_caca(mensaje: str) -> bool:
    """Si contiene el simbolo '\u200e' entonces no es un mensaje"""
    no_es_mensaje_notificacion = not '\u200e' in mensaje
    contiene_emoji_caca = '💩' in mensaje
    
    return no_es_mensaje_notificacion and contiene_emoji_caca

