import pika

params = pika.URLParameters(
    "amqps://plpywkxr:muD8F93b3IEE5egS_4B1yY5cap8I5Xbi@moose.rmq.cloudamqp.com/plpywkxr"
)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue="admin")


def callback(ch, method, properties, body):
    print("received in admin")
    print(body)


channel.basic_consume(queue="admin", on_message_callback=callback, auto_ack="true")

print("started consuming")
channel.start_consuming()
channel.close()
