

import time

from load_datasets import load_financebench
from query import send_query, send_queries, send_queries_parallel
from metrics import calc_bertscore, calc_factscore


def benchmark_financebench(model, debug=True):
    questions, answers = load_financebench()
    if debug: questions, answers = questions[:5], answers[:5]

    preds = send_queries_parallel(questions, model)

    print(f"FinanceBench ({model})")
    print(calc_bertscore(preds, answers))
    # print(calc_factscore(preds, answers))


def benchmark_finben():
    return None


def benchmark_finqa():
    return None


def benchmark_docfinqa():
    return None


def main():
    start = time.time()
    print(benchmark_financebench('gpt-4'))
    # print(benchmark_financebench('gpt-4o'))
    print(f"Total Time: {time.time()-start}")

if __name__ == "__main__":
    main()

