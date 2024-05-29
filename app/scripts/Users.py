import json



class User:
    def __init__(self, name, email, password):
        self.name, self.email, self.password = name, email, password
    


def get():
    with open('app/data/users.json', 'r', encoding='utf-8') as file:
        jString = file.read()
        jDict = json.loads(jString)
    users = []
    for name in jDict:
        data = jDict[name]
        email, password = data['email'], data['password']
        newUser = User(name, email, password)
        users.append(newUser)
    return users

print(get())