"""
- show dbs; - Mostra o Banco de Dados
- use cruddb; 
- show collections; - Mostra a coleção
- db.createCollection('users') - Cria uma coleção User
- show collections; - Mostra a coleção
- db.users.insertOne({name: "Fulano", email:"fulano@email.com", phone:"3243432"}) - Adicionou um User(Registro)
- db.users.insertOne({name: "Test", email:"test@email.com", phone:"67687634"})
- db.users.find({}) - Lista os dados
- db.users.find({name:"Test"}) - Filtrar por um nome
- db.users.update({name: "Test"}, {$set: {name: "Rodrigo"}}) - Atualiza um usuário
- db.users.deleteOne({name:"Fulano"}) - Deleta um usuário
"""