#!/usr/bin/env python
"""Download every model used in the lab ahead of time (do this on good Wi-Fi, NOT in class).
    python prefetch_models.py            # the 5 lab models  (~1.2 GB)
    python prefetch_models.py --homework # + the multilingual model for the take-home notebook (~0.7 GB)
Models land in the standard Hugging Face cache (~/.cache/huggingface). To work fully offline afterwards:
    export HF_HUB_OFFLINE=1      (Windows PowerShell:  $env:HF_HUB_OFFLINE = 1)"""
import sys
from huggingface_hub import HfApi, snapshot_download

LAB = [
    "distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    "dslim/distilbert-NER",
    "distilbert/distilbert-base-uncased",
    "typeform/distilbert-base-uncased-mnli",
    "sentence-transformers/all-MiniLM-L6-v2",
]
HOMEWORK = ["nlptown/bert-base-multilingual-uncased-sentiment"]
SKIP = ["*.h5", "*.msgpack", "*.ot", "*.onnx", "onnx/*", "openvino/*", "*.tflite", "*.mlmodel", "*.gguf",
        "tf_model*", "flax_model*", "rust_model*", "coreml/*"]

api = HfApi()
for repo in LAB + (HOMEWORK if "--homework" in sys.argv else []):
    files = [s.rfilename for s in api.model_info(repo).siblings]
    ignore = list(SKIP)
    if "model.safetensors" in files:
        ignore += ["*.bin"]            # we only need one copy of the weights
    print(f"⬇️  {repo} ...", flush=True)
    path = snapshot_download(repo, ignore_patterns=ignore)
    print(f"   ✅ {path}")
print("\nDone. Verify with:  python check_setup.py")
