points = 19
total = 22
# res = round((points/total)*100, 2) # замінили на .2% форматування в прикладі нижче
print('Correct answers: {:.2%}'.format(points/total))

print(f'Correct answers: {points/total:.2%}')