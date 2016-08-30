
import pymongo

client = pymongo.MongoClient("127.0.0.1", 27017)  # ip或者127.0.0.1
db = client.get_database("yanglao")
collection = db.get_collection("fp_trans_p1")

