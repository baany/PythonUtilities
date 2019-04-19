import json
import string

def extractValues(jsonObj, key):
    """Pull all values of specified key from nested JSON."""
    resultList = []
    def extract(jsonObj, resultList, key):
        """Recursively search for values of key in JSON tree."""
        if (isinstance(jsonObj, dict)):
            for k, v in jsonObj.items():
                if (isinstance(v, dict)):
                    extract(v, resultList, key)
                elif (k == key):
                    resultList.append(v)
        elif (isinstance(jsonObj, list)):
            for item in jsonObj:
                extract(item, resultList, key)
        return (resultList)

    result = extract(jsonObj, resultList, key)
    return (result)

valueJSON = {'a':1, 'b':[2,'t','g7'], 'c':{'d':123, 'e':'xyz'}}
print (extractValues(valueJSON, 'b'))
