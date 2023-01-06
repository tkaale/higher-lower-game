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
    person = game_data.data[random.randint(0,49)]
    return person

def draw_the_second(person_a):
    while True:
        person_b = draw()
        if person_a == person_b:
            continue
        else:
            return [person_a, person_b]
    
#print(draw_the_second(draw()))

def print_name(person_a, person_b):
    print(f"\nCompare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")
    print(art.vs)
    print(f"\nAgainst B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")

#print_name(draw(), draw())

def compare(person_a, person_b, user_choose):
    followers_a = person_a['follower_count']
    followers_b = person_b['follower_count']
    if followers_a > followers_b:
        winner = 'A'
    elif followers_b > followers_a:
        winner = 'B'
    if user_choose == winner:
        return True
    else:
        return False
    


def main():
    while True:
        clear.clear_screen()
        print(art.logo)


if __name__ == "__main__":
    pass