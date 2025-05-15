

import threading

from openai import OpenAI
from keys import OPENAI_API_KEY, DEEPSEEK_API_KEY


openai_client = OpenAI(api_key=OPENAI_API_KEY)
deepseek_client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")


def send_query(query, model="gpt-4"):
    """
    Args:
        query: A string query
        model: The model to answer the query
    
    Returns:
        output: An answer string query
    """
    if model in ("gpt-4", "GPT-4o", "GPT-o1", "GPT-o3"):
        client = openai_client
    elif model in ("deepseek-v3", "deepseek-r1"):
        client = deepseek_client
    else:
        raise Exception("Model is not in the list")

    response = client.responses.create(
        model=model,
        input=query
    )

    return response.output_text


def send_queries(queries, model='gpt-4'):
    return [send_query(query, model) for query in queries]


def send_queries_parallel(queries, model='gpt-4'):
    def send_query_thread(i, query, preds, model):
        preds[i] = send_query(query, model)

    threads = []
    preds = [None] * len(queries)
    for i, query in enumerate(queries):
        thread = threading.Thread(target=send_query_thread, args=(i, query, preds, model))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return preds


if __name__ == "__main__":
    print(send_query("Hello World"))
    print(send_queries(["Howdy!", "Bye!"]))
    print(send_queries_parallel(["Howdy!", "Bye!"]))
