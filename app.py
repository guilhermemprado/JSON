from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

JSON_FILE_PATH = 'data.json'


def load_data():
    with open(JSON_FILE_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_data')
def get_data():
    data = load_data()
    return jsonify(data)


def read_json():
    try:
        with open(JSON_FILE_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def write_json(data):
    with open(JSON_FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


@app.route('/update_data', methods=['POST'])
def update_data():
    try:
        existing_data = read_json()

        updated_data = request.json
        print(updated_data)
        existing_data.update(updated_data)

        write_json(existing_data)

        return 'Dados atualizados com sucesso!', 200

    except Exception as e:
        print('Erro:', e)
        return f'Erro ao atualizar os dados: {e}', 500


if __name__ == '__main__':
    app.run(debug=True)
