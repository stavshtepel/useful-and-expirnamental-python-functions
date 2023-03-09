import base64
import calendar
import functools
import itertools
import string
from collections import Counter, defaultdict
calendar.setfirstweekday(calendar.SUNDAY)
from distutils.util import convert_path


# F to C converter

temp = input("Insert the temptature you would like to convert: ")
fixedTemp=float(temp[0:-1])
if ("F" or "f") in temp:
	convertedTemp=((fixedTemp - 32) * 5/9)
	print(convertedTemp, "C")
elif ("C" or "c") in temp:
	convertedTemp=(9 * fixedTemp + (32 * 5))/5
	print(convertedTemp, "F")


# the day of the week

chosenDate = input("Enter a date: ")
chosenDay = int(chosenDate[0:2])
chosenMonth = int(chosenDate[3:5])
chosenYear = int(chosenDate[6:10])
week_of_the_day=(calendar.weekday(chosenYear, chosenMonth, chosenDay))
if week_of_the_day == 0:
	print("Monday")
elif week_of_the_day == 1:
	print("Tuesday")
elif week_of_the_day == 2:
	print("Wednesday")
elif week_of_the_day == 3:
	print("Thursday")
elif week_of_the_day == 4:
	print("Friday")
elif week_of_the_day == 5:
	print("Saturday")
elif week_of_the_day == 6:
	print("Sunday")

# functions
def func(random_number):
	number=random_number+1
	return number

func(1)

# last early function
def last_early(my_str):
	is_last_early=False
	if my_str[-1].lower() in my_str[0:-1].lower():
		is_last_early = True
	print(is_last_early)
last_early("okay")

# distance function
def distance(num1, num2, num3):
	if ((abs(num1) - abs(num2) == 1) and (abs(num1 - abs(num3) != 1))) or ((abs(num3) - abs(num1) == 1) and abs(num2) - abs(num1) != 1 ):
		is_close = True
	elif (abs(num1) - abs(num3) >=2) or (abs(num3) - abs(num1) >= 2):
		is_close = True
	else:
		is_close = False
	print(is_close)
distance(1, 2, 10)

# filter_teens function

def fix_age(age):
	if (age >= 13) and (age <= 19) and (age != 15) and (age != 16):
		age = 0
	return age

def filter_teens(a=13, b=13, c=13):
	sum = fix_age(a) + fix_age(b) + fix_age(c)
	print(sum)

# filter_teens(1, 2, 13)

# chocolate maker function
def chocolate_maker(small, big, x):
	small_cube = 1
	big_cube = 5
	if small * small_cube + big * big_cube >= x:
		is_valid = True
	else:
		is_valid = False
	print(is_valid)	

chocolate_maker(1, 2, 10)

# calculation function
def func(num1, num2):
	"""
	This function calculates the sun of the numbers given to it.
	:parameter: int
	:return: sum of two numbers
	:rtype: int
	"""
	num3 = num1 + num2
	return num3

def main():
	func(1, 2)
if __name__ == "__main__":
		main()

# shift left function
def shift_left(my_list):
	new_list = ["hello", "hey", 1]
	new_list[0] = my_list[1]
	new_list[1] = my_list[2]
	new_list[2] = my_list[0]
	print(new_list)

shift_left([1, 2, 3])

# format list function
def format_list(my_list):
	if len(my_list) % 2 != 0:
		is_valid = False
		print(is_valid)
	else:
		is_valid = True
		print(", ".join(my_list[::2]) + ", and", my_list[-1])
format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"])

# extend list function
def extend_list_x(list_x, list_y):
	list_x[:0] = list_y
	print(list_x)

extend_list_x([1, 2, 3, 4], [1, 2, 3, 4, 5, 6])

# are_lists_equal function
def are_lists_equal(list1, list2):
	if sorted(list1) == sorted(list2):
		are_lists_equal = True
		print(are_lists_equal)
	else:
		are_lists_equal = False
		print(are_lists_equal)

are_lists_equal([1, 2, 3, 4], [4, 3, 2, 2])

# longest function
def longest(my_list):
	my_list_2 = sorted(my_list, key=len)
	print(my_list_2[-1])

longest(["hello", "to", "you"])

# squared numbers function
def squared_numbers(start, stop):
    num_list = []
    i = start
    while i <= stop:
        num_list += [i * i]
        i += 1
    print(num_list)
