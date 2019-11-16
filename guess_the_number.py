import random
top_end = 10000
bottom_end = 1
while True:
  value = random.randint(bottom_end, top_end)
  print(value)

  while True:
    
    guess = input('guess the number (' + str(bottom_end) +'-' + str(top_end) + ')')

    #print(guess)
    #check here, then if it passes
    #cast it to int and run the rest of the code
    

    if guess.isnumeric() == False:
      print('number pls')
    #name_of_the_string.isnumeric()

    
    elif int(guess) == value:
      print('u got it')
      break     
    elif int(guess) > value:
      print('too high')
      top_end = int(guess)
      #250 = (guess - bottom end) // 2 
      print((int(guess) - bottom_end)//2 + bottom_end)
    elif int(guess) < value:
      print('too low')
      bottom_end = int(guess)
      print((top_end - int(guess))//2 + int(guess))
    else:
      pass  
    
  #input checker loop
  while True:
    again = input('wanna play again')
    if again == 'no' or again == 'yes':
      break  
    else:
      print('yes or no')

  if again == 'no':
    break
