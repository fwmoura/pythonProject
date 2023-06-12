from datetime import date
atual = date.today().year
nasc = int(input('Digite o seu ano de nascimento:' ))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
if idade == 18:
    print('voce deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    print('voce ainda nao tem idade para se alistar')
elif idade > 18:
    print('voce passou da idade de se alistar')