squared_numbers(-3, 3)

# is_greater function
def is_greater(my_list, n):
    big_nums = []
    for item in my_list:
        if item > n:
            big_nums += [item]
    return big_nums
print(is_greater([1, 2, 3, 4, 5, 6], 4))

# numbers_letters_count function
def numbers_letters_count(my_str):
    nums_list = []
    my_list = []
    for letter in my_str:
        if letter.isdigit():
            nums_list += [letter]
    my_list += [len(nums_list)]
    my_list += [len(my_str) - len(nums_list)]
    return my_list
print(numbers_letters_count("hello123"))

# seven boom function
def seven_boom(end_number):
    my_list = []
    for num in range(0, end_number+1):
        if (num % 7 == 0) or ('7' in str(num)):
           num = "BOOM"
        my_list += [num]
    return my_list

print(seven_boom(22))

# sequence_del function
def sequence_del(my_str):
    new_str=""
    for letter in my_str:
        if letter not in new_str:
            new_str += letter
    return new_str
print(sequence_del("HHHHEEEEEYYYYYY"))

shopping list program
shopping_list_str = input("Enter here the product you want to have in your shopping list: ")
chosen_number = None
def shopping_list(shopping_list_str):
    chosen_number = int(input("Enter here a number in the following range: 1-9: "))
    shopping_list = shopping_list_str.split(",")
    if chosen_number == 1:
        print(shopping_list)
    elif chosen_number == 2:
        print(len(shopping_list))
        chosen_number = input("Enter here a number in the following range: 1-9: ")
    elif chosen_number == 3:
        chosen_product = input("Enter here a product: ")
        if chosen_product in shopping_list:
            is_in_list = True
            print("Your product is allready in the shopping list")
        else:
            is_in_list = False
            print("Your product is not in the shopping list")
    elif chosen_number == 4:
        chosen_product_2 = input("Enter here a product: ")
        num_of_occurences = shopping_list.count(chosen_product_2)
        print("the number of times this product appears in the list, is:", num_of_occurences)
    elif chosen_number == 5:
        chosen_product_3 = input("Enter here the product that you want to remove from the shopping list: ")
        shopping_list -= [chosen_product_3]
    elif chosen_number == 6:
        chosen_product_4 = input("Enter here the product that you want to add to the shopping list: ")
        shopping_list += [chosen_product_4]
    elif chosen_number == 7:
        for item in shopping_list:
            if (len(item) < 3) or (not item.isalpha()):
                print(item)
    elif chosen_number == 8:
        new_shopping_list = []
        for item in shopping_list:
            if shopping_list.count(item) > 1:
                shopping_list.remove(item)
    elif chosen_number == 9:
        quit()
while chosen_number != 9:
    shopping_list(shopping_list_str)

# arrow function
def arrow(my_char, max_length):
    number = max_length - 1
    for num in range(1, max_length + 1):
        print(my_char * num)
    while number >= 1:
        print(my_char * number)
        number -= 1
arrow(',', 6)

8.2.1
data = ("self", "py", 1.543)
format_string = "Hello"

print(format_string + "Hello %s.%s learner, you have only %.1f units left before you master the course!" % data)

# get_price function
def get_price(my_tuple):
    return my_tuple[1]

# sort_prices function
def sort_prices(list_of_tuples):
    """
    The function gets list of tuples that in each one of them there is the product name and its price, and returns a list of them sorted.
    :parameter name: list_of_tuples
    :type: list
    :return: The function returns list of the sorted tuples
    :rtype: list
    """
    sorted_list_of_tuples = sorted(list_of_tuples, key=get_price)
    print(sorted_list_of_tuples)
sort_prices([("item1", 74), ("item2", 68)])

# mult_tuple function
def mult_tuple(tuple1, tuple2):
    pairs_tuple = ()
    pairs_tuple_2 = ()
    pairs_list = []
    for item in tuple1:
        pairs_tuple += (item, tuple2[0])
        pairs_tuple += (item, tuple2[1])
    for item in tuple2:
        pairs_tuple += (item, tuple1[0])
        pairs_tuple += (item, tuple1[1])
    for i in range(0, len(pairs_tuple), 2):
        pairs_list.append((pairs_tuple[i], pairs_tuple[i+1]))
    pairs_tuple_2 = tuple(pairs_list)
    print(pairs_tuple_2)
mult_tuple((1, 2), (3, 4))

