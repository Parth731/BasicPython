class computer:

    def config(self):
        print("hello goodmorning")
        print()


comp1 = computer()
print(comp1)  # <class'__main__.computer>
computer.config(comp1)  # hello goodmorning
comp1.config()  # hello goodmorning
