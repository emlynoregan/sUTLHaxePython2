from __future__ import unicode_literals
from __future__ import division
from util2 import Util2
from util3 import Util3
str = unicode
import math as python_lib_Math
import math as Math
import functools as python_lib_Functools
import inspect as python_lib_Inspect
import json as python_lib_Json
from io import StringIO as python_lib_io_StringIO


class _hx_AnonObject:
	def __init__(self, fields):
		self.__dict__ = fields


class Enum:
	_hx_class_name = "Enum"
	_hx_fields = ["tag", "index", "params"]
	_hx_methods = ["__str__"]

	def __init__(self,tag,index,params):
		self.tag = None
		self.index = None
		self.params = None
		self.tag = tag
		self.index = index
		self.params = params

	def __str__(self):
		if (self.params is None):
			return self.tag
		else:
			return (((HxOverrides.stringOrNull(self.tag) + "(") + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in self.params]))) + ")")

Enum._hx_class = Enum


class Class:
	_hx_class_name = "Class"
Class._hx_class = Class


class Date:
	_hx_class_name = "Date"
	_hx_fields = ["date"]
	_hx_methods = ["toString"]

	def toString(self):
		m = ((self.date.month - 1) + 1)
		d = self.date.day
		h = self.date.hour
		mi = self.date.minute
		s = self.date.second
		return ((((((((((Std.string(self.date.year) + "-") + HxOverrides.stringOrNull(((("0" + Std.string(m)) if ((m < 10)) else ("" + Std.string(m)))))) + "-") + HxOverrides.stringOrNull(((("0" + Std.string(d)) if ((d < 10)) else ("" + Std.string(d)))))) + " ") + HxOverrides.stringOrNull(((("0" + Std.string(h)) if ((h < 10)) else ("" + Std.string(h)))))) + ":") + HxOverrides.stringOrNull(((("0" + Std.string(mi)) if ((mi < 10)) else ("" + Std.string(mi)))))) + ":") + HxOverrides.stringOrNull(((("0" + Std.string(s)) if ((s < 10)) else ("" + Std.string(s))))))

Date._hx_class = Date


class EnumValue:
	_hx_class_name = "EnumValue"
EnumValue._hx_class = EnumValue


class Reflect:
	_hx_class_name = "Reflect"
	_hx_statics = ["field", "isFunction", "compare", "deleteField", "copy"]

	@staticmethod
	def field(o,field):
		return python_Boot.field(o,field)

	@staticmethod
	def isFunction(f):
		return ((python_lib_Inspect.isfunction(f) or python_lib_Inspect.ismethod(f)) or hasattr(f,"func_code"))

	@staticmethod
	def compare(a,b):
		if ((a is None) and ((b is None))):
			return 0
		if (a is None):
			return 1
		elif (b is None):
			return -1
		elif (a == b):
			return 0
		elif (a > b):
			return 1
		else:
			return -1

	@staticmethod
	def deleteField(o,field):
		if (not hasattr(o,(("_hx_" + field) if (field in python_Boot.keywords) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)))):
			return False
		del o.__dict__[field]
		return True

	@staticmethod
	def copy(o):
		o2 = _hx_AnonObject({})
		_g = 0
		_g1 = python_Boot.fields(o)
		while (_g < len(_g1)):
			f = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
			_g = (_g + 1)
			value = Reflect.field(o,f)
			setattr(o2,(("_hx_" + f) if (f in python_Boot.keywords) else (("_hx_" + f) if (((((len(f) > 2) and ((ord(f[0]) == 95))) and ((ord(f[1]) == 95))) and ((ord(f[(len(f) - 1)]) != 95)))) else f)),value)
		return o2
Reflect._hx_class = Reflect


