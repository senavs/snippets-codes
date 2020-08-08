class SingletonClass:

    def __new__(cls):
        if not cls.__dict__.get('_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()


if __name__ == '__main__':
    s1 = SingletonClass()
    s2 = SingletonClass.get_instance()

    print(s1)
    print(s2)
