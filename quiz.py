from question import *

def game_start(score, lose):
   """
      fonction pour lancer le jeu
   
   """
   for i in questions:
      print(questions[i]['title'])
      print(questions[i]['statement'])
      verified = questions[i]['answer'][0]
      true_answer = questions[i]['answer']
      for i in questions[i]['proposal']:
         print(i)

      user_answer = input('Entrez votre réponse: \n')

      if user_answer.lower() == verified:
         print('Bonne réponse!\n')
         score += 1
      else:
         print('Mauvaise réponse')
         print(f"La bonne réponse était : {true_answer}\n")
         lose += 1

   print(f"Vous avez fait un score de {score} point(s)")
   print(f"Et vous avez manqué {lose} question(s)")

game_start(score, lose)

