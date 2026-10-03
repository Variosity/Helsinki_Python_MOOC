

while True:
    which_editor = input('Editor: ')
    if which_editor.lower() == 'visual studio code':
        print('an excellent choice!')
        break
    elif which_editor.lower() == 'word' or which_editor.lower() == 'notepad':
        print('awful')
        continue
    else:
        print('not good')
        continue