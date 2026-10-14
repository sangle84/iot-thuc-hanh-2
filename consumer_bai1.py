import pika
from datetime import datetime

QUEUE_NAME = 'iot_lab_queue'


def callback(ch, method, properties, body):
    message = body.decode('utf-8')
    print(f"[Consumer] Nhận lúc {datetime.now().strftime('%H:%M:%S')} - {message}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', port=5672)
        )
        channel = connection.channel()

        channel.queue_declare(queue=QUEUE_NAME, durable=True)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)

        print(f"[Consumer] Dang cho tin nhan trong queue '{QUEUE_NAME}'...")
        channel.start_consuming()
    except Exception as exc:
        print(f"[Consumer] Khong the ket noi RabbitMQ: {exc}")
        print('Vui long kiem tra RabbitMQ da chay tren localhost:5672')


if __name__ == '__main__':
    main()
