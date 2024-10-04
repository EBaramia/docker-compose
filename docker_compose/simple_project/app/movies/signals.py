import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

# Оповещение в случае примьеры фильма 
# def attantion(sender, instance, created, **kwargs):
#     if created and instance.creation_date == datetime.date.today:
#         print(f"Сегодня премьера {instance.title}!")


# post_save.connect(
#     receiver=attantion, 
#     sender='movies.FilmWork', 
#     weak=True, 
#     dispatch_uid='attention_signgl'
#     )

@receiver(post_save, sender="movies.FilmWork")
def attantion(sender, instance, created, **kwargs):
    if created and instance.creation_date == datetime.date.today():
        print(f"Сегодня премьера {instance.title}!")