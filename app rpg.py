from rpg import rpg

mago = rpg('mago',1300, 1040, 177, 'dano mágico')

alado = rpg('alado',1200, 1400, 180, 'poder divino')

bardo = rpg('bardo',1240, 1030, 160, 'talento artístico')

guerreiro = rpg('guerreiro',1600, 'NÃO USA', 202, 'dano físico')

ladino = rpg('ladino',1200, 'NÃO USA', 205, 'mãos leves')


mago.missão()
mago.dano_causado()
mago.dano_sofrido(520)
mago.dano_sofrido(400)
mago.dano_sofrido(800)
mago.missão()
mago.dano_causado()



