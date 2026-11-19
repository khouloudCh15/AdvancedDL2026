# Take-home assignment — Lab 1 &nbsp;·&nbsp; "Evaluate it, extend it, critique it"


> **Why this assignment.** A demo shows a model *can* work. Your final project will be judged on *how well, for whom, and at what risk*.
> This is the first rehearsal: measure a model honestly, ship it in an interface, and read its documentation critically.

## Deliverables (one `.zip` or Git repo)
| # | Deliverable | Points |
|---|---|---|
| 1 | `05_homework_starter.ipynb` **completed, with outputs** (TODO A1, A2, B1 + both written analyses) | 35 |
| 2 | **TextLab extension** — one new tab/feature of your choice (menu below), as a working `textlab_app.py` | 30 |
| 3 | **Model-card critique** — 1 page (Part C of the notebook) | 15 |
| 4 | **Failure log** — 5 inputs that broke *your app* (not only the model), what you did about each | 10 |
| 5 | Repo hygiene — `README.md` with run instructions + a screenshot, `requirements.txt`, no hard-coded absolute paths | 10 |
| ★ | Bonus — deploy to a free **Hugging Face Space** and include the URL | +5 |

## 2 · TextLab extension — choose ONE
| Option | Model / idea | What makes it non-trivial |
|---|---|---|
| **Emotion** | `bhadresh-savani/distilbert-base-uncased-emotion` (6 emotions) | compare with sentiment on the same text; discuss when they disagree |
| **Question answering** | `distilbert/distilbert-base-cased-distilled-squad` | paste a paragraph + question → highlighted answer span with confidence; handle "no answer" |
| **Batch mode** | any of today's models | upload a CSV → table of predictions → downloadable CSV + class-balance bar chart |
| **Compare mode** | two sentiment models side by side | show where they *disagree* and flag low-confidence cases |
| **Semantic search over your own text** | `all-MiniLM-L6-v2` (from Notebook 2) | upload a `.txt`, chunk it, return top-k passages with scores; justify your chunk size |

**Requirements for every option:** (a) the logic lives in a **plain function** with a docstring and at least **3 assertions/tests**;
(b) invalid or empty input raises `gr.Error` with a helpful message; (c) at least 3 `examples`; (d) the model's **licence** is stated in your README;
(e) the app runs from a terminal with `python textlab_app.py` on a clean environment.

## 3 · Model-card critique (1 page)
For **both** models of Part B, answer: training data and languages · intended use and stated limitations · licence and whether commercial use is allowed ·
evidence of evaluation (what metrics, on what data?) · what is **missing** from the card that you would need before deploying · your verdict
(*ship / ship with guardrails / do not ship*) for one concrete scenario you describe in one sentence.

## 4 · Failure log
A table with columns: *input · what happened · root cause (model / tokenization / UI / my code) · fix or decision (e.g. warn the user, change threshold, reject input)*.
Good entries show you **diagnosed** the cause, not just noticed the symptom.

## Grading rubric (applies to items 1–3)
| | Excellent | Adequate | Weak |
|---|---|---|---|
| **Correctness** | all self-checks pass; metrics reproducible | minor errors | self-checks fail |
| **Insight** | explains *why* errors happen with evidence from tokens / data / model card | describes errors, little explanation | lists numbers only |
| **Honesty** | states limits, uncertainty, small-sample caveat (n = 48!) | some caveats | over-claims |
| **Clarity** | a classmate could reproduce it from your README | mostly clear | missing steps |

## Rules
Discuss ideas freely; **write your own code and analysis**. If you use an AI assistant or any online code, **say so** in your README
(what for, which parts) — you must be able to explain every line in the oral check. 

## Hints
* Evaluate **before** you tweak: freeze the test set, change one thing at a time.
* With only 48 examples, a difference of 2–3 points is *noise* — say so.
* Typical trap in Part B: counting `NEUTRAL` as wrong **and** then claiming model B is "worse" — report both views.
