# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
Player_1 = "Ruud Gullit"
Player_2 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = Player_1 + ' ' + str(goal_0) + "," + " " + Player_2 + ' ' + str(goal_1)
# print(scorers)
report = Player_1 + " scored in the " + str(goal_0) + "nd minute" + f"\n{Player_2} scored in the {goal_1}th minute"

print(report)
player = "Ruud Gullit"
first_name = player[player.find("R",0, 4): 4]
# print(first_name)
last_name_len = len(player[player.find("G"):])
name_short = first_name[0] + ". " + player[player.find("G"):]

chant_ruud = (first_name + "! ") * len(first_name)
chant = chant_ruud.strip()


good_chant = chant[-1] != " "
# print(good_chant)