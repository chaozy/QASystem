from flask import Flask
from flask import request
from flask import jsonify

from . import query_Handler
from . import file_upload
from . import pre_process

app = Flask(__name__)

@app.route('/', methods=['POST'])
def upload():
    app.logger.info("Receiving a POST request")
    file = request.files['file']

    app.logger.info("Handling file: " + file.name)
    if not file:
        raise Exception("Document is missing")

    document_store = file_upload.file_upload(file)

    pre_process.process(document_store)
    return "successfully uploaded"

@app.route('/', methods=['GET'])
def query():
    app.logger.info("Receiving a POST request")
    query = request.args.get("query")
    app.logger.info("Handling query: " + query)
    if not query:
        raise Exception("Query is missing")

    if query == "END":
        query_Handler.pipe = None
        return "successfully terminated"
    else:
        res = query_Handler.processQuery(query)
        app.logger.info(res)
        res = res['answers']
        return jsonify(res)