# sort_anagrams function
def sort_anagrams(list_of_strings):
      result = {}
      for i in list_of_strings:
         x = "".join(sorted(i))
         if x in result:
            result[x].append(i)
         else:
            result[x] = [i]
      return list(result.values())

print(sort_anagrams(["hello", "hey" ,"olleh"]))

# some dictionary
def personal_details_func():
    personal_details = {"first_name": "Mariah", "last_name": "Carey", "birth_date": "27.03.1970", "hobbies": ["Sing", "Compose", "Act"]}
    chosen_digit = int(input("Enter a digit from 1-9: "))
    if chosen_digit == 1:
        print(personal_details["last_name"])
    elif chosen_digit == 2:
        print(personal_details["birth_date"][4:6])
    elif chosen_digit == 3:
        print(len(personal_details["hobbies"]))
    elif chosen_digit == 4:
        print(personal_details["hobbies"][-1])
    elif chosen_digit == 5:
        personal_details["hobbies"].append("Cooking")
    elif chosen_digit == 6:
        event_tuple = tuple(personal_details["birth_date"].split("."))
        print(event_tuple)
    elif chosen_digit == 7:
        event_tuple = tuple(personal_details["birth_date"].split("."))
        personal_details["age"] = 2022 - int(event_tuple[2])
        print(personal_details["age"])
personal_details_func()

# count_chairs function
def count_chairs(my_str):
    letters_dict = {}
    for letter in my_str:
        letters_dict[letter] = my_str.count(letter)
    return letters_dict
print(count_chairs("hello"))

inverse_dict function
def inverse_dict(my_dict):
    new_dict = defaultdict(list)
    for key, value in my_dict.items():
        new_dict[value].append(key)
    return dict(new_dict)
print(inverse_dict({"hello": 3, "hey": 2, "banana": 3}))

# are_files_equal function
def are_files_equal(file1, file2):
    with open(file1) as f:
        str1 = f.readlines()
    with open(file2) as f:
        str2 = f.readlines()
    if str1 == str2:
        is_equal = True
        print(is_equal)
    else:
        is_equal = False
        print(is_equal)
are_files_equal("hello.txt", "hi.txt")

def actions():
    some_file = input("Enter here the path to some file: ")
    some_action = input("Enter here the action that you want to do: ")
    words_list = []
    some_list = []
    with open(some_file) as f:
        words_list = f.readlines()
        if some_action == "sort":
            for line in words_list:
                some_list += sorted(line.split())
            print(some_list)
        if some_action == "rev":
            for line in words_list:
                some_list += line.split()[::-1]
            print(some_list)
        if some_action == "last":
            lines_list = []
            n = int(input("Enter here some number: "))
            for line in words_list:
                lines_list += [line[0:-1]]
            for item in lines_list:
                if lines_list.index(item) + 1 >= n:
                    print(item)
actions()

# copy_file_content function
def copy_file_content(source, destination):
    with open(source, "r") as f:
        some_file_content = f.read()
    with open(destination, "w") as f:
        f.write(some_file_content)
copy_file_content("hello.txt", "hi.txt")

who_is_missing function
def who_is_missing(file_name):
    with open(file_name, "r") as f:
        nums = f.readline()[0:-1]
        nums_list = nums.split(",")
        new_nums_list = ([int(x) for x in nums_list])
        highest_num_in_list = sorted(new_nums_list)[-1]
        correct_nums_list = range(1, highest_num_in_list + 1)
        for item in correct_nums_list:
            if item not in new_nums_list:
                print(item)
who_is_missing("hello.txt")

# my_mp3_playlist function
def my_mp3_playlist(file_path):
    with open(file_path, "r") as f:
        some_new_songs_2 = []
        some_songs_tuple = ()
        some_songs = f.readlines()
        some_new_songs = [item[:-2] for item in some_songs]
        for item in some_new_songs:
            some_new_songs_2 += [item.split(";")]
        songs_lengths = []
        for item in some_new_songs_2:
            songs_lengths += [int(item[2].split(":")[0]) * 60 + int(item[2].split(":")[1])]
            biggest_song_length = sorted(songs_lengths)[-1]
            biggest_song_length_index = songs_lengths.index(biggest_song_length)
        some_songs_tuple += (some_new_songs_2[biggest_song_length_index][0],)
        items_count = int()
        for item in some_new_songs_2:
            items_count += 1
        some_songs_tuple += (items_count,)
        items_occurences_list = []
        songs_authors_list = []
        for item in some_new_songs_2:
            songs_authors_list += [item[1]]
        for item in songs_authors_list:
            items_occurences_list += [songs_authors_list.count(item)]
        song_with_most_occurences = sorted(items_occurences_list)[-1]
        index_of_song_with_most_occurences = items_occurences_list.index(song_with_most_occurences)
        some_songs_tuple += (some_new_songs_2[index_of_song_with_most_occurences][1],)
        print(some_songs_tuple)
