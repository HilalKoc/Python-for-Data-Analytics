# ===================================================
# PYTHON DATA STRUCTURES BASICS
# ===================================================


# ---------------------------------------------------
# Task 1: Examine the data types of given values
# ---------------------------------------------------

x = 8           # int
y = 3.2         # float
z = 8j + 18     # complex
a = "Hello World"  # str
b = True        # bool
c = 23 < 22     # bool
l = [1, 2, 3, 4]  # list
d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}  # dict
t = ("Machine Learning", "Data Science")  # tuple
s = {"Python", "Machine Learning", "Data Science"}  # set

type(s)


# ---------------------------------------------------
# Task 2: Convert all letters to uppercase, replace commas and periods with spaces, split word by word
# Expected output: ['THE', 'GOAL', ...]
# ---------------------------------------------------

text = "The goal is to turn data into information, and information into insight."

text.upper().replace(",", " ").replace(".", " ").split()


# ---------------------------------------------------
# Task 3: Apply the following steps to the given list
# ---------------------------------------------------

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Step 1: Check the number of elements in the list
len(lst)

# Step 2: Call the elements at index 0 and index 10
lst[0]
lst[10]

# Step 3: Create the list ["D", "A", "T", "A"] from the given list
data_list = lst[0:4]

# Step 4: Delete the element at index 8
lst.pop(8)

# Step 5: Add a new element
lst.append(1)

# Step 6: Re-insert "N" at index 8
lst.insert(8, "N")


# ---------------------------------------------------
# Task 4: Apply the following steps to the given dictionary
# ---------------------------------------------------

person_dict = {'Christian': ["America", 18],
               'Daisy': ["England", 12],
               'Antonio': ["Spain", 22],
               'Dante': ["Italy", 25]}

# Step 1: Access key values
person_dict.keys()

# Step 2: Access values
person_dict.values()

# Step 3: Update Daisy's age from 12 to 13
person_dict.update({'Daisy': ["England", 13]})

# Step 4: Add a new entry with key "Ahmet" and value ["Turkey", 24]
person_dict.update({'Ahmet': ["Turkey", 24]})

# Step 5: Remove "Antonio" from the dictionary
person_dict.pop("Antonio")


# ---------------------------------------------------
# Task 5: Write a function that takes a list, separates even and odd numbers into separate lists and returns them
# ---------------------------------------------------

l = [2, 13, 18, 93, 22]


def separate_even_odd(lst):
    even_list = []
    odd_list = []
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list, odd_list


even_list, odd_list = separate_even_odd(l)


# ---------------------------------------------------
# Task 6: Print student rankings by faculty using enumerate
# First 3 students belong to Engineering, last 2 to Medicine
# ---------------------------------------------------

ogrenciler = ["Ali", "Veli", "Talat", "Zeynep", "Ece"]

for i, x in enumerate(ogrenciler):
    if i < 3:
        # Index starts from 0, so we add 1 to start ranking from 1
        i += 1
        print("Engineering Faculty", i, ". student", x)
    else:
        # Index continues from 3, but Medicine ranking should start from 1, so we subtract 2
        i -= 2
        print("Medicine Faculty", i, ". student", x)


# ---------------------------------------------------
# Task 7: Print course information using zip
# ---------------------------------------------------

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

for code, credit, quota in zip(ders_kodu, kredi, kontenjan):
    print(f"The course {code} has {credit} credits and a quota of {quota} students.")


# ---------------------------------------------------
# Task 8: Write a function that prints the intersection if set1 contains set2,
# otherwise prints the difference of set2 from set1
# ---------------------------------------------------

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "hilal"])


def compare_sets(set1, set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))


compare_sets(kume1, kume2)
compare_sets(kume2, kume1)