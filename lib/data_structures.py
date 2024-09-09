spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    # spices = []
    # for spicy_food in spicy_foods:
    #     spices.append(spicy_food["name"])

    # return spices
    return [spicy_food["name"] for spicy_food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    # spiciest = []
    # for spicy_food in spicy_foods:
    #     if spicy_food["heat_level"] > 5:
    #         spiciest.append(spicy_food)
    # return spiciest
    return [spicy_food for spicy_food in spicy_foods if spicy_food["heat_level"] > 5]


def print_spicy_foods(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        heat_level = "🌶" * spicy_food["heat_level"]
        print(f"{spicy_food["name"]}  ({spicy_food["cuisine"]}) | Heat Level: {heat_level}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if cuisine == spicy_food["cuisine"]:
            return spicy_food
    return "Did not match any cuisine on our catalogue"


def print_spiciest_foods(spicy_foods):
    for spicy_food in spicy_foods:
        if spicy_food["heat_level"] > 5:
            heat_level = "🌶" * spicy_food["heat_level"]
            print('{} ({}) | Heat Level: {}'.format(spicy_food["name"], spicy_food["cuisine"], heat_level))
            # print(f'{spicy_food["name"]} ({spicy_food["cuisine"]}) | Heat Level: {heat_level}.')


def get_average_heat_level(spicy_foods):
    # total = 0
    # for spicy_food in spicy_foods:
    #     total += spicy_food["heat_level"]

    # return total / len(spicy_food)
    return sum(spicy_food["heat_level"] for spicy_food in spicy_foods) / len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods


print(get_names(spicy_foods))
print(get_spiciest_foods(spicy_foods))
# print(print_spicy_foods(spicy_foods, "American"))
print(get_average_heat_level(spicy_foods))
print(create_spicy_food(spicy_foods,   {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}))
print(print_spiciest_foods(spicy_foods))
print(print_spicy_foods(spicy_foods))