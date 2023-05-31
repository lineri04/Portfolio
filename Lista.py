print('short list demo.')

my_list = [1,2,3,-3,3.14,'pipppi','yank',4,2,8]
print(f'Listan = {my_list}')
print(f'Längd av listan {len(my_list)}') #length of list
print(f'Antal 2:or = {my_list.count(2)}') #Count number of '2'

#list.pop(undex) removes elem at index
elem = my_list.pop() #Remove last elem
print(f'{elem} har tagigts bort. Listan = {my_list}')

elem = my_list.pop(0) #Remove first elem
print(f'{elem} har tagigts bort. Listan = {my_list}')

elem = my_list.pop(3) #Remove fourth elem
print(f'{elem} har tagigts bort. Listan = {my_list}')

my_list.append('17') #Add 17 at end
print(f'Listan 0 {my_list}')

my_list.append (['a','b','c'])
print('?')

my_list.extend([1,2,3,4])
print(f'Listan, extend = {my_list}')

#Modift the list at index
my_list[1] = 'what?'
print(f'Listan = {my_list}')
