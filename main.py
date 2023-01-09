import art, game_data, clear, random

def print_red(skk): print("\033[91m{}\033[00m" .format(skk))
def print_green(skk): print("\033[92m{}\033[00m" .format(skk))

def draw():
    person = game_data.data[random.randint(0,49)]
    return person

def draw_the_second(person_a):
    while True:
        person_b = draw()
        if person_a == person_b:
            continue
        else:
            return person_b
    
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


def user_answer():
    while True:
        user_choose = input("Who has more followers? Type 'A' or 'B': ").upper()
        if user_choose == 'B':
            return 'B'
        elif user_choose == 'A':
            return 'A'
        else:
            print("You can only choose 'A' or 'B'.")
            continue

def main():
    final_score = 0
    while True:
        clear.clear_screen()
        print(art.logo)
        if final_score >= 1:
            print_green(f"You're right! Current score: {final_score}.")
        person_a = draw()
        person_b = draw_the_second(person_a)
        print_name(person_a, person_b)
        user_choose = user_answer()
        if compare(person_a, person_b, user_choose) == True:
            final_score += 1
            continue
        elif compare(person_a, person_b, user_choose) == False:
            clear.clear_screen()
            print(art.logo)
            print_red(f"Sorry, that's wrong. Final score: {final_score}")
        break


if __name__ == "__main__":
    main()
    pass