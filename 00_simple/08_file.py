# coding=utf-8

# indent your Python code to put into an email
import glob
# glob supports Unix style pathname extensions
python_files = glob.glob('*.py')
for file_name in sorted(python_files):
    print('    ------' + file_name)

    with open(file_name, 'r', encoding='UTF-8') as f:
        for line in f:
            print('    ' + line.rstrip())

    print()
