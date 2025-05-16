

from evaluate import load
from query import send_queries_parallel


def query_answer(preds, answers):
    queries = []
    for pred, answer in zip(preds, answers):
        prompt = f"PRED: {pred} ANSWER: {answer}. Given the predictions and answers" \
                  "please tell me if both responses convey the same information. Only reply" \
                  "1 (for correct) and 0 (for incorrect). Do not say anything like 'Sure, let me" \
                  "do it for you'. Use your best judgement."
        queries.append(prompt)
    

def calc_bertscore(preds, answers):
    bertscore = load('bertscore')
    results = bertscore.compute(predictions=preds, references=answers, lang="en")

    results = {
        'precision': sum(results['precision']) / len(results['precision']),
        'f1'       : sum(results['f1']) / len(results['f1']),
        'recall'   : sum(results['recall']) / len(results['recall']),
    }

    return results


def calc_perplexity(preds, answers):
    pass


def calc_factscore(preds, answers):
    pass

