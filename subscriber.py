import redis

CHANNEL = 'Comunicaciones'


if __name__ == '__main__':

    # Conexión con el servidor
    client = redis.StrictRedis(
        host='localhost',
        port=6379,
        db=0
    )

    subscription = client.pubsub()
    subscription.subscribe(CHANNEL)

    print(f'A la espera de mensajes para el canal {CHANNEL}')

    while True:

        message = subscription.get_message()
        if message and message.get('data') and message['data'] != 1:
            payload = message['data'].decode()

            print(payload)
