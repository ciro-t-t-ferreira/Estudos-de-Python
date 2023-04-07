#Biblioteca Regex:
import re

"""
Sintaxe Regex:
[]: indica um caractere que pode pertencer a um dado intervalo. Ex [0-9] pode ser qualquer número,
    [abc] acha as letras a, b ou c.
*: Maraca nenhuma, uma, ou mais ocorrências. Ex: sol* [a real que não entendi esse]
{}: indica quantidade de repetições de uma ocorrência. Ex: [0-9]{5} irá detectar 5 número seguidos.
\d: dígito número de 0 a 9 (equivale a [0-9])
\w: qualquer número, letra, ou _
|: um ou outro caractere. Ex: @|%
(): agrupa pedaços do padrão
?: faz com que o elemento apresentado antes dele seja opcional (se usado após () faz com que todo esse bloco seja opcional)
"""

padrao = "[1-9][a-z][1-9]"
texto = "123 1a4 aaz 11e"


"""
Para detectar um certo padrão dentro de um texto deve-se criar uma string com a sintaxe do regex que
descreve o padrão. Aí podemos usar duas funções:
search: encontra primeira ocorrência
findall: encontra todas ocorrências
"""

resposta_search = re.search(padrao, texto)
resposta_all = re.findall(padrao, texto)

"""
Duas formas de visualizar a resposta: posso só printar a search (mostra um resultado mais complexo) ou
usar a função 'group' pra ver apenas o padrão
"""

print(resposta_search)
print(resposta_search.group())#Se foram utilizados ()s no padrão pode-se colocar um argumento numérico no group pra selecionar apenas um dos padrões
print(resposta_all)


