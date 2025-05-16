

import time

from load_datasets import load_financebench
from query import send_queries_parallel
from metrics import calc_bertscore, calc_factscore


def benchmark_financebench(model, debug=True):
    questions, answers = load_financebench()
    if debug: questions, answers = questions[:3], answers[:3]

    preds = send_queries_parallel(questions, model)
    # if debug:
    #     print(questions)
    #     print(preds)    

    if None in preds:
        raise Exception("None found in predictions.")

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
    print(benchmark_financebench('gpt-4o'))
    print(benchmark_financebench('gpt-o1'))
    print(benchmark_financebench('gpt-o3'))
    benchmark_financebench('deepseek-v3')
    benchmark_financebench('deepseek-r1')
    print(f"Total Time: {time.time()-start}")

if __name__ == "__main__":
    main()

