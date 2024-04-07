class Televisao:
    def __init__(self):
        self._ligado = False
        self._canal = 1
        self._volume = 50

    def is_ligado(self):
        return self._ligado

    def set_ligado(self, ligado):
        self._ligado = ligado

    def get_canal(self):
        return self._canal

    def set_canal(self, canal):
        self._canal = canal

    def get_volume(self):
        return self._volume

    def set_volume(self, volume):
        self._volume = volume

    def __str__(self):
        return f"Ligado: '{self._ligado}' \nCanal: '{self._canal}' \nVolume: '{self._volume}' \n"
