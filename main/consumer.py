import pika, json

# from product.models import Product


params = pika.URLParameters("your_rabbitmq_url")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="main")


def callback(ch, method, properties, body):
    print("Received in main")
    data = json.loads(body)
    print(properties.content_type)
    print(data)

    if properties.content_type == "product_created":
        # product = Product()
        # product.id = data["id"]
        # product.title = data["title"]
        # product.image = data["image"]
        # product.save()
        print("Product Created")

    elif properties.content_type == "product_updated":
        # product = Product.objects.get(id=data["id"])
        # product.title = data["title"]
        # product.image = data["image"]
        # product.save()
        print("Product Updated")

    elif properties.content_type == "product_deleted":
        # product = Product.objects.get(data)
        # product.delete()
        print("Product Deleted")


channel.basic_consume(queue="main", on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
