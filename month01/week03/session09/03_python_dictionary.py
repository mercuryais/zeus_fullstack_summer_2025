# Python dictionary Also called object

# Problem
favorite_sports = ['Ralph Williams, Football'
                ,'Micheal Tippet, Basketball'
                ,'Edward Elgar, Baseball']
ralph_sport = favorite_sports[0]
print(ralph_sport[16:])

# Solution - Dictionary

favorite_sports = {
    'Ralph Williams': 'Frooball',
    'Micheal Tippet': 'Basketball',
    'Edward Elgar': 'Baseball'
}
print(favorite_sports)

# Key              |    Value
# ------------------------------
# Ralph Williams   |    Football
print(favorite_sports['Edward Elgar'])

# Add item to the dictionary 
favorite_sports['Rebecca Clarke'] = 'Netball'
print(favorite_sports)

favorite_sports['Ethel Smyth'] = 'Badmington'
favorite_sports['Frank Bridge'] = 'Rugby'
print(favorite_sports)

# Change item of the dictionary
favorite_sports['Ralph Williams'] = 'Ice Hockey'

# Delete item from the dictionary
del favorite_sports['Rebecca Clarke']
print(favorite_sports)

# Lenght of the dictionary
print(len(favorite_sports))

# Dictionary cannot use +

# X 0.1
favorite_food = {'Belen goimon' : 'Goimon, us, nogoo, haluun nogoo',
                 'salad' : 'toms, mayo, ham, ondog, songino',
                 'buuz' : 'mah, guril, songino'
                 }
print(favorite_food)

# X 0.2
realDic = {'Question' : 'Асуулт',
           "Response" : 'Хариулт'}

# X 0.3
favPet = {'Me' : 'Cat',
          'Sister' : 'Dog',
          'Cat' : 'Mice'}