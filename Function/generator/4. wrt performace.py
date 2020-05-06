import random

name = ['Sunny', 'Bunny', 'Chinny', 'Vinny']
subjects = ['Python', 'Java', 'Blockchain']


def people_Generator(num_people):
    # result = []
    for i in range(num_people):
        person = {
            "id": i,
            "name": random.choice(name),
            "subject": random.choice(subjects)
        }

        yield person


# t1 = time.clock()
people = people_Generator(5)
# t2 = time.clock()

print("TOOK {}".format(next(people)))
print("TOOK {}".format(next(people)))
