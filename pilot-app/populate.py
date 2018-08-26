from random import randint, choice, sample, shuffle
import mlab
import glob, os
from models.service import Service
from models.customer import Customer
from faker import Faker
mlab.connect()
fake = Faker()

description = ["ngoan hiền", "dễ thương", "lễ phép với gia đình", "giỏi nhiều loại nhạc cụ", "nấu ăn ngon", "thông thạo nhiều ngoại ngữ", "biết nói tiếng động vật", "biết thảo mai"]
# get image name list
female_image_list = os.listdir(r"..\pilot-app\static\image\female")
male_image_list = os.listdir(r"..\pilot-app\static\image\male")
for i in range(20):
    print("Saving service", i + 1, "....")
    gender = randint(0,1)
    shuffle(description)     
    if gender == 1:
        new_service = Service(
            name = fake.name(),
            yob = randint(1990, 2000),
            gender = gender,
            height = randint(150, 190),
            phone = fake.phone_number(),
            address = fake.address(),
            status = choice([True, False]),
            descriptions = sample(description,3),
            measurements = [randint(80, 90), randint(60, 70), randint(70, 90)],
            image = "../static/image/male/" + male_image_list.pop()
        )
    elif gender == 0:
        new_service = Service(
            name = fake.name(),
            yob = randint(1990, 2000),
            gender = gender,
            height = randint(150, 190),
            phone = fake.phone_number(),
            address = fake.address(),
            status = choice([True, False]),
            descriptions = sample(description,3),
            measurements = [randint(80, 90), randint(60, 70), randint(70, 90)],
            image = "../static/image/female/" + female_image_list.pop()
        )
    new_service.save()

# # for i in range(20):
# #     print("Saving cusomer", i + 1, "...")
# #     new_customer = Customer(
# #         name = fake.name(),
# #         yob = randint(1980,2000),
# #         gender = randint(0,1),
# #         phone = fake.phone_number(),
# #         job = fake.job(),
# #         company = fake.company(),
# #         contacted = choice([True, False])
# #     )
# #     new_customer.save()
