#Question 1
# class smartphone:
#     make = 'iphone'

#     def call(self):
#         print('calling...')

# my_phone = smartphone()
# print(my_phone.make)
# my_phone.call()

#Question 2
class person:
    def __init__(self, height, gender):
        self.height = height
        self.gender = gender
child = person('6 ft', 'male')
adult = person('5 ft', 'female')
print(child.height)
print(adult.gender)

class child(person):
    pass

child = child('little', 'girl')
print(child.height)
print(child.gender)


#Activity 2
class sad:
    def reaction(self):
        return 'cry'

class happy:
    def reaction(self):
        return 'smile'
    
class angry:
    def reaction(self):
        return 'yell'

for action in [sad(), happy(), angry()]:
    print(action.reaction())