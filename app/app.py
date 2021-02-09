from flask import Flask
from flask import request
from flask import jsonify

from . import bootLoader

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    app.logger.info("Receiving a request")
    if (request.method == "POST"):
        query = request.args.get("query")
        file = request.files['file']
        app.logger.info(query)
        app.logger.info(file.name)
        if not file or not query:
            raise Exception("Missing doc or query")

        filePath  = '/tmp/tmpDoc'
        if (file.filename.endswith('.pdf')):
            filePath += '.pdf'
        elif file.filename.endswith('.txt'):
            filePath += '.txt'
        elif file.filename.endswtih('.doc'):
            filePath += '.doc'

        f = open(filePath, 'wb+')
        f.write(file.read())
        f.close()

        searchResult = bootLoader.run(filePath, query)
        ans = searchResult['answers']
        return jsonify(ans)
    return "hihi"

if __name__ == "__main__":
    app.run(debug=True, port=5000)