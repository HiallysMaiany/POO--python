-- Estudo de Classes em Python: Um exemplo prático com a Classe 'carro' --
##
 O conceito de classes e objetos é um dos pilares da programação orientada a objetos (POO). 
 Em python, o uso de classes permite a criação de estruturas que encapsulam dados e comportamentos
 relacionados, facilitando a modelagem de entidades do mundo real. Vamos explorar o
 desenvolvimento e a funcionalidade de uma classe 'Carro' em python.

 Definição da Classe 'Carro'
 
 A classe 'Carro é uma representação de um veículo automotivo, contendo atributos que descrevem
 suas características e métodos que definem seus comportamentos.

 Construtor '__init__'
 O método '__init__' é um construtor especial que é chamado automaticamente quando um novo 
 objeto da classe é criando. Ele inicializa os atributos do objeto com valores fornecidos como
 argumentos:
 
 
 • 'marca': A marca do carro (Toyota, Ford).
 
 • 'modelo': O modelo do carro (Corolla, Mustang).
 
 • 'cor': A cor do carro (Preto, Vermelho).
 
 • 'combustível': O tipo de combustível que o carro usa (Gasolina, Diesel).

 Além disso, dois atributos adicionais são definidos:

 • 'ligado':  Indica que o carro está ligado (inicialmente 'False')
 
 • 'velocidade': A velocidade atual do carro (inicialmente '0' km/h)
 
##

 Métodos da Classe 'Carro'
 
 Método 'ligar'

 Este método liga o carro, alterando o estado de 'ligado' para 'True' e imprimindo uma mensagem apropriada.
 Se o carro já estiver ligado, uma mensagem indicativa é exibida.


 Método 'acelerar'

 Este método aumenta a velocidade do carro em 1km/h cada vez que é chamado, desde que o carro
 esteja ligado. Caso contrário, uma mensagem indicativa é exibida.

 Método 'frear'

 Este método diminui a velocidade do carro em 1km/h cada vez que é chamado, desde que o carro 
 esteja ligado. Caso contrário, uma mensagem indicativa é exibida.

 ##

 Utilizando a Classe 'carro'

 Para utilizar a classe 'carro', instanciamos objetos e chamamos seus métodos.

 Conclusão

 A classe 'carro' exemplifica como a POO pode ser utilizada em python para modelar objetos do 
 mundo real com atributos e métodos que definem seu estado e comportamento. Através desta
 estrutura, conseguimos criar e manipular instâncias de carros, simulando ações como ligar, desligar, 
 acelerar e frear, com base no estado atual do objeto. Esta abordagem promove um código mais
 organizado, reutilizável e fácil de entender.
 
