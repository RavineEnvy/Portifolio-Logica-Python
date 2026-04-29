from funcoes.identificacao_de_funcao import *

minhaLista = []
print("\nPreenchido")
preencherInventario(minhaLista)
print("\nExibindo")
exibirInventario(minhaLista)

print("\nPesquisando")
localizarListaPorNome(minhaLista)
print("\nAlterando")
depreciacarPorNome(minhaLista, 20)

print("\nExcluindo")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("\nResumindo")
resumirValoresLista(minhaLista)