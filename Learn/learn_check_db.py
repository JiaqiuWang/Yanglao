
import pymongo

client = pymongo.MongoClient("127.0.0.1", 27017)  # ip或者127.0.0.1
db = client.get_database("yanglao")
collection = db.get_collection("fp_trans_p1")
cursor_var = collection.find({}, {"_id": 0, "times": 0, "trans_no": 0,
                                  "pPer_id": 0}).limit(100)
for var_doc in cursor_var:
    print("var_doc_service_name:", var_doc.get("service_name"))
    for var_dict in var_doc:
        print("key:", str(var_dict), ", value:", str(var_doc[var_dict]))
        item_layer3 = \
            str(var_dict) + ":" + str(var_doc[var_dict])
        print(item_layer3)
