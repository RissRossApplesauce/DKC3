# duplicates the template for each input file
# gets all files in a directory that end in 'In.txt' and creates a copy of template.py for each one
# each copy of template.py is renamed to match the In.txt file's name
# any place NAME shows up in the template is also replaced with the input file's name
import glob
a = open('template.py', 'r').read()
for b in glob.glob('./Short Programming/*In.txt'):
    open(b[:-6].split('\\')[-1] + '.py', 'a').write(a.replace('NAME', b[:-6]))
