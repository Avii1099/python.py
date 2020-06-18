#Accessing Value
"Getting the value associated with a key"
dist = {'One': 1, 'Two': 2}
print(dist['One'])
print(dist['Two'])


#Adding new key- value pairs
dist = {'One': 1, 'Two': 2}
print(dist['One'])
print(dist['Two'])
"Adding a key-value pair"
dist['Three'] = 3
dist['Four'] = 4

#Looping through all key-value pairs
fav_lan = {'Arvind': "python", 'Jyoti': 'C & c++'}
for name, language in fav_lan.items():
    print(name+": "+ language)
#Looping through all the keys
for name in fav_lan.keys():
    print(name)
#Looping through all the value
for language in fav_lan.values():
    print(language)


#Storing dictionaries in a list
user = []
new_user = {'Name': 'Arvind',
            'Middle': 'R',
            'Last': 'Singh'}
user.append(new_user)
for user_dict in user:
    for k, v in user_dict.items():
        print(k+' : '+v)
#Define a list of dictionaries directly, without using append():
user = [
    {
            'Name': 'Arvind',
            'Middle': 'R',
            'Last': 'Singh'
    }
]
for user_dict in user:
    for k, v in user_dict.items():
        print(k+' : '+v)

#Storing lists in a dictionary
fav_lan = {
    'Arvind': ['Python', 'java'],
    'Mitul': ['C', 'C++'],
    'Vruti': ['C#', 'J#']
}
for name, language in fav_lan.items():
    print(name+":", end="")
    for lang in language:
        print(""+lang)

