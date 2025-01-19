import json

# 1 - Strings para Dicionário 
person = '{"name": "Rodrigo", "languages": ["Python", "Javascript"]}'  # Corrigido para 'languages'
person_dict = json.loads(person)
print(person_dict)
print(person_dict['languages'])

# 2 - Convertendo dicionário para json
person_json = json.dumps(person_dict)
print(person_json)

# 3 - Formatando json
print(json.dumps(person_dict, indent=4, sort_keys=True))

# 4 - Salvando json em txt
with open('person.txt', 'w') as json_file:
    json.dump(person_dict, json_file)

# 5 - Lendo json externo
with open('iris.json', 'r') as f:
    data = json.load(f)
print(data)
