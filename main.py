# a121_catch_a_turtle.py
#-----import statements-----
#By Ibrahim Shabani
import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----
spot_size = 2
spot_color = "pink"
spot_shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----leaderboard variables-----
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name:")

#-----initialize turtle-----
spot = trtl.Turtle()
spot.penup()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)

score_writer = trtl.Turtle()
score_writer.pu()
score_writer.goto(-180, 170)
score_writer.hideturtle()

counter =  trtl.Turtle()
counter.hideturtle()
counter.pu()
counter.goto(150, 170)
#-----game functions--------
def spot_clicked(x,y):
    if timer_up == False:
        change_position()
        update_score()
def change_position():
    new_xpos = rand.randint(-180, 140)
    new_ypos = rand.randint(-140, 140)
    spot.hideturtle()
    spot.goto(new_xpos, new_ypos)
    spot.showturtle()
def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
    global leader_scores_list
    global leader_names_list
    global score
    global spot

    # load all the leaderboard records into the lists
    lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

    # TODO
    if len(leader_scores_list) < 5 or score > leader_scores_list[4]:
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

    else:
        lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)


#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.bgcolor("purple")
wn.mainloop()
