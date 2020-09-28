# JsonFlattener
Simple JsonFlattener and tool to get all values of a given key

    NAME
        jsonFlattener

    DESCRIPTION
        JSON Flattener to flatten json with the given key separator.
        Get the value of a key with

    CLASSES
        builtins.object
            JSONFlattener

    class JSONFlattener(builtins.object)
     |  JSONFlattener(data: dict)
     |
     |  JSON Flattener to flatten json with the given key separator.
     |  Get the value of a key with
     |
     |  Methods defined here:
     |
     |  __init__(self, data: dict)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  flattenjson(self) -> dict
     |      Returns flattened dictionary
     |
     |  getvalue(self, keyvalue: str) -> dict
     |      Returns all values for given key
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
