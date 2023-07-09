from flask import (
    Blueprint, redirect, render_template, url_for, request, render_template_string
)

Blue = Blueprint('morse', __name__, url_prefix='/morse')

Alfabeto = {

    # ----------LETRAS-------------
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    # ------LETRAS CON TILDE--------

    'Á': '.--.-', 'É': '..-..', 'Ó': '---.',

    # ------------NUMEROS--------------

    '1': '.---', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----',


    # -------SIGNOS DE PUNTUACIÓN-------

    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": ".----.", '!': '-.-.--', '/': '-..-.',
    '(': '-.--.',  ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    '¿': '..-.-',  '¡': '--...-'

}


@Blue.route('/', methods=['GET', 'POST'])
def index():

    area2 = []
    morse = ''
    i=0
    
    if request.method == 'POST':

        area2 = []
        area1 = request.form['string']
        # p=request.form['os']

        t = request.form['task']

        if int(t) == 1:

            for Caracter in area1:

                if Alfabeto.get(Caracter.upper()) is None:

                    morse += ' / '
                else:
                    morse += ' '+Alfabeto.get(Caracter.upper())

            area2.append(morse)

        elif int(t) == 2:

            area1 = request.form['string'].split(' ')

            for LetraMorse in area1:

                for Key in Alfabeto.keys():

                    if Alfabeto.get(Key) == LetraMorse:
                        morse += Key
                        break

                    if LetraMorse=='':
                        morse+=' '
                        break
                    
                    i+=1
                    if i==59:
                        morse+='#'
                
                i=0

            print(area1)
            # morse=''

        print('HEY: ', t)

    return render_template('base.html', morse=morse)

