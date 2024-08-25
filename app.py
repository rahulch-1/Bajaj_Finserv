from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# {"data":["a","b","1"]}
@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bajaj Finserv - Data Processor</title>
    <style>
        /* Existing CSS */
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

        body {
            background-color: #f4f4f4;
            font-family: "Montserrat", sans-serif;
            color: #333333;
        }

        h1 {
            font-size: 2.5rem;
            color: #0a3d62;
            text-align: center;
            margin-bottom: 20px;
        }

        form {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin: 2rem auto;
        }

        textarea {
            width: 100%;
            border-radius: 5px;
            border: 1px solid #0a3d62;
            padding: 10px;
            font-size: 1rem;
            margin-bottom: 15px;
        }

        button {
            width: 100%;
            border-radius: 5px;
            padding: 10px;
            border: none;
            background-color: #0a3d62;
            color: white;
            font-size: 1.2rem;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #0c2c56;
        }

        #response {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin: 2rem auto;
        }

        h2 {
            color: #0a3d62;
        }

        pre {
            background-color: #f4f4f4;
            color: #0a3d62;
            padding: 10px;
            border-radius: 5px;
            white-space: pre-wrap;
            font-size: 1rem;
        }

        label {
            display: block;
            font-size: 1.1rem;
            margin-bottom: 10px;
            color: #0a3d62;
        }

        input[type="checkbox"] {
            margin-right: 10px;
        }

        .hidden {
            display: none;
        }

        #numbersSection,
        #alphabetsSection,
        #highestAlphabetSection,
        #highestNumberSection {
            margin-top: 10px;
            padding: 10px;
            background-color: #e3f2fd;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>

<body>
    <div>
        <h1>Bajaj Finserv Data Processor</h1>
        <form id="jsonForm">
            <textarea id="jsonInput" rows="6" cols="50" placeholder="Enter your JSON data here..."></textarea><br>
            <button type="button" onclick="submitJson()">Process Data</button>
        </form>
        <div id="response">
            <h2>Processing Results</h2>
            <pre id="responseData"></pre>
            <div>
                <label><input type="checkbox" id="showNumbers" onclick="toggleSection()"> Numbers</label>
                <label><input type="checkbox" id="showAlphabets" onclick="toggleSection()"> Alphabets</label>
                <label><input type="checkbox" id="showHighestAlphabet" onclick="toggleSection()"> Highest Alphabet</label>
                <label><input type="checkbox" id="showHighestNumber" onclick="toggleSection()"> Highest Number</label>
            </div>
            <div id="numbersSection" class="hidden"></div>
            <div id="alphabetsSection" class="hidden"></div>
            <div id="highestAlphabetSection" class="hidden"></div>
            <div id="highestNumberSection" class="hidden"></div>
        </div>
    </div>
    <script>
        function submitJson() {
            const jsonInput = document.getElementById('jsonInput').value;
            const url = '/bfhl';

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: jsonInput
            })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('responseData').textContent = JSON.stringify(data, null, 2);
                    document.getElementById('numbersSection').textContent = `Numbers: ${data.numbers.join(', ')}`;
                    document.getElementById('alphabetsSection').textContent = `Alphabets: ${data.alphabets.join(', ')}`;
                    document.getElementById('highestAlphabetSection').textContent = `Highest Alphabet: ${data.highest_alphabet.join(', ')}`;
                    document.getElementById('highestNumberSection').textContent = `Highest Number: ${data.highest_number.join(', ')}`;
                })
                .catch(error => console.error('Error:', error));
        }

        function toggleSection() {
            document.getElementById('numbersSection').classList.toggle('hidden', !document.getElementById('showNumbers').checked);
            document.getElementById('alphabetsSection').classList.toggle('hidden', !document.getElementById('showAlphabets').checked);
            document.getElementById('highestAlphabetSection').classList.toggle('hidden', !document.getElementById('showHighestAlphabet').checked);
            document.getElementById('highestNumberSection').classList.toggle('hidden', !document.getElementById('showHighestNumber').checked);
        }
    </script>
</body>

</html>

'''

@app.route('/bfhl', methods=['POST'])
def post_bfhl():
    data = request.json.get('data', [])
    numbers = [int(x) for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]
    highest_alphabet = [max(alphabets, key=str.lower)] if alphabets else []
    highest_number = [str(max(numbers))] if numbers else []

    response = {
        "is_success": True,
        "user_id": "rahulch",
        "email": "rahul.21bce9779@vitapstudent.ac.in",
        "roll_number": "21BCE9779",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet,
        "highest_number": highest_number
    }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def get_bfhl():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run()
