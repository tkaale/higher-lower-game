import art, game_data, clear, random

# def draw():
#     while True:
#         person_a = game_data.data[random.randint(0,50)]
#         person_b = game_data.data[random.randint(0,50)]
#         if person_a == person_b:
#             continue
#         else:
#             return [person_a, person_b]

def draw():
    person = game_data.data[random.randint(0,50)]
    return person

def draw_the_second(person_a):
    while True:
        person_b = draw()
        if person_a == person_b:
            continue
        else:
            return [person_a, person_b]



def compare(person_a, person_b):
    pass




def main():
    while True:
        clear.clear_screen()
        print(art.logo)

if __name__ == "__main__":
    pass