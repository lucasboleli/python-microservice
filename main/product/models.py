from django.db import models


class Product(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)


class ProductUser(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name="user_product",
                fields=["user_id", "product_id"],
            ),
        ]