my_mp3_playlist("hello.txt")

# my_mp4_playlist function
def my_mp4_playlist(file_path, new_song):
    with open(file_path) as f:
        lines = f.readlines()
        splitted_lines = lines[2].split(";")
        splitted_lines[0] = new_song
        lines[2] = ";".join(splitted_lines)
        lines = [item[:-2] for item in lines]    
        for item in lines:
            print(item)
my_mp4_playlist("hello.txt", "some song")

my_list = [1, 2]
def my_func(some_list):
    result = a * b
    return result
x = map(my_func, my_list[0], my_list[1])
print(list(x))

import functools

def multiply(a, b):
    return a * b

print(functools.reduce(multiply, [1, 2, 3, 4]))

# double_letter function
def some_letter(letter):
  # return letter * 2
def double_letter(my_str):
  # return "".join(list(map(some_letter, my_str)))

print(double_letter("hello"))

# four_dividers function
def devide_in_four(num):
    return num % 4 == 0

def four_deviders(number):
    return list(filter(devide_in_four, range(1, number)))

print(four_deviders(10))

# sum_of_digits function
import functools

def add(a, b):
    return int(a) + int(b)

def sum_of_digits(number):
    return functools.reduce(add, list(str(number)))

print(sum_of_digits(105))

# intersection function
def intersection(list_1, list_2):
    return [i for i in set(list_1) if i in set(list_2)]
print(intersection([1, 2, 3, 4, 4, 5], [4, 5, 6, 7]))

# is_prime function
def is_prime(number):
    return str([True if len([num for num in range(1, number+1) if number % num == 0]) == 2 else False for i in range(1)])[1:-1]
print(is_prime(23))

# is_funny function
def is_funny(string):
    for char in string:
        if char != 'h' and char != 'a':
            return False
        return True

is_funny = lambda string: str(set([True if set(string) == {"a", "h"} or set(string) == {"h", "a"} else False for char in string]))[1:-1]
print(is_funny("sdfokijsdfsdf"))

password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"

print("".join([string.ascii_lowercase[list(string.ascii_lowercase).index(some_letter)+2] for some_letter in password if some_letter in string.ascii_lowercase]))

# animal class
class Animal:
  # count_animals = 0
  # def __init__(self, _animal_name = "Dog"):
      # self._animal_name = _animal_name
      # self._animal_age = 0
      # Animal.count_animals += 1
  # def birthday(self):
      # self._animal_age += 1
  # def get_age(self):
      # return self._animal_age
  # def set_name(self, _new_animal_name):
      # self._animal_name = _new_animal_name
  # def get_name(self):
      # return self._animal_name

dog = Animal("Dog")
count_animals += 1
wolf = Animal("Wolf")
count_animals += 1
dog.birthday()
print(dog.get_age())
print(wolf.get_age())

tiger = Animal("Tiger")
chicken = Animal()
print(tiger.get_name())
print(chicken.get_name())
chicken.set_name("Chicken")
print(chicken.get_name())
print(Animal.count_animals)

class Pixel:
    def __init__(self, _x = 0, _y = 0, _red = 0, _green = 0, _blue = 0):
        self._x = _x
        self._y = _y
        self._red = _red
        self._green = _green
        self._blue = _blue

    def set_coords(self, x, y):
        x = _x
        y = _y

    def set_grayscale(self):
        avarage = (self._red + self._green + self._blue) // 3
        self._red = avarage
        self._green = avarage
        self._blue = avarage
    
    def print_pixel_info(self):
        if (str(self._red) == 0 and str(self._green) == 0 and str(self._blue) > 50):
            print("X: " + str(self._x) + ", Y: " + str(self._y) + ", Color: " + "(" + str(self._red) + ", " + str(self._green) + ", " + str(self._blue) + ")" + " Blue")
        elif (str(self._red) == 0 and str(self._blue) == 0 and str(self._green) > 50):
            print("X: " + str(self._x) + ", Y: " + str(self._y) + ", Color: " + "(" + str(self._red) + ", " + str(self._green) + ", " + str(self._blue) + ")" + " Green")
        elif (self._blue == 0 and self._green == 0 and self._red > 50):
            print("X: " + str(self._x) + ", Y: " + str(self._y) + ", Color: " + "(" + str(self._red) + ", " + str(self._green) + ", " + str(self._blue) + ")" + " Red")
        else:
            print("X: " + str(self._x) + ", Y: " + str(self._y) + ", Color: " + "(" + str(self._red) + ", " + str(self._green) + ", " + str(self._blue) + ")")