class Std:
	_hx_class_name = "Std"
	_hx_statics = ["is", "string", "parseInt", "shortenPossibleNumber", "parseFloat"]

	@staticmethod
	def _hx_is(v,t):
		if ((v is None) and ((t is None))):
			return False
		if (t is None):
			return False
		if (t == Dynamic):
			return True
		isBool = isinstance(v,bool)
		if ((t == Bool) and isBool):
			return True
		if ((((not isBool) and (not (t == Bool))) and (t == Int)) and isinstance(v,int)):
			return True
		vIsFloat = isinstance(v,float)
		def _hx_local_0():
			f = v
			return (((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))
		def _hx_local_1():
			x = v
			def _hx_local_4():
				def _hx_local_3():
					_hx_local_2 = None
					try:
						_hx_local_2 = int(x)
					except Exception as _hx_e:
						_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
						e = _hx_e1
						_hx_local_2 = None
					return _hx_local_2
				return _hx_local_3()
			return _hx_local_4()
		if (((((((not isBool) and vIsFloat) and (t == Int)) and _hx_local_0()) and ((v == _hx_local_1()))) and ((v <= 2147483647))) and ((v >= -2147483648))):
			return True
		if (((not isBool) and (t == Float)) and isinstance(v,(float, int))):
			return True
		if (t == str):
			return isinstance(v,str)
		isEnumType = (t == Enum)
		if ((isEnumType and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_constructs")):
			return True
		if isEnumType:
			return False
		isClassType = (t == Class)
		if ((((isClassType and (not isinstance(v,Enum))) and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_class_name")) and (not hasattr(v,"_hx_constructs"))):
			return True
		if isClassType:
			return False
		def _hx_local_6():
			_hx_local_5 = None
			try:
				_hx_local_5 = isinstance(v,t)
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				e1 = _hx_e1
				_hx_local_5 = False
			return _hx_local_5
		if _hx_local_6():
			return True
		if python_lib_Inspect.isclass(t):
			loop = None
			loop1 = None
			def _hx_local_8(intf):
				f1 = None
				if hasattr(intf,"_hx_interfaces"):
					f1 = intf._hx_interfaces
				else:
					f1 = []
				if (f1 is not None):
					_g = 0
					while (_g < len(f1)):
						i = (f1[_g] if _g >= 0 and _g < len(f1) else None)
						_g = (_g + 1)
						if HxOverrides.eq(i,t):
							return True
						else:
							l = loop1(i)
							if l:
								return True
					return False
				else:
					return False
			loop1 = _hx_local_8
			loop = loop1
			currentClass = v.__class__
			while (currentClass is not None):
				if loop(currentClass):
					return True
				currentClass = python_Boot.getSuperClass(currentClass)
			return False
		else:
			return False

	@staticmethod
	def string(s):
		return unicode(python_Boot.toString1(s,""))

	@staticmethod
	def parseInt(x):
		if (x is None):
			return None
		try:
			return int(x)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e = _hx_e1
			try:
				prefix = None
				_this = HxString.substr(x,0,2)
				prefix = _this.lower()
				if (prefix == "0x"):
					return int(x,16)
				raise _HxException("fail")
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				e1 = _hx_e1
				r = None
				x1 = Std.parseFloat(x)
				try:
					r = int(x1)
				except Exception as _hx_e:
					_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
					e2 = _hx_e1
					r = None
				if (r is None):
					r1 = Std.shortenPossibleNumber(x)
					if (r1 != x):
						return Std.parseInt(r1)
					else:
						return None
				return r

	@staticmethod
	def shortenPossibleNumber(x):
		r = ""
		_g1 = 0
		_g = len(x)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			c = None
			if ((i < 0) or ((i >= len(x)))):
				c = ""
			else:
				c = x[i]
			_g2 = HxString.charCodeAt(c,0)
			if (_g2 is not None):
				if (((((((((((_g2 == 46) or ((_g2 == 57))) or ((_g2 == 56))) or ((_g2 == 55))) or ((_g2 == 54))) or ((_g2 == 53))) or ((_g2 == 52))) or ((_g2 == 51))) or ((_g2 == 50))) or ((_g2 == 49))) or ((_g2 == 48))):
					r = (("null" if r is None else r) + ("null" if c is None else c))
				else:
					break
			else:
				break
		return r

	@staticmethod
	def parseFloat(x):
		try:
			return float(x)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e = _hx_e1
			if (x is not None):
				r1 = Std.shortenPossibleNumber(x)
				if (r1 != x):
					return Std.parseFloat(r1)
			return Math.NaN
Std._hx_class = Std


class Float:
	_hx_class_name = "Float"
Float._hx_class = Float


class Int:
	_hx_class_name = "Int"
Int._hx_class = Int


class Bool:
	_hx_class_name = "Bool"
Bool._hx_class = Bool


class Dynamic:
	_hx_class_name = "Dynamic"
Dynamic._hx_class = Dynamic


class StringBuf:
	_hx_class_name = "StringBuf"
	_hx_fields = ["b"]

	def __init__(self):
		self.b = None
		self.b = python_lib_io_StringIO()

StringBuf._hx_class = StringBuf


class StringTools:
	_hx_class_name = "StringTools"
	_hx_statics = ["isSpace", "ltrim", "rtrim", "trim", "lpad"]

	@staticmethod
	def isSpace(s,pos):
		if (((len(s) == 0) or ((pos < 0))) or ((pos >= len(s)))):
			return False
		c = HxString.charCodeAt(s,pos)
		return (((c > 8) and ((c < 14))) or ((c == 32)))

	@staticmethod
	def ltrim(s):
		l = len(s)
		r = 0
		while ((r < l) and StringTools.isSpace(s,r)):
			r = (r + 1)
		if (r > 0):
			return HxString.substr(s,r,(l - r))
		else:
			return s

	@staticmethod
	def rtrim(s):
		l = len(s)
		r = 0
		while ((r < l) and StringTools.isSpace(s,((l - r) - 1))):
			r = (r + 1)
		if (r > 0):
			return HxString.substr(s,0,(l - r))
		else:
			return s

	@staticmethod
	def trim(s):
		return StringTools.ltrim(StringTools.rtrim(s))

	@staticmethod
	def lpad(s,c,l):
		if (len(c) <= 0):
			return s
		while (len(s) < l):
			s = (("null" if c is None else c) + ("null" if s is None else s))
		return s
StringTools._hx_class = StringTools


class Sutl:
	_hx_class_name = "Sutl"
	_hx_methods = ["ExampleString", "ExampleInt", "ExampleFloat", "ExampleBool", "ExampleNull", "ExampleArray", "ExampleDict", "_processPath", "_doPath", "builtins", "logenter", "logexit", "evaluate", "dec", "_evaluate", "_quoteEvaluate", "_evaluateStringBuiltin", "_evaluateArrayBuiltin", "_evaluateBuiltin", "_evaluateBuiltinSimple", "_evaluateEval", "_evaluateEval2", "_evaluateDict", "_quoteEvaluateDict", "_doevaluateDict", "_evaluateList", "_quoteEvaluateList", "_doevaluateList", "compilelib", "_compilelib"]
	_hx_statics = ["version"]

	def __init__(self):
		pass

	def ExampleString(self):
		return "example string"

	def ExampleInt(self):
		return 1

	def ExampleFloat(self):
		return 1.0

	def ExampleBool(self):
		return True

	def ExampleNull(self):
		return None

	def ExampleArray(self):
		return [1, 2]

	def ExampleDict(self):
		return _hx_AnonObject({'x': 1})

	def _processPath(self,startfrom,parentscope,scope,l,src,tt,b,h):
		la = Util3.get(scope,"a")
		lb = Util3.get(scope,"b")
		lnotfirst = Util3.get(scope,"notfirst",False)
		if lnotfirst:
			return self._doPath(la,lb)
		else:
			laccum = self._doPath([startfrom],la)
			laccum1 = self._doPath(laccum,lb)
			return laccum1

	def _doPath(self,a,b):
		retval = []
		if Util2.isArray(a):
			if ((b is not None) and (not ((Util2.isString(b) and ((Reflect.field(b,"length") == 0)))))):
				_g = 0
				_g1 = None
				def _hx_local_0():
					_hx_local_0 = a
					if Std._hx_is(_hx_local_0,list):
						_hx_local_0
					else:
						raise _HxException("Class cast error")
					return _hx_local_0
				_g1 = _hx_local_0()
				while (_g < len(_g1)):
					lsourceItem = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
					_g = (_g + 1)
					try:
						if (b == "**"):
							x = lsourceItem
							retval.append(x)
							lstack = [lsourceItem]
							while (len(lstack) > 0):
								litem = None
								litem = (None if ((len(lstack) == 0)) else lstack.pop())
								if Util2.isObject(litem):
									_g2 = 0
									_g3 = python_Boot.fields(litem)
									while (_g2 < len(_g3)):
										lattrib = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
										_g2 = (_g2 + 1)
										lelem = Util3.get(litem,lattrib)
										retval.append(lelem)
										lstack.append(lelem)
								elif Util2.isArray(litem):
									_g21 = 0
									_g31 = None
									def _hx_local_0():
										_hx_local_3 = litem
										if Std._hx_is(_hx_local_3,list):
											_hx_local_3
										else:
											raise _HxException("Class cast error")
										return _hx_local_3
									_g31 = _hx_local_0()
									while (_g21 < len(_g31)):
										lelem1 = (_g31[_g21] if _g21 >= 0 and _g21 < len(_g31) else None)
										_g21 = (_g21 + 1)
										x1 = lelem1
										retval.append(x1)
										x2 = lelem1
										lstack.append(x2)
						elif (b == "*"):
							if Util2.isObject(lsourceItem):
								_g22 = 0
								_g32 = python_Boot.fields(lsourceItem)
								while (_g22 < len(_g32)):
									lattrib1 = (_g32[_g22] if _g22 >= 0 and _g22 < len(_g32) else None)
									_g22 = (_g22 + 1)
									lelem2 = Util3.get(lsourceItem,lattrib1)
									retval.append(lelem2)
							elif Util2.isArray(lsourceItem):
								_g23 = 0
								_g33 = None
								def _hx_local_0():
									_hx_local_6 = lsourceItem
									if Std._hx_is(_hx_local_6,list):
										_hx_local_6
									else:
										raise _HxException("Class cast error")
									return _hx_local_6
								_g33 = _hx_local_0()
								while (_g23 < len(_g33)):
									lelem3 = (_g33[_g23] if _g23 >= 0 and _g23 < len(_g33) else None)
									_g23 = (_g23 + 1)
									x3 = lelem3
									retval.append(x3)
						elif (Util2.isObject(lsourceItem) and Util2.isString(b)):
							def _hx_local_8():
								field = b
								return hasattr(lsourceItem,(("_hx_" + field) if (field in python_Boot.keywords) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)))
							if _hx_local_8():
								x4 = Reflect.field(lsourceItem,b)
								retval.append(x4)
						elif (Util2.isSequence(lsourceItem) and Util2.isNumber(b)):
							arr = Util.SequenceToArray(lsourceItem)
							if ((b >= 0) and ((b < len(arr)))):
								x5 = (arr[b] if b >= 0 and b < len(arr) else None)
								retval.append(x5)
					except Exception as _hx_e:
						_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
						ex = _hx_e1
						print(str(ex))
			else:
				retval = a
		return retval

	def builtins(self):
		_g = self
		def _hx_local_0(parentscope,scope,l,src,tt,b,h):
			a = Util3.get(scope,"a",0)
			bb = Util3.get(scope,"b",0)
			if (Util.gettype(a) == Util.gettype(bb)):
				return (a + bb)
			else:
				return None
		def _hx_local_1(parentscope1,scope1,l1,src1,tt1,b1,h1):
			return (Util3.get(scope1,"a",0) - Util3.get(scope1,"b",0))
		def _hx_local_2(parentscope2,scope2,l2,src2,tt2,b2,h2):
			return (Util3.get(scope2,"a",1) * Util3.get(scope2,"b",1))
		def _hx_local_3(parentscope3,scope3,l3,src3,tt3,b3,h3):
			return (Util3.get(scope3,"a",1) / Util3.get(scope3,"b",1))
		def _hx_local_4(parentscope4,scope4,l4,src4,tt4,b4,h4):
			a1 = Util3.get(scope4,"a",None)
			b5 = Util3.get(scope4,"b",None)
			return ((Util.gettype(a1) == Util.gettype(b5)) and (HxOverrides.eq(a1,b5)))
		def _hx_local_5(parentscope5,scope5,l5,src5,tt5,b6,h5):
			a2 = Util3.get(scope5,"a",None)
			b7 = Util3.get(scope5,"b",None)
			return (not (((Util.gettype(a2) == Util.gettype(b7)) and (HxOverrides.eq(a2,b7)))))
		def _hx_local_6(parentscope6,scope6,l6,src6,tt6,b8,h6):
			return (Util3.get(scope6,"a",None) >= Util3.get(scope6,"b",None))
		def _hx_local_7(parentscope7,scope7,l7,src7,tt7,b9,h7):
			return (Util3.get(scope7,"a",None) <= Util3.get(scope7,"b",None))
		def _hx_local_8(parentscope8,scope8,l8,src8,tt8,b10,h8):
			return (Util3.get(scope8,"a",None) > Util3.get(scope8,"b",None))
		def _hx_local_9(parentscope9,scope9,l9,src9,tt9,b11,h9):
			return (Util3.get(scope9,"a",None) < Util3.get(scope9,"b",None))
		def _hx_local_10(parentscope10,scope10,l10,src10,tt10,b12,h10):
			if hasattr(scope10,(("_hx_" + "a") if ("a" in python_Boot.keywords) else (("_hx_" + "a") if (((((len("a") > 2) and ((ord("a"[0]) == 95))) and ((ord("a"[1]) == 95))) and ((ord("a"[(len("a") - 1)]) != 95)))) else "a"))):
				if hasattr(scope10,(("_hx_" + "b") if ("b" in python_Boot.keywords) else (("_hx_" + "b") if (((((len("b") > 2) and ((ord("b"[0]) == 95))) and ((ord("b"[1]) == 95))) and ((ord("b"[(len("b") - 1)]) != 95)))) else "b"))):
					return (Util3.isTruthy(Util3.get(scope10,"a",False)) and Util3.isTruthy(Util3.get(scope10,"b",False)))
				else:
					return Util3.isTruthy(Util3.get(scope10,"a",False))
			else:
				return Util3.isTruthy(Util3.get(scope10,"b",False))
		def _hx_local_11(parentscope11,scope11,l11,src11,tt11,b13,h11):
			return (Util3.isTruthy(Util3.get(scope11,"a",False)) or Util3.isTruthy(Util3.get(scope11,"b",False)))
		def _hx_local_12(parentscope12,scope12,l12,src12,tt12,b14,h12):
			return (not Util3.isTruthy(Util3.get(scope12,"b",False)))
		def _hx_local_13(parentscope13,scope13,l13,src13,tt13,b15,h13):
			retval = None
			condvalue = False
			if hasattr(scope13,(("_hx_" + "cond") if ("cond" in python_Boot.keywords) else (("_hx_" + "cond") if (((((len("cond") > 2) and ((ord("cond"[0]) == 95))) and ((ord("cond"[1]) == 95))) and ((ord("cond"[(len("cond") - 1)]) != 95)))) else "cond"))):
				condvalue = Util3.isTruthy(_g._evaluate(parentscope13,Util3.get(scope13,"cond"),l13,src13,tt13,b15,h13))
			if condvalue:
				if hasattr(scope13,(("_hx_" + "true") if ("true" in python_Boot.keywords) else (("_hx_" + "true") if (((((len("true") > 2) and ((ord("true"[0]) == 95))) and ((ord("true"[1]) == 95))) and ((ord("true"[(len("true") - 1)]) != 95)))) else "true"))):
					retval = _g._evaluate(parentscope13,Util3.get(scope13,"true"),l13,src13,tt13,b15,h13)
			elif hasattr(scope13,(("_hx_" + "false") if ("false" in python_Boot.keywords) else (("_hx_" + "false") if (((((len("false") > 2) and ((ord("false"[0]) == 95))) and ((ord("false"[1]) == 95))) and ((ord("false"[(len("false") - 1)]) != 95)))) else "false"))):
				retval = _g._evaluate(parentscope13,Util3.get(scope13,"false"),l13,src13,tt13,b15,h13)
			return retval
		def _hx_local_15(parentscope14,scope14,l14,src14,tt14,b16,h14):
			obj = Util3.get(scope14,"map")
			if Util2.isObject(obj):
				retval1 = python_Boot.fields(obj)
				def _hx_local_14(a3,b17):
					return Reflect.compare(a3,b17)
				retval1.sort(key= python_lib_Functools.cmp_to_key(_hx_local_14))
				return retval1
			else:
				return None
		def _hx_local_18(parentscope15,scope15,l15,src15,tt15,b18,h15):
			obj1 = Util3.get(scope15,"map")
			if Util2.isObject(obj1):
				keys = python_Boot.fields(obj1)
				def _hx_local_16(a4,b19):
					return Reflect.compare(a4,b19)
				Reflect.field(keys,"sort")(_hx_local_16)
				def _hx_local_17(key):
					return Util3.get(obj1,key)
				vals = Reflect.field(keys,"map")(_hx_local_17)
				return vals
			else:
				return None
		def _hx_local_19(parentscope16,scope16,l16,src16,tt16,b20,h16):
			item = Util3.get(scope16,"list",Util3.get(scope16,"value"))
			if Util2.isSequence(item):
				arr = Util.SequenceToArray(item)
				return len(arr)
			else:
				return 0
		def _hx_local_20(parentscope17,scope17,l17,src17,tt17,b21,h17):
			item1 = Util3.get(scope17,"value")
			return Util.gettype(item1)
		def _hx_local_23(parentscope18,scope18,l18,src18,tt18,b22,h18):
			retval2 = _hx_AnonObject({})
			arr1 = Util3.get(scope18,"value")
			if Util2.isArray(arr1):
				_g1 = 0
				_g11 = None
				def _hx_local_0():
					_hx_local_21 = arr1
					if Std._hx_is(_hx_local_21,list):
						_hx_local_21
					else:
						raise _HxException("Class cast error")
					return _hx_local_21
				_g11 = _hx_local_0()
				while (_g1 < len(_g11)):
					entry = (_g11[_g1] if _g1 >= 0 and _g1 < len(_g11) else None)
					_g1 = (_g1 + 1)
					if ((Util2.isArray(entry) and ((Reflect.field(entry,"length") >= 2))) and Util2.isString(HxOverrides.arrayGet(entry, 0))):
						field = HxOverrides.arrayGet(entry, 0)
						setattr(retval2,(("_hx_" + field) if (field in python_Boot.keywords) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),HxOverrides.arrayGet(entry, 1))
			return retval2
		def _hx_local_24(parentscope19,scope19,l19,src19,tt19,b23,h19):
			retval3 = _hx_AnonObject({})
			listobj = Util3.get(scope19,"list")
			t = Util3.get(scope19,"t")
			accum = Util3.get(scope19,"accum")
			if Util2.isSequence(listobj):
				_hx_list = Util.SequenceToArray(listobj)
				s2 = _hx_AnonObject({})
				if Util2.isObject(parentscope19):
					s2 = Util.shallowCopy(parentscope19)
				Util.addObject(s2,scope19)
				_g12 = 0
				_g2 = len(_hx_list)
				while (_g12 < _g2):
					ix = _g12
					_g12 = (_g12 + 1)
					item2 = (_hx_list[ix] if ix >= 0 and ix < len(_hx_list) else None)
					setattr(s2,(("_hx_" + "item") if ("item" in python_Boot.keywords) else (("_hx_" + "item") if (((((len("item") > 2) and ((ord("item"[0]) == 95))) and ((ord("item"[1]) == 95))) and ((ord("item"[(len("item") - 1)]) != 95)))) else "item")),item2)
					setattr(s2,(("_hx_" + "accum") if ("accum" in python_Boot.keywords) else (("_hx_" + "accum") if (((((len("accum") > 2) and ((ord("accum"[0]) == 95))) and ((ord("accum"[1]) == 95))) and ((ord("accum"[(len("accum") - 1)]) != 95)))) else "accum")),accum)
					setattr(s2,(("_hx_" + "ix") if ("ix" in python_Boot.keywords) else (("_hx_" + "ix") if (((((len("ix") > 2) and ((ord("ix"[0]) == 95))) and ((ord("ix"[1]) == 95))) and ((ord("ix"[(len("ix") - 1)]) != 95)))) else "ix")),ix)
					accum = _g._evaluate(s2,t,l19,src19,tt19,b23,h19)
			return accum
		def _hx_local_25(parentscope20,scope20,l20,src20,tt20,b24,h20):
			return _g._processPath(src20,parentscope20,scope20,l20,src20,tt20,b24,h20)
		def _hx_local_26(parentscope21,scope21,l21,src21,tt21,b25,h21):
			return _g._processPath(parentscope21,parentscope21,scope21,l21,src21,tt21,b25,h21)
		def _hx_local_27(parentscope22,scope22,l22,src22,tt22,b26,h22):
			return _g._processPath(l22,parentscope22,scope22,l22,src22,tt22,b26,h22)
		def _hx_local_28(parentscope23,scope23,l23,src23,tt23,b27,h23):
			return _g._processPath(tt23,parentscope23,scope23,l23,src23,tt23,b27,h23)
		def _hx_local_29(parentscope24,scope24,l24,src24,tt24,b28,h24):
			la = Util3.get(scope24,"a")
			lb = Util3.get(scope24,"b")
			lnotfirst = Util3.get(scope24,"notfirst")
			if lnotfirst:
				return _g._doPath(la,lb)
			elif (la is None):
				return _g._doPath([lb],None)
			else:
				return _g._doPath([la],lb)
		def _hx_local_30(parentscope25,scope25,l25,src25,tt25,b29,h25):
			lb1 = Util3.get(scope25,"b")
			if Util2.isSequence(lb1):
				arr2 = Util.SequenceToArray(lb1)
				if (len(arr2) > 0):
					return (arr2[0] if 0 < len(arr2) else None)
				else:
					return None
			else:
				return None
		def _hx_local_31(parentscope26,scope26,l26,src26,tt26,b30,h26):
			lb2 = Util3.get(scope26,"b")
			if Util2.isSequence(lb2):
				arr3 = Util.SequenceToArray(lb2)
				if (len(arr3) > 0):
					return arr3[1:None]
				else:
					return []
			else:
				return None
		def _hx_local_33(parentscope27,scope27,l27,src27,tt27,b31,h27):
			lvalue = Util3.get(scope27,"value")
			lsep = Util3.get(scope27,"sep",",")
			lmax = Util3.get(scope27,"max")
			retval4 = None
			if (not Util2.isString(lvalue)):
				pass
			elif (not ((Util3.isTruthy(lsep) and Util2.isString(lsep)))):
				pass
			elif (not ((Util2.isNumber(lmax) or ((lmax is None))))):
				pass
			else:
				lstr = None
				def _hx_local_0():
					_hx_local_32 = lvalue
					if Std._hx_is(_hx_local_32,str):
						_hx_local_32
					else:
						raise _HxException("Class cast error")
					return _hx_local_32
				lstr = _hx_local_0()
				retval4 = lvalue.split(lsep)
				if (((lmax is not None) and ((lmax >= 0))) and ((lmax < len(lstr)))):
					lresult1 = retval4[0:(lmax - 1)]
					lresult2 = retval4[(-1 * (((len(retval4) - lmax) + 1))):None]
					python_internal_ArrayImpl._set(lresult1, (lmax - 1), lsep.join([python_Boot.toString1(x1,'') for x1 in lresult2]))
					retval4 = lresult1
			return retval4
		def _hx_local_34(parentscope28,scope28,l28,src28,tt28,b32,h28):
			lvalue1 = Util3.get(scope28,"value")
			retval5 = None
			if (not Util2.isString(lvalue1)):
				pass
			else:
				retval5 = StringTools.trim(lvalue1)
			return retval5
		def _hx_local_36(parentscope29,scope29,l29,src29,tt29,b33,h29):
			lvalue2 = Util3.get(scope29,"value")
			lsub = Util3.get(scope29,"sub")
			retval6 = None
			if (not Util2.isString(lvalue2)):
				pass
			elif (not ((Util3.isTruthy(lsub) and Util2.isString(lsub)))):
				pass
			else:
				_this = None
				def _hx_local_0():
					_hx_local_35 = lvalue2
					if Std._hx_is(_hx_local_35,str):
						_hx_local_35
					else:
						raise _HxException("Class cast error")
					return _hx_local_35
				_this = _hx_local_0()
				retval6 = _this.find(lsub)
			return retval6
		functions = _hx_AnonObject({'+': _hx_local_0, '-': _hx_local_1, 'x': _hx_local_2, '/': _hx_local_3, '=': _hx_local_4, '!=': _hx_local_5, '>=': _hx_local_6, '<=': _hx_local_7, '>': _hx_local_8, '<': _hx_local_9, '&&': _hx_local_10, '||': _hx_local_11, '!': _hx_local_12, '_hx_if': _hx_local_13, 'keys': _hx_local_15, 'values': _hx_local_18, 'len': _hx_local_19, 'type': _hx_local_20, 'makemap': _hx_local_23, 'reduce': _hx_local_24, '$': _hx_local_25, '@': _hx_local_26, '*': _hx_local_27, '~': _hx_local_28, '%': _hx_local_29, 'head': _hx_local_30, 'tail': _hx_local_31, 'split': _hx_local_33, 'trim': _hx_local_34, 'pos': _hx_local_36})
		_g3 = 0
		_g13 = python_Boot.fields(functions)
		while (_g3 < len(_g13)):
			fieldname = (_g13[_g3] if _g3 >= 0 and _g3 < len(_g13) else None)
			_g3 = (_g3 + 1)
			field1 = ("has" + ("null" if fieldname is None else fieldname))
			def _hx_local_38(parentscope30,scope30,l30,src30,tt30,b34,h30):
				return True
			setattr(functions,(("_hx_" + field1) if (field1 in python_Boot.keywords) else (("_hx_" + field1) if (((((len(field1) > 2) and ((ord(field1[0]) == 95))) and ((ord(field1[1]) == 95))) and ((ord(field1[(len(field1) - 1)]) != 95)))) else field1)),_hx_local_38)
		return functions

	def logenter(self,msg,s,t,h):
		if (h > 0):
			print(str(((("(" + Std.string(h)) + "): ") + ("null" if msg is None else msg))))
			print(str((" - s: " + HxOverrides.stringOrNull(haxe_format_JsonPrinter.xprint(s,None,"  ")))))
			print(str((" - t: " + HxOverrides.stringOrNull(haxe_format_JsonPrinter.xprint(t,None,"  ")))))

	def logexit(self,msg,r,h):
		if (h > 0):
			print(str(((("(" + Std.string(h)) + "): ") + ("null" if msg is None else msg))))
			print(str((" - r: " + HxOverrides.stringOrNull(haxe_format_JsonPrinter.xprint(r,None,"  ")))))

	def evaluate(self,src,tt,l,h = 0):
		if (h is None):
			h = 0
		retval = self._evaluate(src,tt,l,src,tt,self.builtins(),h)
		return retval

	def dec(self,x):
		return (x - 1)

	def _evaluate(self,s,t,l,src,tt,b,h):
		if (not Util3.isTruthy(h)):
			h = 0
		r = None
		self.logenter("_evaluate",s,t,h)
		if Util3.isEval(t):
			r = self._evaluateEval(True,s,t,l,src,tt,b,self.dec(h))
		elif Util3.isEval2(t):
			r = self._evaluateEval2(s,t,l,src,tt,b,self.dec(h))
		elif Util3.isBuiltinEval(t):
			r = self._evaluateBuiltin(s,t,l,src,tt,b,self.dec(h))
		elif Util3.isQuoteEval(t):
			r = self._quoteEvaluate(s,Util3.get(t,"'"),l,src,tt,b,self.dec(h))
		elif Util3.isColonEval(t):
			r = Util3.get(t,":")
		elif Util3.isDictTransform(t):
			r = self._evaluateDict(s,t,l,src,tt,b,self.dec(h))
		elif Util.isArrayBuiltinEval(t,b):
			r = self._evaluateArrayBuiltin(s,t,l,src,tt,b,self.dec(h))
		elif Util3.isListTransform(t):
			tlist = Util.SequenceToArray(t)
			if ((len(tlist) > 0) and (((tlist[0] if 0 < len(tlist) else None) == "&&"))):
				r = Util.flatten(self._evaluateList(s,tlist[1:None],l,src,tt,b,self.dec(h)))
			else:
				r = self._evaluateList(s,t,l,src,tt,b,self.dec(h))
		elif Util.isStringBuiltinEval(t,b):
			r = self._evaluateStringBuiltin(s,t,l,src,tt,b,self.dec(h))
		else:
			r = t
		self.logexit("_evaluate",r,h)
		return r

	def _quoteEvaluate(self,s,t,l,src,tt,b,h):
		self.logenter("_quoteEvaluate",s,t,h)
		r = None
		if Util3.isDoubleQuoteEval(t):
			r = self._evaluate(s,Util3.get(t,"''"),l,src,tt,b,self.dec(h))
		elif Util3.isDictTransform(t):
			r = self._quoteEvaluateDict(s,t,l,src,tt,b,self.dec(h))
		elif Util3.isListTransform(t):
			r = self._quoteEvaluateList(s,t,l,src,tt,b,self.dec(h))
		else:
			r = t
		self.logexit("_quoteEvaluate",r,h)
		return r

	def _evaluateStringBuiltin(self,s,t,l,src,tt,b,h):
		strt = None
		def _hx_local_0():
			_hx_local_0 = t
			if Std._hx_is(_hx_local_0,str):
				_hx_local_0
			else:
				raise _HxException("Class cast error")
			return _hx_local_0
		strt = _hx_local_0()
		larr = strt.split(".")
		larr2 = []
		_g = 0
		while (_g < len(larr)):
			litem = (larr[_g] if _g >= 0 and _g < len(larr) else None)
			_g = (_g + 1)
			try:
				i = Std.parseInt(litem)
				if (i is not None):
					larr2.append(i)
				else:
					larr2.append(litem)
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				err = _hx_e1
				larr2.append(litem)
		return self._evaluateArrayBuiltin(s,larr2,l,src,tt,b,h)

	def _evaluateArrayBuiltin(self,s,t,l,src,tt,b,h):
		retval = None
		arrt = None
		def _hx_local_0():
			_hx_local_0 = t
			if Std._hx_is(_hx_local_0,list):
				_hx_local_0
			else:
				raise _HxException("Class cast error")
			return _hx_local_0
		arrt = _hx_local_0()
		lop = None
		if (len(arrt) > 0):
			def _hx_local_0():
				_hx_local_1 = (arrt[0] if 0 < len(arrt) else None)
				if Std._hx_is(_hx_local_1,str):
					_hx_local_1
				else:
					raise _HxException("Class cast error")
				return _hx_local_1
			lop = _hx_local_0()
		if (len(lop) > 0):
			lopChar = None
			if (0 >= len(lop)):
				lopChar = ""
			else:
				lopChar = lop[0]
			uset = _hx_AnonObject({'&': Util.getArrayBuiltinName(lop), 'args': arrt[1:None], 'head': (lopChar == "^")})
			retval = self._evaluateBuiltin(s,uset,l,src,tt,b,self.dec(h))
		return retval

	def _evaluateBuiltin(self,s,t,l,src,tt,b,h):
		self.logenter("_evaluateBuiltin",s,t,h)
		retval = None
		if hasattr(t,(("_hx_" + "args") if ("args" in python_Boot.keywords) else (("_hx_" + "args") if (((((len("args") > 2) and ((ord("args"[0]) == 95))) and ((ord("args"[1]) == 95))) and ((ord("args"[(len("args") - 1)]) != 95)))) else "args"))):
			args = Util3.get(t,"args")
			builtinname = self._evaluate(s,Util3.get(t,"&"),l,src,tt,b,self.dec(h))
			if (len(args) == 0):
				uset = _hx_AnonObject({'&': builtinname})
				retval = self._evaluateBuiltinSimple(False,s,uset,l,src,tt,b,self.dec(h))
			elif (len(args) == 1):
				uset1 = _hx_AnonObject({'&': builtinname, 'b': self._evaluate(s,(args[0] if 0 < len(args) else None),l,src,tt,b,self.dec(h))})
				retval = self._evaluateBuiltinSimple(False,s,uset1,l,src,tt,b,self.dec(h))
			else:
				_hx_list = None
				def _hx_local_0():
					_hx_local_0 = self._evaluateList(s,args[1:None],l,src,tt,b,self.dec(h))
					if Std._hx_is(_hx_local_0,list):
						_hx_local_0
					else:
						raise _HxException("Class cast error")
					return _hx_local_0
				_hx_list = _hx_local_0()
				retval = self._evaluate(s,(args[0] if 0 < len(args) else None),l,src,tt,b,self.dec(h))
				notfirst = False
				_g = 0
				while (_g < len(_hx_list)):
					item = (_hx_list[_g] if _g >= 0 and _g < len(_hx_list) else None)
					_g = (_g + 1)
					uset2 = _hx_AnonObject({'&': builtinname, 'a': retval, 'b': item, 'notfirst': notfirst})
					retval = self._evaluateBuiltinSimple(False,s,uset2,l,src,tt,b,self.dec(h))
					notfirst = True
			if (Util2.isArray(retval) and Util3.isTruthy(Util3.get(t,"head"))):
				arrretval = None
				def _hx_local_0():
					_hx_local_2 = retval
					if Std._hx_is(_hx_local_2,list):
						_hx_local_2
					else:
						raise _HxException("Class cast error")
					return _hx_local_2
				arrretval = _hx_local_0()
				if (len(arrretval) > 0):
					retval = (arrretval[0] if 0 < len(arrretval) else None)
				else:
					retval = None
		else:
			retval = self._evaluateBuiltinSimple(True,s,t,l,src,tt,b,h)
		self.logexit("_evaluateBuiltin",retval,h)
		return retval

	def _evaluateBuiltinSimple(self,needseval,s,t,l,src,tt,b,h):
		retval = None
		builtinname = Util3.get(t,"&")
		builtinf = Util3.get(b,builtinname)
		llibname = None
		if builtinf:
			llibname = ("_override_" + Std.string(Util3.get(t,"&")))
		else:
			llibname = Util3.get(t,"&")
		if (Util2.isObject(l) and hasattr(l,(("_hx_" + llibname) if (llibname in python_Boot.keywords) else (("_hx_" + llibname) if (((((len(llibname) > 2) and ((ord(llibname[0]) == 95))) and ((ord(llibname[1]) == 95))) and ((ord(llibname[(len(llibname) - 1)]) != 95)))) else llibname)))):
			t2 = Util.shallowCopy(t)
			value = ["^*", Util3.get(t,"&")]
			setattr(t2,(("_hx_" + "!") if ("!" in python_Boot.keywords) else (("_hx_" + "!") if (((((len("!") > 2) and ((ord("!"[0]) == 95))) and ((ord("!"[1]) == 95))) and ((ord("!"[(len("!") - 1)]) != 95)))) else "!")),value)
			Reflect.deleteField(t2,"&")
			retval = self._evaluateEval(needseval,s,t2,l,src,tt,b,self.dec(h))
		elif (builtinf is not None):
			sX = None
			if needseval:
				sX = self._evaluateDict(s,t,l,src,tt,b,self.dec(h))
			else:
				sX = t
			s2 = None
			if Util2.isObject(s):
				s2 = Util.shallowCopy(s)
				Util.addObject(s2,sX)
			else:
				s2 = sX
			l2 = l
			if hasattr(t,(("_hx_" + "*") if ("*" in python_Boot.keywords) else (("_hx_" + "*") if (((((len("*") > 2) and ((ord("*"[0]) == 95))) and ((ord("*"[1]) == 95))) and ((ord("*"[(len("*") - 1)]) != 95)))) else "*"))):
				l2 = self._evaluateDict(s,Util3.get(t,"*"),l,src,tt,b,self.dec(h))
			retval = builtinf(s,s2,l2,src,tt,b,self.dec(h))
		return retval

	def _evaluateEval(self,needseval,s,t,l,src,tt,b,h):
		self.logenter("_evaluateEval",s,t,h)
		retval = None
		teval = None
		if needseval:
			teval = self._evaluateDict(s,t,l,src,tt,b,h)
		else:
			teval = t
		t2 = Util3.get(teval,"!")
		s2 = _hx_AnonObject({})
		if Util2.isObject(s):
			s2 = Util.shallowCopy(s)
		Util.addObject(s2,teval)
		l2 = l
		if hasattr(t,(("_hx_" + "*") if ("*" in python_Boot.keywords) else (("_hx_" + "*") if (((((len("*") > 2) and ((ord("*"[0]) == 95))) and ((ord("*"[1]) == 95))) and ((ord("*"[(len("*") - 1)]) != 95)))) else "*"))):
			l2 = self._evaluate(s,Util3.get(t,"*"),l,src,tt,b,h)
		r = self._evaluate(s2,t2,l2,src,tt,b,h)
		self.logexit("_evaluateEval",r,h)
		return r

	def _evaluateEval2(self,s,t,l,src,tt,b,h):
		self.logenter("_evaluateEval2",s,t,h)
		retval = None
		t2 = self._evaluate(s,Util3.get(t,"!!"),l,src,tt,b,h)
		s2 = s
		if hasattr(t,(("_hx_" + "s") if ("s" in python_Boot.keywords) else (("_hx_" + "s") if (((((len("s") > 2) and ((ord("s"[0]) == 95))) and ((ord("s"[1]) == 95))) and ((ord("s"[(len("s") - 1)]) != 95)))) else "s"))):
			ts = self._evaluate(s,Util3.get(t,"s"),l,src,tt,b,h)
			if Util2.isObject(ts):
				s2 = _hx_AnonObject({})
				if Util2.isObject(s):
					s2 = Util.shallowCopy(s)
				Util.addObject(s2,t2)
			else:
				s2 = ts
		l2 = l
		if hasattr(t,(("_hx_" + "*") if ("*" in python_Boot.keywords) else (("_hx_" + "*") if (((((len("*") > 2) and ((ord("*"[0]) == 95))) and ((ord("*"[1]) == 95))) and ((ord("*"[(len("*") - 1)]) != 95)))) else "*"))):
			l2 = self._evaluate(s,Util3.get(t,"*"),l,src,tt,b,h)
		r = self._evaluate(s2,t2,l2,src,tt,b,h)
		self.logexit("_evaluateEval",r,h)
		return r

	def _evaluateDict(self,s,t,l,src,tt,b,h):
		self.logenter("_evaluateDict",s,t,h)
		retval = self._doevaluateDict(False,s,t,l,src,tt,b,self.dec(h))
		self.logexit("_evaluateDict",retval,h)
		return retval

	def _quoteEvaluateDict(self,s,t,l,src,tt,b,h):
		self.logenter("_quoteEvaluateDict",s,t,h)
		retval = self._doevaluateDict(True,s,t,l,src,tt,b,self.dec(h))
		self.logexit("_quoteEvaluateDict",retval,h)
		return retval

	def _doevaluateDict(self,usequoteform,s,t,l,src,tt,b,h):
		retval = _hx_AnonObject({})
		_g = 0
		_g1 = python_Boot.fields(t)
		while (_g < len(_g1)):
			key = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
			_g = (_g + 1)
			if usequoteform:
				value = self._quoteEvaluate(s,Util3.get(t,key),l,src,tt,b,h)
				setattr(retval,(("_hx_" + key) if (key in python_Boot.keywords) else (("_hx_" + key) if (((((len(key) > 2) and ((ord(key[0]) == 95))) and ((ord(key[1]) == 95))) and ((ord(key[(len(key) - 1)]) != 95)))) else key)),value)
			else:
				lnewt = self._evaluate(s,Util3.get(t,key),l,src,tt,b,h)
				setattr(retval,(("_hx_" + key) if (key in python_Boot.keywords) else (("_hx_" + key) if (((((len(key) > 2) and ((ord(key[0]) == 95))) and ((ord(key[1]) == 95))) and ((ord(key[(len(key) - 1)]) != 95)))) else key)),lnewt)
		return retval

	def _evaluateList(self,s,t,l,src,tt,b,h):
		self.logenter("_evaluateList",s,t,h)
		retval = self._doevaluateList(False,s,t,l,src,tt,b,self.dec(h))
		self.logexit("_evaluateList",retval,h)
		return retval

	def _quoteEvaluateList(self,s,t,l,src,tt,b,h):
		self.logenter("_quoteEvaluateList",s,t,h)
		retval = self._doevaluateList(True,s,t,l,src,tt,b,self.dec(h))
		self.logexit("_quoteEvaluateList",retval,h)
		return retval

	def _doevaluateList(self,usequoteform,s,t,l,src,tt,b,h):
		tarr = Util.SequenceToArray(t)
		retval = list(tarr)
		_g1 = 0
		_g = len(tarr)
		while (_g1 < _g):
			ix = _g1
			_g1 = (_g1 + 1)
			elem = (tarr[ix] if ix >= 0 and ix < len(tarr) else None)
			if usequoteform:
				elem = self._quoteEvaluate(s,elem,l,src,tt,b,h)
			else:
				elem = self._evaluate(s,elem,l,src,tt,b,h)
			python_internal_ArrayImpl._set(retval, ix, elem)
		return retval

	def compilelib(self,decls,dists):
		return self._compilelib(decls,dists,_hx_AnonObject({}),self.builtins())

	def _compilelib(self,decls,dists,l,b):
		resultlib = _hx_AnonObject({})
		resultliblib = _hx_AnonObject({})
		if Util2.isObject(l):
			resultlib = Util.shallowCopy(l)
		all_candidate_decls = _hx_AnonObject({})
		_g = 0
		while (_g < len(decls)):
			decl = (decls[_g] if _g >= 0 and _g < len(decls) else None)
			_g = (_g + 1)
			declname = Util3.get(decl,"name","")
			if (hasattr(decl,(("_hx_" + "requires") if ("requires" in python_Boot.keywords) else (("_hx_" + "requires") if (((((len("requires") > 2) and ((ord("requires"[0]) == 95))) and ((ord("requires"[1]) == 95))) and ((ord("requires"[(len("requires") - 1)]) != 95)))) else "requires"))) and Util2.isArray(Util3.get(decl,"requires"))):
				reqnames = None
				def _hx_local_0():
					_hx_local_1 = Util3.get(decl,"requires")
					if Std._hx_is(_hx_local_1,list):
						_hx_local_1
					else:
						raise _HxException("Class cast error")
					return _hx_local_1
				reqnames = _hx_local_0()
				_g1 = 0
				while (_g1 < len(reqnames)):
					reqname = (reqnames[_g1] if _g1 >= 0 and _g1 < len(reqnames) else None)
					_g1 = (_g1 + 1)
					def _hx_local_3():
						field = reqname
						return hasattr(l,(("_hx_" + field) if (field in python_Boot.keywords) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)))
					if (not _hx_local_3()):
						if Util3.isPrefix(reqname,declname):
							field1 = reqname
							value = Util3.get(decl,"transform-t")
							setattr(resultlib,(("_hx_" + field1) if (field1 in python_Boot.keywords) else (("_hx_" + field1) if (((((len(field1) > 2) and ((ord(field1[0]) == 95))) and ((ord(field1[1]) == 95))) and ((ord(field1[(len(field1) - 1)]) != 95)))) else field1)),value)
						else:
							field2 = reqname
							setattr(all_candidate_decls,(("_hx_" + field2) if (field2 in python_Boot.keywords) else (("_hx_" + field2) if (((((len(field2) > 2) and ((ord(field2[0]) == 95))) and ((ord(field2[1]) == 95))) and ((ord(field2[(len(field2) - 1)]) != 95)))) else field2)),[])
		_g2 = 0
		_g11 = python_Boot.fields(all_candidate_decls)
		while (_g2 < len(_g11)):
			reqname1 = (_g11[_g2] if _g2 >= 0 and _g2 < len(_g11) else None)
			_g2 = (_g2 + 1)
			candidate_decls = Util3.get(all_candidate_decls,reqname1)
			_g21 = 0
			while (_g21 < len(dists)):
				dist = (dists[_g21] if _g21 >= 0 and _g21 < len(dists) else None)
				_g21 = (_g21 + 1)
				_g3 = 0
				while (_g3 < len(dist)):
					decl1 = (dist[_g3] if _g3 >= 0 and _g3 < len(dist) else None)
					_g3 = (_g3 + 1)
					declname1 = Util3.get(decl1,"name","")
					if Util3.isPrefix(reqname1,declname1):
						HxOverrides.push(candidate_decls, decl1)
		_g4 = 0
		_g12 = python_Boot.fields(all_candidate_decls)
		while (_g4 < len(_g12)):
			reqname2 = (_g12[_g4] if _g4 >= 0 and _g4 < len(_g12) else None)
			_g4 = (_g4 + 1)
			candidate_decls1 = Util3.get(all_candidate_decls,reqname2)
			if Util3.isTruthy(candidate_decls1):
				candidate_decls_arr = None
				def _hx_local_0():
					_hx_local_8 = candidate_decls1
					if Std._hx_is(_hx_local_8,list):
						_hx_local_8
					else:
						raise _HxException("Class cast error")
					return _hx_local_8
				candidate_decls_arr = _hx_local_0()
				_g22 = 0
				while (_g22 < len(candidate_decls_arr)):
					candidate_decl = (candidate_decls_arr[_g22] if _g22 >= 0 and _g22 < len(candidate_decls_arr) else None)
					_g22 = (_g22 + 1)
					clresult = self._compilelib([candidate_decl],dists,resultlib,b)
					clresultlib = Util3.get(clresult,"lib")
					Util.addObject(resultlib,clresultlib)
					value1 = Util3.get(candidate_decl,"transform-t")
					setattr(resultlib,(("_hx_" + reqname2) if (reqname2 in python_Boot.keywords) else (("_hx_" + reqname2) if (((((len(reqname2) > 2) and ((ord(reqname2[0]) == 95))) and ((ord(reqname2[1]) == 95))) and ((ord(reqname2[(len(reqname2) - 1)]) != 95)))) else reqname2)),value1)
					break
		return _hx_AnonObject({'lib': resultlib})

	@staticmethod
	def version():
		return "0.1"

Sutl._hx_class = Sutl


class Sutlcore:
	_hx_class_name = "Sutlcore"
	_hx_statics = ["get", "getStr"]

	@staticmethod
	def get():
		text = Sutlcore.getStr()
		return python_lib_Json.loads(text,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'object_hook': python_Lib.dictToAnon})))

	@staticmethod
	def getStr():
		return "\n\t\t[\n\t\t  {\n\t\t    \"transform-t\": {\n\t\t      \"map-t\": \"^@.t\", \n\t\t      \"accum\": [], \n\t\t      \"list\": \"^@.list\", \n\t\t      \"t\": {\n\t\t        \"'\": [\n\t\t          \"&&\", \n\t\t          \"^@.accum\", \n\t\t          [\n\t\t            {\n\t\t              \"!\": \"^@.map-t\"\n\t\t            }\n\t\t          ]\n\t\t        ]\n\t\t      }, \n\t\t      \"&\": \"reduce\"\n\t\t    }, \n\t\t    \"name\": \"map_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"reverse_core_emlynoregan_com\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"true\": {\n\t\t        \"'\": [\n\t\t          \"&&\", \n\t\t          {\n\t\t            \"!\": \"^*.reverse_core_emlynoregan_com\", \n\t\t            \"list\": [\n\t\t              \"&tail\", \n\t\t              \"^@.list\"\n\t\t            ]\n\t\t          }, \n\t\t          [\n\t\t            \"&head\", \n\t\t            \"^@.list\"\n\t\t          ]\n\t\t        ]\n\t\t      }, \n\t\t      \"false\": {\n\t\t        \"'\": []\n\t\t      }, \n\t\t      \"cond\": \"^@.list\", \n\t\t      \"&\": \"if\"\n\t\t    }, \n\t\t    \"name\": \"reverse_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"transform-t\": {\n\t\t      \"accum\": [], \n\t\t      \"list\": \"^@.list\", \n\t\t      \"t\": {\n\t\t        \"'\": {\n\t\t          \"true\": {\n\t\t            \"'\": [\n\t\t              \"&&\", \n\t\t              \"^@.accum\", \n\t\t              \"^@.item\"\n\t\t            ]\n\t\t          }, \n\t\t          \"false\": {\n\t\t            \"'\": \"^@.accum\"\n\t\t          }, \n\t\t          \"cond\": {\n\t\t            \"'\": [\n\t\t              \"&!=\", \n\t\t              \"^@.item\", \n\t\t              null\n\t\t            ]\n\t\t          }, \n\t\t          \"&\": \"if\"\n\t\t        }\n\t\t      }, \n\t\t      \"&\": \"reduce\"\n\t\t    }, \n\t\t    \"name\": \"removenulls_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"count_core_emlynoregan_com\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"true\": {\n\t\t        \"'\": {\n\t\t          \"accum\": 0, \n\t\t          \"list\": \"^@.obj\", \n\t\t          \"t\": {\n\t\t            \"'\": {\n\t\t              \"a\": {\n\t\t                \"!\": \"^*.count_core_emlynoregan_com\", \n\t\t                \"obj\": \"^@.item\"\n\t\t              }, \n\t\t              \"b\": \"^@.accum\", \n\t\t              \"&\": \"+\"\n\t\t            }\n\t\t          }, \n\t\t          \"&\": \"reduce\"\n\t\t        }\n\t\t      }, \n\t\t      \"false\": 1, \n\t\t      \"cond\": {\n\t\t        \"'\": {\n\t\t          \"a\": \"list\", \n\t\t          \"b\": {\n\t\t            \"value\": \"^@.obj\", \n\t\t            \"&\": \"type\"\n\t\t          }, \n\t\t          \"&\": \"=\"\n\t\t        }\n\t\t      }, \n\t\t      \"&\": \"if\"\n\t\t    }, \n\t\t    \"name\": \"count_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"transform-t\": {\n\t\t      \"b\": {\n\t\t        \"list\": \"^@.list\", \n\t\t        \"accum\": [\n\t\t          [], \n\t\t          \"^@.lists\"\n\t\t        ], \n\t\t        \"t\": {\n\t\t          \":\": [\n\t\t            [\n\t\t              \"&&\", \n\t\t              \"^@.accum.0\", \n\t\t              [\n\t\t                [\n\t\t                  \"&&\", \n\t\t                  {\n\t\t                    \"true\": {\n\t\t                      \"b\": \"^@.accum.1\", \n\t\t                      \"&\": \"head\"\n\t\t                    }, \n\t\t                    \"false\": [], \n\t\t                    \"cond\": {\n\t\t                      \":\": {\n\t\t                        \"list\": \"^@.accum.1\", \n\t\t                        \"&\": \"len\"\n\t\t                      }\n\t\t                    }, \n\t\t                    \"&\": \"if\"\n\t\t                  }, \n\t\t                  [\n\t\t                    \"^@.item\"\n\t\t                  ]\n\t\t                ]\n\t\t              ]\n\t\t            ], \n\t\t            {\n\t\t              \"b\": \"^@.accum.1\", \n\t\t              \"&\": \"tail\"\n\t\t            }\n\t\t          ]\n\t\t        }, \n\t\t        \"&\": \"reduce\"\n\t\t      }, \n\t\t      \"&\": \"head\"\n\t\t    }, \n\t\t    \"name\": \"foldone_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"foldone_core\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"accum\": [], \n\t\t      \"list\": \"^@.list\", \n\t\t      \"t\": {\n\t\t        \"'\": {\n\t\t          \"list\": \"^@.item\", \n\t\t          \"lists\": \"^@.accum\", \n\t\t          \"&\": \"foldone_core\"\n\t\t        }\n\t\t      }, \n\t\t      \"&\": \"reduce\"\n\t\t    }, \n\t\t    \"name\": \"zip_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"zip\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"value\": {\n\t\t        \"list\": [\n\t\t          [\n\t\t            \"&&\", \n\t\t            {\n\t\t              \"map\": \"^@.map1\", \n\t\t              \"&\": \"keys\"\n\t\t            }, \n\t\t            {\n\t\t              \"map\": \"^@.map2\", \n\t\t              \"&\": \"keys\"\n\t\t            }\n\t\t          ], \n\t\t          [\n\t\t            \"&&\", \n\t\t            {\n\t\t              \"map\": \"^@.map1\", \n\t\t              \"&\": \"values\"\n\t\t            }, \n\t\t            {\n\t\t              \"map\": \"^@.map2\", \n\t\t              \"&\": \"values\"\n\t\t            }\n\t\t          ]\n\t\t        ], \n\t\t        \"&\": \"zip\"\n\t\t      }, \n\t\t      \"&\": \"makemap\"\n\t\t    }, \n\t\t    \"name\": \"addmaps_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"transform-t\": [\n\t\t      \"^@\", \n\t\t      \"map\", \n\t\t      [\n\t\t        \"^@\", \n\t\t        \"key\"\n\t\t      ]\n\t\t    ], \n\t\t    \"name\": \"mapget_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"map_core\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"value\": {\n\t\t        \"list\": \"^@.list\", \n\t\t        \"t\": {\n\t\t          \"'\": [\n\t\t            \"^@.item\", \n\t\t            true\n\t\t          ]\n\t\t        }, \n\t\t        \"&\": \"map_core\"\n\t\t      }, \n\t\t      \"&\": \"makemap\"\n\t\t    }, \n\t\t    \"name\": \"keys2map_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"transform-t\": {\n\t\t      \"accum\": [], \n\t\t      \"list\": \"^@.list\", \n\t\t      \"t\": {\n\t\t        \":\": [\n\t\t          \"&&\", \n\t\t          \"^@.accum\", \n\t\t          {\n\t\t            \"true\": [\n\t\t              {\n\t\t                \":\": \"^@.item\"\n\t\t              }\n\t\t            ], \n\t\t            \"false\": [], \n\t\t            \"cond\": {\n\t\t              \":\": {\n\t\t                \"!\": \"^@.filter-t\"\n\t\t              }\n\t\t            }, \n\t\t            \"&\": \"if\"\n\t\t          }\n\t\t        ]\n\t\t      }, \n\t\t      \"&\": \"reduce\"\n\t\t    }, \n\t\t    \"name\": \"filter_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"hasitems_core_emlynoregan_com\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"true\": {\n\t\t        \"'\": {\n\t\t          \"true\": {\n\t\t            \"'\": {\n\t\t              \"true\": true, \n\t\t              \"false\": {\n\t\t                \"'\": {\n\t\t                  \"!\": \"^*.hasitems_core_emlynoregan_com\", \n\t\t                  \"list\": {\n\t\t                    \"''\": {\n\t\t                      \"b\": \"^@.list\", \n\t\t                      \"&\": \"tail\"\n\t\t                    }\n\t\t                  }\n\t\t                }\n\t\t              }, \n\t\t              \"cond\": {\n\t\t                \"'\": {\n\t\t                  \"!\": \"^*.hasitems_core_emlynoregan_com\", \n\t\t                  \"list\": {\n\t\t                    \"''\": {\n\t\t                      \"b\": \"^@.list\", \n\t\t                      \"&\": \"head\"\n\t\t                    }\n\t\t                  }\n\t\t                }\n\t\t              }, \n\t\t              \"&\": \"if\"\n\t\t            }\n\t\t          }, \n\t\t          \"false\": false, \n\t\t          \"cond\": {\n\t\t            \"'\": {\n\t\t              \"a\": {\n\t\t                \"list\": \"^@.list\", \n\t\t                \"&\": \"len\"\n\t\t              }, \n\t\t              \"b\": 0, \n\t\t              \"&\": \">\"\n\t\t            }\n\t\t          }, \n\t\t          \"&\": \"if\"\n\t\t        }\n\t\t      }, \n\t\t      \"false\": {\n\t\t        \"a\": \"^@.list\", \n\t\t        \"b\": null, \n\t\t        \"&\": \"!=\"\n\t\t      }, \n\t\t      \"cond\": {\n\t\t        \"'\": {\n\t\t          \"a\": \"list\", \n\t\t          \"b\": {\n\t\t            \"value\": \"^@.list\", \n\t\t            \"&\": \"type\"\n\t\t          }, \n\t\t          \"&\": \"=\"\n\t\t        }\n\t\t      }, \n\t\t      \"&\": \"if\"\n\t\t    }, \n\t\t    \"name\": \"hasitems_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"hasitems_core\", \n\t\t      \"filter_core\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"list\": {\n\t\t        \"filter-t\": {\n\t\t          \"'\": {\n\t\t            \"a\": \"^@.item\", \n\t\t            \"b\": \"^@.outeritem\", \n\t\t            \"&\": \"=\"\n\t\t          }\n\t\t        }, \n\t\t        \"list\": \"^@.list\", \n\t\t        \"outeritem\": \"^@.item\", \n\t\t        \"&\": \"filter_core\"\n\t\t      }, \n\t\t      \"&\": \"hasitems_core\"\n\t\t    }, \n\t\t    \"name\": \"isinlist_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"isinlist_core\", \n\t\t      \"filter_core\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"filter-t\": {\n\t\t        \":\": [\n\t\t          \"&!\", \n\t\t          {\n\t\t            \"item\": \"^@.item\", \n\t\t            \"list\": \"^@.arr2\", \n\t\t            \"&\": \"isinlist_core\"\n\t\t          }\n\t\t        ]\n\t\t      }, \n\t\t      \"list\": \"^@.arr1\", \n\t\t      \"&\": \"filter_core\"\n\t\t    }, \n\t\t    \"name\": \"subtractarrs_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"subtractarrs_core\", \n\t\t      \"map_core\", \n\t\t      \"mapget_core\", \n\t\t      \"zip\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"value\": {\n\t\t        \"list\": [\n\t\t          {\n\t\t            \"arr2\": \"^@.keys\", \n\t\t            \"arr1\": {\n\t\t              \"map\": \"^@.map\", \n\t\t              \"&\": \"keys\"\n\t\t            }, \n\t\t            \"&\": \"subtractarrs_core\"\n\t\t          }, \n\t\t          {\n\t\t            \"list\": {\n\t\t              \"arr2\": \"^@.keys\", \n\t\t              \"arr1\": {\n\t\t                \"map\": \"^@.map\", \n\t\t                \"&\": \"keys\"\n\t\t              }, \n\t\t              \"&\": \"subtractarrs_core\"\n\t\t            }, \n\t\t            \"t\": {\n\t\t              \":\": {\n\t\t                \"key\": \"^@.item\", \n\t\t                \"&\": \"mapget_core\"\n\t\t              }\n\t\t            }, \n\t\t            \"&\": \"map_core\"\n\t\t          }\n\t\t        ], \n\t\t        \"&\": \"zip\"\n\t\t      }, \n\t\t      \"&\": \"makemap\"\n\t\t    }, \n\t\t    \"name\": \"removekeys_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"transform-t\": {\n\t\t      \"accum\": \"^@.item\", \n\t\t      \"list\": \"^@.pipeline-t\", \n\t\t      \"t\": {\n\t\t        \":\": {\n\t\t          \"!\": \"^@.item\", \n\t\t          \"item\": \"^@.accum\", \n\t\t          \"accum\": null\n\t\t        }\n\t\t      }, \n\t\t      \"&\": \"reduce\"\n\t\t    }, \n\t\t    \"name\": \"pipeline_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"transform-t\": {\n\t\t      \"value\": [\n\t\t        [\n\t\t          \"^@.item\", \n\t\t          {\n\t\t            \"!\": [\n\t\t              \"&&\", \n\t\t              {\n\t\t                \":\": \"^%\"\n\t\t              }, \n\t\t              {\n\t\t                \"value\": [\n\t\t                  [\n\t\t                    \":\", \n\t\t                    \"^@.map\"\n\t\t                  ]\n\t\t                ], \n\t\t                \"&\": \"makemap\"\n\t\t              }, \n\t\t              \"^@.item\"\n\t\t            ]\n\t\t          }\n\t\t        ]\n\t\t      ], \n\t\t      \"&\": \"makemap\"\n\t\t    }, \n\t\t    \"name\": \"splitmapone_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"zip\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"list\": [\n\t\t        {\n\t\t          \"&\": \"keys\"\n\t\t        }, \n\t\t        {\n\t\t          \"&\": \"values\"\n\t\t        }\n\t\t      ], \n\t\t      \"&\": \"zip\"\n\t\t    }, \n\t\t    \"name\": \"unmakemap_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"map_core\", \n\t\t      \"splitmapone_core\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"list\": {\n\t\t        \"map\": \"^@.map\", \n\t\t        \"&\": \"keys\"\n\t\t      }, \n\t\t      \"t\": \"^*.splitmapone_core\", \n\t\t      \"&\": \"map_core\"\n\t\t    }, \n\t\t    \"name\": \"splitmap_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"filter_core\", \n\t\t      \"splitmap_core\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"filter-t\": {\n\t\t        \":\": [\n\t\t          \"&!=\", \n\t\t          [\n\t\t            \"&head\", \n\t\t            {\n\t\t              \"map\": \"^@.item\", \n\t\t              \"&\": \"values\"\n\t\t            }\n\t\t          ], \n\t\t          null\n\t\t        ]\n\t\t      }, \n\t\t      \"list\": {\n\t\t        \"map\": \"^@.map\", \n\t\t        \"&\": \"splitmap_core\"\n\t\t      }, \n\t\t      \"&\": \"filter_core\"\n\t\t    }, \n\t\t    \"name\": \"removenovaluemaps_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"removenovaluemaps_core\", \n\t\t      \"addmaps_core\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"list\": {\n\t\t        \"map\": \"^@.map\", \n\t\t        \"&\": \"removenovaluemaps_core\"\n\t\t      }, \n\t\t      \"accum\": {}, \n\t\t      \"t\": {\n\t\t        \":\": {\n\t\t          \"map2\": \"^@.item\", \n\t\t          \"map1\": \"^@.accum\", \n\t\t          \"&\": \"addmaps_core\"\n\t\t        }\n\t\t      }, \n\t\t      \"&\": \"reduce\"\n\t\t    }, \n\t\t    \"name\": \"removenullattribs_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"zip\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"map\": {\n\t\t        \"value\": {\n\t\t          \"list\": [\n\t\t            \"^@.list\", \n\t\t            \"^@.list\"\n\t\t          ], \n\t\t          \"&\": \"zip\"\n\t\t        }, \n\t\t        \"&\": \"makemap\"\n\t\t      }, \n\t\t      \"&\": \"keys\"\n\t\t    }, \n\t\t    \"name\": \"removedupstrarr_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"filter_core\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"filter-t\": {\n\t\t        \":\": [\n\t\t          \"&=\", \n\t\t          [\n\t\t            \"&!\", \n\t\t            [\n\t\t              \"&!\", \n\t\t              \"^@.left\"\n\t\t            ]\n\t\t          ], \n\t\t          [\n\t\t            \"&<\", \n\t\t            {\n\t\t              \"!\": [\n\t\t                \"&&\", \n\t\t                {\n\t\t                  \":\": \"^@\"\n\t\t                }, \n\t\t                [\n\t\t                  \"item\"\n\t\t                ], \n\t\t                \"^@.keypath\"\n\t\t              ]\n\t\t            }, \n\t\t            {\n\t\t              \"!\": [\n\t\t                \"&&\", \n\t\t                {\n\t\t                  \":\": \"^@\"\n\t\t                }, \n\t\t                [\n\t\t                  \"head\"\n\t\t                ], \n\t\t                \"^@.keypath\"\n\t\t              ]\n\t\t            }\n\t\t          ]\n\t\t        ]\n\t\t      }, \n\t\t      \"head\": {\n\t\t        \"b\": \"^@.list\", \n\t\t        \"&\": \"head\"\n\t\t      }, \n\t\t      \"list\": {\n\t\t        \"b\": \"^@.list\", \n\t\t        \"&\": \"tail\"\n\t\t      }, \n\t\t      \"&\": \"filter_core\"\n\t\t    }, \n\t\t    \"name\": \"qsfilter_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"qsfilter_core\", \n\t\t      \"quicksort_core_emlynoregan_com\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"true\": {\n\t\t        \":\": [\n\t\t          \"&&\", \n\t\t          {\n\t\t            \"list\": {\n\t\t              \"left\": true, \n\t\t              \"list\": \"^@.list\", \n\t\t              \"&\": \"qsfilter_core\"\n\t\t            }, \n\t\t            \"&\": \"quicksort_core_emlynoregan_com\"\n\t\t          }, \n\t\t          [\n\t\t            {\n\t\t              \"b\": \"^@.list\", \n\t\t              \"&\": \"head\"\n\t\t            }\n\t\t          ], \n\t\t          {\n\t\t            \"list\": {\n\t\t              \"left\": false, \n\t\t              \"list\": \"^@.list\", \n\t\t              \"&\": \"qsfilter_core\"\n\t\t            }, \n\t\t            \"&\": \"quicksort_core_emlynoregan_com\"\n\t\t          }\n\t\t        ]\n\t\t      }, \n\t\t      \"false\": [], \n\t\t      \"cond\": {\n\t\t        \":\": \"^@.list\"\n\t\t      }, \n\t\t      \"&\": \"if\"\n\t\t    }, \n\t\t    \"name\": \"quicksort_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"map_core\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"value\": {\n\t\t        \"t\": {\n\t\t          \":\": [\n\t\t            {\n\t\t              \"!\": [\n\t\t                \"&&\", \n\t\t                {\n\t\t                  \":\": \"^%\"\n\t\t                }, \n\t\t                [\n\t\t                  \"^@.item\"\n\t\t                ], \n\t\t                \"^@.keypath\"\n\t\t              ]\n\t\t            }, \n\t\t            \"^@.item\"\n\t\t          ]\n\t\t        }, \n\t\t        \"&\": \"map_core\"\n\t\t      }, \n\t\t      \"&\": \"makemap\"\n\t\t    }, \n\t\t    \"name\": \"idlisttomap_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"transform-t\": [\n\t\t      \"^%\", \n\t\t      {\n\t\t        \"!\": {\n\t\t          \"'\": {\n\t\t            \"true\": {\n\t\t              \"'\": {\n\t\t                \"accum\": {\n\t\t                  \"index\": 0, \n\t\t                  \"result\": \"\"\n\t\t                }, \n\t\t                \"list\": \"^@.list\", \n\t\t                \"t\": {\n\t\t                  \"'\": {\n\t\t                    \"true\": {\n\t\t                      \"'\": {\n\t\t                        \"index\": 1, \n\t\t                        \"result\": \"^@.item\"\n\t\t                      }\n\t\t                    }, \n\t\t                    \"false\": {\n\t\t                      \"'\": {\n\t\t                        \"true\": {\n\t\t                          \"'\": {\n\t\t                            \"index\": [\n\t\t                              \"&+\", \n\t\t                              \"^@.accum.index\", \n\t\t                              1\n\t\t                            ], \n\t\t                            \"result\": [\n\t\t                              \"&+\", \n\t\t                              \"^@.accum.result\", \n\t\t                              \"^@.lastseparator\", \n\t\t                              \"^@.item\"\n\t\t                            ]\n\t\t                          }\n\t\t                        }, \n\t\t                        \"false\": {\n\t\t                          \"'\": {\n\t\t                            \"index\": [\n\t\t                              \"&+\", \n\t\t                              \"^@.accum.index\", \n\t\t                              1\n\t\t                            ], \n\t\t                            \"result\": [\n\t\t                              \"&+\", \n\t\t                              \"^@.accum.result\", \n\t\t                              \"^@.separator\", \n\t\t                              \"^@.item\"\n\t\t                            ]\n\t\t                          }\n\t\t                        }, \n\t\t                        \"cond\": {\n\t\t                          \"'\": [\n\t\t                            \"&=\", \n\t\t                            \"^@.listlen\", \n\t\t                            [\n\t\t                              \"&+\", \n\t\t                              \"^@.accum.index\", \n\t\t                              1\n\t\t                            ]\n\t\t                          ]\n\t\t                        }, \n\t\t                        \"&\": \"if\"\n\t\t                      }\n\t\t                    }, \n\t\t                    \"cond\": {\n\t\t                      \"'\": [\n\t\t                        \"&=\", \n\t\t                        \"^@.accum.index\", \n\t\t                        0\n\t\t                      ]\n\t\t                    }, \n\t\t                    \"&\": \"if\"\n\t\t                  }\n\t\t                }, \n\t\t                \"&\": \"reduce\"\n\t\t              }\n\t\t            }, \n\t\t            \"false\": null, \n\t\t            \"cond\": {\n\t\t              \"'\": \"^@.list\"\n\t\t            }, \n\t\t            \"&\": \"if\"\n\t\t          }\n\t\t        }, \n\t\t        \"lastseparator\": {\n\t\t          \"true\": {\n\t\t            \"'\": \"^@.lastseparator\"\n\t\t          }, \n\t\t          \"false\": {\n\t\t            \"'\": {\n\t\t              \"true\": {\n\t\t                \"'\": \"^@.separator\"\n\t\t              }, \n\t\t              \"false\": \" and \", \n\t\t              \"cond\": {\n\t\t                \"'\": \"^@.separator\"\n\t\t              }, \n\t\t              \"&\": \"if\"\n\t\t            }\n\t\t          }, \n\t\t          \"cond\": {\n\t\t            \"'\": \"^@.lastseparator\"\n\t\t          }, \n\t\t          \"&\": \"if\"\n\t\t        }, \n\t\t        \"listlen\": {\n\t\t          \"list\": \"^@.list\", \n\t\t          \"&\": \"len\"\n\t\t        }, \n\t\t        \"separator\": {\n\t\t          \"true\": {\n\t\t            \"'\": \"^@.separator\"\n\t\t          }, \n\t\t          \"false\": \", \", \n\t\t          \"cond\": {\n\t\t            \"'\": \"^@.separator\"\n\t\t          }, \n\t\t          \"&\": \"if\"\n\t\t        }\n\t\t      }, \n\t\t      \"result\"\n\t\t    ], \n\t\t    \"name\": \"join_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"transform-t\": {\n\t\t      \"!\": {\n\t\t        \":\": {\n\t\t          \"!\": {\n\t\t            \":\": [\n\t\t              \"^%\", \n\t\t              {\n\t\t                \"accum\": {\n\t\t                  \"index\": 0, \n\t\t                  \"result\": []\n\t\t                }, \n\t\t                \"list\": \"^@.list\", \n\t\t                \"t\": {\n\t\t                  \":\": {\n\t\t                    \"true\": {\n\t\t                      \":\": {\n\t\t                        \"index\": [\n\t\t                          \"&+\", \n\t\t                          \"^@.accum.index\", \n\t\t                          1\n\t\t                        ], \n\t\t                        \"result\": [\n\t\t                          \"&&\", \n\t\t                          \"^@.accum.result\", \n\t\t                          \"^@.item\"\n\t\t                        ]\n\t\t                      }\n\t\t                    }, \n\t\t                    \"false\": {\n\t\t                      \":\": {\n\t\t                        \"index\": [\n\t\t                          \"&+\", \n\t\t                          \"^@.accum.index\", \n\t\t                          1\n\t\t                        ], \n\t\t                        \"result\": \"^@.accum.result\"\n\t\t                      }\n\t\t                    }, \n\t\t                    \"cond\": {\n\t\t                      \":\": [\n\t\t                        \"&&&\", \n\t\t                        [\n\t\t                          \"&>=\", \n\t\t                          \"^@.accum.index\", \n\t\t                          \"^@.start\"\n\t\t                        ], \n\t\t                        [\n\t\t                          \"&<\", \n\t\t                          \"^@.accum.index\", \n\t\t                          \"^@.stop\"\n\t\t                        ]\n\t\t                      ]\n\t\t                    }, \n\t\t                    \"&\": \"if\"\n\t\t                  }\n\t\t                }, \n\t\t                \"&\": \"reduce\"\n\t\t              }, \n\t\t              \"result\"\n\t\t            ]\n\t\t          }, \n\t\t          \"start\": {\n\t\t            \"!\": \"^@.fixarg\", \n\t\t            \"defaultarg\": 0, \n\t\t            \"arg\": \"^@.start\"\n\t\t          }, \n\t\t          \"stop\": {\n\t\t            \"!\": \"^@.fixarg\", \n\t\t            \"defaultarg\": {\n\t\t              \"list\": \"^@.list\", \n\t\t              \"&\": \"len\"\n\t\t            }, \n\t\t            \"arg\": \"^@.stop\"\n\t\t          }\n\t\t        }\n\t\t      }, \n\t\t      \"fixarg\": {\n\t\t        \":\": {\n\t\t          \"true\": {\n\t\t            \":\": {\n\t\t              \"true\": {\n\t\t                \":\": [\n\t\t                  \"&+\", \n\t\t                  {\n\t\t                    \"list\": \"^@.list\", \n\t\t                    \"&\": \"len\"\n\t\t                  }, \n\t\t                  \"^@.arg\"\n\t\t                ]\n\t\t              }, \n\t\t              \"false\": {\n\t\t                \":\": \"^@.arg\"\n\t\t              }, \n\t\t              \"cond\": {\n\t\t                \":\": [\n\t\t                  \"&<\", \n\t\t                  \"^@.arg\", \n\t\t                  0\n\t\t                ]\n\t\t              }, \n\t\t              \"&\": \"if\"\n\t\t            }\n\t\t          }, \n\t\t          \"false\": \"^@.defaultarg\", \n\t\t          \"cond\": {\n\t\t            \":\": \"^@.arg\"\n\t\t          }, \n\t\t          \"&\": \"if\"\n\t\t        }\n\t\t      }\n\t\t    }, \n\t\t    \"name\": \"slice_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"transform-t\": {\n\t\t      \"accum\": null, \n\t\t      \"list\": \"^@.list\", \n\t\t      \"t\": {\n\t\t        \"'\": {\n\t\t          \"true\": {\n\t\t            \"'\": \"^@.accum\"\n\t\t          }, \n\t\t          \"false\": {\n\t\t            \"'\": \"^@.item\"\n\t\t          }, \n\t\t          \"cond\": {\n\t\t            \"'\": [\n\t\t              \"&!=\", \n\t\t              \"^@.accum\", \n\t\t              null\n\t\t            ]\n\t\t          }, \n\t\t          \"&\": \"if\"\n\t\t        }\n\t\t      }, \n\t\t      \"&\": \"reduce\"\n\t\t    }, \n\t\t    \"name\": \"coalesce_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"isinlist_core\"\n\t\t    ], \n\t\t    \"transform-t\": [\n\t\t      \"^%\", \n\t\t      {\n\t\t        \"accum\": {\n\t\t          \"found\": false, \n\t\t          \"result\": null\n\t\t        }, \n\t\t        \"list\": \"^@.cases\", \n\t\t        \"t\": {\n\t\t          \"'\": {\n\t\t            \"true\": {\n\t\t              \"'\": \"^@.accum\"\n\t\t            }, \n\t\t            \"false\": {\n\t\t              \"'\": {\n\t\t                \"true\": {\n\t\t                  \"'\": {\n\t\t                    \"true\": {\n\t\t                      \"'\": {\n\t\t                        \"true\": {\n\t\t                          \"'\": {\n\t\t                            \"found\": true, \n\t\t                            \"result\": \"^@.item.1\"\n\t\t                          }\n\t\t                        }, \n\t\t                        \"false\": {\n\t\t                          \"'\": \"^@.accum\"\n\t\t                        }, \n\t\t                        \"cond\": {\n\t\t                          \"'\": {\n\t\t                            \"!\": \"^*.isinlist_core\", \n\t\t                            \"item\": \"^@.value\", \n\t\t                            \"list\": \"^@.item.0\"\n\t\t                          }\n\t\t                        }, \n\t\t                        \"&\": \"if\"\n\t\t                      }\n\t\t                    }, \n\t\t                    \"false\": {\n\t\t                      \"'\": {\n\t\t                        \"true\": {\n\t\t                          \"'\": {\n\t\t                            \"found\": true, \n\t\t                            \"result\": \"^@.item.1\"\n\t\t                          }\n\t\t                        }, \n\t\t                        \"false\": {\n\t\t                          \"'\": \"^@.accum\"\n\t\t                        }, \n\t\t                        \"cond\": {\n\t\t                          \"'\": [\n\t\t                            \"&=\", \n\t\t                            \"^@.item.0\", \n\t\t                            \"^@.value\"\n\t\t                          ]\n\t\t                        }, \n\t\t                        \"&\": \"if\"\n\t\t                      }\n\t\t                    }, \n\t\t                    \"cond\": {\n\t\t                      \"'\": [\n\t\t                        \"&=\", \n\t\t                        {\n\t\t                          \"value\": \"^@.item.0\", \n\t\t                          \"&\": \"type\"\n\t\t                        }, \n\t\t                        \"list\"\n\t\t                      ]\n\t\t                    }, \n\t\t                    \"&\": \"if\"\n\t\t                  }\n\t\t                }, \n\t\t                \"false\": {\n\t\t                  \"'\": {\n\t\t                    \"found\": true, \n\t\t                    \"result\": \"^@.item\"\n\t\t                  }\n\t\t                }, \n\t\t                \"cond\": {\n\t\t                  \"'\": [\n\t\t                    \"&&&\", \n\t\t                    [\n\t\t                      \"&=\", \n\t\t                      {\n\t\t                        \"value\": \"^@.item\", \n\t\t                        \"&\": \"type\"\n\t\t                      }, \n\t\t                      \"list\"\n\t\t                    ], \n\t\t                    [\n\t\t                      \"&=\", \n\t\t                      {\n\t\t                        \"list\": \"^@.item\", \n\t\t                        \"&\": \"len\"\n\t\t                      }, \n\t\t                      2\n\t\t                    ]\n\t\t                  ]\n\t\t                }, \n\t\t                \"&\": \"if\"\n\t\t              }\n\t\t            }, \n\t\t            \"cond\": {\n\t\t              \"'\": \"^@.accum.found\"\n\t\t            }, \n\t\t            \"&\": \"if\"\n\t\t          }\n\t\t        }, \n\t\t        \"&\": \"reduce\"\n\t\t      }, \n\t\t      \"result\"\n\t\t    ], \n\t\t    \"name\": \"switch_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"transform-t\": [\n\t\t      \"^%\", \n\t\t      {\n\t\t        \"accum\": {\n\t\t          \"found\": false, \n\t\t          \"result\": null\n\t\t        }, \n\t\t        \"list\": \"^@.cases\", \n\t\t        \"t\": {\n\t\t          \"'\": {\n\t\t            \"true\": {\n\t\t              \"'\": \"^@.accum\"\n\t\t            }, \n\t\t            \"false\": {\n\t\t              \"'\": {\n\t\t                \"true\": {\n\t\t                  \"'\": {\n\t\t                    \"true\": {\n\t\t                      \"'\": {\n\t\t                        \"found\": true, \n\t\t                        \"result\": {\n\t\t                          \"!\": \"^@.item.1\"\n\t\t                        }\n\t\t                      }\n\t\t                    }, \n\t\t                    \"false\": {\n\t\t                      \"'\": \"^@.accum\"\n\t\t                    }, \n\t\t                    \"cond\": {\n\t\t                      \"'\": {\n\t\t                        \"!\": {\n\t\t                          \"!\": \"^@.item.0\"\n\t\t                        }\n\t\t                      }\n\t\t                    }, \n\t\t                    \"&\": \"if\"\n\t\t                  }\n\t\t                }, \n\t\t                \"false\": {\n\t\t                  \"'\": {\n\t\t                    \"found\": true, \n\t\t                    \"result\": {\n\t\t                      \"!\": \"^@.item\"\n\t\t                    }\n\t\t                  }\n\t\t                }, \n\t\t                \"cond\": {\n\t\t                  \"'\": [\n\t\t                    \"&&&\", \n\t\t                    [\n\t\t                      \"&=\", \n\t\t                      {\n\t\t                        \"value\": \"^@.item\", \n\t\t                        \"&\": \"type\"\n\t\t                      }, \n\t\t                      \"list\"\n\t\t                    ], \n\t\t                    [\n\t\t                      \"&=\", \n\t\t                      {\n\t\t                        \"list\": \"^@.item\", \n\t\t                        \"&\": \"len\"\n\t\t                      }, \n\t\t                      2\n\t\t                    ]\n\t\t                  ]\n\t\t                }, \n\t\t                \"&\": \"if\"\n\t\t              }\n\t\t            }, \n\t\t            \"cond\": {\n\t\t              \"'\": \"^@.accum.found\"\n\t\t            }, \n\t\t            \"&\": \"if\"\n\t\t          }\n\t\t        }, \n\t\t        \"&\": \"reduce\"\n\t\t      }, \n\t\t      \"result\"\n\t\t    ], \n\t\t    \"name\": \"when_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"transform-t\": [\n\t\t      \"&=\", \n\t\t      {\n\t\t        \"value\": \"^@.item\", \n\t\t        \"&\": \"type\"\n\t\t      }, \n\t\t      \"map\"\n\t\t    ], \n\t\t    \"name\": \"isdict_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"transform-t\": [\n\t\t      \"&=\", \n\t\t      {\n\t\t        \"value\": \"^@.item\", \n\t\t        \"&\": \"type\"\n\t\t      }, \n\t\t      \"list\"\n\t\t    ], \n\t\t    \"name\": \"islist_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"isdict_core\", \n\t\t      \"islist_core\"\n\t\t    ], \n\t\t    \"transform-t\": [\n\t\t      \"&!\", \n\t\t      [\n\t\t        \"&||\", \n\t\t        {\n\t\t          \"&\": \"isdict_core\"\n\t\t        }, \n\t\t        {\n\t\t          \"&\": \"islist_core\"\n\t\t        }\n\t\t      ]\n\t\t    ], \n\t\t    \"name\": \"issimple_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"hasitems_core\", \n\t\t      \"isdict_core\", \n\t\t      \"islist_core\", \n\t\t      \"switch_core\", \n\t\t      \"map_core\", \n\t\t      \"isinlist_core\", \n\t\t      \"newdiff_core\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"!\": {\n\t\t        \":\": {\n\t\t          \"!\": {\n\t\t            \":\": {\n\t\t              \"true\": {\n\t\t                \":\": \"^@.value\"\n\t\t              }, \n\t\t              \"cond\": {\n\t\t                \":\": {\n\t\t                  \"!\": \"^@.keepvalue\"\n\t\t                }\n\t\t              }, \n\t\t              \"&\": \"if\"\n\t\t            }\n\t\t          }, \n\t\t          \"value\": {\n\t\t            \"cases\": [\n\t\t              [\n\t\t                \"map\", \n\t\t                {\n\t\t                  \"true\": {\n\t\t                    \":\": {\n\t\t                      \"value\": {\n\t\t                        \"list\": {\n\t\t                          \"map\": \"^@.new\", \n\t\t                          \"&\": \"keys\"\n\t\t                        }, \n\t\t                        \"t\": {\n\t\t                          \":\": {\n\t\t                            \"true\": {\n\t\t                              \":\": {\n\t\t                                \"true\": null, \n\t\t                                \"false\": {\n\t\t                                  \":\": {\n\t\t                                    \"!\": {\n\t\t                                      \":\": {\n\t\t                                        \"true\": {\n\t\t                                          \":\": [\n\t\t                                            \"^@.item\", \n\t\t                                            \"^@.value\"\n\t\t                                          ]\n\t\t                                        }, \n\t\t                                        \"cond\": {\n\t\t                                          \":\": {\n\t\t                                            \"!\": \"^@.keepvalue\"\n\t\t                                          }\n\t\t                                        }, \n\t\t                                        \"&\": \"if\"\n\t\t                                      }\n\t\t                                    }, \n\t\t                                    \"value\": {\n\t\t                                      \"new\": [\n\t\t                                        \"^%\", \n\t\t                                        \"^@.new\", \n\t\t                                        \"^@.item\"\n\t\t                                      ], \n\t\t                                      \"old\": [\n\t\t                                        \"^%\", \n\t\t                                        \"^@.old\", \n\t\t                                        \"^@.item\"\n\t\t                                      ], \n\t\t                                      \"&\": \"newdiff_core\"\n\t\t                                    }\n\t\t                                  }\n\t\t                                }, \n\t\t                                \"cond\": {\n\t\t                                  \":\": [\n\t\t                                    \"&=\", \n\t\t                                    [\n\t\t                                      \"^%\", \n\t\t                                      \"^@.new\", \n\t\t                                      \"^@.item\"\n\t\t                                    ], \n\t\t                                    [\n\t\t                                      \"^%\", \n\t\t                                      \"^@.old\", \n\t\t                                      \"^@.item\"\n\t\t                                    ]\n\t\t                                  ]\n\t\t                                }, \n\t\t                                \"&\": \"if\"\n\t\t                              }\n\t\t                            }, \n\t\t                            \"false\": {\n\t\t                              \":\": [\n\t\t                                \"^@.item\", \n\t\t                                [\n\t\t                                  \"^%\", \n\t\t                                  \"^@.new\", \n\t\t                                  \"^@.item\"\n\t\t                                ]\n\t\t                              ]\n\t\t                            }, \n\t\t                            \"cond\": {\n\t\t                              \":\": {\n\t\t                                \"list\": {\n\t\t                                  \"map\": \"^@.old\", \n\t\t                                  \"&\": \"keys\"\n\t\t                                }, \n\t\t                                \"&\": \"isinlist_core\"\n\t\t                              }\n\t\t                            }, \n\t\t                            \"&\": \"if\"\n\t\t                          }\n\t\t                        }, \n\t\t                        \"&\": \"map_core\"\n\t\t                      }, \n\t\t                      \"&\": \"makemap\"\n\t\t                    }\n\t\t                  }, \n\t\t                  \"false\": {\n\t\t                    \":\": \"^@.new\"\n\t\t                  }, \n\t\t                  \"cond\": {\n\t\t                    \":\": {\n\t\t                      \"item\": \"^@.old\", \n\t\t                      \"&\": \"isdict_core\"\n\t\t                    }\n\t\t                  }, \n\t\t                  \"&\": \"if\"\n\t\t                }\n\t\t              ], \n\t\t              [\n\t\t                \"list\", \n\t\t                {\n\t\t                  \"!\": {\n\t\t                    \":\": {\n\t\t                      \"true\": {\n\t\t                        \":\": \"^@.list\"\n\t\t                      }, \n\t\t                      \"false\": [], \n\t\t                      \"cond\": {\n\t\t                        \":\": {\n\t\t                          \"&\": \"hasitems_core\"\n\t\t                        }\n\t\t                      }, \n\t\t                      \"&\": \"if\"\n\t\t                    }\n\t\t                  }, \n\t\t                  \"list\": {\n\t\t                    \"true\": {\n\t\t                      \":\": [\n\t\t                        \"^%\", \n\t\t                        {\n\t\t                          \"accum\": {\n\t\t                            \"index\": 0, \n\t\t                            \"result\": []\n\t\t                          }, \n\t\t                          \"list\": \"^@.new\", \n\t\t                          \"t\": {\n\t\t                            \":\": {\n\t\t                              \"index\": [\n\t\t                                \"&+\", \n\t\t                                \"^@.accum.index\", \n\t\t                                1\n\t\t                              ], \n\t\t                              \"result\": [\n\t\t                                \"&&\", \n\t\t                                \"^@.accum.result\", \n\t\t                                [\n\t\t                                  {\n\t\t                                    \"!\": {\n\t\t                                      \":\": {\n\t\t                                        \"true\": {\n\t\t                                          \":\": \"^@.value\"\n\t\t                                        }, \n\t\t                                        \"cond\": {\n\t\t                                          \":\": {\n\t\t                                            \"!\": \"^@.keepvalue\"\n\t\t                                          }\n\t\t                                        }, \n\t\t                                        \"&\": \"if\"\n\t\t                                      }\n\t\t                                    }, \n\t\t                                    \"value\": {\n\t\t                                      \"new\": \"^@.item\", \n\t\t                                      \"old\": [\n\t\t                                        \"^%\", \n\t\t                                        \"^@.old\", \n\t\t                                        \"^@.accum.index\"\n\t\t                                      ], \n\t\t                                      \"&\": \"newdiff_core\"\n\t\t                                    }\n\t\t                                  }\n\t\t                                ]\n\t\t                              ]\n\t\t                            }\n\t\t                          }, \n\t\t                          \"&\": \"reduce\"\n\t\t                        }, \n\t\t                        \"result\"\n\t\t                      ]\n\t\t                    }, \n\t\t                    \"false\": {\n\t\t                      \":\": \"^@.new\"\n\t\t                    }, \n\t\t                    \"cond\": {\n\t\t                      \":\": {\n\t\t                        \"item\": \"^@.old\", \n\t\t                        \"&\": \"islist_core\"\n\t\t                      }\n\t\t                    }, \n\t\t                    \"&\": \"if\"\n\t\t                  }\n\t\t                }\n\t\t              ], \n\t\t              {\n\t\t                \"false\": {\n\t\t                  \":\": \"^@.new\"\n\t\t                }, \n\t\t                \"cond\": {\n\t\t                  \":\": [\n\t\t                    \"&=\", \n\t\t                    \"^@.new\", \n\t\t                    \"^@.old\"\n\t\t                  ]\n\t\t                }, \n\t\t                \"&\": \"if\"\n\t\t              }\n\t\t            ], \n\t\t            \"value\": {\n\t\t              \"value\": \"^@.new\", \n\t\t              \"&\": \"type\"\n\t\t            }, \n\t\t            \"&\": \"switch_core\"\n\t\t          }\n\t\t        }\n\t\t      }, \n\t\t      \"keepvalue\": {\n\t\t        \":\": [\n\t\t          \"&||\", \n\t\t          \"^@.value\", \n\t\t          [\n\t\t            \"&!\", \n\t\t            {\n\t\t              \"item\": {\n\t\t                \"&\": \"type\"\n\t\t              }, \n\t\t              \"list\": [\n\t\t                \"null\", \n\t\t                \"map\", \n\t\t                \"list\"\n\t\t              ], \n\t\t              \"&\": \"isinlist_core\"\n\t\t            }\n\t\t          ]\n\t\t        ]\n\t\t      }\n\t\t    }, \n\t\t    \"name\": \"newdiff_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"transform-t\": {\n\t\t      \"accum\": [], \n\t\t      \"t\": {\n\t\t        \":\": {\n\t\t          \"true\": {\n\t\t            \":\": \"^@.item\"\n\t\t          }, \n\t\t          \"false\": {\n\t\t            \":\": \"^@.accum\"\n\t\t          }, \n\t\t          \"cond\": {\n\t\t            \":\": [\n\t\t              \"&>\", \n\t\t              {\n\t\t                \"list\": \"^@.item\", \n\t\t                \"&\": \"len\"\n\t\t              }, \n\t\t              {\n\t\t                \"list\": \"^@.accum\", \n\t\t                \"&\": \"len\"\n\t\t              }\n\t\t            ]\n\t\t          }, \n\t\t          \"&\": \"if\"\n\t\t        }\n\t\t      }, \n\t\t      \"&\": \"reduce\"\n\t\t    }, \n\t\t    \"name\": \"longest_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"applynewdiff_core\", \n\t\t      \"when_core\", \n\t\t      \"removedupstrarr_core\", \n\t\t      \"map_core\", \n\t\t      \"longest_core\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"!\": {\n\t\t        \":\": {\n\t\t          \"cases\": [\n\t\t            [\n\t\t              {\n\t\t                \":\": [\n\t\t                  \"&=\", \n\t\t                  null, \n\t\t                  \"^@.diff\"\n\t\t                ]\n\t\t              }, \n\t\t              {\n\t\t                \":\": \"^@.old\"\n\t\t              }\n\t\t            ], \n\t\t            [\n\t\t              {\n\t\t                \":\": [\n\t\t                  \"&!=\", \n\t\t                  \"^@.oldtype\", \n\t\t                  \"^@.difftype\"\n\t\t                ]\n\t\t              }, \n\t\t              {\n\t\t                \":\": \"^@.diff\"\n\t\t              }\n\t\t            ], \n\t\t            [\n\t\t              {\n\t\t                \":\": [\n\t\t                  \"&=\", \n\t\t                  \"^@.difftype\", \n\t\t                  \"map\"\n\t\t                ]\n\t\t              }, \n\t\t              {\n\t\t                \":\": {\n\t\t                  \"!\": {\n\t\t                    \":\": {\n\t\t                      \"value\": {\n\t\t                        \"list\": \"^@.keys\", \n\t\t                        \"t\": {\n\t\t                          \":\": [\n\t\t                            \"^@.item\", \n\t\t                            {\n\t\t                              \"diff\": [\n\t\t                                \"^@\", \n\t\t                                \"diff\", \n\t\t                                \"^@.item\"\n\t\t                              ], \n\t\t                              \"old\": [\n\t\t                                \"^@\", \n\t\t                                \"old\", \n\t\t                                \"^@.item\"\n\t\t                              ], \n\t\t                              \"&\": \"applynewdiff_core\"\n\t\t                            }\n\t\t                          ]\n\t\t                        }, \n\t\t                        \"&\": \"map_core\"\n\t\t                      }, \n\t\t                      \"&\": \"makemap\"\n\t\t                    }\n\t\t                  }, \n\t\t                  \"keys\": {\n\t\t                    \"list\": [\n\t\t                      \"&&\", \n\t\t                      {\n\t\t                        \"map\": \"^@.old\", \n\t\t                        \"&\": \"keys\"\n\t\t                      }, \n\t\t                      {\n\t\t                        \"map\": \"^@.diff\", \n\t\t                        \"&\": \"keys\"\n\t\t                      }\n\t\t                    ], \n\t\t                    \"&\": \"removedupstrarr_core\"\n\t\t                  }\n\t\t                }\n\t\t              }\n\t\t            ], \n\t\t            [\n\t\t              {\n\t\t                \":\": [\n\t\t                  \"&=\", \n\t\t                  \"^@.difftype\", \n\t\t                  \"list\"\n\t\t                ]\n\t\t              }, \n\t\t              {\n\t\t                \":\": {\n\t\t                  \"!\": {\n\t\t                    \":\": [\n\t\t                      \"^%\", \n\t\t                      {\n\t\t                        \"list\": \"^@.longestlist\", \n\t\t                        \"accum\": {\n\t\t                          \"index\": 0, \n\t\t                          \"result\": []\n\t\t                        }, \n\t\t                        \"t\": {\n\t\t                          \":\": {\n\t\t                            \"index\": [\n\t\t                              \"&+\", \n\t\t                              \"^@.accum.index\", \n\t\t                              1\n\t\t                            ], \n\t\t                            \"result\": [\n\t\t                              \"&&\", \n\t\t                              \"^@.accum.result\", \n\t\t                              {\n\t\t                                \"diff\": [\n\t\t                                  \"^@\", \n\t\t                                  \"diff\", \n\t\t                                  \"^@.accum.index\"\n\t\t                                ], \n\t\t                                \"old\": [\n\t\t                                  \"^@\", \n\t\t                                  \"old\", \n\t\t                                  \"^@.accum.index\"\n\t\t                                ], \n\t\t                                \"&\": \"applynewdiff_core\"\n\t\t                              }\n\t\t                            ]\n\t\t                          }\n\t\t                        }, \n\t\t                        \"&\": \"reduce\"\n\t\t                      }, \n\t\t                      \"result\"\n\t\t                    ]\n\t\t                  }, \n\t\t                  \"longestlist\": {\n\t\t                    \"list\": [\n\t\t                      \"^@.old\", \n\t\t                      \"^@.diff\"\n\t\t                    ], \n\t\t                    \"&\": \"longest_core\"\n\t\t                  }\n\t\t                }\n\t\t              }\n\t\t            ], \n\t\t            {\n\t\t              \":\": \"^@.diff\"\n\t\t            }\n\t\t          ], \n\t\t          \"&\": \"when_core\"\n\t\t        }\n\t\t      }, \n\t\t      \"oldtype\": {\n\t\t        \"value\": \"^@.old\", \n\t\t        \"&\": \"type\"\n\t\t      }, \n\t\t      \"difftype\": {\n\t\t        \"value\": \"^@.diff\", \n\t\t        \"&\": \"type\"\n\t\t      }\n\t\t    }, \n\t\t    \"name\": \"applynewdiff_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"transform-t\": {\n\t\t      \"accum\": null, \n\t\t      \"t\": {\n\t\t        \":\": {\n\t\t          \"true\": {\n\t\t            \":\": {\n\t\t              \"value\": [\n\t\t                [\n\t\t                  \"!!\", \n\t\t                  {\n\t\t                    \"value\": [\n\t\t                      [\n\t\t                        \":\", \n\t\t                        \"^@.item\"\n\t\t                      ]\n\t\t                    ], \n\t\t                    \"&\": \"makemap\"\n\t\t                  }\n\t\t                ], \n\t\t                [\n\t\t                  \"s\", \n\t\t                  \"^@.accum\"\n\t\t                ]\n\t\t              ], \n\t\t              \"&\": \"makemap\"\n\t\t            }\n\t\t          }, \n\t\t          \"false\": {\n\t\t            \":\": \"^@.item\"\n\t\t          }, \n\t\t          \"cond\": {\n\t\t            \":\": \"^@.accum\"\n\t\t          }, \n\t\t          \"&\": \"if\"\n\t\t        }\n\t\t      }, \n\t\t      \"&\": \"reduce\"\n\t\t    }, \n\t\t    \"name\": \"combine_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"combine_core\", \n\t\t      \"keys2map_core\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"requires\": {\n\t\t        \"map\": {\n\t\t          \"list\": {\n\t\t            \"!\": {\n\t\t              \"accum\": {\n\t\t                \":\": [\n\t\t                  \"&&\"\n\t\t                ]\n\t\t              }, \n\t\t              \"list\": \"&@.list.*.requires\", \n\t\t              \"t\": {\n\t\t                \":\": [\n\t\t                  \"&&\", \n\t\t                  \"^@.accum\", \n\t\t                  \"^@.item\"\n\t\t                ]\n\t\t              }, \n\t\t              \"&\": \"reduce\"\n\t\t            }\n\t\t          }, \n\t\t          \"&\": \"keys2map_core\"\n\t\t        }, \n\t\t        \"&\": \"keys\"\n\t\t      }, \n\t\t      \"transform-t\": {\n\t\t        \"list\": \"&@.list.*.transform-t\", \n\t\t        \"&\": \"combine_core\"\n\t\t      }\n\t\t    }, \n\t\t    \"name\": \"declcombine_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"transform-t\": {\n\t\t      \"accum\": 0, \n\t\t      \"t\": {\n\t\t        \":\": {\n\t\t          \"!\": {\n\t\t            \":\": {\n\t\t              \"true\": {\n\t\t                \":\": \"^@.accum\"\n\t\t              }, \n\t\t              \"false\": {\n\t\t                \":\": \"^@.item\"\n\t\t              }, \n\t\t              \"cond\": {\n\t\t                \":\": [\n\t\t                  \"&>=\", \n\t\t                  \"^@.accum\", \n\t\t                  \"^@.item\"\n\t\t                ]\n\t\t              }, \n\t\t              \"&\": \"if\"\n\t\t            }\n\t\t          }\n\t\t        }\n\t\t      }, \n\t\t      \"&\": \"reduce\"\n\t\t    }, \n\t\t    \"name\": \"max_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"transform-t\": {\n\t\t      \"accum\": 0, \n\t\t      \"t\": {\n\t\t        \":\": {\n\t\t          \"!\": {\n\t\t            \":\": {\n\t\t              \"true\": {\n\t\t                \":\": \"^@.accum\"\n\t\t              }, \n\t\t              \"false\": {\n\t\t                \":\": \"^@.itemlen\"\n\t\t              }, \n\t\t              \"cond\": {\n\t\t                \":\": [\n\t\t                  \"&>=\", \n\t\t                  \"^@.accum\", \n\t\t                  \"^@.itemlen\"\n\t\t                ]\n\t\t              }, \n\t\t              \"&\": \"if\"\n\t\t            }\n\t\t          }, \n\t\t          \"itemlen\": {\n\t\t            \"list\": \"^@.item\", \n\t\t            \"&\": \"len\"\n\t\t          }\n\t\t        }\n\t\t      }, \n\t\t      \"&\": \"reduce\"\n\t\t    }, \n\t\t    \"name\": \"lenmax_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"switch_core\", \n\t\t      \"coalesce_core\", \n\t\t      \"traverse_core_emlynoregan_com\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"!\": {\n\t\t        \":\": {\n\t\t          \"cases\": [\n\t\t            [\n\t\t              \"map\", \n\t\t              {\n\t\t                \"value\": {\n\t\t                  \"accum\": [], \n\t\t                  \"list\": {\n\t\t                    \"map\": \"^@.source\", \n\t\t                    \"&\": \"keys\"\n\t\t                  }, \n\t\t                  \"t\": {\n\t\t                    \":\": {\n\t\t                      \"!\": {\n\t\t                        \":\": [\n\t\t                          \"&&\", \n\t\t                          \"^@.accum\", \n\t\t                          [\n\t\t                            [\n\t\t                              \"^@.item\", \n\t\t                              {\n\t\t                                \"source\": \"^@.transformedvalue\", \n\t\t                                \"&\": \"traverse_core_emlynoregan_com\"\n\t\t                              }\n\t\t                            ]\n\t\t                          ]\n\t\t                        ]\n\t\t                      }, \n\t\t                      \"transformedvalue\": {\n\t\t                        \"!\": \"^@.traverse-t\", \n\t\t                        \"value\": [\n\t\t                          \"^@\", \n\t\t                          \"source\", \n\t\t                          \"^@.item\"\n\t\t                        ], \n\t\t                        \"key\": \"^@.item\"\n\t\t                      }\n\t\t                    }\n\t\t                  }, \n\t\t                  \"&\": \"reduce\"\n\t\t                }, \n\t\t                \"&\": \"makemap\"\n\t\t              }\n\t\t            ], \n\t\t            [\n\t\t              \"list\", \n\t\t              [\n\t\t                \"^%\", \n\t\t                {\n\t\t                  \"accum\": {\n\t\t                    \"index\": 0, \n\t\t                    \"result\": []\n\t\t                  }, \n\t\t                  \"list\": \"^@.source\", \n\t\t                  \"t\": {\n\t\t                    \":\": {\n\t\t                      \"index\": [\n\t\t                        \"&+\", \n\t\t                        \"^@.index\", \n\t\t                        1\n\t\t                      ], \n\t\t                      \"result\": {\n\t\t                        \"!\": {\n\t\t                          \":\": [\n\t\t                            \"&&\", \n\t\t                            \"^@.accum.result\", \n\t\t                            [\n\t\t                              {\n\t\t                                \"source\": \"^@.transformedvalue\", \n\t\t                                \"&\": \"traverse_core_emlynoregan_com\"\n\t\t                              }\n\t\t                            ]\n\t\t                          ]\n\t\t                        }, \n\t\t                        \"transformedvalue\": {\n\t\t                          \"!\": \"^@.traverse-t\", \n\t\t                          \"value\": \"^@.item\", \n\t\t                          \"key\": \"^@.index\"\n\t\t                        }\n\t\t                      }\n\t\t                    }\n\t\t                  }, \n\t\t                  \"&\": \"reduce\"\n\t\t                }, \n\t\t                \"result\"\n\t\t              ]\n\t\t            ], \n\t\t            {\n\t\t              \"!\": \"^@.traverse-t\", \n\t\t              \"value\": \"^@.source\"\n\t\t            }\n\t\t          ], \n\t\t          \"value\": {\n\t\t            \"value\": \"^@.source\", \n\t\t            \"&\": \"type\"\n\t\t          }, \n\t\t          \"&\": \"switch_core\"\n\t\t        }\n\t\t      }, \n\t\t      \"traverse-t\": {\n\t\t        \"list\": [\n\t\t          \"^@.traverse-t\", \n\t\t          \"^@.t\"\n\t\t        ], \n\t\t        \"&\": \"coalesce_core\"\n\t\t      }\n\t\t    }, \n\t\t    \"name\": \"traverse_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"switch_core\", \n\t\t      \"coalesce_core\", \n\t\t      \"filttrav_core_emlynoregan_com\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"!\": {\n\t\t        \":\": {\n\t\t          \"cases\": [\n\t\t            [\n\t\t              \"map\", \n\t\t              {\n\t\t                \"value\": {\n\t\t                  \"accum\": [], \n\t\t                  \"list\": {\n\t\t                    \"map\": \"^@.source\", \n\t\t                    \"&\": \"keys\"\n\t\t                  }, \n\t\t                  \"t\": {\n\t\t                    \":\": {\n\t\t                      \"!\": {\n\t\t                        \":\": {\n\t\t                          \"true\": {\n\t\t                            \":\": [\n\t\t                              \"&&\", \n\t\t                              \"^@.accum\", \n\t\t                              [\n\t\t                                [\n\t\t                                  \"^@.item\", \n\t\t                                  {\n\t\t                                    \"source\": [\n\t\t                                      \"^@\", \n\t\t                                      \"source\", \n\t\t                                      \"^@.item\"\n\t\t                                    ], \n\t\t                                    \"&\": \"filttrav_core_emlynoregan_com\"\n\t\t                                  }\n\t\t                                ]\n\t\t                              ]\n\t\t                            ]\n\t\t                          }, \n\t\t                          \"false\": {\n\t\t                            \":\": \"^@.accum\"\n\t\t                          }, \n\t\t                          \"cond\": {\n\t\t                            \":\": \"^@.keepvalue\"\n\t\t                          }, \n\t\t                          \"&\": \"if\"\n\t\t                        }\n\t\t                      }, \n\t\t                      \"keepvalue\": {\n\t\t                        \"!\": \"^@.filter-t\", \n\t\t                        \"value\": [\n\t\t                          \"^@\", \n\t\t                          \"source\", \n\t\t                          \"^@.item\"\n\t\t                        ], \n\t\t                        \"key\": \"^@.item\"\n\t\t                      }\n\t\t                    }\n\t\t                  }, \n\t\t                  \"&\": \"reduce\"\n\t\t                }, \n\t\t                \"&\": \"makemap\"\n\t\t              }\n\t\t            ], \n\t\t            [\n\t\t              \"list\", \n\t\t              [\n\t\t                \"^%\", \n\t\t                {\n\t\t                  \"accum\": {\n\t\t                    \"index\": 0, \n\t\t                    \"result\": []\n\t\t                  }, \n\t\t                  \"list\": \"^@.source\", \n\t\t                  \"t\": {\n\t\t                    \":\": {\n\t\t                      \"index\": [\n\t\t                        \"&+\", \n\t\t                        \"^@.index\", \n\t\t                        1\n\t\t                      ], \n\t\t                      \"result\": {\n\t\t                        \"!\": {\n\t\t                          \":\": {\n\t\t                            \"true\": {\n\t\t                              \":\": [\n\t\t                                \"&&\", \n\t\t                                \"^@.accum.result\", \n\t\t                                {\n\t\t                                  \"source\": \"^@.item\", \n\t\t                                  \"&\": \"filttrav_core_emlynoregan_com\"\n\t\t                                }\n\t\t                              ]\n\t\t                            }, \n\t\t                            \"false\": {\n\t\t                              \":\": \"^@.accum.result\"\n\t\t                            }, \n\t\t                            \"cond\": {\n\t\t                              \":\": \"^@.keepvalue\"\n\t\t                            }, \n\t\t                            \"&\": \"if\"\n\t\t                          }\n\t\t                        }, \n\t\t                        \"keepvalue\": {\n\t\t                          \"!\": \"^@.filter-t\", \n\t\t                          \"value\": \"^@.item\", \n\t\t                          \"key\": \"^@.index\"\n\t\t                        }\n\t\t                      }\n\t\t                    }\n\t\t                  }, \n\t\t                  \"&\": \"reduce\"\n\t\t                }, \n\t\t                \"result\"\n\t\t              ]\n\t\t            ], \n\t\t            \"^@.source\"\n\t\t          ], \n\t\t          \"value\": {\n\t\t            \"value\": \"^@.source\", \n\t\t            \"&\": \"type\"\n\t\t          }, \n\t\t          \"&\": \"switch_core\"\n\t\t        }\n\t\t      }, \n\t\t      \"filter-t\": {\n\t\t        \"list\": [\n\t\t          \"^@.filter-t\", \n\t\t          \"^@.t\"\n\t\t        ], \n\t\t        \"&\": \"coalesce_core\"\n\t\t      }\n\t\t    }, \n\t\t    \"name\": \"filttrav_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }, \n\t\t  {\n\t\t    \"requires\": [\n\t\t      \"switch_core\", \n\t\t      \"removenullattribs_core\", \n\t\t      \"addmaps_core\", \n\t\t      \"meta_core\", \n\t\t      \"removekeys_core\", \n\t\t      \"unmakemap_core\"\n\t\t    ], \n\t\t    \"transform-t\": {\n\t\t      \"true\": {\n\t\t        \":\": {\n\t\t          \"cases\": [\n\t\t            [\n\t\t              \"map\", \n\t\t              {\n\t\t                \"map2\": {\n\t\t                  \"map\": {\n\t\t                    \"value\": [\n\t\t                      [\n\t\t                        \"!\", \n\t\t                        {\n\t\t                          \"t\": \"^@.t.-!\", \n\t\t                          \"&\": \"meta_core\"\n\t\t                        }\n\t\t                      ], \n\t\t                      [\n\t\t                        \"!!\", \n\t\t                        {\n\t\t                          \"t\": \"^@.t.-!!\", \n\t\t                          \"&\": \"meta_core\"\n\t\t                        }\n\t\t                      ], \n\t\t                      [\n\t\t                        \":\", \n\t\t                        {\n\t\t                          \"t\": \"^@.t.-:\", \n\t\t                          \"&\": \"meta_core\"\n\t\t                        }\n\t\t                      ], \n\t\t                      [\n\t\t                        \"'\", \n\t\t                        {\n\t\t                          \"t\": \"^@.t.-'\", \n\t\t                          \"&\": \"meta_core\"\n\t\t                        }\n\t\t                      ], \n\t\t                      [\n\t\t                        \"&&\", \n\t\t                        {\n\t\t                          \"t\": \"^@.t.-&&\", \n\t\t                          \"&\": \"meta_core\"\n\t\t                        }\n\t\t                      ], \n\t\t                      [\n\t\t                        \"&\", \n\t\t                        {\n\t\t                          \"t\": \"^@.t.-&\", \n\t\t                          \"&\": \"meta_core\"\n\t\t                        }\n\t\t                      ]\n\t\t                    ], \n\t\t                    \"&\": \"makemap\"\n\t\t                  }, \n\t\t                  \"&\": \"removenullattribs_core\"\n\t\t                }, \n\t\t                \"map1\": {\n\t\t                  \"keys\": [\n\t\t                    \"-!\", \n\t\t                    \"-!!\", \n\t\t                    \"-&\", \n\t\t                    \"-&&\", \n\t\t                    \"-:\", \n\t\t                    \"-'\"\n\t\t                  ], \n\t\t                  \"map\": {\n\t\t                    \"value\": {\n\t\t                      \"list\": {\n\t\t                        \"map\": \"^@.t\", \n\t\t                        \"&\": \"unmakemap_core\"\n\t\t                      }, \n\t\t                      \"t\": {\n\t\t                        \":\": [\n\t\t                          [\n\t\t                            \"^%\", \n\t\t                            \"^@.item\", \n\t\t                            0\n\t\t                          ], \n\t\t                          {\n\t\t                            \"t\": [\n\t\t                              \"^%\", \n\t\t                              \"^@.item\", \n\t\t                              1\n\t\t                            ], \n\t\t                            \"&\": \"meta_core\"\n\t\t                          }\n\t\t                        ]\n\t\t                      }, \n\t\t                      \"&\": \"map_core\"\n\t\t                    }, \n\t\t                    \"&\": \"makemap\"\n\t\t                  }, \n\t\t                  \"&\": \"removekeys_core\"\n\t\t                }, \n\t\t                \"&\": \"addmaps_core\"\n\t\t              }\n\t\t            ], \n\t\t            [\n\t\t              \"list\", \n\t\t              {\n\t\t                \"true\": {\n\t\t                  \":\": [\n\t\t                    \"&&\", \n\t\t                    {\n\t\t                      \":\": [\n\t\t                        \"&&\"\n\t\t                      ]\n\t\t                    }, \n\t\t                    {\n\t\t                      \"b\": {\n\t\t                        \"list\": \"^@.t\", \n\t\t                        \"t\": {\n\t\t                          \":\": {\n\t\t                            \"t\": \"^@.item\", \n\t\t                            \"&\": \"meta_core\"\n\t\t                          }\n\t\t                        }, \n\t\t                        \"&\": \"map_core\"\n\t\t                      }, \n\t\t                      \"&\": \"tail\"\n\t\t                    }\n\t\t                  ]\n\t\t                }, \n\t\t                \"false\": {\n\t\t                  \":\": {\n\t\t                    \"list\": \"^@.t\", \n\t\t                    \"t\": {\n\t\t                      \":\": {\n\t\t                        \"t\": \"^@.item\", \n\t\t                        \"&\": \"meta_core\"\n\t\t                      }\n\t\t                    }, \n\t\t                    \"&\": \"map_core\"\n\t\t                  }\n\t\t                }, \n\t\t                \"cond\": {\n\t\t                  \":\": [\n\t\t                    \"&=\", \n\t\t                    [\n\t\t                      \"^%\", \n\t\t                      \"^@.t\", \n\t\t                      0\n\t\t                    ], \n\t\t                    \"-&&\"\n\t\t                  ]\n\t\t                }, \n\t\t                \"&\": \"if\"\n\t\t              }\n\t\t            ], \n\t\t            \"^@.t\"\n\t\t          ], \n\t\t          \"value\": {\n\t\t            \"value\": \"^@.t\", \n\t\t            \"&\": \"type\"\n\t\t          }, \n\t\t          \"&\": \"switch_core\"\n\t\t        }\n\t\t      }, \n\t\t      \"cond\": {\n\t\t        \":\": [\n\t\t          \"&!=\", \n\t\t          \"^@.t\", \n\t\t          null\n\t\t        ]\n\t\t      }, \n\t\t      \"&\": \"if\"\n\t\t    }, \n\t\t    \"name\": \"meta_core_emlynoregan_com\", \n\t\t    \"language\": \"sUTL0\"\n\t\t  }\n\t\t]\n\t\t"
Sutlcore._hx_class = Sutlcore

class ValueType(Enum):
	_hx_class_name = "ValueType"
	_hx_constructs = ["TNull", "TInt", "TFloat", "TBool", "TObject", "TFunction", "TClass", "TEnum", "TUnknown"]

	@staticmethod
	def TClass(c):
		return ValueType("TClass", 6, [c])

	@staticmethod
	def TEnum(e):
		return ValueType("TEnum", 7, [e])
ValueType.TNull = ValueType("TNull", 0, list())
ValueType.TInt = ValueType("TInt", 1, list())
ValueType.TFloat = ValueType("TFloat", 2, list())
ValueType.TBool = ValueType("TBool", 3, list())
ValueType.TObject = ValueType("TObject", 4, list())
ValueType.TFunction = ValueType("TFunction", 5, list())
ValueType.TUnknown = ValueType("TUnknown", 8, list())
ValueType._hx_class = ValueType


class Type:
	_hx_class_name = "Type"
	_hx_statics = ["getClass", "typeof"]

	@staticmethod
	def getClass(o):
		if (o is None):
			return None
		if ((o is not None) and (((o == str) or python_lib_Inspect.isclass(o)))):
			return None
		if isinstance(o,_hx_AnonObject):
			return None
		if hasattr(o,"_hx_class"):
			return o._hx_class
		if hasattr(o,"__class__"):
			return o.__class__
		else:
			return None

	@staticmethod
	def typeof(v):
		if (v is None):
			return ValueType.TNull
		elif isinstance(v,bool):
			return ValueType.TBool
		elif isinstance(v,int):
			return ValueType.TInt
		elif isinstance(v,float):
			return ValueType.TFloat
		elif isinstance(v,str):
			return ValueType.TClass(str)
		elif isinstance(v,list):
			return ValueType.TClass(list)
		elif (isinstance(v,_hx_AnonObject) or python_lib_Inspect.isclass(v)):
			return ValueType.TObject
		elif isinstance(v,Enum):
			return ValueType.TEnum(v.__class__)
		elif (isinstance(v,type) or hasattr(v,"_hx_class")):
			return ValueType.TClass(v.__class__)
		elif callable(v):
			return ValueType.TFunction
		else:
			return ValueType.TUnknown
Type._hx_class = Type


class Util:
	_hx_class_name = "Util"
	_hx_statics = ["isStringBuiltinEval", "isArrayBuiltinEval", "getArrayBuiltinName", "gettype", "MakeExcept", "deepEqual", "deepEqual2", "deepCopy", "addObject", "StringToArray", "SequenceToArray", "flatten", "loadcoredist", "shallowCopy"]

	@staticmethod
	def isStringBuiltinEval(obj,b):
		retval = Util2.isString(obj)
		if retval:
			_hx_str = None
			def _hx_local_0():
				_hx_local_0 = obj
				if Std._hx_is(_hx_local_0,str):
					_hx_local_0
				else:
					raise _HxException("Class cast error")
				return _hx_local_0
			_hx_str = _hx_local_0()
			larr = _hx_str.split(".")
			retval = Util.isArrayBuiltinEval(larr,b)
		return retval

	@staticmethod
	def isArrayBuiltinEval(obj,b):
		retval = Util2.isArray(obj)
		if retval:
			arr = Util.SequenceToArray(obj)
			retval = (len(arr) > 0)
			if retval:
				lopArr = arr[0:1]
				lop = None
				if (len(lopArr) > 0):
					lop = (lopArr[0] if 0 < len(lopArr) else None)
				else:
					lop = None
				retval = Util2.isString(lop)
				if retval:
					lopStr = None
					def _hx_local_0():
						_hx_local_0 = lop
						if Std._hx_is(_hx_local_0,str):
							_hx_local_0
						else:
							raise _HxException("Class cast error")
						return _hx_local_0
					lopStr = _hx_local_0()
					lopSignifier = None
					if (0 >= len(lopStr)):
						lopSignifier = ""
					else:
						lopSignifier = lopStr[0]
					lopSignifier1 = None
					if (0 >= len(lopStr)):
						lopSignifier1 = ""
					else:
						lopSignifier1 = lopStr[0]
					lopBuiltinName = Util.getArrayBuiltinName(lopStr)
					retval = ((((lopSignifier1 == "&") or ((lopSignifier1 == "^")))) and hasattr(b,(("_hx_" + lopBuiltinName) if (lopBuiltinName in python_Boot.keywords) else (("_hx_" + lopBuiltinName) if (((((len(lopBuiltinName) > 2) and ((ord(lopBuiltinName[0]) == 95))) and ((ord(lopBuiltinName[1]) == 95))) and ((ord(lopBuiltinName[(len(lopBuiltinName) - 1)]) != 95)))) else lopBuiltinName))))
		return retval

	@staticmethod
	def getArrayBuiltinName(aOp):
		if ((len(aOp) is not None) and ((len(aOp) > 0))):
			return HxString.substr(aOp,1,(len(aOp) - 1))
		else:
			return None

	@staticmethod
	def gettype(item):
		if Util2.isObject(item):
			return "map"
		elif Util2.isArray(item):
			return "list"
		elif Util2.isString(item):
			return "string"
		elif Util2.isNumber(item):
			return "number"
		elif Util2.isBool(item):
			return "boolean"
		elif (item is None):
			return "null"
		else:
			return "unknown"

	@staticmethod
	def MakeExcept(aMessage,aPath):
		retval = ".".join([python_Boot.toString1(x1,'') for x1 in aPath])
		if (retval != ""):
			retval = ((("null" if retval is None else retval) + ": ") + ("null" if aMessage is None else aMessage))
		else:
			retval = aMessage
		return retval

	@staticmethod
	def deepEqual(aObj1,aObj2,maxdepth = 100):
		if (maxdepth is None):
			maxdepth = 100
		return Util.deepEqual2(aObj1,aObj2,[],maxdepth)

	@staticmethod
	def deepEqual2(aObj1,aObj2,path,maxdepth = 100):
		if (maxdepth is None):
			maxdepth = 100
		s = Sutl()
		retval = False
		if (maxdepth > 0):
			obj1Type = Util.gettype(aObj1)
			obj2Type = Util.gettype(aObj2)
			retval = (obj1Type == obj2Type)
			if (not retval):
				raise _HxException(Util.MakeExcept(((((((("Different types: type(" + Std.string(aObj1)) + ")=") + ("null" if obj1Type is None else obj1Type)) + ", type(") + Std.string(aObj2)) + ")=") + ("null" if obj2Type is None else obj2Type)),path))
			if retval:
				if (obj1Type == "map"):
					obj1Fields = python_Boot.fields(aObj1)
					obj2Fields = python_Boot.fields(aObj2)
					retval = (len(obj1Fields) == len(obj2Fields))
					if (not retval):
						raise _HxException(Util.MakeExcept(((((((("Keys don't match: fields(" + Std.string(aObj1)) + ")=") + Std.string(obj1Fields)) + ", fields(") + Std.string(aObj2)) + ")=") + Std.string(obj2Fields)),path))
					if retval:
						_g = 0
						while (_g < len(obj1Fields)):
							obj1Field = (obj1Fields[_g] if _g >= 0 and _g < len(obj1Fields) else None)
							_g = (_g + 1)
							path.append(obj1Field)
							retval = (hasattr(aObj2,(("_hx_" + obj1Field) if (obj1Field in python_Boot.keywords) else (("_hx_" + obj1Field) if (((((len(obj1Field) > 2) and ((ord(obj1Field[0]) == 95))) and ((ord(obj1Field[1]) == 95))) and ((ord(obj1Field[(len(obj1Field) - 1)]) != 95)))) else obj1Field))) and Util.deepEqual2(Reflect.field(aObj1,obj1Field),Reflect.field(aObj2,obj1Field),path,(maxdepth - 1)))
							if (len(path) == 0):
								None
							else:
								path.pop()
							if (not retval):
								break
				elif (obj1Type == "list"):
					retval = HxOverrides.eq(Reflect.field(aObj1,"length"),Reflect.field(aObj2,"length"))
					if (not retval):
						raise _HxException(Util.MakeExcept(((((((("Array lengths don't match: length(" + Std.string(aObj1)) + ")=") + Std.string(Reflect.field(aObj1,"length"))) + ", length(") + Std.string(aObj2)) + ")=") + Std.string(Reflect.field(aObj2,"length"))),path))
					if retval:
						_hx_len = None
						def _hx_local_0():
							_hx_local_1 = Reflect.field(aObj1,"length")
							if Std._hx_is(_hx_local_1,Int):
								_hx_local_1
							else:
								raise _HxException("Class cast error")
							return _hx_local_1
						_hx_len = _hx_local_0()
						_g1 = 0
						while (_g1 < _hx_len):
							ix = _g1
							_g1 = (_g1 + 1)
							path.append(ix)
							retval = Util.deepEqual2(HxOverrides.arrayGet(aObj1, ix),HxOverrides.arrayGet(aObj2, ix),path,(maxdepth - 1))
							if (len(path) == 0):
								None
							else:
								path.pop()
							if (not retval):
								break
				else:
					retval = HxOverrides.eq(aObj1,aObj2)
					if (not retval):
						raise _HxException(Util.MakeExcept((((("Values don't match (" + Std.string(aObj1)) + ", ") + Std.string(aObj2)) + ")"),path))
		return retval

	@staticmethod
	def deepCopy(aObj):
		retval = None
		s = Sutl()
		objType = Util.gettype(aObj)
		if (objType == "map"):
			retval = _hx_AnonObject({})
			objFields = python_Boot.fields(aObj)
			_g = 0
			while (_g < len(objFields)):
				objField = (objFields[_g] if _g >= 0 and _g < len(objFields) else None)
				_g = (_g + 1)
				value = Util.deepCopy(Reflect.field(aObj,objField))
				setattr(retval,(("_hx_" + objField) if (objField in python_Boot.keywords) else (("_hx_" + objField) if (((((len(objField) > 2) and ((ord(objField[0]) == 95))) and ((ord(objField[1]) == 95))) and ((ord(objField[(len(objField) - 1)]) != 95)))) else objField)),value)
		elif (objType == "list"):
			retval = []
			_g1 = 0
			_g11 = None
			def _hx_local_0():
				_hx_local_1 = aObj
				if Std._hx_is(_hx_local_1,list):
					_hx_local_1
				else:
					raise _HxException("Class cast error")
				return _hx_local_1
			_g11 = _hx_local_0()
			while (_g1 < len(_g11)):
				elem = (_g11[_g1] if _g1 >= 0 and _g1 < len(_g11) else None)
				_g1 = (_g1 + 1)
				Reflect.field(retval,"push")(Util.deepCopy(elem))
		else:
			retval = aObj
		return retval

	@staticmethod
	def addObject(aBase,aAdd):
		if (Util2.isObject(aBase) and Util2.isObject(aAdd)):
			_g = 0
			_g1 = python_Boot.fields(aAdd)
			while (_g < len(_g1)):
				key = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
				_g = (_g + 1)
				value = Reflect.field(aAdd,key)
				setattr(aBase,(("_hx_" + key) if (key in python_Boot.keywords) else (("_hx_" + key) if (((((len(key) > 2) and ((ord(key[0]) == 95))) and ((ord(key[1]) == 95))) and ((ord(key[(len(key) - 1)]) != 95)))) else key)),value)

	@staticmethod
	def StringToArray(aStrObj):
		retval = None
		if Util2.isString(aStrObj):
			retval = []
			liststr = None
			def _hx_local_0():
				_hx_local_0 = aStrObj
				if Std._hx_is(_hx_local_0,str):
					_hx_local_0
				else:
					raise _HxException("Class cast error")
				return _hx_local_0
			liststr = _hx_local_0()
			_g1 = 0
			_g = len(liststr)
			while (_g1 < _g):
				ix = _g1
				_g1 = (_g1 + 1)
				x = None
				if ((ix < 0) or ((ix >= len(liststr)))):
					x = ""
				else:
					x = liststr[ix]
				retval.append(x)
		return retval

	@staticmethod
	def SequenceToArray(aObj):
		retval = None
		if Util2.isArray(aObj):
			def _hx_local_0():
				_hx_local_0 = aObj
				if Std._hx_is(_hx_local_0,list):
					_hx_local_0
				else:
					raise _HxException("Class cast error")
				return _hx_local_0
			retval = _hx_local_0()
		elif Util2.isString(aObj):
			retval = Util.StringToArray(aObj)
		return retval

	@staticmethod
	def flatten(lst):
		retval = []
		_g = 0
		while (_g < len(lst)):
			elem = (lst[_g] if _g >= 0 and _g < len(lst) else None)
			_g = (_g + 1)
			if Util2.isArray(elem):
				a = elem
				retval = (retval + a)
			else:
				x = elem
				retval.append(x)
		return retval

	@staticmethod
	def loadcoredist():
		return Sutlcore.get()

	@staticmethod
	def shallowCopy(aObj):
		retval = None
		objType = Util.gettype(aObj)
		if (objType == "map"):
			retval = Reflect.copy(aObj)
		elif (objType == "list"):
			retval = []
			_g = 0
			_g1 = None
			def _hx_local_0():
				_hx_local_0 = aObj
				if Std._hx_is(_hx_local_0,list):
					_hx_local_0
				else:
					raise _HxException("Class cast error")
				return _hx_local_0
			_g1 = _hx_local_0()
			while (_g < len(_g1)):
				elem = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
				_g = (_g + 1)
				Reflect.field(retval,"push")(elem)
		else:
			retval = aObj
		return retval
Util._hx_class = Util


class SlowUtil2:
	_hx_class_name = "Util2"
	_hx_statics = ["isObject", "isArray", "isString", "isSequence", "isInt", "isNumber", "isBool"]

	@staticmethod
	def isObject(obj):
		retval = (Type.typeof(obj) == ValueType.TObject)
		return retval

	@staticmethod
	def isArray(obj):
		retval = Std._hx_is(obj,list)
		return retval

	@staticmethod
	def isString(obj):
		retval = (Type.getClass(obj) == str)
		return retval

	@staticmethod
	def isSequence(obj):
		return (Util2.isArray(obj) or Util2.isString(obj))

	@staticmethod
	def isInt(obj):
		ltype = Type.typeof(obj)
		return (ltype == ValueType.TInt)

	@staticmethod
	def isNumber(obj):
		ltype = Type.typeof(obj)
		return ((ltype == ValueType.TInt) or ((ltype == ValueType.TFloat)))

	@staticmethod
	def isBool(obj):
		ltype = Type.typeof(obj)
		return (ltype == ValueType.TBool)



class SlowUtil3:
	_hx_class_name = "Util3"
	_hx_statics = ["isBuiltinEval", "isEval", "isEval2", "isQuoteEval", "isDoubleQuoteEval", "isColonEval", "isDictTransform", "isListTransform", "isTruthy", "isPrefix", "get"]

	@staticmethod
	def isBuiltinEval(obj):
		return (Util2.isObject(obj) and hasattr(obj,(("_hx_" + "&") if ("&" in python_Boot.keywords) else (("_hx_" + "&") if (((((len("&") > 2) and ((ord("&"[0]) == 95))) and ((ord("&"[1]) == 95))) and ((ord("&"[(len("&") - 1)]) != 95)))) else "&"))))

	@staticmethod
	def isEval(obj):
		return (Util2.isObject(obj) and hasattr(obj,(("_hx_" + "!") if ("!" in python_Boot.keywords) else (("_hx_" + "!") if (((((len("!") > 2) and ((ord("!"[0]) == 95))) and ((ord("!"[1]) == 95))) and ((ord("!"[(len("!") - 1)]) != 95)))) else "!"))))

	@staticmethod
	def isEval2(obj):
		return (Util2.isObject(obj) and hasattr(obj,(("_hx_" + "!!") if ("!!" in python_Boot.keywords) else (("_hx_" + "!!") if (((((len("!!") > 2) and ((ord("!!"[0]) == 95))) and ((ord("!!"[1]) == 95))) and ((ord("!!"[(len("!!") - 1)]) != 95)))) else "!!"))))

	@staticmethod
	def isQuoteEval(obj):
		return (Util2.isObject(obj) and hasattr(obj,(("_hx_" + "'") if ("'" in python_Boot.keywords) else (("_hx_" + "'") if (((((len("'") > 2) and ((ord("'"[0]) == 95))) and ((ord("'"[1]) == 95))) and ((ord("'"[(len("'") - 1)]) != 95)))) else "'"))))

	@staticmethod
	def isDoubleQuoteEval(obj):
		return (Util2.isObject(obj) and hasattr(obj,(("_hx_" + "''") if ("''" in python_Boot.keywords) else (("_hx_" + "''") if (((((len("''") > 2) and ((ord("''"[0]) == 95))) and ((ord("''"[1]) == 95))) and ((ord("''"[(len("''") - 1)]) != 95)))) else "''"))))

	@staticmethod
	def isColonEval(obj):
		return (Util2.isObject(obj) and hasattr(obj,(("_hx_" + ":") if (":" in python_Boot.keywords) else (("_hx_" + ":") if (((((len(":") > 2) and ((ord(":"[0]) == 95))) and ((ord(":"[1]) == 95))) and ((ord(":"[(len(":") - 1)]) != 95)))) else ":"))))

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
			retval = (Reflect.field(aObj,"length") > 0)
		elif Util2.isString(aObj):
			retval = (aObj != "")
		elif Util2.isNumber(aObj):
			retval = (aObj != 0)
		elif Util2.isBool(aObj):
			retval = aObj
		elif Util2.isObject(aObj):
			retval = (len(python_Boot.fields(aObj)) > 0)
		else:
			retval = (aObj is not None)
		return retval

	@staticmethod
	def isPrefix(str1,str2):
		return (str2.find(str1) == 0)

	@staticmethod
	def get(obj,key,_hx_def = None):
		retval = None
		if Util2.isObject(obj):
			retval = Reflect.field(obj,key)
		if (retval is None):
			retval = _hx_def
		return retval



class haxe_IMap:
	_hx_class_name = "haxe.IMap"
haxe_IMap._hx_class = haxe_IMap


class haxe_ds_StringMap:
	_hx_class_name = "haxe.ds.StringMap"
	_hx_fields = ["h"]
	_hx_methods = ["keys"]
	_hx_interfaces = [haxe_IMap]

	def keys(self):
		this1 = None
		_this = self.h.keys()
		this1 = iter(_this)
		return python_HaxeIterator(this1)

haxe_ds_StringMap._hx_class = haxe_ds_StringMap


class haxe_format_JsonPrinter:
	_hx_class_name = "haxe.format.JsonPrinter"
	_hx_fields = ["buf", "replacer", "indent", "pretty", "nind"]
	_hx_methods = ["write", "fieldsString", "quote"]
	_hx_statics = ["print"]

	def __init__(self,replacer,space):
		self.buf = None
		self.replacer = None
		self.indent = None
		self.pretty = None
		self.nind = None
		self.replacer = replacer
		self.indent = space
		self.pretty = (space is not None)
		self.nind = 0
		self.buf = StringBuf()

	def write(self,k,v):
		if (self.replacer is not None):
			v = self.replacer(k,v)
		_g = Type.typeof(v)
		if ((_g.index) == 8):
			self.buf.b.write("\"???\"")
		elif ((_g.index) == 4):
			self.fieldsString(v,python_Boot.fields(v))
		elif ((_g.index) == 1):
			v1 = v
			self.buf.b.write(Std.string(v1))
		elif ((_g.index) == 2):
			v2 = None
			def _hx_local_0():
				f = v
				return (((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))
			if _hx_local_0():
				v2 = v
			else:
				v2 = "null"
			self.buf.b.write(Std.string(v2))
		elif ((_g.index) == 5):
			self.buf.b.write("\"<fun>\"")
		elif ((_g.index) == 6):
			c = _g.params[0]
			if (c == str):
				self.quote(v)
			elif (c == list):
				v3 = v
				s = "".join(map(chr,[91]))
				self.buf.b.write(s)
				_hx_len = len(v3)
				last = (_hx_len - 1)
				_g1 = 0
				while (_g1 < _hx_len):
					i = _g1
					_g1 = (_g1 + 1)
					if (i > 0):
						s1 = "".join(map(chr,[44]))
						self.buf.b.write(s1)
					else:
						_hx_local_1 = self
						_hx_local_2 = _hx_local_1.nind
						_hx_local_1.nind = (_hx_local_2 + 1)
						_hx_local_2
					if self.pretty:
						s2 = "".join(map(chr,[10]))
						self.buf.b.write(s2)
					if self.pretty:
						v4 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
						self.buf.b.write(Std.string(v4))
					self.write(i,(v3[i] if i >= 0 and i < len(v3) else None))
					if (i == last):
						_hx_local_3 = self
						_hx_local_4 = _hx_local_3.nind
						_hx_local_3.nind = (_hx_local_4 - 1)
						_hx_local_4
						if self.pretty:
							s3 = "".join(map(chr,[10]))
							self.buf.b.write(s3)
						if self.pretty:
							v5 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
							self.buf.b.write(Std.string(v5))
				s4 = "".join(map(chr,[93]))
				self.buf.b.write(s4)
			elif (c == haxe_ds_StringMap):
				v6 = v
				o = _hx_AnonObject({})
				_hx_local_5 = v6.keys()
				while _hx_local_5.hasNext():
					k1 = _hx_local_5.next()
					value = v6.h.get(k1,None)
					setattr(o,(("_hx_" + k1) if (k1 in python_Boot.keywords) else (("_hx_" + k1) if (((((len(k1) > 2) and ((ord(k1[0]) == 95))) and ((ord(k1[1]) == 95))) and ((ord(k1[(len(k1) - 1)]) != 95)))) else k1)),value)
				self.fieldsString(o,python_Boot.fields(o))
			elif (c == Date):
				v7 = v
				self.quote(v7.toString())
			else:
				self.fieldsString(v,python_Boot.fields(v))
		elif ((_g.index) == 7):
			i1 = None
			e = v
			i1 = e.index
			v8 = i1
			self.buf.b.write(Std.string(v8))
		elif ((_g.index) == 3):
			v9 = v
			self.buf.b.write(Std.string(v9))
		elif ((_g.index) == 0):
			self.buf.b.write("null")
		else:
			pass

	def fieldsString(self,v,fields):
		s = "".join(map(chr,[123]))
		self.buf.b.write(s)
		_hx_len = len(fields)
		last = (_hx_len - 1)
		first = True
		_g = 0
		while (_g < _hx_len):
			i = _g
			_g = (_g + 1)
			f = (fields[i] if i >= 0 and i < len(fields) else None)
			value = Reflect.field(v,f)
			if Reflect.isFunction(value):
				continue
			if first:
				_hx_local_0 = self
				_hx_local_1 = _hx_local_0.nind
				_hx_local_0.nind = (_hx_local_1 + 1)
				_hx_local_1
				first = False
			else:
				s1 = "".join(map(chr,[44]))
				self.buf.b.write(s1)
			if self.pretty:
				s2 = "".join(map(chr,[10]))
				self.buf.b.write(s2)
			if self.pretty:
				v1 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
				self.buf.b.write(Std.string(v1))
			self.quote(f)
			s3 = "".join(map(chr,[58]))
			self.buf.b.write(s3)
			if self.pretty:
				s4 = "".join(map(chr,[32]))
				self.buf.b.write(s4)
			self.write(f,value)
			if (i == last):
				_hx_local_2 = self
				_hx_local_3 = _hx_local_2.nind
				_hx_local_2.nind = (_hx_local_3 - 1)
				_hx_local_3
				if self.pretty:
					s5 = "".join(map(chr,[10]))
					self.buf.b.write(s5)
				if self.pretty:
					v2 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
					self.buf.b.write(Std.string(v2))
		s6 = "".join(map(chr,[125]))
		self.buf.b.write(s6)

	def quote(self,s):
		s1 = "".join(map(chr,[34]))
		self.buf.b.write(s1)
		i = 0
		while True:
			c = None
			index = i
			i = (i + 1)
			if (index >= len(s)):
				c = -1
			else:
				c = ord(s[index])
			if (c == -1):
				break
			if (c == 34):
				self.buf.b.write("\\\"")
			elif (c == 92):
				self.buf.b.write("\\\\")
			elif (c == 10):
				self.buf.b.write("\\n")
			elif (c == 13):
				self.buf.b.write("\\r")
			elif (c == 9):
				self.buf.b.write("\\t")
			elif (c == 8):
				self.buf.b.write("\\b")
			elif (c == 12):
				self.buf.b.write("\\f")
			else:
				s2 = "".join(map(chr,[c]))
				self.buf.b.write(s2)
		s3 = "".join(map(chr,[34]))
		self.buf.b.write(s3)

	@staticmethod
	def xprint(o,replacer = None,space = None):
		printer = haxe_format_JsonPrinter(replacer, space)
		printer.write("",o)
		return printer.buf.b.getvalue()

haxe_format_JsonPrinter._hx_class = haxe_format_JsonPrinter


class python_Boot:
	_hx_class_name = "python.Boot"
	_hx_statics = ["keywords", "toString1", "fields", "simpleField", "field", "getInstanceFields", "getSuperClass", "getClassFields", "prefixLength", "unhandleKeywords"]

	@staticmethod
	def toString1(o,s):
		if (o is None):
			return "null"
		if isinstance(o,str):
			return o
		if (s is None):
			s = ""
		if (len(s) >= 5):
			return "<...>"
		if isinstance(o,bool):
			if o:
				return "true"
			else:
				return "false"
		if isinstance(o,int):
			return unicode(o)
		if isinstance(o,float):
			try:
				if (o == int(o)):
					def _hx_local_1():
						def _hx_local_0():
							v = o
							return Math.floor((v + 0.5))
						return str(_hx_local_0())
					return _hx_local_1()
				else:
					return unicode(o)
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				e = _hx_e1
				return unicode(o)
		if isinstance(o,list):
			o1 = o
			l = len(o1)
			st = "["
			s = (("null" if s is None else s) + "\t")
			_g = 0
			while (_g < l):
				i = _g
				_g = (_g + 1)
				prefix = ""
				if (i > 0):
					prefix = ","
				st = (("null" if st is None else st) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1((o1[i] if i >= 0 and i < len(o1) else None),s))))))
			st = (("null" if st is None else st) + "]")
			return st
		try:
			if hasattr(o,"toString"):
				return o.toString()
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			pass
		if (python_lib_Inspect.isfunction(o) or python_lib_Inspect.ismethod(o)):
			return "<function>"
		if hasattr(o,"__class__"):
			if isinstance(o,_hx_AnonObject):
				toStr = None
				try:
					fields = python_Boot.fields(o)
					fieldsStr = None
					_g1 = []
					_g11 = 0
					while (_g11 < len(fields)):
						f = (fields[_g11] if _g11 >= 0 and _g11 < len(fields) else None)
						_g11 = (_g11 + 1)
						x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
						_g1.append(x)
					fieldsStr = _g1
					toStr = (("{ " + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " }")
				except Exception as _hx_e:
					_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
					e2 = _hx_e1
					return "{ ... }"
				if (toStr is None):
					return "{ ... }"
				else:
					return toStr
			if isinstance(o,Enum):
				o2 = o
				l1 = len(o2.params)
				hasParams = (l1 > 0)
				if hasParams:
					paramsStr = ""
					_g2 = 0
					while (_g2 < l1):
						i1 = _g2
						_g2 = (_g2 + 1)
						prefix1 = ""
						if (i1 > 0):
							prefix1 = ","
						paramsStr = (("null" if paramsStr is None else paramsStr) + HxOverrides.stringOrNull(((("null" if prefix1 is None else prefix1) + HxOverrides.stringOrNull(python_Boot.toString1((o2.params[i1] if i1 >= 0 and i1 < len(o2.params) else None),s))))))
					return (((HxOverrides.stringOrNull(o2.tag) + "(") + ("null" if paramsStr is None else paramsStr)) + ")")
				else:
					return o2.tag
			if hasattr(o,"_hx_class_name"):
				if (o.__class__.__name__ != "type"):
					fields1 = python_Boot.getInstanceFields(o)
					fieldsStr1 = None
					_g3 = []
					_g12 = 0
					while (_g12 < len(fields1)):
						f1 = (fields1[_g12] if _g12 >= 0 and _g12 < len(fields1) else None)
						_g12 = (_g12 + 1)
						x1 = ((("" + ("null" if f1 is None else f1)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f1),(("null" if s is None else s) + "\t"))))
						_g3.append(x1)
					fieldsStr1 = _g3
					toStr1 = (((HxOverrides.stringOrNull(o._hx_class_name) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr1]))) + " )")
					return toStr1
				else:
					fields2 = python_Boot.getClassFields(o)
					fieldsStr2 = None
					_g4 = []
					_g13 = 0
					while (_g13 < len(fields2)):
						f2 = (fields2[_g13] if _g13 >= 0 and _g13 < len(fields2) else None)
						_g13 = (_g13 + 1)
						x2 = ((("" + ("null" if f2 is None else f2)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f2),(("null" if s is None else s) + "\t"))))
						_g4.append(x2)
					fieldsStr2 = _g4
					toStr2 = (((("#" + HxOverrides.stringOrNull(o._hx_class_name)) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr2]))) + " )")
					return toStr2
			if (o == str):
				return "#String"
			if (o == list):
				return "#Array"
			if callable(o):
				return "function"
			try:
				if hasattr(o,"__repr__"):
					return o.__repr__()
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				pass
			if hasattr(o,"__str__"):
				return o.__str__([])
			if hasattr(o,"__name__"):
				return o.__name__
			return "???"
		else:
			return unicode(o)

	@staticmethod
	def fields(o):
		a = []
		if (o is not None):
			if hasattr(o,"_hx_fields"):
				fields = o._hx_fields
				return list(fields)
			if isinstance(o,_hx_AnonObject):
				d = o.__dict__
				keys = d.keys()
				handler = python_Boot.unhandleKeywords
				for k in keys:
					a.append(handler(k))
			elif hasattr(o,"__dict__"):
				a1 = []
				d1 = o.__dict__
				keys1 = d1.keys()
				for k in keys1:
					a.append(k)
		return a

	@staticmethod
	def simpleField(o,field):
		if (field is None):
			return None
		field1 = None
		if field in python_Boot.keywords:
			field1 = ("_hx_" + field)
		elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
			field1 = ("_hx_" + field)
		else:
			field1 = field
		if hasattr(o,field1):
			return getattr(o,field1)
		else:
			return None

	@staticmethod
	def field(o,field):
		if (field is None):
			return None
		_hx_local_0 = len(field)
		if (_hx_local_0 == 10):
			if (field == "charCodeAt"):
				if isinstance(o,str):
					s4 = o
					def _hx_local_1(a11):
						return HxString.charCodeAt(s4,a11)
					return _hx_local_1
		elif (_hx_local_0 == 11):
			if (field == "toLowerCase"):
				if isinstance(o,str):
					s1 = o
					def _hx_local_2():
						return HxString.toLowerCase(s1)
					return _hx_local_2
			elif (field == "toUpperCase"):
				if isinstance(o,str):
					s2 = o
					def _hx_local_3():
						return HxString.toUpperCase(s2)
					return _hx_local_3
			elif (field == "lastIndexOf"):
				if isinstance(o,str):
					s6 = o
					def _hx_local_4(a13):
						return HxString.lastIndexOf(s6,a13)
					return _hx_local_4
				elif isinstance(o,list):
					a2 = o
					def _hx_local_5(x2):
						return python_internal_ArrayImpl.lastIndexOf(a2,x2)
					return _hx_local_5
		elif (_hx_local_0 == 9):
			if (field == "substring"):
				if isinstance(o,str):
					s9 = o
					def _hx_local_6(a15):
						return HxString.substring(s9,a15)
					return _hx_local_6
		elif (_hx_local_0 == 5):
			if (field == "split"):
				if isinstance(o,str):
					s7 = o
					def _hx_local_7(d):
						return HxString.split(s7,d)
					return _hx_local_7
			elif (field == "shift"):
				if isinstance(o,list):
					x14 = o
					def _hx_local_8():
						return python_internal_ArrayImpl.shift(x14)
					return _hx_local_8
			elif (field == "slice"):
				if isinstance(o,list):
					x15 = o
					def _hx_local_9(a18):
						return python_internal_ArrayImpl.slice(x15,a18)
					return _hx_local_9
		elif (_hx_local_0 == 4):
			if (field == "copy"):
				if isinstance(o,list):
					def _hx_local_10():
						x6 = o
						return list(x6)
					return _hx_local_10
			elif (field == "join"):
				if isinstance(o,list):
					def _hx_local_11(sep):
						x9 = o
						return sep.join([python_Boot.toString1(x1,'') for x1 in x9])
					return _hx_local_11
			elif (field == "push"):
				if isinstance(o,list):
					x11 = o
					def _hx_local_12(e):
						return python_internal_ArrayImpl.push(x11,e)
					return _hx_local_12
			elif (field == "sort"):
				if isinstance(o,list):
					x16 = o
					def _hx_local_13(f2):
						python_internal_ArrayImpl.sort(x16,f2)
					return _hx_local_13
		elif (_hx_local_0 == 7):
			if (field == "indexOf"):
				if isinstance(o,str):
					s5 = o
					def _hx_local_14(a12):
						return HxString.indexOf(s5,a12)
					return _hx_local_14
				elif isinstance(o,list):
					a = o
					def _hx_local_15(x1):
						return python_internal_ArrayImpl.indexOf(a,x1)
					return _hx_local_15
			elif (field == "unshift"):
				if isinstance(o,list):
					x12 = o
					def _hx_local_16(e1):
						python_internal_ArrayImpl.unshift(x12,e1)
					return _hx_local_16
			elif (field == "reverse"):
				if isinstance(o,list):
					a4 = o
					def _hx_local_17():
						python_internal_ArrayImpl.reverse(a4)
					return _hx_local_17
		elif (_hx_local_0 == 3):
			if (field == "map"):
				if isinstance(o,list):
					x4 = o
					def _hx_local_18(f):
						return python_internal_ArrayImpl.map(x4,f)
					return _hx_local_18
			elif (field == "pop"):
				if isinstance(o,list):
					x10 = o
					def _hx_local_19():
						return python_internal_ArrayImpl.pop(x10)
					return _hx_local_19
		elif (_hx_local_0 == 8):
			if (field == "toString"):
				if isinstance(o,str):
					s10 = o
					def _hx_local_20():
						return HxString.toString(s10)
					return _hx_local_20
				elif isinstance(o,list):
					x3 = o
					def _hx_local_21():
						return python_internal_ArrayImpl.toString(x3)
					return _hx_local_21
			elif (field == "iterator"):
				if isinstance(o,list):
					x7 = o
					def _hx_local_22():
						return python_internal_ArrayImpl.iterator(x7)
					return _hx_local_22
		elif (_hx_local_0 == 6):
			if (field == "length"):
				if isinstance(o,str):
					s = o
					return len(s)
				elif isinstance(o,list):
					x = o
					return len(x)
			elif (field == "charAt"):
				if isinstance(o,str):
					s3 = o
					def _hx_local_23(a1):
						return HxString.charAt(s3,a1)
					return _hx_local_23
			elif (field == "substr"):
				if isinstance(o,str):
					s8 = o
					def _hx_local_24(a14):
						return HxString.substr(s8,a14)
					return _hx_local_24
			elif (field == "filter"):
				if isinstance(o,list):
					x5 = o
					def _hx_local_25(f1):
						return python_internal_ArrayImpl.filter(x5,f1)
					return _hx_local_25
			elif (field == "concat"):
				if isinstance(o,list):
					a16 = o
					def _hx_local_26(a21):
						return python_internal_ArrayImpl.concat(a16,a21)
					return _hx_local_26
			elif (field == "insert"):
				if isinstance(o,list):
					a3 = o
					def _hx_local_27(a17,x8):
						python_internal_ArrayImpl.insert(a3,a17,x8)
					return _hx_local_27
			elif (field == "remove"):
				if isinstance(o,list):
					x13 = o
					def _hx_local_28(e2):
						return python_internal_ArrayImpl.remove(x13,e2)
					return _hx_local_28
			elif (field == "splice"):
				if isinstance(o,list):
					x17 = o
					def _hx_local_29(a19,a22):
						return python_internal_ArrayImpl.splice(x17,a19,a22)
					return _hx_local_29
		else:
			pass
		field1 = None
		if field in python_Boot.keywords:
			field1 = ("_hx_" + field)
		elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
			field1 = ("_hx_" + field)
		else:
			field1 = field
		if hasattr(o,field1):
			return getattr(o,field1)
		else:
			return None

	@staticmethod
	def getInstanceFields(c):
		f = None
		if hasattr(c,"_hx_fields"):
			f = c._hx_fields
		else:
			f = []
		if hasattr(c,"_hx_methods"):
			a = c._hx_methods
			f = (f + a)
		sc = python_Boot.getSuperClass(c)
		if (sc is None):
			return f
		else:
			scArr = python_Boot.getInstanceFields(sc)
			scMap = set(scArr)
			res = []
			_g = 0
			while (_g < len(f)):
				f1 = (f[_g] if _g >= 0 and _g < len(f) else None)
				_g = (_g + 1)
				if (not f1 in scMap):
					scArr.append(f1)
			return scArr

	@staticmethod
	def getSuperClass(c):
		if (c is None):
			return None
		try:
			if hasattr(c,"_hx_super"):
				return c._hx_super
			return None
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			pass
		return None

	@staticmethod
	def getClassFields(c):
		if hasattr(c,"_hx_statics"):
			x = c._hx_statics
			return list(x)
		else:
			return []

	@staticmethod
	def unhandleKeywords(name):
		name = unicode(name)
		if (HxString.substr(name,0,python_Boot.prefixLength) == "_hx_"):
			real = HxString.substr(name,python_Boot.prefixLength,None)
			if real in python_Boot.keywords:
				return real
		return name
