# -*- coding: utf-8 -*-
"""
es_translations.py -- Spanish copy for Fernhollow Landscape Co. (the ESP/ENG toggle).
Plain characters only in data-es values (the toggle sets textContent, so HTML
entities would show literally). Avoid double quotes inside values.
"""

NAV_ES = {
    "SERVICES": "SERVICIOS",
    "SPECIALS": "OFERTAS",
    "Specials": "Ofertas",
    "FIND US": "UBICACIÓN",
    "Find Us": "Ubicación",
    "CATERING": "BANQUETES",
    "Catering": "Banquetes",
    "CALENDAR": "CALENDARIO",
    "Calendar": "Calendario",
    "QUOTE": "COTIZAR",
    "Quote": "Cotizar",
}

ORDER_LABEL_ES = "COTIZACIÓN GRATIS"
CALL_LABEL_ES = "LLAMAR"
FOLLOW_ES = "Síguenos"

DEMO_BANNER_ES = "Sitio de demostración · una empresa de jardinería ficticia de mAIntAIn Style — sin cotizaciones ni cuadrillas reales"

# Homepage
HERO_BADGE_ES = "Diseño · Instalación · Cuidado todo el año"
HERO_HEADING_ES = 'Un jardín para <span class="nw">cada estación</span>.'
HERO_SUB_ES = "Diseño, siembra, obras de piedra y cuidado todo el año. Del primer tulipán a la última nevada, mantenemos tu jardín como si alguien lo quisiera."
HERO_MENU_BTN_ES = "Ver servicios y precios"
TRUST_ES = [
    ("Desde 2009", "Cuadrilla familiar"),
    ("Cotizaciones gratis", "Visita en la misma semana"),
    ("Todo el año", "Cortar, sembrar, construir, quitar nieve"),
    ("Lun-Sáb 7am-5pm", "Abierto hoy"),
]
FAVORITES_WHY_ES = "¿POR QUÉ FERNHOLLOW LANDSCAPE CO.?"
FAVORITES_SETS_APART_ES = "Lo que nos distingue"
FEATURES_ES = [
    ("Césped que se nota", "Corte semanal, bordes, fertilización y aireación en un calendario que se ajusta a tu terreno, para que el pasto se mantenga espeso y parejo."),
    ("Patios y obras de piedra", "Patios de lajas, caminos de adoquín y muros bien nivelados y hechos para aguantar heladas y deshielos."),
    ("Jardines que duran", "Camas diseñadas para tu luz y tu tierra, sembradas a mano, con mantillo y bordes. Color de primavera a la primera helada."),
]
SPECIALS_TAG_ES = "OFERTA DEL MES"
SPECIALS_TITLE_ES = "Paquete de limpieza de otoño"
SPECIALS_BODY_ES = "Retiro de hojas, poda de camas y un último corte por $249 en terrenos de hasta un cuarto de acre. Reserva antes del 31 de octubre."
SPECIALS_CTA_ES = ORDER_LABEL_ES
STORY_TAG_ES = "NUESTRA HISTORIA"
STORY_TITLE_ES = "Con raíces aquí desde 2009."
STORY_BODY_ES = ("Fernhollow Landscape Co. es una empresa de jardinería ficticia. La creamos para que veas cómo luce un sitio web de "
                 "mAIntAIn Style y cómo Client Style permite al dueño cambiarlo con solo pedirlo. Cambia la oferta del mes, "
                 "agrega un servicio, mueve el horario. Toma una frase.")
CTA_TITLE_ES = "Caminemos tu jardín"
CTA_SUB_ES = "Cuéntanos qué tienes en mente y para cuándo. El formulario es una demostración, no se envía nada."
CTA_BUTTON_ES = ORDER_LABEL_ES
FIND_US_TITLE_ES = "Encuéntranos"
DIRECTIONS_ES = "Cómo llegar →"

