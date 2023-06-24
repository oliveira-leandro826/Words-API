from flask import Flask, request, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        'status': 'error',
        'message': 'Rota inexistente.'
    }), 404

@app.route('/vowel_count', methods=['POST'])
def vowel_count():
    try:
        if request.content_type != 'application/json':
            return jsonify({
                'status': 'error',
                'message': 'O content-type deve ser application/json.'
            }), 415

        data = request.get_json()
        vowels = ['a', 'e', 'i', 'o', 'u']
        words_dict = {}

        if type(data) != dict or 'words' not in data.keys():
            return jsonify({
                'status': 'error',
                'message': 'JSON mal formatado.'
            }), 400

        words = data['words']
        
        for word in words:
            count = 0

            for vowel in vowels:
                count += word.lower().count(vowel) 
            
            words_dict[word] = count

        return jsonify(words_dict)
    except Exception as exception:
        print(exception)

        return jsonify({
            'status': 'error',
            'message': 'Erro interno na API.'
        }), 500

@app.route('/sort', methods=['POST'])
def sort():
    try:
        if request.content_type != 'application/json':
            return jsonify({
                'status': 'error',
                'message': 'O content-type deve ser application/json.'
            }), 415

        data = request.get_json()
        desc = False

        if (
            type(data) != dict 
            or 'words' not in data.keys() 
            or 'order' not in data.keys()
        ):
            return jsonify({
                'status': 'error',
                'message': 'JSON mal formatado.'
            }), 400

        words = data['words']

        if data['order'] == 'desc':
            desc = True
        
        words = sorted(words, reverse=desc)

        return jsonify(words)
    except Exception as exception:
        print(exception)
        raise exception

        return jsonify({
            'status': 'error',
            'message': 'Erro interno na API.'
        }), 500