python_Boot._hx_class = python_Boot


class python_HaxeIterator:
	_hx_class_name = "python.HaxeIterator"
	_hx_fields = ["it", "x", "has", "checked"]
	_hx_methods = ["next", "hasNext"]

	def __init__(self,it):
		self.it = None
		self.x = None
		self.has = None
		self.checked = None
		self.checked = False
		self.has = False
		self.x = None
		self.it = it

	def next(self):
		if (not self.checked):
			self.hasNext()
		self.checked = False
		return self.x

	def hasNext(self):
		if (not self.checked):
			try:
				self.x = self.it.__next__()
				self.has = True
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				if isinstance(_hx_e1, StopIteration):
					s = _hx_e1
					self.has = False
					self.x = None
				else:
					raise _hx_e
			self.checked = True
		return self.has

python_HaxeIterator._hx_class = python_HaxeIterator


class python__KwArgs_KwArgs_Impl_:
	_hx_class_name = "python._KwArgs.KwArgs_Impl_"
	_hx_statics = ["fromT"]

	@staticmethod
	def fromT(d):
		d1 = python_Lib.anonAsDict(d)
		return d1
python__KwArgs_KwArgs_Impl_._hx_class = python__KwArgs_KwArgs_Impl_


class python_Lib:
	_hx_class_name = "python.Lib"
	_hx_statics = ["dictToAnon", "anonToDict", "anonAsDict", "dictAsAnon"]

	@staticmethod
	def dictToAnon(v):
		return _hx_AnonObject(v.copy())

	@staticmethod
	def anonToDict(o):
		if isinstance(o,_hx_AnonObject):
			return o.__dict__.copy()
		else:
			return None

	@staticmethod
	def anonAsDict(o):
		if isinstance(o,_hx_AnonObject):
			return o.__dict__
		else:
			return None

	@staticmethod
	def dictAsAnon(d):
		return _hx_AnonObject(d)
