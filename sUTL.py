from hxsUTL2 import Sutl, _hx_AnonObject

class sUTL():
    _s = None
    
    @classmethod
    def _isObject(cls, obj):
        return isinstance(obj, dict)
    
    @classmethod
    def _isSequence(cls, obj):
        return isinstance(obj, list) or isinstance(obj, set) or isinstance(obj, tuple)
    
    @classmethod
    def _toHx(cls, aObj):
        if cls._isObject(aObj):
            convDict = {key: cls._toHx(aObj[key]) for key in aObj}
            return _hx_AnonObject(convDict)
        elif cls._isSequence(aObj):
            return [cls._toHx(litem) for litem in aObj]
        elif isinstance(aObj, str):
            return unicode(aObj)
        else:
            return aObj

    @classmethod
    def _fromHx(cls, aObj):
        if isinstance(aObj, _hx_AnonObject):
            retval = dict(aObj.__dict__)
            retval = {key: cls._fromHx(retval[key]) for key in retval}
            return retval
        elif cls._isSequence(aObj):
            return [cls._fromHx(litem) for litem in aObj]
        else:
            return aObj

    def sutl(self):
        if not self._s:
            self._s = Sutl()
        return self._s
    
    @classmethod
    def version(cls):
        return Sutl.version()
    
    def evaluate(self, s, t, l, h):
        shx = self._toHx(s)
        thx = self._toHx(t)
        lhx = self._toHx(l)
        hhx = self._toHx(h)
        rhx = self.sutl().evaluate(shx, thx, lhx, hhx)
        r = self._fromHx(rhx)
        return r 

    def evaluatehx(self, shx, thx, lhx, hhx):
        rhx = self.sutl().evaluate(shx, thx, lhx, hhx)
        return rhx

    def _evaluate(self, s, t, l, src, tt, b, h):
        shx = self._toHx(s)
        thx = self._toHx(t)
        lhx = self._toHx(l)
        srchx = self._toHx(src)
        tthx = self._toHx(tt)
        bhx = self._toHx(b)
        hhx = self._toHx(h)
        rhx = self.sutl()._evaluate(shx, thx, lhx, srchx, tthx, bhx, hhx)
        r = self._fromHx(rhx)
        return r 
        
    def compilelib(self, decls, dists):
        declshx = self._toHx(decls)
        distshx = self._toHx(dists)
        librhx = self.sutl().compilelib(declshx, distshx)
        libr = self._fromHx(librhx)
        return libr

    def builtins(self):
        bhx = self.sutl().builtins()
        return self._fromHx(bhx)
        