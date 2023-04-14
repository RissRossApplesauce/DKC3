# duplicates the template for each input file
# gets all files in a directory that end in 'In.txt' and creates a copy of template.py for each one
# each copy of template.py is renamed to match the In.txt file's name
# any place NAME shows up in the template is also replaced with the input file's name
import glob
a = open('template.py', 'r').read()
for b in glob.glob('./Short Programming/*In.txt'):
    open(b[:-6].split('\\')[-1] + '.py', 'a').write(a.replace('NAME', b[:-6]))

"""
Equivalent to this:
import glob
template_text = open('template.py', 'r').read()
# grab all of the input file names in the Short Programming directory. keep in mind they change the folder structure sometimes
for filename in glob.glob('./Short Programming/*In.txt'):
    # clean up the name of the file
    filename_without_intxt = b[:-6]
    filename_without_path = filename_without_intxt.split('\\')[-1]
    
    # create a new template file with a matching name
    new_template_name = filename_without_path + '.py'
    new_template = open(new_template_name, 'a') # note that this is append mode, this is because we accidentally ran this file and erased our already-existing code a few times
    
    # replace string 'NAME' with the input file's name and write to the file
    template_text_with_name = template_text.replace('NAME', filename_without_intxt)
    new_template.write(template_text_with_name)
"""