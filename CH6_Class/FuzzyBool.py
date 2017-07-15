class FuzzyBool:
    def __init__(self, value=0.0):
        self.__value = value if 0.0 <= value <= 1.0 else 0.0

    def __invert__(self): #equal to ~ operator
        return FuzzyBool(1.0 - self.__value)

    def __and__(self, other):
        return FuzzyBool(min(self.__value, other.__value))

    def __iand__(self, other):
        self.__value = min(self.__value, other.__value)
        return self
    
    def __or__(self, other):
        return max(self.__value, other.__value)
    
    def __ior__(self, other):
        self.__value = max(self.__value, other.__value)
        return self

    def __repr__(self):
        return ("{0}({1})".format(self.__class__.__name__, self.__value))
    # __class__.name , represent

    def __str__(self):
        return str(self.__value)

    # operate as  bool(fuzzy), doing the conversion
    def __bool__(self):
        return self.__value > 0.85

    def __int__(self):
        return round(self.__value)

    def __float__(self):
        return self.__value

    # To have full (< . <= , ==, != , >= , >),  we at least created < <= ==, 
    # the python would do the rest for you
    def __lt__(self, other):
        return self.__value < other.__value

    def __eq__(self, other):
        return self.__value == other.__value

    def __lq__(self, other):
        return self.__value <= other.__value

    def __hash__(self):
        return hash(id(self))
    #id is a built-in function to return a hash-id, mostly would be the memory address

    def __format__(self, format_spec):
        return self.__value.__format__(format_spec)

    @staticmethod
    def conjunction(*fuzzies):
        return FuzzyBool(min([float(x) for x in fuzzies]))

    def disjunction(*fuzzies):
        return FuzzyBool(max([float(x) for x in fuzzies]))

