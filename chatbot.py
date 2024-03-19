import re
import unicodedata
import sys
import random


class Base:
    habitats = {
        "desierto": ["dromedarios", "camello", "lince rojo", "licaon", "tortuga africana", "papion sagrado", "borrego cimarron", "tarantula", "lobo mexicano"],
        "pastizales": ["loro gris", "puerco espin", "hiena", "tortuga aldabra", "tortuga mapini", "tortuga leopardo", "tortuga patas amarillas", "tortuga patas rojas", "leon africano", "rinoceronte blanco", "antilope acuatico", "ganso egipcio", "antilope sable", "hipopotamo", "ganso chino", "antilope orix", "antilope ñu", "cebra", "jirafa", "gallina de guinea", "grulla coronada", "avestruz", "antilope nilgo", "venado cerdo", "muflon europeo", "antilope gemsbock", "wallaby", "canguro rojo", "llama", "antilope nyala", "bisonte americano", "liebre de la patagonia"],
        "franja costera": ["pinguino","foca", "lobo marino"],
        "tundra": ["oso polar"],
        "aviario": ["flamenco", "cisne", "aguila real", "halcon peregrino", "condor de los andes", "aguila cola blanca", "aguila rojinegra", "aguililla cola roja", "aguila caminera", "zopilote rey", "buho", "caracara", "zopilote comun", "condor de california", "pato pijiji", "emú"],
        "bosque templado": ["xoloitzcuintle", "venado cola blanca", "pavo real", "guajolote norteño", "teporingo", "mono japones", "mapache", "cacomixtle", "zorrillo", "oso pardo", "caracal", "lobo canadiense", "gamo", "zorro artico", "panda rojo", "panda gigante", "venado sika", "wapiti", "lobo mexicano", "tigre de sumatra"],
        "bosque tropical": ["ajolote", "jaguar negro", "ocelote", "capibara", "cotorra de la patagonia", "mono ardilla", "jaguar", "mono araña", "capuchino de cuernos", "coati", "martucha", "capuchino de gargante blanca", "oso de anteojos", "binturong", "mono rhesus", "mono araña", "chimpance", "puma", "paloma verde", "venado temazate", "aguti dorado", "orangutan", "cocodrilo", "titi de goeldi", "titi cabeza de leon dorado", "titi copete de algodon", "gorila", "pantera", "leopardo", "tapir", "mono patas", "tigre de bengala"]
    }

    habitats_2 = {
        "desierto": ["dromedarios", "camellos", "linces rojos", "licaones", "tortugas africanas", "papiones sagrados", "borregos cimarrones", "tarantulas", "lobos mexicanos"],
        "pastizales": ["loros grises", "puerco espines", "hienas", "tortugas aldabra", "tortugas mapini", "tortugas leopardos", "tortugas patas amarillas", "tortugas patas rojas","tortugas", "leones africanos","leones",'leones', "rinocerontes blancos", "antilopes acuaticos", "gansos egipcios", "antilopes sable", "hipopotamos", "gansos chino", "antilopes orix", "antilopes ñu", "cebras", "jirafas", "gallinas de guinea", "grullas coronadas", "avestruzes", "antilopes nilgo", "venados cerdo", "muflones europeos", "antilopes gemsbock", "wallabys", "canguros rojo", "llamas", "antilopes nyala", "bisontes americanos", "liebres de la patagonia"],
        "franja costera": ["pinguinos","focas", "lobos marinos"],
        "tundra": ["osos polares"],
        "aviario": ["flamencos", "cisnes", "aguilas reales", "halcones peregrinos", "condores de los andes", "aguilas cola blanca", "aguilas rojinegra", "aguilillas cola roja", "aguilas camineras", "zopilotes rey", "buhos", "caracaras", "zopilotes comunes", "condores de california", "patos pijiji", "emús"],
        "bosque templado": ["xoloitzcuintles", "venados cola blanca", "pavos reales", "guajolotes norteños", "teporingos", "monos japoneses", "mapaches", "cacomixtles", "zorrillos", "osos pardos", "caracales", "lobos canadienses", "gamos", "zorros artico","pandas", "pandas rojos", "pandas gigantes", "venados sika", "wapitis", "lobos mexicanos", "tigres de sumatra"],
        "bosque tropical": ["ajolotes", "jaguares negros", "ocelotes", "capibaras", "cotorras de la patagonia", "monos ardilla", "jaguares", "monos araña", "capuchinos de cuernos", "coatis", "martuchas", "capuchinos de gargante blanca", "osos de anteojos", "binturong", "monos rhesus", "monos araña", "chimpances", "pumas", "palomas verdes", "venados temazates", "agutis dorados", "orangutanes", "cocodrilos", "titis de goeldi", "titis cabeza de leon dorado", "titis copete de algodon", "gorilas","panteras", "leopardos", "tapires", "monos patas", "tigres de bengala"]
    }


    def get_habitat(self, animal):
        for habitat, animals in self.habitats.items():
            if animal in animals:
                return habitat
        return None


    def get_habitats(self):
        return list(self.habitats.keys())


    def get_animals(self):
        animals = []
        for habitat in self.habitats.values():
            animals.extend(habitat)
        return animals
    
    #Plurales
    def get_habitat_2(self, animal_plural):
        for habitat, animals in self.habitats_2.items():
            if animal_plural in animals:
                return habitat
        return None

    def get_animals_2(self):
        animals = []
        for habitat in self.habitats_2.values():
            animals.extend(habitat)
        return animals

