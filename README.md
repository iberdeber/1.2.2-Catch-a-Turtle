# 1.2.2-Catch-a-Turtle
My attempt at completing the super large 1.2.2 assignment for CSP
It is a lot of work :(
I did get a very weird error message that I couldn't fix
There was something wrong with lines 62 and 79 in main, though the problem came on suddenly and I have no idea what I did wrong:


line 62, in countdown
    manage_leaderboard()


line 79, in manage_leaderboard
    if len(leader_scores_list) < 5 or score > leader_scores_list[4]:
TypeError: '>' not supported between instances of 'int' and 'str'

