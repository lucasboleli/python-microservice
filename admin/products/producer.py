import pika, json

params = pika.URLParameters(
    "amqps://plpywkxr:muD8F93b3IEE5egS_4B1yY5cap8I5Xbi@moose.rmq.cloudamqp.com/plpywkxr"
)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange="", routing_key="main", body=json.dumps(body), properties=properties
    )
