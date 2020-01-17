import json 

#load file 
with open('Yemen_2010.json', encoding='utf-16') as file:
    conflicts = json.load(file)

with open('Yemen_2010.csv', 'w') as file:
    file.writelines('id,type_of_violence,deaths\n')
    for conflict in conflicts:
        file.writelines(f'{conflict["id"]}, {conflict["type_of_violence"]}, {conflict["best"]}\n')


print(conflict)
