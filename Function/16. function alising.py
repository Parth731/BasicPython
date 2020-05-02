def wish(name):
    print(name, "good morning")


greeting = wish
print(id(wish))
print(id(greeting))
wish("parth")
greeting("neeraj")

# deleting one function name

del wish
# wish("parth") #error
greeting("neeraj")