something = Pixel(5, 6, 250, 0, 0)
something.print_pixel_info()
something.set_grayscale()
something.print_pixel_info()

BigThing class
class BigThing():
    def __init__(self, _some_var):
        self._some_var = _some_var

    def size(self):
        if isinstance(self._some_var, int):
            return self._some_var
        elif isinstance(self._some_var, list) or isinstance(self._some_var, dict) or isinstance(self._some_var, str):
            return len(self._some_var)

class BigCat(BigThing):
    def __init__(self, _some_var, _weigth):
        BigThing.__init__(self, _some_var)
        self._weigth = _weigth

    def size(self):
        if self._weigth > 15 and self._weigth < 20:
            return "Fat"
        elif self._weigth > 20:
            return "Vary Fat"
        else:
            return "OK"

my_thing = BigThing("hello")
print(my_thing.size())

my_cat = BigCat("hello", 22)
print(my_cat.size())

class Animal():
    def __init__(self, _name, _hunger = 0, zoo_name = "some zoo name"):
        self._name = _name
        self._hunger = _hunger
        self.zoo_name = zoo_name

    def get_name(self):
        """
        returns the name of the animal
        :param base: base value
        :type base: str
        :return: the function returns the name of the animal
        :rtype: str
        """
        return self._name

    def is_hungry(self):
        """
        returns the hunger level of the animal
        :param base: base value
        :type base: int
        :return: the method returns the hunger level of the animal
        :rtype: int
        """
        if self._hunger > 0:
            return True
        else:
            return False

    def feed(self):
        """
        reduces the hunger level of the animal
        :param base: base value
        :type base: int
        """
        self._hunger -= 1

    def talk(self, value):
        """
        prints the phrase that every animal is saying
        :param base: base value
        :type base: str
        """
        print(value)

class Dog(Animal):
    def __init__(self, name, hunger = 0, value = "woof woof"):
        Animal.__init__(self, name, _hunger = 0)
        self.value = value

    def fetch_stick(self):
        """
        prints the special say of the dog
        :param base: base value
        :type base: str
        """
        print("There you go, sir!")
    
class Cat(Animal):
    def __init__(self, name, hunger = 0, value = "meow"):
        Animal.__init__(self, name, _hunger = 0)
        self.value = value

    def chase_laser(self):
        """
        prints the special say of the cat
        :param base: base value
        :type base: str
        """
        print("Meeeeeow")

class Skunk(Animal):
    def __init__(self, name, hunger = 0, value = "tssssss", _stink_count = 6):
        Animal.__init__(self, name, _hunger = 0)
        self.value = value
        self._stink_count = _stink_count

    def stink(self):
        """
        prints the special say of the skunk
        :param base: base value
        :type base: str
        """
        print("Dear lord!")

class Unicorn(Animal):
    def __init__(self, name, hunger = 0, value = "Good day, darling"):
        Animal.__init__(self, name, _hunger = 0)
        self.value = value

    def sing(self):
        """
        prints the special say of the unicorn
        :param base: base value
        :type base: str
        """
        print("some song")

class Dragon(Animal):
    def __init__(self, name, hunger = 0, value = "Raaaawr", _color = "Green"):
        Animal.__init__(self, name, _hunger = 0)
        self.value = value
        self._color = _color

    def breath_fire(self):
        """
        prints the special say of the dragon
        :param base: base value
        :type base: str
        """
        print("$@#$@#@$")

