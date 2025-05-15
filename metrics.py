

from evaluate import load


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

