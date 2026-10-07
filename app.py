import gradio as gr
import random
import urllib.parse

# 📚 Base de conocimiento
base_conocimiento = [
    {
        "claves": ["servicio", "hacen", "ofrecen","servicios"],
        "respuesta": """Nuestros servicios:\n
        • Inducción.
        • HiperOPAC.
        • Prétamo y uso interno.
        • Asesorías personalizadas.
        • Renovación de material telefónica y presencial.
        • Agendamiento en línea de capacitación.
        • Cambio de datos del domicilio.
        • Envío de alertas y sugerencias.
        • Extracto de cuenta.
        • Asistente de investigación (IA).
        • Bx de comendación.
        • Elaboración de bibliografías.
        • Conmutación bibliográfica.
        • Préstamo interbibliotecario.
        • Programa ABC (Bibliografía para cursos).
        • Servicios de alertas y novedades bibliográficas.
        • Talleres de desarrollo de habilidades informativas.
        • Bufé literario.
        • Club de amigos.
        • Literatura para oír.
        • Proyección de películas.
        • Tertulias literarias."""
    },
    {
        "claves": ["norma", "regla", "prohibido", "comer"],
        "respuesta": "Debes mantener el silencio, no consumir alimentos, no fumar, levantar las sillas al moverlas, cuidar la tapicería y superficies, cuidar los materiales y acatar las sugerencias de los funcionarios."
    },
    {
        "claves": ["contacto", "numero", "llamar","telefono","teléfono","teléfonos"],
        "respuesta": "Realiza tu llamada a los siguiente números...\n Contacto: 6056931919 Ext 2806 - 4115"
    },
    {
        "claves": ["préstamos interbibliotecario", "préstamo interbibliotecario", "prestamos interbibliotecario","prestamo interbibliotecario"],
        "respuesta": "Puedes solicitar préstamos de recursos de información pertenecientes a las Instituciones con las cuales tenemos convenios, a través del correo electrónico infobiblioteca@utb.edu.co."
    },
    {
        "claves": ["devolver", "devolución", "devolucion","devoluciones"],
        "respuesta": "Puedes realizar las devoluciones en cualquier sede.\nLos libros se solicitan y devuelven en los puntos de Circulación y Préstamo: Primer piso en la Biblioteca Ternera y cuarto piso (Sala 403, Edificio MB) en Manga ."
    },
    {
        "claves": ["primo", "catalogo", "catálogo"],
        "respuesta": "PRIMO es el catálogo en línea donde puedes buscar, reservar y renovar libros...\n👉 [Ir al catálogo](https://primo.utb.edu.co/discovery/search?vid=57UTB_INST:57UTB_INST)"
    },
    {
        "claves": ["fototeca", "fotos", "archivo fotografico","archivo fotográfico","fotografía","fotografia","foto"],
        "respuesta": "🖼️ La fototeca de la UTB conserva material fotográfico institucional e histórico. Puedes consultarla para fines académicos o de investigación a través de la biblioteca...\n👉 [Visitar la fototeca](https://www.utb.edu.co/biblioteca/fototeca-historica-cartagena-de-indias/)\nPara material de la Fototeca, debes enviar una solicitud detallando lo relacionado con el material al correo electrónico fototeca@utb.edu.co"
    },
    {
        "claves": ["biblioteca utb", "pagina de la biblioteca","página de la biblioteca", "informacion de biblioteca", "web biblioteca","información de biblioteca"],
        "respuesta": "🌐 En la página oficial...\n👉 [Visitar biblioteca UTB](https://www.utb.edu.co/biblioteca-utb/)"
    },
    {
        "claves": ["prestamo", "préstamo","préstamos","prestamos", "prestar", "libros prestar", "cuantos libros", "cuantos dias", "tiempo prestamo","prestan","prestado"],
        "respuesta": """Inicia sesión en el buscador  Primo y ve a la sección 'Mi Cuenta' / 'Mis Préstamos'.\nLos libros se solicitan en circulación y préstamo (primer piso de la biblioteca) y cuarto piso (Sala 403, Edificio MB) en Manga de manera presencial y con su carnet estudiantil.\n📚 Reglamento de préstamo:
    
        👩‍🎓 Estudiantes:
        • General: 3 libros por 7 días  
        • Literatura/Arte/Geografía e historia: 2 libros por 15 días  
        • Trabajo de grado/Monografías/Tesis: 2 libros por 5 días  
        • Reserva: 2 libros Hasta el siguiente día hábil
        • Audiovisual: 2 libros por 5 días  
        • Hemeroteca: 1 libro por 2 días  
        • Referencia/Referencia continúa/Prensa: Solo consulta en sala  
        
        👩‍🎓 Estudiantes de maestría y doctorado:
        • General: 10 libros por 7 días  
        • Literatura/Arte/Geografía e historia: 2 libros por 15 días  
        • Trabajo de grado/Monografías/Tesis: 2 libros por 5 días  
        • Reserva: 2 libros Hasta el siguiente día hábil
        • Audiovisual: 2 libros por 5 días  
        • Hemeroteca: 1 libro por 2 días  
        • Referencia/Referencia continúa/Prensa: Solo consulta en sala  
        
        👨‍🏫 Profesores:
        • General: 3 libros por 7 días  
        • Literatura/Arte/Geografía e historia: 2 libros por 15 días  
        • Trabajo de grado/Monografías/Tesis: 2 libros por 5 días  
        • Reserva: 2 libros Hasta el siguiente día hábil
        • Audiovisual: 2 libros por 5 días  
        • Hemeroteca: 1 libro por 2 días  
        • Referencia/Referencia continúa/Prensa: Solo consulta en sala

        👩🏻‍💻 Empleados:
        • General: 2 libros por 7 días  
        • Literatura/Arte/Geografía e historia: 2 libros por 15 días  
        • Trabajo de grado/Monografías/Tesis: 2 libros por 5 días  
        • Reserva: 2 libros Hasta el siguiente día hábil
        • Audiovisual: 2 libros por 5 días  
        • Hemeroteca: 1 libro por 2 días  
        • Referencia/Referencia continúa/Prensa: Solo consulta en sala  

        👩‍🎓 Egresado:
        • General: 2 libros por 7 días  
        • Literatura/Arte/Geografía e historia: 2 libros por 7 días  
        
        🙎🏻‍♀️Club de amigos: 
        • Literatura/Arte/Geografía e historia: 2 libros
        
        🏫 Instituciones con convenio de préstamo interbibliotecario:
        • General: 10 libros
        
        💸 Multas:
        • $1.000 por día (general)  
        • $2.000 por día (material especial)"""
    }

]

