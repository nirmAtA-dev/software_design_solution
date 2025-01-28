import math 

def birthday_paradox(samples, no_of_bits):
    total_sample_space = no_of_bits ** 2

    collision = 1 - (math.factorial(total_sample_space) / (math.factorial(total_sample_space - samples)*(pow(total_sample_space, samples))))
    return collision * 100



if __name__ == "__main__":
    # for 4 files and odds of collision
    print("Number of Files    Odds of Collision")
    for i in range(1,5):
        collision_percentage = birthday_paradox(i,2)
        print(f"{i}                  {collision_percentage}")

    print(">4                 100%")
