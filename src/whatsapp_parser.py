"""Módulo para convertir los mensajes de Whatsapp. Es importante ver que los chats
de Android y los de iPhone no son iguales"""

from datetime import datetime, timedelta
import pandas as pd


def android_parser(mensaje: str) -> tuple[str, str, str]:
    """Función que a partir de un mensaje de WhatsApp me devuelve
    la fecha, la hora y la nombre que escribió el mensaje.

    :param mensaje: mensaje de WhatsApp del exportado. Un renglón del txt.
    :return: tupla de fecha, hora y nombre.
    """
    # limpiamos el caracter raro
    mensaje = mensaje.replace("\u202f", "")

    # obtener fecha
    fecha = mensaje.split(", ")[0]

    # obtener hora
    hora = mensaje.split(", ")  # hago [String] de dos elementos separando por la coma
    hora = hora[1]  # elijo el elemento 1 (donde está la hora)
    hora = hora.split(" - ")  # separo por el - que siempre está
    hora = hora[0]

    # obtener nombre
    nombre = mensaje.split(" - ")
    nombre = nombre[1].split(":")[0]

    return (fecha, hora, nombre)


def iphone_parser(mensaje: str) -> tuple:
    """Función que a partir de un mensaje de WhatsApp me devuelve
    la fecha, la hora y la nombre que escribió el mensaje.

    :param mensaje: mensaje de WhatsApp del exportado. Un renglón del txt.
    :return: tupla de fecha, hora y nombre.
    """
    print(mensaje)
    pos = mensaje.find("]") + 1
    date_str = mensaje[:pos]
    date_time_obj = pd.to_datetime(date_str, format="[%d/%m/%y, %H:%M:%S]")

    fecha = datetime.strftime(date_time_obj, "%d/%m/%y")
    hora = datetime.strftime(date_time_obj, "%H:%M")

    mensaje = mensaje[pos + 1 :]

    nombre = "".join(mensaje.split(":")[0])

    caca = ":".join(mensaje.split(":")[1:])
    es_diarrea = "💧" in caca

    # saco emojis de caca
    caca = caca.replace("💩", "").replace("💧", "")

    # busco por hora o fecha (o ambas) en mensaje caca
    caca = caca.split(" ")

    fecha_edit = ""
    hora_edit = ""

    for c in caca:
        if ":" in c:
            hora_edit = c.strip()
        elif "/" in c:
            fecha_edit = c.strip()

    # si hay fecha_edit entonces la fecha es fecha_edit
    # y hora es hora_edit
    if fecha_edit:
        # si no tiene año, entonces es el año actual
        if len(fecha_edit.split("/")) == 2:
            fecha_edit = fecha_edit + "/" + datetime.strftime(date_time_obj, "%y")
        fecha = fecha_edit

    # si no hay fecha_edit, y la hora_edit > hora, entonces
    # fecha es fecha - 1 día, y hora es hora_edit
    if hora_edit:
        try:
            hora_edit = datetime.strptime(hora_edit, "%H:%M")
        except ValueError:
            print("ERRRRRRRRORR", hora_edit)
            print("Cant caracteres:", len(hora_edit))
        hora_edit = hora_edit.time()

        if hora_edit > datetime.strptime(hora, "%H:%M").time():
            fecha = datetime.strptime(fecha, "%d/%m/%y") - timedelta(days=1)
            fecha = datetime.strftime(fecha, "%d/%m/%y")

        hora = hora_edit.strftime("%H:%M")

    return fecha, hora, nombre, es_diarrea


def es_mensaje_caca(mensaje: str) -> bool:
    """Si contiene el simbolo '\u200e' entonces no es un mensaje"""
    es_mensaje_notificacion = "\u200e" in mensaje and "<" not in mensaje
    contiene_emoji_caca = "💩" in mensaje

    return not es_mensaje_notificacion and contiene_emoji_caca
