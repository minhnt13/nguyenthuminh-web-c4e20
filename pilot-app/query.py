from models.service import Service
import mlab

mlab.connect()
id_to_find = "5b78268be58fb90dc0904e1d"
all_service = Service.objects()
# hera = Serivce.objects(id=id_to_find)
# hera = Service.objects.get(id_to_find)
service = Service.objects.with_id(id_to_find)
# first_service = all_service[0]
# print(first_service["name"])
if service is not None:
    # service.delete()
    service.update(set__yob=2000)
    service.reload()
    print(service.to_mongo())
    print("Deleted")
else:
    print("Not found")