import os
#  Disabling parallelism to avoid deadlocks
os.environ["TOKENIZERS_PARALLELISM"] = "false"

pipe = None

# The preprocessing of document is needed, which will assign values to pipe
def processQuery(query):
    if pipe is None:
        raise Exception("Preprocessing of document is needed!")
    queryResult = pipe.run(query=query, top_k_retriever=3, top_k_reader=5)
    return queryResult