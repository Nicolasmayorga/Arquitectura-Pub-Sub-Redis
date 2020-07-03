import redis

CHANNEL = 'Comunicaciones'


if __name__ == '__main__':

    # Conexión con el servidor
    client = redis.StrictRedis(
        host='localhost',
        port=6379,
        db=0
    )

    # Mensaje del usuario
    message = input('ingresa un mensaje: ')

    # Envío a través del canal
    client.publish(CHANNEL, message)
