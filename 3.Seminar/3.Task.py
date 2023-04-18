# Напишите программу для печати всех уникальных
# значений в словаре.


dictionary=[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}] 

tmp=[list(i.values())[0].strip() for i in dictionary]
print(set(tmp))