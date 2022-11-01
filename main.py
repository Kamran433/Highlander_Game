import random
import up_art
import up_data
cond=True
score=0
while cond==True:
 z=random.randint(0,49)
 i=random.randint(0,49)
 m=up_data.data[z]
 n=up_data.data[i]
 c=m["name"]
 d=m["description"]
 e=m["country"]
 f=n["name"]
 g=n["description"]
 h=n["country"]
 print(up_art.logo)
 print(f"Compare A : {c}, {d}, {e}")
 print(up_art.vs)
 print(f"Against B : {f}, {g}, {h}\n")
 cho=input("Who has more followers? Type 'A' or 'B': ")
 if cho=="A":
   if m["follower_count"]>n["follower_count"]:
     print("You Win!")
     score+=1
     cond=True
     clear()
     print(f"You're right! Current score: {score}")
   elif m["follower_count"]<n["follower_count"]:
     clear()
     print(up_art.logo)
     print(f"Sorry, that's wrong. Final score: {score}")
     cond=False
 elif cho=="B":
   if m["follower_count"]<n["follower_count"]:
     print("You Win!")
     score+=1
     cond=True
     clear()
     print(f"You're right! Current score: {score}")
   elif m["follower_count"]>n["follower_count"]:
     clear()
     print(up_art.logo)
     print(f"Sorry, that's wrong. Final score: {score}")
     cond=False
