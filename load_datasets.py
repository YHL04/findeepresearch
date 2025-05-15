

import pandas as pd


def load_financebench():
    """
    Load Finance Bench according to instructions from its github.

    - financebench_id (int):            Unique identifier of the question
    - question (str):                   Question of interest
    - answer (str):                     Human-annotated gold answer
    - dataset_subset_label (str):       Label to identify in which data subset the question is present ("OPEN_SOURCE" or "CLOSED_SOURCE")
    - evidence (list[dict])             List of EvidenceDict's. 
    - justification (str)               Human-Annotated justification of the gold answer
    - question_type (str)               Type of Question: 'metrics-generated', 'domain-relevant', 'novel-generated' 
    - question_reasoning (str)          Reasoning Type needed to solve the question
    - domain_question_num (str)         ID of domain-relevant questions (`dg01` to `dg25`), "None" for 'metrics-generated' and 'novel-generated' questions
    - company (str)                     Company of Interest
    - doc_name (str)                    Unique Document Identifier. Format: {COMPANY}_{PERIOD}_{TYPE}. Some exceptions have the format {COMPANY}_{PERIOD}_{TYPE}_dated-{DATE}


    Each EvidenceDict contains four fields: 
        - "evidence_text" (str):            Extracted evidence text from annotators (sentence, paragraph or page) 
        - "evidence_doc_name" (str):        Unique Document Identifier of the relevant document containing the evidence
        - "evidence_page_num" (int):        Page number of the evidence text (ZERO-indexed)
        - "evidence_text_full_page" (str):  Full page extract containing the evidence text
    """
    df_questions = pd.read_json("datasets/financebench/financebench_open_source.jsonl", lines=True)
    # df_meta = pd.read_json("datasets/financebench/financebench_document_information.jsonl", lines=True)
    # df_full = pd.merge(df_questions, df_meta, on="doc_name")
    questions = df_questions['question'].tolist()
    evidence_text = [e for e in df_questions['evidence'].tolist()]
    evidence = []
    for e in evidence_text:
        concatenated = ""
        for e_ in e:
            concatenated += e_['evidence_text_full_page']
        evidence.append(concatenated)

    questions = [f"{q} {e}" for q, e in zip(questions, evidence)]

    return questions, df_questions['answer'].tolist()


def load_financebench_sections():
    """
    Load Finance Bench according to instructions from its github and partition them according to
    metrics-generated, domain-relevant, and novel-generated.
    """
    df_questions = pd.read_json("datasets/financebench/financebench_open_source.jsonl", lines=True)
    # df_meta = pd.read_json("datasets/financebench/financebench_document_information.jsonl", lines=True)
    # df_full = pd.merge(df_questions, df_meta, on="doc_name")

    metrics_generated = df_questions[df_questions['metrics-generated'] == 'metrics-generated']
    domain_relevant = df_questions[df_questions['domain-relevant'] == 'domain-relevant']
    novel_generated = df_questions[df_questions['novel-generated'] == 'novel-generated']

    df_sections = {
        'metrics-generated': (metrics_generated['question'].tolist(), metrics_generated['answer'].tolist()),
        'domain-relevant': (domain_relevant['question'].tolist(), domain_relevant['answer'].tolist()),
        'novel-generated': (novel_generated['question'].tolist(), novel_generated['answer'].tolist()),
    }

    return df_sections


def load_finben():
    """
    Load FinBen, need to request access. Not implemented.
    """
    pass


if __name__ == "__main__":
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    print(load_financebench())

