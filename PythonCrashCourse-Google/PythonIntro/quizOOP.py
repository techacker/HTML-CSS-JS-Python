# Question 1 (in video)
class Flower:
    color = 'unknown'

rose = Flower()
rose.color = "red"

violet = Flower()
violet.color = "violet"

this_pun_is_for_you = "Sugar is sweet and so are you!"

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you) 

# Question 2:

# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
    x = 0
    x = you.apples
    you.apples = me.apples
    me.apples = x
    return you.apples, me.apples
    
def exchange_ideas(you, me):
    x = 0
    x = you.ideas
    you.ideas += me.ideas
    me.ideas += x
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))



# Question 3

# define a basic city class
class City:
    name = ""
    country = ""
    elevation = 0 
    population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
    return_city = City()

    if min_population < city1.population:
        return_city = city1

    if min_population < city2.population and min_population > city1.population:
        return_city = city2

    if min_population < city3.population and min_population > city1.population and min_population > city2.population:
        return_city = city3

    if return_city.name:
        return return_city.name + ", " + return_city.country
    else:
        return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""


# Question 5
class Furniture:
    color = ""
    material = ""

table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table)) 
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch)) 
# Should be "This piece of furniture is made of red leather"