# sample python object
python_data = {'name':'Abebe','age':20,'city':'Addis Abeba'}
python_data = [[1,2,3,4,5]]

# ------------------------------------------------------------------------------#

# 1, using the json module
import json
#serializing python object to JSON string
json_string = json.dumps(python_data)
print(json_string)

# serializing python object to JSON string and writing it to a file
with open("my_file.json",'r+') as file_obj:
    json.dump(python_data,file_obj)
    print(file_obj.read())

#deserializing JSON string to python object
deserialized_data = json.loads(json_string)
print(deserialized_data)

# deserializing JSON string from a file to a python object
with open('my_file.json','r+') as read_jsonfile_obj:
    deserialized_data = json.load(read_jsonfile_obj)
    print(deserialized_data)

# ------------------------------------------------------------------------------#

# 2, using the pickel module
import pickle

#serializing python object to pickel string
pickle_string = pickle.dumps(python_data)
print(pickle_string)
# serializing python object to pickel string and writing it to a file
with open('my_file.pkl','wb') as file_obj:
    pickle.dump(python_data,file_obj)  # writing have 2 parameters
    # print(file_obj.read())  # not supported here

#deserializing pickel string to python object
deserialized_data = pickle.loads(pickle_string)
print(deserialized_data)

# deserializing pickel string from a file to a python object
with open('my_file.pkl','rb') as read_picklefile_obj:
    deserialized_data = pickle.load(read_picklefile_obj)     # reading have 1 parameter
    print(deserialized_data)

# ------------------------------------------------------------------------------#

#  Warning: The pickle module is not secure. Only unpickle data you trust.
