from util2 import Util2

_keywords = set(["and", "del", "from", "not", "with", "as", "elif", "global", "or", "yield", "assert", "else", "if", "pass", "None", "break", "except", "import", "raise", "True", "class", "exec", "in", "return", "False", "continue", "finally", "is", "try", "def", "for", "lambda", "while"])

class Util3:
    _hx_class_name = "Util3"
    _hx_statics = ["isBuiltinEval", "isStringBuiltinEval", "isEval", "isEval2", "isQuoteEval", "isDoubleQuoteEval", "isColonEval", "isDictTransform", "isListTransform", "isTruthy", "isPrefix"]

    @staticmethod
    def isBuiltinEval(obj):
        return (Util2.isObject(obj) and hasattr(obj, "&"))

    @staticmethod
    def isEval(obj):
        return (Util2.isObject(obj) and hasattr(obj, "!"))

    @staticmethod
    def isEval2(obj):
        return (Util2.isObject(obj) and hasattr(obj, "!!"))

    @staticmethod
    def isQuoteEval(obj):
        return (Util2.isObject(obj) and hasattr(obj, "'"))

    @staticmethod
    def isDoubleQuoteEval(obj):
        return (Util2.isObject(obj) and hasattr(obj, "''"))

    @staticmethod
    def isColonEval(obj):
        return (Util2.isObject(obj) and hasattr(obj, ":"))

    @staticmethod
    def isDictTransform(obj):
        return Util2.isObject(obj)

    @staticmethod
    def isListTransform(obj):
        return Util2.isArray(obj)

    @staticmethod
    def isTruthy(aObj):
        retval = False
        if Util2.isArray(aObj):
            retval = len(aObj) > 0
        elif Util2.isString(aObj):
            retval = (aObj != "")
        elif Util2.isNumber(aObj):
            retval = (aObj != 0)
        elif Util2.isBool(aObj):
            retval = aObj
        elif Util2.isObject(aObj):
            retval = (len((aObj.__dict__).keys()) > 0)
        else:
            retval = (aObj is not None)
        return retval

    @staticmethod
    def isPrefix(str1,str2):
        return (str2.find(str1) == 0)


    @staticmethod
    def get(obj,key, adef = None):
        retval = None
        
        if Util2.isObject(obj):
            if key in _keywords:
                key1 = "_hx_%s" % key
            else:
                key1 = key
            retval = getattr(obj, key1) if hasattr(obj, key1) else None
        if (retval is None):
            retval = adef
        return retval

Util3._hx_class = Util3