def main():

    my_dog = Dog("Brownie", 10)
    my_cat = Cat("Zelda", 3)
    my_skunk = Skunk("Stinky", 0)
    my_unicorn = Unicorn("Keith", 7)
    some_dragon = Dragon("Lizzy", 1450)

    my_second_dog = Dog("Doggo", 80)
    my_second_cat = Cat("Kitty", 80)
    my_second_skunk = Skunk("Stinky Jr.", 80)
    my_second_unicorn = Unicorn("Clair", 80)
    my_second_dragon = Dragon("McFly", 80)
    
    zoo_lst = [my_dog, my_cat, my_skunk, my_unicorn, some_dragon, my_second_dog, my_second_cat, my_second_skunk, my_second_unicorn, my_second_dragon]

    for animal in zoo_lst:
        print(str(type(animal))[17:-2] + " " + animal.get_name())
        while animal.is_hungry():
            animal.feed()
        animal.talk(animal.value)
        if (isinstance(animal, Dog)):
            animal.fetch_stick()
        if (isinstance(animal, Cat)):
            animal.chase_laser()
        if (isinstance(animal, Skunk)):
            animal.stink()
        if (isinstance(animal, Unicorn)):
            animal.sing()
        if (isinstance(animal, Dragon)):
            animal.breath_fire()
    
    print(my_dog.zoo_name)
    print(my_dog.talk()

if __name__ == "__main__":
    main()

def func1():
    y = range(5)
    x = iter(y)
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())

def func2():
    x = int(input("Enter here a number: "))
    y = 0
    print(x/y)

def func3(marks):
    assert True
    assert False

def func4():
    import ksdfsdijfsdijfsdef.something

def func5():
    my_dict = {1: "hello", 2: "something"}
    print(my_dict[3])

def func6():
    if 3 in range(5)
        print("hey")

def func7():
    if 3 in range(5):
    print("hey")

def func8():
    x = 100
    y = "100"
    print(x/y)

def read_file(file_name):
    try:
        print("__CONTENT_START__")
        fo = open(file_name, "r")
    except:
        print("__NO_SUCH_FILE__")
    else:
        print(fo.read())
        fo.close()
    finally:
        print("__CONTENT_END__")

read_file("hello.txt")

# send_invation function
def send_invation(name, age):
    class UnderAge(Exception):
        def __init__(self, arg):
            self._arg = arg
        def __str__(self):
            return("Your age is below 18 years old. your age is: %s years old .you will become 18 years old in " + str(18 - age) + " years from now.")
        def get_arg(self):
            return self._arg
    try:
        if int(age) < 18:
            raise UnderAge (age)
    except UnderAge as e:
        print("Your age should be 18 in order to get to the party")
    else:
        print("Your should send an invite to " + name)
send_invation("john", 15)

# check_input function
class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "the username %s you entered contains illegal characters" % self._arg
    def get_arg(self):
        return _arg

class UsernameTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "The username you entered is too short"
    def get_arg(self):
        return _arg

class UsernameTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "The username you entered is too long"
    def get_arg(self):
        return _arg

class PasswordMissingCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "The password you entered is missing some characters"
    def get_arg(self):
        return _arg

class Uppercase(PasswordMissingCharacter):
    def __init__(self, arg):
        PasswordMissingCharacter.__init__(self, arg)
        self._arg = arg

    def __str__(self):
        return PasswordMissingCharacter.__str__(self) + " (Uppercase)"

class Lowercase(PasswordMissingCharacter):
    def __init__(self, arg):
        PasswordMissingCharacter.__init__(self, arg)
        self._arg = arg

    def __str__(self):
        return PasswordMissingCharacter.__str__(self) + " (Lowercase)"

class Digit(PasswordMissingCharacter):
    def __str__(self):
        return PasswordMissingCharacter.__str__(self) + " (Digit)"

class Special(PasswordMissingCharacter):
    def __str__(self):
        return PasswordMissingCharacter.__str__(self) + " (Special)"

class PasswordTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "The password you enterd is too short"
    def get_arg(self):
        return _arg

class PasswordTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "the username %s you entered contains illegal characters"
    def get_arg(self):
        return self._arg

