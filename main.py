import tweepy, re, time
import threading
from random import randint

def crear_bot():
    """Esta función crea el bot y devuelve la api lista para su uso. 
    Aquí se deben reemplazar las claves. """
    
    consumer_key = 'Og049lLlEW59rMkpC5Z21Z8wq'
    consumer_secret = '13ZpqfHdp1LVAk5LgqWbsEuFrZu93ciXqKtDZGarsySYmASABs'
    key = '1243252730662735872-IAzn9xgrnM9GCGaeQvasZ8IosOEhP1'
    secret = 'aFK6ki8h1BZkbMAQryFuSZpv3LJzgkKXZc3lVWGlBRZ0Y'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

COLA = 'queue.txt'

def chequear_imagen(imagen_seleccionada):
    cont = 0
    for imagen in imagenes_posteadas:
        if imagen_seleccionada == imagen:
            cont = cont + 1
    if cont > 0:
        return True
    else:
        return False

def leer_cola(COLA):
    """ Lee los números de las imágenes que ya se han publicado. """
    cola = open(COLA, 'r')
    imagenes_posteadas_recibidas = cola.read().split(',')
    cola.close()
    imagenes_posteadas = [int(x) for x in imagenes_posteadas_recibidas]
    return imagenes_posteadas

def guardar_cola(COLA, imagenes_posteadas):
    """ Actualiza la cola con las imágenes publicadas. """
    cola = open(COLA, 'w')
    cola.write(str(imagenes_posteadas)[1:-1]) #Guarda la lista sin los paréntesis
    cola.close()
    return

def extraer_tweet(path=None):
    if not path:
        return "No se abrió ningún archivo"
    try:
        with open(path, 'r', encoding='utf-8', errors='surrogateescape') as book:
            text = book.read()
        if text:
            return buscar_tweet(text)
    except:
        return "Archivo no encontrado"

def buscar_tweet(text):
    status = 200
    while not (5 < status < 125):

        index = randint(0,len(text))

        init_index = text[index:].find('"') + index + 1
        last_index = text[init_index:].find('"') + init_index
        status = len(text[init_index:last_index])

    tweet = re.sub("\n", " ", text[init_index:last_index])
    return tweet

def post():
    while True:
        api = crear_bot()
        reply = extraer_tweet("text.txt")
        try:
            api.update_status(str(reply))
            print("===== Tweet posteado correctamente ===== \n")
        except tweepy.TweepError as e:
            print("Error: " + str(e))
        time.sleep(43200) #12 horas // Periodo de publicación de las imágenes

def post_imagen():
    while True:
        api = crear_bot()

        #Seleccione un número que no esté en la lista
        is_repeated = True
        while is_repeated:
            imagen_seleccionada = randint(0,7) #Número de la primera imagen (0) y de la última.
            is_repeated = chequear_imagen(imagen_seleccionada)

        #Si no está en la lista, se publica
        try:
            api.update_status_with_media("", f'images\{imagen_seleccionada}.png')
            print(f"Imagen número {imagen_seleccionada} posteada correctamente.")
        except:
            print("La imagen no pudo ser publicada. Error de la API.")

        #Actualiza la pila
        if len(imagenes_posteadas) < 5: #Número de números a almacenar en la cola
            imagenes_posteadas.append(imagen_seleccionada)
        else:
            imagenes_posteadas.append(imagen_seleccionada)
            imagenes_posteadas.pop(0)

        print(imagenes_posteadas)
        print("\n")

        #Delay y persistencia de la lista
        guardar_cola(COLA, imagenes_posteadas)
        time.sleep(259200) #72 hours

if __name__ == '__main__':
    imagenes_posteadas = leer_cola(COLA)

    hilo_1 = threading.Thread(target=post)
    hilo_2 = threading.Thread(target=post_imagen)

    hilo_1.start()
    hilo_2.start()