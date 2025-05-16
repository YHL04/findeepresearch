

import threading

from openai import OpenAI
from keys import OPENAI_API_KEY, DEEPSEEK_API_KEY


openai_client = OpenAI(api_key=OPENAI_API_KEY)
deepseek_client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")


def send_query_gpt4(query):
    response = openai_client.responses.create(
        model="gpt-4",
        input=query
    )

    return response.output_text


def send_query_gpt4o(query):
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": query
            }
        ]
    )

    return response.choices[0].message.content


def send_query_gpto1(query):
    response = openai_client.chat.completions.create(
        model="o1",
        messages=[
            {
                "role": "user",
                "content": query
            }
        ]
    )

    return response.choices[0].message.content


def send_query_gpto3(query):
    response = openai_client.chat.completions.create(
        model="o3",
        messages=[
            {
                "role": "user",
                "content": query
            }
        ]
    )

    return response.choices[0].message.content


def send_query_deepseekv3(query):
    response = deepseek_client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "user",
                "content": query
            }
        ]
    )

    return response.choices[0].message.content 


def send_query_deepseekr1(query):
    response = deepseek_client.chat.completions.create(
        model="deepseek-reasoner",
        messages=[
            {
                "role": "user",
                "content": query
            }
        ]
    )

    return response.choices[0].message.content 


def send_query(query, model="gpt-4"):
    """
    Args:
        query: A string query
        model: The model to answer the query
    
    Returns:
        output: An answer string query
    """
    if model == "gpt-4":
        return send_query_gpt4(query)
    elif model == "gpt-4o":
        return send_query_gpt4o(query)
    elif model == "gpt-o1":
        return send_query_gpto1(query)
    elif model == "gpt-o3":
        return send_query_gpto3(query)
    elif model == "deepseek-v3":
        return send_query_deepseekv3(query)
    elif model == "deepseek-r1":
        return send_query_deepseekr1(query)
    else:
        raise Exception("Model not in list.")


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

    response_mini = openai_client.chat.completions.create(
        model="o1",
        messages=[
            {
                "role": "user",
                "content": "Write a Python script that takes a matrix represented as a string with format '[1,2],[3,4],[5,6]' and prints the transpose in the same format."
            },
            {
                "role": "user",
                "content": "Hello World."
            },
        ]
    )
    print(response_mini)

    # print(send_query("Hello World"))
    # print(send_queries(["Howdy!", "Bye!"]))
    # print(send_queries_parallel(["Howdy!", "Bye!"]))
