l1 = int(input('Digite o primeiro lado: '))
l2 = int(input('Digite o segundo lado: '))
l3 = int(input('Digite o terceiro lado: '))

if(l1>0) and (l2>0) and (l3>0):
 if(l1 +l2 > l3) and (l2 + l3 > l1) and (l3 + l1 > l2):

     if(l1 == l2 == l3):
      print('É um triangulo equilatero, pois todos os lados são iguais');

     else:
      if(l1 == l2) or (l1 == l3) or (l2 == l3):
          print('Isosceles,pois tem dois lados iguais');

      else:
          if(l1 != l2 != l3):
              print('É um triangulo escaleno, pois tem os lados diferentes');
 else:
     print('O valor de dois lados nao pode ser menor que um');

else:
    print('Os valores de um lado do triangulo nao podem ser zero');