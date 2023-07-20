from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/capture', methods=['POST'])
def capture():
    data = request.json
    image_data = data.get('image_data', None)

    # Here, you can process and save the image data as required.
    # For simplicity, we'll just print the image data.
    print(image_data)

    # You can return a response to the client if needed.
    return jsonify({'message': 'Image received successfully'})


if __name__ == '__main__':
    app.run(debug=True)