python_Lib._hx_class = python_Lib


class python_internal_ArrayImpl:
	_hx_class_name = "python.internal.ArrayImpl"
	_hx_statics = ["get_length", "concat", "iterator", "indexOf", "lastIndexOf", "toString", "pop", "push", "unshift", "remove", "shift", "slice", "sort", "splice", "map", "filter", "insert", "reverse", "_get", "_set"]

	@staticmethod
	def get_length(x):
		return len(x)

	@staticmethod
	def concat(a1,a2):
		return (a1 + a2)

	@staticmethod
	def iterator(x):
		return python_HaxeIterator(x.__iter__())

	@staticmethod
	def indexOf(a,x,fromIndex = None):
		_hx_len = len(a)
		l = None
		if (fromIndex is None):
			l = 0
		elif (fromIndex < 0):
			l = (_hx_len + fromIndex)
		else:
			l = fromIndex
		if (l < 0):
			l = 0
		_g = l
		while (_g < _hx_len):
			i = _g
			_g = (_g + 1)
			if (a[i] == x):
				return i
		return -1

	@staticmethod
	def lastIndexOf(a,x,fromIndex = None):
		_hx_len = len(a)
		l = None
		if (fromIndex is None):
			l = _hx_len
		elif (fromIndex < 0):
			l = ((_hx_len + fromIndex) + 1)
		else:
			l = (fromIndex + 1)
		if (l > _hx_len):
			l = _hx_len
		def _hx_local_1():
			l = (l - 1)
			return l
		while (_hx_local_1() > -1):
			if (a[l] == x):
				return l
		return -1

	@staticmethod
	def toString(x):
		return (("[" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in x]))) + "]")

	@staticmethod
	def pop(x):
		if (len(x) == 0):
			return None
		else:
			return x.pop()

	@staticmethod
	def push(x,e):
		x.append(e)
		return len(x)

	@staticmethod
	def unshift(x,e):
		x.insert(0, e)

	@staticmethod
	def remove(x,e):
		try:
			x.remove(e)
			return True
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e1 = _hx_e1
			return False

	@staticmethod
	def shift(x):
		if (len(x) == 0):
			return None
		return x.pop(0)

	@staticmethod
	def slice(x,pos,end = None):
		return x[pos:end]

	@staticmethod
	def sort(x,f):
		x.sort(key= python_lib_Functools.cmp_to_key(f))

	@staticmethod
	def splice(x,pos,_hx_len):
		if (pos < 0):
			pos = (len(x) + pos)
		if (pos < 0):
			pos = 0
		res = x[pos:(pos + _hx_len)]
		del x[pos:(pos + _hx_len)]
		return res

	@staticmethod
	def map(x,f):
		return list(map(f,x))

	@staticmethod
	def filter(x,f):
		return list(filter(f,x))

	@staticmethod
	def insert(a,pos,x):
		a.insert(pos, x)

	@staticmethod
	def reverse(a):
		a.reverse()

	@staticmethod
	def _get(x,idx):
		if ((idx > -1) and ((idx < len(x)))):
			return x[idx]
		else:
			return None

	@staticmethod
	def _set(x,idx,v):
		l = len(x)
		while (l < idx):
			x.append(None)
			l = (l + 1)
		if (l == idx):
			x.append(v)
		else:
			x[idx] = v
		return v
