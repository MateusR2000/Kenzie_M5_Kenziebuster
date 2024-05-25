from django.db import models

class MovieRating(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"

class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(
        blank=True,
        max_length=10,
        default=""
    )
    rating = models.CharField(
        max_length=20,
        choices=MovieRating.choices,
        default=MovieRating.G
    )
    synopsis = models.TextField(blank=True, default="")
    user = models.ForeignKey(
        "users.User",
        on_delete=models.PROTECT,
        related_name="movies",
    )

    orders = models.ManyToManyField(
        "users.User",
        related_name="movies_orders",
        through="movies_orders.MovieOrder"
    )

 