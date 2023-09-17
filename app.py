from flask import Flask, render_template, request
from encryption_algorithms import caesar_cipher, vigenere_cipher

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted_text = ""
    if request.method == 'POST':
        text_to_encrypt = request.form.get('text_to_encrypt')
        algorithm_choice = request.form.get('algorithm_choice')
        
        if algorithm_choice == "caesar":
            encrypted_text = caesar_cipher(text_to_encrypt, shift=3)

        elif algorithm_choice == "vigenere":
            encrypted_text = vigenere_cipher(text_to_encrypt, keyword="KEY")

    return render_template('index.html', output=encrypted_text)


if __name__ == '__main__':
    app.run(debug=True)
