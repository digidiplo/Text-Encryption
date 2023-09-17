from flask import Flask, render_template, request
from encryption_algorithms import caesar_cipher, generateKey, cipherText, originalText

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted_text = ""
    if request.method == 'POST':
        text_to_encrypt = request.form.get('text_to_encrypt')
        algorithm_choice = request.form.get('algorithm_choice')
        shift_or_key = request.form.get('shift_or_key')
        
        if algorithm_choice == "caesar":
            encrypted_text = caesar_cipher(text_to_encrypt, shift_or_key)
            
        elif algorithm_choice == "vigenere":
            key = generateKey(text_to_encrypt, "KEY")  # "KEY" can be replaced by a user-inputted keyword
            encrypted_text = cipherText(text_to_encrypt, shift_or_key)
            
    return render_template('index.html', output=encrypted_text)


if __name__ == '__main__':
    app.run(debug=True)
