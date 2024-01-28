from faker import Faker

fake = Faker()

payload = {
    "email": fake.email(),
    "password": fake.password(),
    "name": fake.name()
}
