s = "hello"
useful_methods = [m for m in dir(s) if "__" not in m]
print(useful_methods)

print(help(s.capitalize))
print(s.capitalize())

print("HELLO".casefold()) # same as .lower() method

print("hello".center(50))
print("hello".center(50, "."))

print("I see a little dove".count("e")) # how many times do I see 'e' ?
print("banananananananananana".count("ana"))
x = "I do not cook nor compare"
print(f"There are {x.count("o")}os inside: '{x}'")
print("hellooo00000ooollolo".find("l", 10))

s = "bob goes home to meet bob so they can take their bob and go bobing"
pos = 0
while True:
    start = s.find("bob", pos)
    if start == -1:
        break
    print("found bob on position", start)
    pos = start + 1

items = ["cat", "rat", "mouse", "house"]
print("+another+".join(items))
print("I LIKE to go HIKIng!!".lower().upper())
print("i like to go skiing".title())
# replace, replaces item with item inside the string
print("i like to go skiing".replace("i", "1").replace("e", "3"))
# split, makes a list of the string split by the delimiter!
print("I like to go skiing".split())
