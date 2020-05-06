class computer:

    def __init__(self, cpu, ram):  # it is automatic call
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("cpu -> ", self.cpu, "RAM-> ", self.ram)


com1 = computer("i5", 16)
com2 = computer("ryzen 3", 8)

com1.config()
com2.config()
