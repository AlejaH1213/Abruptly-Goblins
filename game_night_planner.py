#people who are attending game night
gamers = []
#function to 
def add_gamer(gamer,gamers_list):

  if gamer.get('name') and gamer.get('availability'):
    gamers_list.append(gamer)
  else:
    print('Gamer missing critical information')