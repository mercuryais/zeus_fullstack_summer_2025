# Python lists 

wizard_list = 'splider legs, toe of frog, bat wing, slug butter, snake dandruff'
print(wizard_list)
print(wizard_list[0:12])

#wizard list
wizard_list = ['splider legs', 'toe of frog', 'bat wing', 'slug butter',
                'snake dandruff']
print(wizard_list)
print(wizard_list[0])
#exercise print all other wizard things
print(wizard_list[1])
print(wizard_list[2])
print(wizard_list[3])
print(wizard_list[4])

# list 
print(f'Length of the wizard list is {len(wizard_list)}')

# change values of the list 
wizard_list[2] = 'snail tongue'
print(wizard_list)

wizard_list[4] = 'snake poison'

print(wizard_list)
# select between indexes
print(wizard_list[2:5])

#negative index

print("FROM HERE !!!" * 5)
print(wizard_list[-1])
print(wizard_list[-3:])

some_numbers = [1,2,5,10,20]
some_strings = ['Which', 'Witch', 'Is', 'Which']

# mixed list
numbers_and_strings = ['Why', 'was', 6, 'afraid', 'of', 7, 'because', 7, 8, 9]
print(numbers_and_strings)

my_list = [some_numbers, some_strings]
print(my_list)

# Add items to the list
wizard_list.append('bear burp')
print(wizard_list)

wizard_list.append('mandrake')
wizard_list.append('hemlock')
wizard_list.append('swamp gas')
print(wizard_list) 

# Delete items form the list
del wizard_list[4]
del wizard_list[7]

# sorting
list1 = [10,4,5,-1,0,11]
print(list1.sort())
print(list1)


# Цэг, () хоерын ялгаа
# Яагаад ['Why', 'was', 6, 'afraid', 'of', 7, 'because', 7, 8, 9] гэж

fs = ("fsfs", "sdds", "dfdf", "gfdgddfg", "dgdfg") # is tuple () is usually recommended
fs = "fsfs" "sdds" "dfdf" "gfdgddfg" "dgdfg" # just like + in every space
print(fs)
vx = "fsfs sdds dfdf gsdgdfgdfg dfgdfg" # string
rw = ["sdfsdfsdfsdfsffsdfsf"] # just a list
re = ["sdfsdf" "sdfsdf" "sfsdfsdf" "sdfsf"] # just a single list 
re = ["sdfsdf", "sdfsdf", "sfsdfsdf", "sdfsf"]
