# Lab 1 — From `pipeline()` to a working NLP app
**Transformers · Hugging Face · Gradio · small BERT models** &nbsp;|&nbsp; 2 hours &nbsp;|&nbsp; Master's level

By the end of this lab you will have built **TextLab**, a five-tab web app (sentiment, named entities, fill-the-blank,
zero-shot classification, semantic FAQ search) from small BERT-family models — and you will know what happens inside each
`pipeline()` call. It is also the skeleton of your **final project**.

## Schedule
| Notebook | What you do |
|---|---|
| *(setup)* | `python check_setup.py`, demo of the finished app |
| `01_hf_pipelines` | Hub & licences, four pipelines, **break the model**, zero-shot templates |
| `02_under_the_hood` | tokenizer → tensors → logits, rebuild a pipeline, embeddings & semantic search, masked LM |
| `03_gradio_basics` | `Interface`, `Label`, `HighlightedText`, `Blocks` & tabs, your own interface |
| `04_textlab_app` | write 5 functions, self-test, launch the app, export `textlab_app.py` |
|take-home assignment |

Take-home: `notebooks/05_homework_starter.ipynb` + `assignment/ASSIGNMENT.md`. How this feeds your final project: `assignment/FINAL_PROJECT_BRIDGE.md`.

## Quick start (do this *before* the lab, on good Wi-Fi)
```bash
python -m venv .venv && source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python prefetch_models.py                                 # downloads ~1.2 GB of models once
python check_setup.py                                     # must end with "All good"
jupyter lab
```
**No local install?** Use Google Colab: upload the `notebooks/` and `data/` folders, run the commented `!pip install` line at the top of each notebook,
and restart the runtime once. CPU is enough for everything in this lab.

## How the notebooks work
* Cells marked **TODO n** are yours. Cells with `assert` are **self-checks** — a green ✅ means you are right.
* Work in order; every notebook ends with a *Checkpoint* that tells you what you should be able to explain.
* Stuck for more than 5 minutes? Ask a neighbour, then the instructor. Finished early? Do the ⭐ bonus cells.

## Folder map
```
notebooks/     01–04 for the lab, 05 take-home
data/          mini_reviews.csv (48 labelled reviews, used in the take-home)
assignment/    ASSIGNMENT.md, FINAL_PROJECT_BRIDGE.md
check_setup.py, prefetch_models.py, requirements.txt
```

## Troubleshooting
| Symptom | Fix |
|---|---|
| `Port 7860 is in use` / old app still running | run `gr.close_all()` in a cell, or restart the kernel |
| Very slow first run | the model is downloading (≈250 MB each); later runs are instant |
| `ModuleNotFoundError` | the notebook kernel is not your venv: `python -m ipykernel install --user --name lab1` then pick it in Jupyter |
| `Passed CPU tensor to MPS op` (Mac) | pass `device=-1` to `pipeline(...)`, or `export PYTORCH_ENABLE_MPS_FALLBACK=1` |
| `OSError: ... couldn't connect to huggingface.co` | offline: models must be pre-downloaded, then `export HF_HUB_OFFLINE=1` |
| Colab: gradio link does not appear | use `app.launch(share=True)` |