def check_input(username, password):
    try:
        flag_lower = None
        flag_upper = None
        flag_digit = None
        flag_punctuation = None
        flag_username_letter = None
        flag_username_digit = None
        flag_username_underline = None
        some_char = None
        some_char_index = None
        for i in username:
            if i in string.ascii_letters:
                flag_username_letter = True
            if i in string.digits:
                flag_username_digit = True
            if i == "_":
                flag_username_underline = True
            if i in string.punctuation[0:26] + string.punctuation[28:32]:
                some_char = i
                some_char_index = username.index(i)
                raise UsernameContainsIllegalCharacter(username)
        if not (flag_username_letter and flag_username_digit and flag_username_underline):
            raise UsernameContainsIllegalCharacter(username)
        if len(username) < 3:
            raise UsernameTooShort (username)
        if len(username) > 16:
            raise UsernameTooLong (username)
        for i in password:
            if i.islower():
                flag_lower = True
            if i.isupper():
                flag_upper = True
            if i in string.punctuation:
                flag_punctuation = True
            if i.isdigit():
                flag_digit = True
        if not (flag_lower and flag_upper and flag_digit and flag_punctuation):
            for key in {"flag_lower": flag_lower, "flag_upper": flag_upper, "flag_digit": flag_digit, "flag_punctuation": flag_punctuation}:
                if {"flag_lower": flag_lower, "flag_upper": flag_upper, "flag_digit": flag_digit, "flag_punctuation": flag_punctuation}[key] != True:
                    if key == "flag_upper":
                        raise Uppercase(password)
                    if key == "flag_lower":
                        raise Lowercase(password)
                    if key == "flag_digit":
                        raise Digit(password)
                    if key == "flag_punctuation":
                        raise Special(password)
                        
        if len(password) < 8:
            raise PasswordTooShort (password)
        if len(password) > 40:
            raise PasswordTooLong (password)
    except Uppercase:
        print("Uppercase")
    except Lowercase:
        print("Lowercase")
    except Digit:
        print("Digit")
    except Special:
        print("Special")
    except PasswordTooShort:
        print("Password is too short. Please fix it and type it here again")
    except PasswordTooLong:
        print("Password is too long. Please fix it and type is here again")
    except UsernameContainsIllegalCharacter:
        print("Username contains illegal character" + ' "' + str(some_char) + '"' + " at index " + str(some_char_index))
    except UsernameTooShort:
        print("Username is too short, Please fix it and type if here again")
    except UsernameTooLong:
        print("Username is too long. Please fix it and type it here again")
    else:
        print("OK")

check_input("A_a1.", "12345678")
check_input("1", "2")
check_input("0123456789ABCDEFG", "2")
check_input("A_1", "2")
check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
check_input("A_1", "abcdefghijklmnop")
check_input("A_1", "ABCDEFGHIJLKMNOP")
check_input("A_1", "ABCDEFGhijklmnop")
check_input("A_1", "4BCD3F6h1jk1mn0p")
check_input("A_1", "4BCD3F6.1jk1mn0p")

check_input("A_1", "Aa1!83743")

def translate(sentence):
    new_sentence = []
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    translated_words = (words[i] for i in sentence.split( ))
    for i in translated_words:
        new_sentence += [i] 
    return " ".join(new_sentence)

print(translate("el gato esta en la casa"))

def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def first_prime_over(n):
    prime_numbers = (i for i in range(n, n+11) if is_prime(i))
    print(next(prime_numbers))
first_prime_over(1000000)

def parse_ranges(ranges_string):
    list1 = []
    delimate_string = (i.split("-") for i in ranges_string.split(","))
    ranges = (range(int(i[0]), int(i[1]) + 1) for i in delimate_string)
    for i in ranges:
        list1 += list(i)
    return list1
    # for i in ranges:
    #     list1 += [list(i)]
    # return list1

print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))

def gen_fibo():
    num = 0
    number = 0
    numbers_list = [0, 1]
    yield 0
    while number > -1:
        yield numbers_list[-1]
        number = numbers_list[num] + numbers_list[num + 1]
        numbers_list += [number]
        num += 1

fibo_gen = gen_fibo()

def gen_secs():
    seconds = (i for i in range(60))
    return seconds

def gen_minutes():
    minutes = (i for i in range(60))
    return minutes

def gen_hours():
    hours = (i for i in range(24))
    return hours

def gen_time():
    sec = gen_secs()
    min = gen_minutes()
    hour = gen_hours()
    next_sec = next(sec)
    next_min = next(min)
    next_hour = next(hour)
    yield "00:00:00"
    for hour in gen_hours():
        hours = str(hour).zfill(2)
        for minute in gen_minutes():
            minutes = str(minute).zfill(2)
            for second in gen_secs():
                seconds = str(second).zfill(2)
                yield hours + ":" + minutes + ":" + seconds
     