python_internal_ArrayImpl._hx_class = python_internal_ArrayImpl


class _HxException(Exception):
	_hx_class_name = "_HxException"
	_hx_fields = ["val"]
	_hx_methods = []
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = Exception


	def __init__(self,val):
		self.val = None
		message = str(val)
		Exception.__init__(self, message)
		self.val = val

_HxException._hx_class = _HxException


class HxOverrides:
	_hx_class_name = "HxOverrides"
	_hx_statics = ["eq", "stringOrNull", "push", "map", "arrayGet", "mapKwArgs"]

	@staticmethod
	def eq(a,b):
		if (isinstance(a,list) or isinstance(b,list)):
			return a is b
		return (a == b)

	@staticmethod
	def stringOrNull(s):
		if (s is None):
			return "null"
		else:
			return s

	@staticmethod
	def push(x,e):
		if isinstance(x,list):
			_this = x
			_this.append(e)
			return len(_this)
		return x.push(e)

	@staticmethod
	def map(x,f):
		if isinstance(x,list):
			return list(map(f,x))
		return x.map(f)

	@staticmethod
	def arrayGet(a,i):
		if isinstance(a,list):
			x = a
			if ((i > -1) and ((i < len(x)))):
				return x[i]
			else:
				return None
		else:
			return a[i]

	@staticmethod
	def mapKwArgs(a,v):
		a1 = python_Lib.dictAsAnon(python_Lib.anonToDict(a))
		def _hx_local_0():
			_this = v.keys()
			def _hx_local_2():
				def _hx_local_1():
					this1 = iter(_this)
					return python_HaxeIterator(this1)
				return _hx_local_1()
			return _hx_local_2()
		_hx_local_3 = _hx_local_0()
		while _hx_local_3.hasNext():
			k = _hx_local_3.next()
			val = v.get(k)
			if hasattr(a1,k):
				x = getattr(a1,k)
				setattr(a1,val,x)
				delattr(a1,k)
		return a1
