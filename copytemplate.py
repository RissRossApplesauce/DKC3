import glob
a = open('template.py', 'r').read()
# for b in glob.glob('./Short Programming/*In.txt'):
for b in glob.glob('./2017/*In.txt'):
    open(b[:-6].split('\\')[-1] + '.py', 'a').write(a.replace('NAME', b[:-6]))
