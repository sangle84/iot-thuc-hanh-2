import json
import random
import time

import pika

QUEUE_NAME = 'sensor_data_queue'


def main():
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', port=5672)
        )
        channel = connection.channel()
        channel.queue_declare(queue=QUEUE_NAME, durable=True)

        device_id = 'sensor-01'
        while True:
            payload = {
                'device_id': device_id,
                'temperature': round(random.uniform(20.0, 50.0), 2),
                'humidity': round(random.uniform(30.0, 80.0), 2),
            }

            channel.basic_publish(
                exchange='',
                routing_key=QUEUE_NAME,
                body=json.dumps(payload),
                properties=pika.BasicProperties(delivery_mode=2),
            )
            print(f"[Sensor Producer] Gui dulieu: {payload}")
            time.sleep(3)
    except KeyboardInterrupt:
        print('\n[Sensor Producer] Dung chuong trinh.')
    except Exception as exc:
        print(f"[Sensor Producer] Khong the ket noi RabbitMQ: {exc}")
        print('Vui long kiem tra RabbitMQ da chay tren localhost:5672')


if __name__ == '__main__':
    main()
