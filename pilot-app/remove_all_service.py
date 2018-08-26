from models.service import Service
import mlab
mlab.connect()
all_service = Service.objects()
for index,service in enumerate(all_service):
    print("Deleted", index + 1)
    service.delete()
print("All deleted")
# all_service.delete()
