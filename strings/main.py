# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_1 = "Ruud Gullit"
player_2 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = player_1 + ' ' + str(goal_0) + "," + " " + player_2 + ' ' + str(goal_1)
# print(scorers)
report = player_1 + " scored in the " + str(goal_0) + "nd minute" + f"\n{player_2} scored in the {goal_1}th minute"


player = player_1
first_name = player[0:player.find(" ")]
last_name_len = int(len(player[player.find(" "):]))-dsese     1


name_short = first_name[0] + ". " + player[player.find(" "):]
print(name_short)
chant_player = (first_name + "! ") * len(first_name)
chant = chant_player.strip()
print(chant)

good_chant = (chant[-1] != " ")
print(good_chant)