gen_time_2 = gen_time()

def gen_years(start=2022):
    global year
    year = start
    some_var = True
    while some_var == True:
        year += 1
        yield year
years = gen_years()

def gen_months():
    months_gen = (i for i in range(1, 13))
    return months_gen

def gen_days(month=1, leap_year=True):
        if year % 4 == 0:
            leap_year = True
        else:
            leap_year = False
        if month == 1:
            return (i for i in range(1, 32))  
        elif month == 2:
            if leap_year:
                return (i for i in range(1, 29))  
            else:
                return (i for i in range(1, 30))
        elif month == 3:
            return (i for i in range(1, 32))
        elif month == 4:
            return (i for i in range(1, 32))
        elif month == 5:
            return (i for i in range(1, 32))
        elif month == 6:
            return (i for i in range(1, 31))
        elif month == 7:
            return (i for i in range(1, 32))
        elif month == 8:
            return (i for i in range(1, 32))
        elif month == 9:
            return (i for i in range(1, 31))
        elif month == 10:
            return (i for i in range(1, 32))
        elif month == 11:
            return (i for i in range(1, 31))
        elif month == 12:
            return (i for i in range(1, 32))
        else:
            return None

def gen_date(some_year, some_month):
    for year in gen_years(some_year):
        years = str(year).zfill(4)
        for month in gen_months():
            months = str(month).zfill(2)
            for day in gen_days(some_month):
                days = str(day).zfill(2)
                for i in gen_time():
                    yield days + "/" + months + "/" + years + " " + i

some_date = gen_date(2022, 1)
num = 1000000
for i in some_date:
    print(next(itertools.islice(some_date, num, None)))
    num = num * 2

def add(a, b):
    return a + b

wallet_cash = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
num = 7
tuples_list = []
while num <= len(wallet_cash):
    nums_tuple = itertools.combinations(wallet_cash, num)
    for i in nums_tuple:
        if functools.reduce(add, i) == 100:
            tuples_list += [i]
    num += 1
for i in set(tuples_list):
                print(i)
        

class MusicNotes():
    def __init__(self):
        self.first_row = [55, 61.74, 65,41, 73.42, 82.41, 87.31, 98]
        self.first_row = [55, 61.74, 65,41, 73.42, 82.41, 87.31, 98]
        self.first_row = [55, 61.74, 65,41, 73.42, 82.41, 87.31, 98]
        self.first_row = [55, 61.74, 65,41, 73.42, 82.41, 87.31, 98]
        self.first_row = [55, 61.74, 65,41, 73.42, 82.41, 87.31, 98]
        self.octab_index = -1
    def __iter__(self):
        return self

    def __next__(self):
        if self.octab_index >= len(self.first_row) -1:
            raise StopIteration
        self.octab_index += 1
        return self.first_row[self.octab_index]

some_note = iter(MusicNotes())
for i in some_note:
    print(i)

my_str = "CgkJICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAuLS0tW1tfX11dLS0tLS4KICAgICAgICAgICAgICA7LS0tLS0tLS0tLS0tLS58ICAgICAgIF9fX18KICAgICAgICAgICAgICB8ICAgICAgICAgICAgIHx8ICAgLi0tW1tfX11dLS0tLgogICAgICAgICAgICAgIHwgICAgICAgICAgICAgfHwgIDstLS0tLS0tLS0tLS58CiAgICAgICAgICAgICAgfCAgICAgICAgICAgICB8fCAgfCAgICAgICAgICAgfHwKICAgICAgICAgICAgICB8X19fX19fX19fX19fX3wvICB8ICAgICAgICAgICB8fAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHxfX19fX19fX19fX3wvCgo="

my_str_encoded = my_str.encode()
my_str_decoded = base64.b64decode(my_str_encoded)
print(my_str_decoded)

class GreetingCard():
    def __init__(self, recipient="Dana Ev", sender="Eyal Ch"):
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self):
        print(self._sender)
        print(self._recipient)

class BirthdayCard(GreetingCard):
    def __init__(self, sender_age, recipient="Dana Ev", sender="Eyal Ch"):
        GreetingCard.__init__(self, recipient="Dava Ev", sender="Eyal Ch")
        self._sender_age = sender_age

    def greeting_msg(self):
        GreetingCard.greeting_msg(self)
        print("Happy Birthday" + " " + str(self._sender_age))


