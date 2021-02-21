import os

path = '.'
fs = os.listdir(path)
fs.sort()

folders = []

for i in fs:
    if os.path.isdir(i):
        if i[0] != '.':
            folders.append(i)

target_file = './_sidebar.md'

file = open(target_file, 'w')
for i in folders:
    file.write('* '+i+'\n')
    for j in os.listdir('./'+i):
        if os.path.splitext(j)[-1] == ".md":
            file.write('\n\t'+'* '+'['+j[:-3]+']'+'('+i+'/'+j+')'+'\n')
file.close()
