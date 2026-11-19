#!/usr/bin/env python
"""Run this FIRST:  python check_setup.py
Checks your Python packages, your connection to the Hugging Face Hub, which lab models are already
downloaded, and runs one tiny model so you know everything works."""
import importlib, platform, sys, urllib.request

MODELS = [
    "distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    "dslim/distilbert-NER",
    "distilbert/distilbert-base-uncased",
    "typeform/distilbert-base-uncased-mnli",
    "sentence-transformers/all-MiniLM-L6-v2",
]
ok = True
print(f"Python {platform.python_version()} on {platform.system()} {platform.machine()}")
if sys.version_info < (3, 9):
    print("❌ Python 3.9+ required"); ok = False

print("\nPackages")
for mod, label in [("torch", "torch"), ("transformers", "transformers"), ("gradio", "gradio"),
                   ("huggingface_hub", "huggingface_hub"), ("pandas", "pandas"),
                   ("sklearn", "scikit-learn"), ("matplotlib", "matplotlib")]:
    try:
        m = importlib.import_module(mod)
        print(f"  ✅ {label:16s} {getattr(m, '__version__', '?')}")
    except Exception as e:
        print(f"  ❌ {label:16s} missing  ->  pip install -r requirements.txt"); ok = False

if not ok:
    sys.exit("\nFix the problems above, then run this script again.")

import torch
print(f"\nCompute: {'GPU (CUDA)' if torch.cuda.is_available() else 'CPU'}  (CPU is fine for this lab)")

print("\nHugging Face Hub")
online = True
try:
    urllib.request.urlopen("https://huggingface.co", timeout=6)
    print("  ✅ reachable")
except Exception:
    online = False
    print("  ⚠️  not reachable — models must already be in your local cache (see prefetch_models.py)")

from huggingface_hub import try_to_load_from_cache
print("\nLab models in your local cache")
missing = []
for repo in MODELS:
    cached = isinstance(try_to_load_from_cache(repo, "config.json"), str)
    print(f"  {'✅' if cached else '⬇️ '} {repo}")
    if not cached: missing.append(repo)
if missing:
    print(f"\n  {len(missing)} model(s) will download on first use (~250 MB each). To get them all now:  python prefetch_models.py")
    if not online:
        sys.exit("❌ offline and models missing — ask the instructor for the offline model pack.")

print("\nSmoke test")
from transformers import pipeline
clf = pipeline("sentiment-analysis", model=MODELS[0])
print("  ", clf("This lab is going to be fun!")[0])
print("\n✅ All good — open JupyterLab:  jupyter lab")
