from Televisao import Televisao
from ControleRemoto import ControRemoto

tv = Televisao()
controle = ControRemoto('Preto', 235.50, tv)
print(controle.informacoes())

controle.ligarDesligar()
controle.escolherCanal(35)
controle.volumeUp()
print(controle.informacoes())

controle.canalUp()
controle.mute()
print(controle.informacoes())

controle.canalDown()
controle.unmute()
print(controle.informacoes())
