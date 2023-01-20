'''6. O DBA da empresa criou um script para fazer uma atualização no banco de dados
MongoDB:

var sku = "" // a pessoa informa o sku aqui
var estoque = 0 // valor a ser informado do novo estoque

db.produto.update(
    {
        sku: sku
    },
    {
        $inc: estoque
    }
)

O problema que esse script está em JavaScript do MongoDB. Logo, escreva para
nós a função Python ajustar_estoque() com o seus devidos parâmetros para que
realize a atualização na coleção produto conforme o script que o DBA passou para nós.

Tempo estimado: 10 minutos. Dificuldade: média. A pessoa sabe ler o script do
MongoDB? Consegue ver e traduzir o que precisamos para o Python?'''

from pymongo import MongoClient

url_conexao = 'mongodb+srv://dellamaf:33762636@cluster0.m52rote.mongodb.net'
client = MongoClient(url_conexao)

collection = client.magalu.produtos

def ajustar_estoque(sku, estoque, collection):
    collection.update_one({"sku": sku}, {"$set": {"estoque": estoque}})


if __name__ == '__main__':
    sku = input('Digite o sku do produto: ')
    estoque = int(input('Digite a nova quantidade no estoque: '))

    ajustar_estoque(sku, estoque, collection)