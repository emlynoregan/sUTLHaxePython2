


#from util2 import Util2

# _keywords = set(["and", "del", "from", "not", "with", "as", "elif", "global", "or", "yield", "assert", "else", "if", "pass", "None", "break", "except", "import", "raise", "True", "class", "exec", "in", "return", "False", "continue", "finally", "is", "try", "def", "for", "lambda", "while"])

class UtilReflect:
    _hx_class_name = "UtilReflect"
    _hx_statics = ["fields", "hasField", "field", "setField", "deleteField"]

    @staticmethod
    def calckey(key):
        return "_hx_%s" % key if key in python_Boot.keywords else key
    
    @staticmethod
    def fields(obj):
        return python_Boot.fields(obj)
#     @staticmethod
#     def fields(obj):
#         retval = None
#          
#         if Util2.isObject(obj):
#             retval = [UtilReflect.calckey(key) for key in obj.__dict__]
#  
#         return retval

    @staticmethod
    def hasField(obj,fieldname):
        retval = False
        
        if Util2.isObject(obj):
            key1 = UtilReflect.calckey(fieldname)
            retval = hasattr(obj, key1)
        return retval

    @staticmethod
    def field(obj,fieldname):
        retval = None
        
        if Util2.isObject(obj):
            key1 = UtilReflect.calckey(fieldname)
            retval = getattr(obj, key1) if hasattr(obj, key1) else None
        return retval

    @staticmethod
    def setField(obj,fieldname,value):
        if Util2.isObject(obj):
            key1 = UtilReflect.calckey(fieldname)
            setattr(obj, key1, value)

    @staticmethod
    def deleteField(obj,fieldname):
        retval = None
        
        if Util2.isObject(obj):
            key1 = UtilReflect.calckey(fieldname)
            if hasattr(obj, key1):
                delattr(obj, key1)
        return retval

UtilReflect._hx_class = UtilReflect

