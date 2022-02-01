
object = {"a":{"b":{"c":"d"}}}

def get_value(obj,key):
    keys = []
    value = {}
    while type(value) == dict:
        keys.append(list(obj.keys())[0])
        value = list(obj.values())[0]
        obj = list(obj.values())[0]
    if key in keys:
        print(value)
    else:
        print("Invalid Key")
 
get_value(object,"a")