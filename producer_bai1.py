import pika

QUEUE_NAME = 'iot_lab_queue'


def main():
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', port=5672)
        )
        channel = connection.channel()

        channel.queue_declare(queue=QUEUE_NAME, durable=True)

        message = 'Xin chao tu producer Bai 1!'
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE_NAME,
            body=message,
            properties=pika.BasicProperties(delivery_mode=2),
        )

        print(f"[Producer] Da gui message vao queue '{QUEUE_NAME}': {message}")
        connection.close()
    except Exception as exc:
        print(f"[Producer] Khong the ket noi RabbitMQ: {exc}")
        print('Vui long kiem tra RabbitMQ da chay tren localhost:5672')


if __name__ == '__main__':
    main()
