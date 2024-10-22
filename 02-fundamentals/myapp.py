from math import trunc

from mymodule import physics

user_input = input("Zadejte vaši hmotnost: ")
print('Na měsíci by jste vážil %.2f kg.' % physics.weight_on_moon(int(user_input)))
user_input = input("Zadejte rychlost (m/s): ")
print(f'Rychlost {user_input} m/s je {physics.percent_of_light_speed(int(user_input))} % rychlosti světla.')
user_input = input("Zadejte čas (s): ")
print(f'Zvuk by za tuto dobu uletěl {physics.sound_travel_distance(int(user_input))} m.')