# 👋 Saludos
saludos = ["hola", "buenas", "buenos días", "buenas tardes", "buenas noches"]

# 🧠 Memoria simple
historial_global = []

 
# 🧹 Limpiar texto
def limpiar_consulta(texto):
    palabras_basura = [
        "el", "la", "los", "las","necesito", "quiero", "buscar", "buscando", "busca", "busco", "buscame",
        "estoy", "como", "solicito","un", "una", "libro", "de", "por", "favor",
        "me", "puedes", "ayudar", "con", "tambien", "ademas", "otro"
    ]

    palabras = texto.lower().split()
    palabras_limpias = [p for p in palabras if p not in palabras_basura]

    return " ".join(palabras_limpias)

# 🔀 Separar múltiples libros
def separar_consultas(texto):
    separadores = [" y ", ",", " e "]
    
    for sep in separadores:
        if sep in texto:
            return [t.strip() for t in texto.split(sep)]
    
    return [texto]

# 🔗 Generar link PRIMO
def generar_link_primo(consulta):
    base_url = "https://primo.utb.edu.co/discovery/search"

    params = {
        "vid": "57UTB_INST:57UTB_INST",
        "query": f"any,contains,{consulta}"
    }

    return f"{base_url}?{urllib.parse.urlencode(params)}"

# 🤖 Función principal
def dividir_intenciones(texto):
    separadores = [" y ", ",", " tambien ", " también "]
    
    for sep in separadores:
        if sep in texto:
            return [t.strip() for t in texto.split(sep)]
    
    return [texto]
