import string
import random
from django.utils.text import slugify


def generate_random_character(c=11):
    characters = string.ascii_lowercase + string.digits
    random_slug = []
    for _ in range(c):
        random_slug.append(random.choice(characters))
    return ''.join(random_slug)
    
def generate_slugify(text):
    return slugify(str(text))
