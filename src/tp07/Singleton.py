"""
   
 auth : l.devigne

"""


class Singleton(type):
    __instance = None

    def __call__(self, *args, **kargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kargs)
        else:
            self.__instance.__init__(*args, **kargs)
        return self.__instance
