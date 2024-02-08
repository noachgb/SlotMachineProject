import random
import replit
money=1000
memz = ['$','7','F']

while True:
  a1=random.choice(memz)
  a2=random.choice(memz)
  a3=random.choice(memz)
  a4=random.choice(memz)
  print('Your money: ',money)
  print('Choose difficulty:')
  print('1.EZ (Cost:25)')
  print('2.Normal (Cost: 50)')
  print('3.Hard (Cost: 100)')
  print('4.Impossibruh (Cost: 250)')
  print('5.Choose this for extra money (No clickbait)')
  a= int(input('Choose: '))
  if money < 25:
    print('Uang abis boz')
    print('Yah miskin aokwowkoawkoawk')
    break
  if a==1:
    if money>=25:
      money-= 25
      print(a1)
      if a1=='$':
        money += random.randint(50,75)
        print('You win ',)
        print('Your money: ',money)
        input()
        replit.clear()
      elif a1=='7':
        money+= 100
        print('Jekpot!')
        print('Your money: ',money)
        input()
        replit.clear()
      elif a1=='F':
        money-=20
        print('F')
        print('Lost 20')
        print('Your money: ',money)
        input()
        replit.clear()
      else:
        print('Ur RNG s u c c')
        print('Your money: ',money)
        input()
        replit.clear()
  elif a==2:
    if money>=50:
      money-= 50
      print(a1,a2)
      if a1=='$' and a1==a2:
        money += random.randint(100,150)
        print('You win ')
        print('Your money: ',money)
        input()
        replit.clear()
      elif a1=='7'and a1==a2:
        money+= 200
        print('Jekpot!')
        print('Your money: ',money)
        input()
        replit.clear()
      elif a1=='F' and a1==a2:
        money-=25
        print('F')
        print('Lost 25')
        print('Your money: ',money)
        input()
        replit.clear()
      else:
        print('Ur RNG s u c c')
        print('Your money: ',money)
        input()
        replit.clear()
    elif money<50:
      print('Not enough money')
      input()
      replit.clear()
  elif a==3:
    if money>=100:
      money-= 100
      print(a1,a2,a3)
      if a1=='$' and a1==a2 and a1==a3:
        money += random.randint(200,250)
        print('You win ')
        print('Your money: ',money)
        input()
        replit.clear()
      elif a1=='7' and a1==a2 and a1==a3:
        money+= 300
        print('Jekpot!')
        print('Your money: ',money)
        input()
        replit.clear()
      elif a1=='F' and a1==a3 and a1==a2:
        money-=50
        print('F')
        print('Lost 50')
        print('Your money: ',money)
        input()
        replit.clear()
      else:
        print('Ur RNG s u c c')
        print('Your money: ',money)
        input()
        replit.clear()
    elif money<100:
      print('Not enough money')
      input()
      replit.clear()
  elif a==4:
    if money>=250:
      money-= 250
      print(a1,a2,a3,a4)
      if a1=='$' and a1==a2 and a1==a3 and a1==a4:
        money += random.randint(500,600)
        print('You win ')
        print('Your money: ',money)
        input()
        replit.clear()
      elif a1=='7' and a1==a2 and a1==a3 and a1==a4:
        money+= 750
        print('Jekpot!')
        print('Your money: ',money)
        input()
        replit.clear()
      elif a1=='F' and a1==a3 and a1==a2 and a1==a4:
        money-=100
        print('F')
        print('Lost 100')
        print('Your money: ',money)
        input()
        replit.clear()
      else:
        print('Ur RNG s u c c')
        print('Your money: ',money)
        input()
        replit.clear()
    elif money<250:
      print('Not enough money')
      input()
      replit.clear()
  elif a==5:
    print('Get jebaited! aokwaowkoawk')
    break