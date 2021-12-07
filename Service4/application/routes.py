from application import app
from flask import request, Response
from random import randint

#Generates a reward based on the generated random numbers and letters
@app.route('/prize2', methods = ['POST'])
def prize2():
   code = request.data.decode('utf-8')
   if code[0] == '1' or code[4] == 'E':
      winning = 'You won £50!'
   elif code[0] == '2':
      winning = 'You won £100,000!'
   elif code [0] == '4':
      winning = 'You won £50,000,000!'
   else:
      winning = "You lost this time, try next time!"
   return Response(winning, mimetype= 'text/plain')