# Services page
MENU_INTRO_ES = "Todo aquí es inventado para la demostración, incluidos los precios."
MENU_SECTION_TITLES_ES = {
    "lawn": "Cuidado del césped",
    "gardens": "Jardines y siembra",
    "stone": "Patios y obras de piedra",
    "trees": "Árboles y setos",
    "irrigation": "Riego",
    "seasonal": "Cuidado de otoño e invierno",
}
MENU_ITEMS_ES = {
    "lawn": [
        ("Corte semanal", "Corte, bordes, recorte y limpieza con sopladora. Precio por visita según el tamaño del terreno."),
        ("Aireación y resiembra", "Aireación con núcleos y semilla de calidad, en primavera u otoño."),
        ("Programa de fertilizante", "Un plan de cinco pasos de fertilización durante el año."),
        ("Limpieza de primavera", "Se retiran los restos, se podan las camas y se hace el primer corte del año."),
    ],
    "gardens": [
        ("Diseño e instalación de camas", "Plano, preparación del suelo, plantas y mantillo para una cama de hasta 9 metros cuadrados."),
        ("Mantillo y bordes", "Mantillo nuevo de cinco centímetros con un borde limpio."),
        ("Macetas de temporada", "Macetas sembradas que se cambian cada estación."),
        ("Visita de salud de plantas", "Un recorrido, poda y un plan de cuidado."),
    ],
    "stone": [
        ("Patio de lajas", "Excavación, base compactada y lajas colocadas a mano."),
        ("Camino de adoquín", "Adoquines entrelazados en el patrón que elijas, con bordes y arena."),
        ("Muro de contención", "De bloque o piedra natural, con drenaje y relleno."),
        ("Círculo para fogata", "Anillo de piedra y base de grava, listo para las noches."),
    ],
    "trees": [
        ("Forma de setos", "Líneas limpias y parte superior pareja, con los restos retirados."),
        ("Poda de arbustos", "En el momento justo para cada planta, para que florezca y conserve su forma."),
        ("Poda de árboles", "Elevación de copa y retiro de ramas secas, hasta 4.5 metros."),
        ("Retiro de tocones", "Triturado bajo el nivel del suelo y relleno con tierra."),
    ],
    "irrigation": [
        ("Revisión de aspersores", "Revisamos cada zona, arreglamos boquillas y ajustamos el programador."),
        ("Nueva zona de riego", "Líneas enterradas, aspersores y conexión al controlador."),
        ("Riego por goteo para camas", "Agua donde la necesitan las raíces, sin desperdicio."),
        ("Preparación para el invierno", "Purga con aire comprimido antes de la primera helada."),
    ],
    "seasonal": [
        ("Retiro de hojas de otoño", "Rastrillado, soplado y retirado. Precio según el tamaño del terreno."),
        ("Quitanieves", "Entrada y caminos, por pasada, con opción de temporada."),
        ("Escalones y caminos", "Palea a mano y se trata con sal para hielo."),
        ("Servicio de sal para hielo", "Descongelante seguro para mascotas en caminos y escalones."),
    ],
}

# Quote page
RES_ES = {
    "tag": "COTIZACIÓN GRATIS", "title": "Caminemos tu jardín",
    "lead": "Cuéntanos qué tienes en mente. Este es un formulario de demostración: no se envía nada.",
    "name": "Tu nombre", "email": "Correo electrónico", "date": "Fecha preferida de visita", "time": "Hora",
    "notes": "Notas", "notes_ph": "Un perro suelto, una cerca con llave, una idea que viste en línea...",
    "party": "Tamaño del terreno", "seat": "¿Cuándo quieres empezar?", "need": "¿Qué servicios te interesan?",
    "stay": "Mantente en contacto", "news": "Envíenme consejos de temporada y ofertas",
    "submit": "PEDIR COTIZACIÓN", "note": "Solo demostración. Nada de lo que escribas se guarda ni se envía.",
    "party_opts": ["Chico (hasta 5,000 pies²)", "Mediano (5,000 a 10,000 pies²)", "Grande (10,000 pies² a 1 acre)", "Más de 1 acre"],
    "seat_opts": ["Lo antes posible", "Este mes", "En los próximos 3 meses", "Solo estoy planeando"],
    "need_opts": ["Cuidado del césped", "Jardines y siembra", "Patio o obra de piedra",
                  "Árboles y setos", "Riego", "Quitanieves o limpieza de temporada"],
}
