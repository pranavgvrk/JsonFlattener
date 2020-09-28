'''
JSON Flattener to flatten json with the given key separator.
Get the value of a key with
'''

import json
import re


class JSONFlattener:
    '''
    JSON Flattener to flatten json with the given key separator.
    Get the value of a key with
    '''
    def __init__(self, data: dict):
        if isinstance(data, dict):
            self.__data = data
        elif isinstance(data, str):
            self.__data = json.loads(data)
        else:
            raise TypeError('Input should be a stringified json or dict type')
        self.__dict = {}
        self.__jflatten(self.__data)

    def __jflatten(self, data: dict, parentkey: str = '') -> dict:
        if isinstance(data, dict):
            for key, value in data.items():
                self.__jflatten(value, f'{parentkey}.{key}')
        elif isinstance(data, list):
            for key, value in enumerate(data):
                self.__jflatten(value, f'{parentkey}.{key}')
        else:
            self.__dict[parentkey] = data

    def flattenjson(self) -> dict:
        '''
        Returns flattened dictionary
        '''
        return self.__dict

    def getvalue(self, keyvalue: str) -> dict:
        '''
        Returns all values for given key
        '''
        pattern = fr"{keyvalue}$"
        matchedvalues = {}
        for key, value in self.__dict.items():
            matches = re.search(pattern, key)
            if matches and key[matches.start() - 1] == key[0]:
                matchedvalues[key] = value
        return matchedvalues
