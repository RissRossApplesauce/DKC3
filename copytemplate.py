import glob
with open('template.py') as a:
    # for b in glob.glob('.\Short Programming\*In.txt'):
    for b in glob.glob('.\WordSearch\*In.txt'):
        with open(b[:-6].split('\\')[-1] + '.py', 'w') as d:
            d.write(a.read().replace('NAME', b[:-6]))
