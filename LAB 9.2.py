'''
LAB 9.2 Adressbok
'''
import os

def show_content():
    with open('Addresbok', mode='r')as f:
        for line in f:
            print(line,end='')

def add_namn():
    nummer = input('Nummer (q=quit):')
    namn = input('Note (q=quit):')
    with open('Addresbok',mode='a') as f1:
        s = f'{namn}: {nummer}\n'
        f1.write(s)

    return

def remove_name():
    src = 'temp.text.txt'
    dest = 'Addresbok'
    with open(dest) as f1, open(src,mode='w') as f2:
        for nr,line in enumerate(f1):
            ans = input(f'Ta bort [{line[:-1]}] (j/n) ')
            
            if ans.lower() == 'j':
                f2.write(line)

    if os.path.exists(dest+'.old'):
        os.remove(dest+'.old')
        
    os.rename(dest,dest+'.old')
    os.rename(src, dest)
    print ("Ett namn har tagits bort.")

ans = 'nonsens'
while ans != '':     
    ans = input('vad vill du göra\n \t1. Lägga till namn\n\t2. Lista alla namn\n\t3. Ta bort ett namn\n\t4. Välj mellan 1,2 eller 3:  ')
    if ans == '1':
       add_namn()
    elif ans == '2':
        show_content()
    elif ans == '3':
       remove_name()
    elif ans == '':
        pass
    else:
        print('Ogiltigt val')


