class rpg:
    def __init__(self,categoria, vida, mana, dano, habilidade):
        self.categoria = categoria
        self.vida = vida
        self.mana = mana
        self.dano = dano
        self.habilidade = habilidade
        self.dano_alterado = 0 
        self.vivo = True

    def dano_causado(self):
        if self.vivo:
           self.dano_alterado += self.dano
           print (f'{self.categoria} causou {self.dano_alterado} de dano utilizando {self.habilidade}')
        else:
            print(f'{self.categoria} está morto e não pode causar dano.')

    def dano_sofrido(self,dano):
        if self.vivo:
           self.vida -= dano
           if self.vida <= 0:
              self.vivo = False
              print(f'{self.categoria} sofreu {dano} de dano e morreu.')
           else:
               print(f'{self.categoria} sofreu {dano} de dano, restando {self.vida} de HP')
        else:
            print(f'{self.categoria} sofreu {dano} de dano, restando {self.vida} de HP')

    def missão(self):
        if self.vivo:
           print(f'{self.categoria} está na missão de derrotar o Dragão das masmorras e precisará utilizar {self.habilidade} para vencê-lo')
        else:
            print(f'{self.categoria} está morto e não pode participar de missões')
            
