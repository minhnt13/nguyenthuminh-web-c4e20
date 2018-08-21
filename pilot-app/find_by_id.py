import mlab
from models.service import Service
# mongodb://<dbuser>:<dbpassword>@ds125872.mlab.com:25872/muadongkhonglanh
mlab.connect()
id_to_find = "5b781d9fe58fb90d78d85c4a"
# 1st way
doc_to_find = Service.objects.with_id(id_to_find)
# 2nd way
# doc_to_find = Service.objects.get(id=id_to_find)
if doc_to_find != None:
    print("ID = ", doc_to_find["id"], ",", doc_to_find["name"])
else:
    print("ID not found")
# delete
doc_to_find.delete()
