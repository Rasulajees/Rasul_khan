a=input("team 1_name:")
b=input("team 2_name:")

team1_players=int(input("team 1_players:"))
team2_players=int(input("team 2_players:"))


team1_score =input("team 1_Score:") 
team2_score =input("team 2_Score:")

if(team1_score > team2_score):
    print("winner!",a)

elif(team2_score > team1_score):
    print("winner!",b)

elif team1_score == team2_score:
    print("The match is a draw!")

else:
    print(" no match")

#----------------------------------------------------------------
# Example usage
''' csk_score =input("Score: ") 
rcb_score =input("Score:")

if is_draw(csk_score, rcb_score):
    print("The match is a draw!")
else:
    print("The match is not a draw.")"""


#----------------------------------------------------------------

"""Fan=input( "enter your comment here:")
if(Fan=="on"):
    print("fan is on")  
else:
    print("fan is off")   """ 
#----------------------------------------------------------------
"""Fan=input("enter your commend:")  
if("off==fan"):
    print("fan is off")
else:
    print("off:fan is on")'''