def responder(mensaje, historial):
    
    mensaje = mensaje.lower().strip()
    partes = dividir_intenciones(mensaje)   # 

    saludo = ""
    respuesta = ""

    if any(s in mensaje for s in ["hola", "buenas", "buenos días", "buenas tardes","buenas noches"]):
        saludo = "¡Hola! 😊\n\n"

    # 👋 SOLO SALUDO
    if any(s in mensaje for s in saludos) and len(mensaje.strip()) < 10:
        return random.choice([
            "¡Hola! 😊 Soy tu asistente de la biblioteca UTB 📚\n\n¿En qué puedo ayudarte?",
            "¡Hola! 👋 Estoy aquí para ayudarte con la biblioteca 📚",
            "¡Hola! 😄 Puedes preguntarme sobre libros, horarios, servicios y más"
        ])

    # 🎓 CAPACITACIONES
    if "capacit" in mensaje or "asesor" in mensaje:
        respuesta += """🎓 Puedes agendar tu capacitación aquí, ingresando con tus credenciales institucionales:

👉 [Agendar capacitación](https://outlook.office365.com/book/ServiciosBibliotecarios@utb.edu.co/?ismsaljsauthenabled=true)

"""

    # 📚 HORARIO
    if any(p in mensaje for p in ["horario", "hora", "abren", "cierran", "trabajan"]):
        respuesta += """📚 Nuestro horario es:

Campus Tecnológico: Lunes a viernes: 7am - 7pm / Sábados: 8am - 12m  
Casa Lemaitre: Lunes a jueves: 7am - 5pm / Viernes: 7am - 6pm / Sábado: 8am - 2pm

"""

    # 📊 BASES DE DATOS
    if "bases de datos" in mensaje or "biblioteca digital" in mensaje:
        respuesta += """📊 Entra al portal de la Biblioteca, sección 'Bases de Datos'. Ingresa con tu usuario y contraseña institucional para consultar recursos especializados.

👉 [Biblioteca digital](https://www.utb.edu.co/biblioteca-utb/biblioteca-digital/)

"""

    # 🏛️ REPOSITORIO
    if "repositorio" in mensaje or "tesis" in mensaje:
        respuesta += """🏛️Encuentra artículos de investigación, libros, revistas, fotos y demás recursos de tu interés, producidos por la Universidad Tecnológica de Bolívar.:

👉 [Repositorio UTB](https://repositorio.utb.edu.co/home)

"""
    # 🔎 BÚSQUEDA DE UN LIBRO
    if any(p in mensaje for p in ["como buscar", "cómo buscar", "búsqueda de un libro", "como hago una busqueda"]):
        respuesta += """🔎 Para buscar un libro en la biblioteca:

    1. Ingresa al catálogo PRIMO  
    2. Escribe el título, autor o tema  
    3. Usa los filtros para refinar resultados  

👉 [Ir a PRIMO](https://primo.utb.edu.co/discovery/search?vid=57UTB_INST:57UTB_INST)

"""
    # 💻 SOLICITUD DE DOCUMENTO DIGITAL
    if any(p in mensaje for p in ["artículo", "articulo", "capítulo","capitulo","capitulo de libro","caítulo de libro"]):
        respuesta += """💻 Usa el buscador  Primo, identificarse con sus credenciales (correo y contraseña institucional) realizar la búsqueda y seleccionar el documento haciendo la respectiva solicitud a la biblioteca.\nSi el artículo/capítulo de libro no se encuentra en el catálogo puedes solicitarlo por nuestro formulario en blanco.

🎥 Video:
👉 [Solicitud de documento digital](https://www.youtube.com/watch?v=CbTWl0Htq7w)

📄 Formulario:
👉 [Formulario en blanco](https://primo.utb.edu.co/discovery/blankIll?vid=57UTB_INST:57UTB_INST)

"""
    
    # 📚 UBICAR LIBRO EN ESTANTERÍA (HYPEROPAC)
    if any(p in mensaje for p in ["ubicar", "ubico", "estantería","estanteria"]):
        respuesta += """📚 Busca el libro en Primo filtrando por la disponibilidad en la Biblioteca Luis Enrique Borja Baron el cual te dará acceso al HiperOpac. Si necesitas ayuda, el personal de sala te guiará.

👉 [Descargar presentación](https://huggingface.co/spaces/Mapu25/chatbot-biblioteca/resolve/main/HiperOPAC.pptx)
"""
    # 📖 ASISTENTE IA
    if any(p in mensaje for p in ["asistente de investigación", "asistente de investigacion", "inteligencia artificial"]):
        respuesta += """📖 Asistente de investigación:

👉 [Ir al asistente](https://primo.utb.edu.co/discovery/researchAssistant?vid=57UTB_INST:57UTB_INST)

🎥 Video:
👉 [Ver video](https://www.youtube.com/watch?v=aMJm7gFbCJw&t=1s)

"""
     #PROGRAMA ABC
    if any(p in mensaje for p in ["programa ABC", "programa abc", "bibliografía para cursos","bibliografia para cursos"]):
        respuesta += """📖 Programa ABC:

🎥 Video Cite it del programa ABC:
👉 [Ver video](https://www.youtube.com/watch?v=w8XN3VgD68k)

"""
    mensaje = mensaje.lower().replace(",", " ").strip()
    partes = dividir_intenciones(mensaje)
    
    # 🔁 PROCESAR CADA PARTE
    for parte in partes:
        parte = parte.strip()
    
        # 🚫 IGNORAR BASURA
        if not parte or len(parte) < 3:
            continue

        # 📖 RENOVACIÓN
        if any(p in parte for p in ["renov", "renuevo", "renovar", "renovación", "renovacion"]):
            respuesta += """📖 Renovación de libros: Podrás extender los períodos de préstamos una vez dentro de la fecha establecida de devolución, de forma presencial, telefónica o virtual desde el catálogo del Sistema de Bibliotecas, ingresando con tu usuario y contraseña.

👉 [Renovar en PRIMO](https://primo.utb.edu.co/discovery/account?vid=57UTB_INST:57UTB_INST&section=loans&lang=es)

"""
        # 📚 RESERVA
        if any(p in parte for p in ["reserv", "reservo", "reservar", "reserva"]):
            respuesta += """📚 Reserva de libros: Puedes reservar libros físicos directamente desde el buscador Primo iniciando sesión con tu cuenta y contraseña.

👉 [Ir al catálogo](https://primo.utb.edu.co/discovery/search?vid=57UTB_INST:57UTB_INST)

🎥 Video guía:
👉 [Ver video](https://www.youtube.com/watch?v=ahmo6iLG2Es&t=141s)

"""

    # 📄 PAZ Y SALVO
    if "paz y salvo" in mensaje:
        respuesta += """📄 Solicita tu paz y salvo en el siguiente link. Además de realizar la solicitud por el formulario debe tener en cuenta que no puede tener multa bibliográfica, y que de acuerdo con la opción de grado cargar el soporte en la solicitud realizada. 

👉 [Formulario](https://forms.office.com/pages/responsepage.aspx?id=UJ5k6tInGEOcuS_P_hb9QfLUIQI8HudFvLRcZQ9xPDZUOFhFMUkzNlNOWFJXSDNSNTIwSTdRNlc5WC4u&route=shorturl)

"""

    # ✍🏻 TRABAJOS DE GRADO
    if any(p in mensaje for p in ["subir", "enviar", "cargar", "depositar", "subo", "subir tesis", "entregar tesis", "trabajo de grado","autoarchivo"]):
        respuesta += """✍🏻 Solamente es responsabilidad del docente cargar el trabajo de grado al autoarchivo. Debes seguir la guía de auto-archivo disponible en la sección de Trabajos de Grado de la web. Asegúrate de tener el formato de autorización firmado y el archivo en PDF.

👉 [Depósitos](https://primo.utb.edu.co/deposit/57UTB_INST&auth=SAML)

"""

    # 🔎 BÚSQUEDA DE LIBROS (SOLO SI ES BÚSQUEDA REAL)
    palabras_busqueda = [
        "buscar", "busco", "buscame",
        "quiero leer", "necesito el libro", "estoy buscando"
    ]
    
    if (
        any(p in mensaje for p in palabras_busqueda)
        and not any(p in mensaje for p in [
            "como", "cómo",   # 🔥 CLAVE: bloquea preguntas explicativas
            "renov", "prest", "reserv", "ubicar", "estanter"
        ])
    ):
        consulta = limpiar_consulta(mensaje).strip()
    
        if consulta:
            consultas = separar_consultas(consulta)
    
            texto = "🔎 Encontré esto:\n\n"
    
            for c in consultas:
                link = generar_link_primo(c)
                texto += f"📚 **{c.capitalize()}**\n👉 [Ver en PRIMO]({link})\n\n"
    
            respuesta += texto
            
