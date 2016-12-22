
class Util2:
    _hx_class_name = "Util2"
    _hx_statics = ["isObject", "isArray", "isString", "isSequence", "isInt", "isNumber", "isBool"]

    @staticmethod
    def isObject(obj):
        #print obj
        return obj and obj.__class__.__name__ == "_hx_AnonObject"

    @staticmethod
    def isArray(obj):
        return isinstance(obj, list)

    @staticmethod
    def isString(obj):
        return isinstance(obj, basestring)

    @staticmethod
    def isSequence(obj):
        return (Util2.isArray(obj) or Util2.isString(obj))

    @staticmethod
    def isInt(obj):
        return isinstance(obj, int)

    @staticmethod
    def isNumber(obj):
        return isinstance(obj, (int, float, long)) and not Util2.isBool(obj)

    @staticmethod
    def isBool(obj):
        return isinstance(obj, bool)

Util2._hx_class = Util2
