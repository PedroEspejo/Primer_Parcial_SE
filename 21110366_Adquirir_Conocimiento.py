class BaseConocimiento:
    def __init__(self):
        self.conocimiento = {
            "Hola": "¡Hola! ¿Cómo estás?",
            "Como estas?": "Estoy bien, ¿y tú?",
            "de que te gustaría hablar?": "Podemos hablar de cualquier cosa. ¿Tienes algún tema en mente?"
        }

    def obtener_respuesta(self, pregunta):
        if pregunta in self.conocimiento:
            return self.conocimiento[pregunta]
        else:
            return "Lo siento, no entiendo. ¿Podrías proporcionar más información?"

    def agregar_conocimiento(self, pregunta, respuesta):
        self.conocimiento[pregunta] = respuesta


def chat():
    base_de_conocimiento = BaseConocimiento()
    print("Bienvenido al chat. Ingresa 'Salir' para terminar.")

    while True:
        entrada_usuario = input("Tú: ")
        if entrada_usuario.lower() == 'salir':
            print("Adiós. ¡Hasta luego!")
            break

        respuesta = base_de_conocimiento.obtener_respuesta(entrada_usuario)
        print("ChatBot:", respuesta)

        if respuesta == "Lo siento, no entiendo. ¿Podrías proporcionar más información?":
            print("ChatBot: ¿Qué respuesta darías a esa pregunta?")
            respuesta_nueva = input("Tú: ")
            base_de_conocimiento.agregar_conocimiento(entrada_usuario, respuesta_nueva)
            print("ChatBot: Entendido. He aprendido algo nuevo.")

# Ejecutar el chat
chat()