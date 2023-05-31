
'''
LAB 9.1 Adressbok
'''

def add_entry(f_fil, namn, nummer):

    with open(f_fil,mode='a') as f1:
        s = f'\n{namn}: {nummer}'
        f1.write(s)

    return


title = input('Namn på filen:')
title += '.txt'
with open(title, mode = 'w') as f1:
    
    s = f'fil: {title}\n'
    f1.write(s)

entry = input('Nummer (q=quit):')
while entry != 'q':
    name = input('Note (q=quit):')
    add_entry(title,entry,name)
    entry = input('Nummer (q=quit):')
