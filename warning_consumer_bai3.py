import pika

EXCHANGE_NAME = 'iot_alert_exchange'
QUEUE_NAME = 'warning_queue'
ROUTING_KEY = 'warning'


def callback(ch, method, properties, body):
    message = body.decode('utf-8')
    print(f"[Warning Consumer] Nhan thong bao: {message}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', port=5672)
        )
        channel = connection.channel()

        channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='direct', durable=True)
        channel.queue_declare(queue=QUEUE_NAME, durable=True)
        channel.queue_bind(exchange=EXCHANGE_NAME, queue=QUEUE_NAME, routing_key=ROUTING_KEY)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)

        print(f"[Warning Consumer] Dang lang nghe routing key '{ROUTING_KEY}'...")
        channel.start_consuming()
    except Exception as exc:
        print(f"[Warning Consumer] Khong the ket noi RabbitMQ: {exc}")
        print('Vui long kiem tra RabbitMQ da chay tren localhost:5672')


if __name__ == '__main__':
    main()
