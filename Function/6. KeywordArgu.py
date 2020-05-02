def wish(name, msg):
    print("hello", name, msg)


wish(name="Parth", msg="Good morning")
wish(msg="Good morning", name="Parth")

# wish("Durga","GoodMorning")      ==>valid
# wish("Durga",msg="GoodMorning")     ==>valid
# wish(name="Durga","GoodMorning")   ==>invalid
