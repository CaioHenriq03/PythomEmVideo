aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media']:
    aluno['situacao'] = 'Recuperacao'
else:
    aluno["situacao"] = "Reprovado"

for k, v in aluno.items():
    print(f'{k} é igual a {v}')