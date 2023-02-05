import random
from SoundSys.Sound import Sound

edhelp_sign = "Ed Help sign"
exit_sign = "Exit sign"
toilet_sign = "Toilet sign"
long_text = "Long text"

obj1 = Sound([583, 281], 0, "Object 1. " + edhelp_sign, True)
obj2 = Sound([1097, 60], 0, "Object 2. " + "Library Cafe", True)
example_1 = [obj1, obj2]

obj1 = Sound([245, 188], 0, "Object 1. " + toilet_sign, True)
obj2 = Sound([914, 274], 0, "Object 2. " + exit_sign, True)
obj3 = Sound([1179, 258], 0, "Object 3. " + long_text, True)
example_2 = [obj1, obj2, obj3]

obj1 = Sound([308, 253], 0, "Object 1. " + "Cinema City", True)
example_3 = [obj1]

obj1 = Sound([249, 348], 0, "Object 1. " + "Il Calcio bistro", True)
obj2 = Sound([986, 253], 0, "Object 2. " + edhelp_sign, True)
obj3 = Sound([749, 230], 0, "Object 3. " + long_text, True)
example_4 = [obj2, obj3, obj1]


obj1 = Sound([249, 348], 0, "Object 1. " + "This is an example sign here", True)
obj2 = Sound([986, 253], 0, "Object 2. " + edhelp_sign, True)
obj3 = Sound([749, 230], 0, "Object 3. " + 'This is a no eating area', True)
obj4 = Sound([749, 230], 0, "Object 4. " + 'Welcome to the edinburgh library, This is the ground floor', True)
example_5 = [obj1, obj2, obj3,obj4]


all_examples = [example_1, example_2, example_3, example_4,example_5]


def give_me_a_scan():
    i = random.choice(range(len(all_examples)))

    return i, all_examples[i]
