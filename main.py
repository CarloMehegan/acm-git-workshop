import random

def calculate_compatibility(name1, name2) -> int:
    names = [name1, name2]
    seed = "".join(names)
    gen = random.Random(seed)
    compatibility = (gen.random()) * 100 + 1
    return int(compatibility)

if __name__ == "__main__":
    print("aloooo")
    name1 = input("name 1: ")
    name2 = input("name 1: ")
    print(calculate_compatibility(name1, name2))
