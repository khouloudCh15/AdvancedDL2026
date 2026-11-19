# From Lab 1 to your final project

> Adapt the details to your actual project brief — this page maps *today's skills* to *project milestones* so nothing you learn is wasted.

## 1 · What today gave you, and where it reappears
| Lab skill | Where you will need it in the final project |
|---|---|
| Browse the Hub, read a model card, check the licence | **Model selection & justification** (a required section in any serious report) |
| `pipeline(...)` in one line | **Baseline in 10 minutes** — always start here before anything fancy |
| Tokenizer / tensors / logits | **Debugging**: why was this input mis-classified? Truncation? Token budget? Language? |
| Task heads (classification, token, MLM, embeddings) | Choosing the *right formulation* for your task |
| Embeddings + cosine search | Retrieval, deduplication, clustering, and the **R in RAG** later in the course |
| Evaluation by *tag / slice*, confident errors | The evaluation chapter: **per-slice metrics and error analysis**, not one global accuracy |
| Gradio `Interface` / `Blocks` | The **demo** you present; also a user-testing tool |
| Exported `textlab_app.py` + `requirements.txt` | A **reproducible** deliverable the grader can run |

## 2 · A strong project has six parts
1. **Task & users** — one sentence: *who* does *what* with the output? What is a costly mistake?
2. **Data** — source, size, licence, how you split it, what is *not* in it.
3. **Baseline** — a pipeline or zero-shot model, evaluated honestly (today's Part A).
4. **Improvement** — one or two *controlled* changes (a better model, fine-tuning, prompt/template, threshold, retrieval…) with the same test set.
5. **Evaluation** — metrics **per slice**, confident errors, a statement about uncertainty (small n!).
6. **Interface & limits** — a working app, plus a *"when not to use this"* section.

## 3 · Starter ideas (all doable with today's tools)
| Idea | Models | Evaluation to show |
|---|---|---|
| **Multilingual support-ticket router** | zero-shot (NLI) vs fine-tuned small BERT, language ID | accuracy per language and per class; cost of a mis-route |
| **Domain-specific semantic search** (course notes, legal clauses, FAQs) | MiniLM-style embeddings (+ reranker later) | recall@k on questions you write yourself; failure cases |
| **Review-mining dashboard** | sentiment + NER + emotion on a public review dataset | agreement between models; slices by product/length |
| **Model-comparison tool** | 2–3 models on one task, side by side in Gradio | disagreement analysis; speed vs quality trade-off |
| **Bias & robustness probe** | masked-LM / classifier under perturbations (negation, typos, names) | change in prediction rate under each perturbation |

## 4 · Decisions to make before the next session
- [ ] A task and a user (one sentence)
- [ ] Two candidate datasets (and their licences)
- [ ] One baseline model from the Hub (and its licence)
- [ ] How you will measure success *before* you build
- [ ] A shared repo with `README.md`, `requirements.txt`, `notebooks/`, `app/`

## 5 · Common pitfalls (seen every year)
* **Evaluating on the data you tuned on.** Freeze a test set first.
* **One global accuracy.** Report per slice; 90 % overall can hide 40 % on a minority group.
* **Reporting without baselines.** "87 %" means nothing without "versus 85 % for the zero-shot baseline".
* **Ignoring licences and data privacy.** Check before you build on it.
* **Spending the whole project on the UI.** A simple, correct, well-evaluated app beats a beautiful, untested one.
