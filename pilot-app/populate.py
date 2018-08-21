from random import randint, choice
import mlab
# from models.service import Service
from models.customer import Customer
from faker import Faker
mlab.connect()
fake = Faker()

# for i in range(50):
#     print("Saving service", i + 1, "....")
#     new_service = Service(
#         name = fake.name(),
#         yob = randint(1990, 2000),
#         gender = randint(0,1),
#         height = randint(150, 190),
#         phone = fake.phone_number(),
#         address = fake.adress(),
#         status = choice([True, False])
    # )
for i in range(20):
    print("Saving cusomer", i + 1, "...")
    new_customer = Customer(
        name = fake.name(),
        yob = randint(1980,2000),
        gender = randint(0,1),
        phone = fake.phone_number(),
        job = fake.job(),
        company = fake.company(),
        contacted = choice([True, False])
    )
    new_customer.save()