# 📚 BASE DE CONOCIMIENTO (CLAVE)
    for item in base_conocimiento:
        if any(p in mensaje for p in item["claves"]):
            respuesta += item["respuesta"] + "\n\n"
            break

            
    # ❌ SI NO HAY RESPUESTA
    if not respuesta:
        return random.choice([
            "No tengo esa información 😅",
            "Puedes preguntarme sobre libros, horarios, servicios y más 📚"
        ])

    # ✅ RESPUESTA FINAL
    return saludo + respuesta

chat = gr.ChatInterface(
    responder,
    title="📚 Biblioteca UTB",
    description="Asistente virtual de la biblioteca",
    chatbot=gr.Chatbot(
        value=[
            {
                "role": "assistant",
                "content": "👋 ¡Hola! Soy tu asistente de la biblioteca UTB 📚\n\nPuedo ayudarte con:\n📊Bases de datos\n🔎Búsqueda de libros\n🎓Capacitaciones\n📷Fototeca\n📅Horarios\n🧾Paz y salvo\n📗Préstamos y renovación\n📄Reglamento\n👩🏻‍💻Repositorio\n💻Servicios\n✍🏻Trabajos de grado\n\n¿En qué te ayudo?"
            }
        ]
    )
)

chat.launch(ssr_mode=False)