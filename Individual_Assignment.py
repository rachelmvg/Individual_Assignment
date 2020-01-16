import json 

#load file 
with open('Yemen_2011.json', encoding='utf-16') as file:
    conflicts = json.load(file)

with open('Yemen_2011.csv', 'w', encoding = 'utf-16') as file:
    file.writelines('source and event,type of violence,amount of deaths (best)\n')
    for conflict in conflicts:
        file.writelines(f'{conflict["source_article"]}, {conflict["type_of_violence"]}, {conflict["best"]}\n')


#{conflicts['deaths_]}, {conflicts['deaths_b']}, {conflicts['deaths_civilians']}, {conflicts['deaths_unknown']},

print(conflict)