class ChatBot:

    #Constructor
    def __init__(self):
        pass


    #Regresa una respuesta en base al mensaje que escribio el usuario
    def get_response(self, user_input):
        return self.check_all_messages(self.clean_str(user_input))


    #Devuelve la cadena depurada dentro de una lista
    def clean_str(self, str):
    
        #Removemos acentos
        accents = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
        str_normalized = unicodedata.normalize('NFD', str)
        str = str_normalized.translate(accents)
        
        #Removemos caracteres especiales
        str = re.split(r'\s|[,.:;¿?¡!-_#$%&/1234567890]\s*', str.lower())
        
        for i in range(str.count('')):
            str.remove('')
        
        return str
    

    #Calcula la probabilidad de más de una posible respuesta en base a una serie de parametros
    def message_probability(self, user_message, recognized_words, single_response=False, required_word=[]):
        message_certainty = 0
        has_required_words = True

        #Recorrido del mensaje para encontra palabras clave
        for word in user_message:
            if word in recognized_words:
                message_certainty +=1

        #percentage = float(message_certainty) / float (len(recognized_words))

        #Recorrido del mensaje para encontrar palabra obligatoria
        for word in required_word:
            if word not in user_message:
                has_required_words = False
                break

        #Regresa la certeza del mensaje
        if has_required_words or single_response:
            return message_certainty
        else:
            return 0

    #Revisa el mensaje enviado por el usuario y busca palabras clave para escojer una respuesta
    def check_all_messages(self, message):
            highest_prob = {}
            bd = Base()

            def response(bot_response, list_of_words, single_response = False, required_words = []):
                nonlocal highest_prob
                highest_prob[random.choice(bot_response)] = self.message_probability(message, list_of_words, single_response, required_words)

 
            #Respuestas a saludos
            response(['Hola, ¿puedo ayudarte en algo?', 'Gracias por saludar, ¿puedo servirte en algo?'], ['hola', 'tal', 'saludos', 'buenas', 'tardes', 'buenos', 'dias'], single_response=True)
            #Respuestas a despedidas
            response(['¡Nos vemos!','Hasta luego...'],['adios','hasta','luego','nos','vemos','bye','me','voy'], single_response=True)
            #Respuestas a agradecimientos
            response(['De nada, me alegro haber sido de utilidad', '¡Es un placer!', '¡De nada!'], ['gracias', 'agradezco', 'thanks','ha','sido','util','utilidad','agradecer','agradecerte'], single_response=True)
            #Respuestas de ¿Como estas?
            response(['Me siento bien, ¿que tal tú?', 'Estoy bien, ¿y tú?'], ['estas', 'va', 'vas', 'sientes','sentir'])
            #Respuestas existenciales 
            response(['Soy una IA con el único proposito de responder algunas preguntas acerca del zoológico de Chapultepec, ¿requieres alguna información?'],['eres', 'quien', 'haces', 'limitaciones', 'existes', 'crearon', 'humano'], single_response=True)
            #Respuestas de pago por entrada
            response(['La entrada al zoológico es totalmente gratis', 'No se cobra por la entrada al zoológico'], ['entrada', 'visita', 'entrar', 'visitar'], single_response=True)
            #Respuestas de estacionamiento
            response(['Hay más de un estacionamiento en la zona, da click el siguiente enlace para conocer más detalles de estos. https://www.chapultepec.org.mx/wp-content/uploads/2019/01/estacionamientos-y-ban%CC%83os.pdf'],['estacionamiento', 'entrar', 'estacionarme', 'carro', 'auto', 'aparcar', 'estacionar', 'aparcamiento'], single_response=True)
            #Respuestas a horario
            response(['El zoológico abre de Martes a Domingo de 9:00 AM hasta las 4:30 PM, los días lunes no abre.'],['horario','apertura','cierre','hora','dias','abren'], single_response=True)
            #Respuestas a servicios
            response(['El zoológico cuenta con diversos servicios, puedes mirar un mapa para encontrar lo que buscas en el siguiente link. http://data.sedema.cdmx.gob.mx/zoo_chapultepec/mapa/'],['alimentos','salidas','banos','emergencia','telefonos','sanitarios','oficinas','puntos','reunion','area','educativa','primeros','auxilios','sillas','ruedas','paqueteria','venta','mapas','guias','servicios','comida','comer'],single_response=True)                 
            #Respuesta a No
            response(['¿No? Está bien'],['no'])
            #Respuesta a Sí
            response(['Vale'],['si'])
            #Respuesta sobre su nombre
            response(['¡Mi nombre es Doge Guide y estoy listo para ayudarte a explorar el zoologico!', 'Soy Doge Guide y me encantara ayudarte en cualquiera de tus dudas'],['llamas', 'nombre', 'llamarte', 'identificas', 'identifiquese'], single_response=True)
            #Respuestas habitats disponibles
            response(['Los habitats disponibles son: ' + ', '.join(bd.get_habitats())], ['habitat', 'habitats', 'biomas', "seccion", "secciones", "partes"], single_response=True)
            #Respuestas a mapa
            response(['El mapa del zoologico se encuentra en el siguiente link. http://data.sedema.cdmx.gob.mx/zoo_chapultepec/mapa/'],['mapa'],single_response=True)
            

            #Respuestas habitats de animales en singular
            for animal in bd.get_animals():
                    
                    cutted_str = animal.split()

                    key_words = cutted_str + ['habitat', 'busco','donde', 'esta', 'encontrar','estan', 'ubicacion','buscar']
                    
                    response([f"El/La {animal.title()} se encuentra en la sección {bd.get_habitat(animal).upper()}."], key_words, single_response=True)

            #Respuestas habitats de animales en plural
            for animal in bd.get_animals_2():
                    
                    cutted_str = animal.split()

                    key_words = cutted_str + ['habitat', 'busco','encontrar', 'ubicacion','buscar']
                    
                    response([f"Las/Los {animal.title()} se encuentran en la sección {bd.get_habitat_2(animal).upper()}."], key_words, single_response=True)

            #Respuestas a animales que no logró encontrar
            response(['No logre encontrar esos animales en el zoologico, lo lamento'],['buscar','habitat', 'encontrar','ubicacion','busco'],single_response=True)


            # Respuesta a preguntas sobre los animales
            response(['Los animales que hay son: ' + ', '.join(bd.get_animals())],
                      ['animales'], single_response=True)



            best_match = max(highest_prob, key=highest_prob.get)

            return self.unknown() if highest_prob[best_match] < 1 else best_match


    #Respuestas para mensajes que no entiende
    def unknown(self):
        response = random.choice(['¿Puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'No entiendo tu pregunta', 'No puedo responder esa pregunta'])
        return response
