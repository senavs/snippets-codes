class SingletonMeta(type):

    def __call__(cls, *args, **kwargs):
        raise RuntimeError('Classes Singleton têm o construtor privado.')

    def get_instance(cls, *args, **kwargs):
        if not cls.__dict__.get('_instance'):
            cls._instance = type.__call__(cls, *args, **kwargs)
        return cls._instance


class Singleton(metaclass=SingletonMeta):
    pass
