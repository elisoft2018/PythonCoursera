import csv

a_list = ['Pedro', 'Florencia', 'Matias', 'Jorge', 'Maria', 'Ines']
with open('archivo.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(a_list)

reader = csv.reader(['Hola|,Mundo', 'Python'], escapechar='|')
file_content = list(reader)

print(file_content)

