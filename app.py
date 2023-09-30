from flask import Flask, render_template, request
from encryption_algorithms import caesar_cipher, cipherText, reverse_caeser, generateKey, originalText

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    processed_text = ""
    if request.method == 'POST':
        text_to_process = request.form.get('text_to_process')
        algorithm_choice = request.form.get('algorithm_choice')
        shift_or_key = request.form.get('shift_or_key')
        action = request.form.get('action')
        
        if algorithm_choice == "caesar":
            if action == "encrypt":
                processed_text = caesar_cipher(text_to_process, int(shift_or_key))
            elif action == "decrypt":
                processed_text = reverse_caeser(text_to_process, int(shift_or_key))
            
        elif algorithm_choice == "vigenere":
            key = shift_or_key
            if action == "encrypt":
                processed_text = cipherText(text_to_process, key)
            elif action == "decrypt":
                process_text = originalText(text_to_process, key)
    
    return render_template('index.html', output=processed_text)


if __name__ == '__main__':
    app.run(debug=True)
