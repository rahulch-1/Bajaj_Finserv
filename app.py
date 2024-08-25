from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>21BCE9779</title>
    <style>
        /* Add your CSS styling here */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f7f7f7;
        }
        h1 {
            color: #333;
        }
        textarea {
            width: 100%;
            padding: 10px;
            font-size: 14px;
        }
        button {
            margin-top: 10px;
            padding: 10px 15px;
            font-size: 16px;
            cursor: pointer;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
        }
        select {
            margin-top: 10px;
            padding: 10px;
            font-size: 16px;
        }
        pre {
            background-color: #efefef;
            padding: 15px;
            border-radius: 5px;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        .hidden {
            display: none;
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
        <div id="dropdownSection" class="hidden">
            <label for="responseFilter">Select data to display:</label>
            <select id="responseFilter" multiple>
                <option value="numbers">Numbers</option>
                <option value="alphabets">Alphabets</option>
                <option value="highest_lowercase_alphabet">Highest Lowercase Alphabet</option>
            </select>
            <button type="button" onclick="filterResponse()">Show Data</button>
        </div>
        <div id="response" class="hidden">
            <h2>Processing Results</h2>
            <pre id="responseData"></pre>
        </div>
    </div>
    <script>
        function submitJson() {
            const jsonInput = document.getElementById('jsonInput').value;
            try {
                JSON.parse(jsonInput); // Validate JSON
            } catch (e) {
                alert('Invalid JSON format');
                return;
            }

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
                document.getElementById('response').classList.remove('hidden');
                document.getElementById('dropdownSection').classList.remove('hidden');
                document.getElementById('responseData').textContent = JSON.stringify(data, null, 2);
            })
            .catch(error => console.error('Error:', error));
        }

        function filterResponse() {
            const data = JSON.parse(document.getElementById('responseData').textContent);
            const filter = Array.from(document.getElementById('responseFilter').selectedOptions).map(option => option.value);

            const filteredData = {};
            filter.forEach(key => {
                if (data[key]) {
                    filteredData[key] = data[key];
                }
            });

            // Update the display with the filtered data
            document.getElementById('responseData').textContent = JSON.stringify(filteredData, null, 2);
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
    
    # Filter only lowercase alphabets
    lowercase_alphabets = [char for char in alphabets if char.islower()]
    
    # Find the highest lowercase alphabet
    highest_lowercase_alphabet = [max(lowercase_alphabets)] if lowercase_alphabets else []

    response = {
        "is_success": True,
        "user_id": "Chereddy_Rahul",
        "email": "rahul.21bce9779@vitapstudent.ac.in",
        "roll_number": "21BCE9779",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet
    }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def get_bfhl():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run()