HxOverrides._hx_class = HxOverrides


class HxString:
	_hx_class_name = "HxString"
	_hx_statics = ["split", "charCodeAt", "charAt", "lastIndexOf", "toUpperCase", "toLowerCase", "indexOf", "toString", "get_length", "substring", "substr"]

	@staticmethod
	def split(s,d):
		if (d == ""):
			return list(s)
		else:
			return s.split(d)

	@staticmethod
	def charCodeAt(s,index):
		if ((((s is None) or ((len(s) == 0))) or ((index < 0))) or ((index >= len(s)))):
			return None
		else:
			return ord(s[index])

	@staticmethod
	def charAt(s,index):
		if ((index < 0) or ((index >= len(s)))):
			return ""
		else:
			return s[index]

	@staticmethod
	def lastIndexOf(s,_hx_str,startIndex = None):
		if (startIndex is None):
			return s.rfind(_hx_str, 0, len(s))
		else:
			i = s.rfind(_hx_str, 0, (startIndex + 1))
			startLeft = None
			if (i == -1):
				startLeft = max(0,((startIndex + 1) - len(_hx_str)))
			else:
				startLeft = (i + 1)
			check = s.find(_hx_str, startLeft, len(s))
			if ((check > i) and ((check <= startIndex))):
				return check
			else:
				return i

	@staticmethod
	def toUpperCase(s):
		return s.upper()

	@staticmethod
	def toLowerCase(s):
		return s.lower()

	@staticmethod
	def indexOf(s,_hx_str,startIndex = None):
		if (startIndex is None):
			return s.find(_hx_str)
		else:
			return s.find(_hx_str, startIndex)

	@staticmethod
	def toString(s):
		return s

	@staticmethod
	def get_length(s):
		return len(s)

	@staticmethod
	def substring(s,startIndex,endIndex = None):
		if (startIndex < 0):
			startIndex = 0
		if (endIndex is None):
			return s[startIndex:]
		else:
			if (endIndex < 0):
				endIndex = 0
			if (endIndex < startIndex):
				return s[endIndex:startIndex]
			else:
				return s[startIndex:endIndex]

	@staticmethod
	def substr(s,startIndex,_hx_len = None):
		if (_hx_len is None):
			return s[startIndex:]
		else:
			if (_hx_len == 0):
				return ""
			return s[startIndex:(startIndex + _hx_len)]
HxString._hx_class = HxString

Math.NEGATIVE_INFINITY = float("-inf")
Math.POSITIVE_INFINITY = float("inf")
Math.NaN = float("nan")
Math.PI = python_lib_Math.pi

python_Boot.keywords = set(["and", "del", "from", "not", "with", "as", "elif", "global", "or", "yield", "assert", "else", "if", "pass", "None", "break", "except", "import", "raise", "True", "class", "exec", "in", "return", "False", "continue", "finally", "is", "try", "def", "for", "lambda", "while"])
python_Boot.prefixLength = len("_hx_")