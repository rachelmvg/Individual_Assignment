import json 

#load file 
with open('Yemen_2011.json', encoding='utf-16') as file:
    conflicts = json.load(file)

with open('Yemen_2011.csv', 'w') as file:
    file.writelines('id,type_of_violence,deaths\n')
    for conflict in conflicts:
        file.writelines(f'{conflict["id"]}, {conflict["type_of_violence"]}, {conflict["best"]}\n')


#{conflicts['deaths_]}, {conflicts['deaths_b']}, {conflicts['deaths_civilians']}, {conflicts['deaths_unknown']},

print(conflict)
