# from singleton.com_classe import SingletonClass
from com_metaclasse import Singleton


class BancoDados(Singleton):
    n_conexao: int = 0

    def __new__(cls, *args, **kwargs):
        cls.n_conexao += 1
        return object.__new__(cls)

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self._conectado = False

    def conectar(self):
        if not self._conectado:
            print(f'{hex(id(self))} se conectou no banco')
            self._conectado = True

    def desconectar(self):
        if self._conectado:
            print(f'{hex(id(self))} se desconectou do banco')
            self._conectado = False

    def __repr__(self):
        return f'{type(self).__qualname__}(host={self.host}, port={self.port}, conectado={self._conectado})'


if __name__ == '__main__':
    c1 = BancoDados.get_instance('localhost', 5000)
    c2 = BancoDados.get_instance('localhost', 5000)
    c3 = BancoDados.get_instance('localhost', 5000)
    c4 = BancoDados.get_instance('localhost', 5000)

    c1.conectar()
    c2.conectar()
    c3.conectar()
    c4.conectar()

    print('Quantidade de conexões:', BancoDados.n_conexao)
