class ControRemoto:
    def __init__(self, cor, peso, televisao):
        self.cor = cor
        self.peso = peso
        self.televisao = televisao

    def ligarDesligar(self):
        self.televisao.set_ligado(not self.televisao.is_ligado())

    def _verificar_televisao_ligada(self):
        if not self.televisao.is_ligado():
            return False
        return True

    def volumeUp(self):
        if self._verificar_televisao_ligada():
            if self.televisao.get_volume() < 100:
                self.televisao.set_volume(self.televisao.get_volume() + 1)
            else:
                print('VOLUME MÁXIMO!!!')

    def volumeDown(self):
        if self._verificar_televisao_ligada():
            if self.televisao.get_volume() > 0:
                self.televisao.set_volume(self.televisao.get_volume() - 1)
            else:
                print('VOLUME MÍNIMO')

    def mute(self):
        if self._verificar_televisao_ligada():
            self.televisao.set_volume(0)

    def unmute(self):
        if self._verificar_televisao_ligada():
            self.televisao.set_volume(50)

    def canalUp(self):
        if self._verificar_televisao_ligada():
            if self.televisao.get_canal() < 35:
                self.televisao.set_canal(self.televisao.get_canal() + 1)
            else:
                self.televisao.set_canal(1)

    def canalDown(self):
        if self._verificar_televisao_ligada():
            if self.televisao.get_canal() > 1:
                self.televisao.set_canal(self.televisao.get_canal() - 1)
            else:
                self.televisao.set_canal(35)
    
    def escolherCanal(self, num):
        if self._verificar_televisao_ligada():
            if num >= 1 and num <= 35:
                self.televisao.set_canal(num)
            else:
                print('Canal inexistente na lista')

    def informacoes(self):
        return self.televisao