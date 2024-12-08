from faker import Faker
import random

fake = Faker()

popular_domains = [
    "gmail.com",
    "yahoo.com",
    "outlook.com",
    "icloud.com",
    "mail.com",
    "mail.ru",
    "yandex.ru"
]

def create_random_user_data():
    unique_email = f"{fake.email().split('@')[0]}_{random.randint(1000, 9999)}@{random.choice(popular_domains)}"
    return {
        "email": unique_email,
        "password": fake.password(),
        "name": fake.name()
    }