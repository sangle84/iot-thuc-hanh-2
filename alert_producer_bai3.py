import sys

import pika

EXCHANGE_NAME = 'iot_alert_exchange'


def main():
    if len(sys.argv) < 3:
        print('Usage: python alert_producer_bai3.py <warning|critical|info> "message"')
        return

    routing_key = sys.argv[1].strip().lower()
    message = ' '.join(sys.argv[2:])

    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', port=5672)
        )
        channel = connection.channel()

        channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='direct', durable=True)
        channel.basic_publish(
            exchange=EXCHANGE_NAME,
            routing_key=routing_key,
            body=message,
            properties=pika.BasicProperties(delivery_mode=2),
        )
        print(f"[Alert Producer] Gui message voi routing key '{routing_key}': {message}")
        connection.close()
    except Exception as exc:
        print(f"[Alert Producer] Khong the ket noi RabbitMQ: {exc}")
        print('Vui long kiem tra RabbitMQ da chay tren localhost:5672')


if __name__ == '__main__':
    main()
