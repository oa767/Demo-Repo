"""
This program is written to port text JSON files into Mongo collections.
It assumes the JSON files have the structure:
    {
        "some_fld1": { some more fields },
        "some_fld2": { some more fields },
        .
        .
        .
        "some_fldN": { some more fields },
    }
It assumes that cause that's what we've been using!
"""
import sys
import json
import pymongo as pm


def read_collection(json_version):
    """
    A function to read a colleciton off of disk.
    """
    try:
        with open(json_version) as file:
            return json.loads(file.read())
    except FileNotFoundError:
        print(f"{json_version} not found.")
        return None


def new_ent_from_json(key_name, ent_name, ent_data):
    dict1 = {key_name: ent_name}
    return {**dict1, **ent_data}


client = pm.MongoClient("mongodb+srv://oabouelnour:<cBhCCuTa3adSBKxc>@cluster0.52jag.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", server_api=ServerApi('1'))

if len(sys.argv) < 4:
    # the key in the JSON file will become an ordinary field
    # in the Mongo DB, but we need to give it a name!
    print(f"Usage: {sys.argv[0]} db_name collection_name key_name")
    exit(1)

#db = client[sys.argv[1]]
#print(db)
db = "chatDB"

#collect_nm = sys.argv[2]
#print(f"{collect_nm=}")
#collection = db[collect_nm]
collection = db["rooms"]

#json_file = collect_nm + ".json"
json_file = "rooms.json"
#print(f"{json_file=}")

#key_name = sys.argv[3]
#print(f"{key_name=}")
key_name = "num_users"

collect = read_collection(json_file)

for entity_nm in collect:
    new_entity = new_ent_from_json(key_name,
                                   entity_nm,
                                   collect[entity_nm])
    print(f"{new_entity=}")
    collection.insert_one(new_entity)

print(collection)
print("\n\nSUCCESS!!!\n\n")
