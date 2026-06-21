"""
hinglish-nlp
============
A powerful NLP toolkit for Hinglish (Roman Hindi + English) text analysis.

Quick start
-----------
>>> from hinglish import analyze
>>> result = analyze("yaar bahut mast movie thi!")
>>> print(result["mood"])       # positive
>>> print(result["emotions"])   # {'joy': 0.35}

>>> from hinglish import analyze_batch, transliterate, detect_emotion
"""

from .analyzer import (
    analyze,
    analyze_batch,
    transliterate,
    detect_language,
    detect_emotion,
    is_sarcastic,
    HinglishAnalysis,
    HinglishAnalyzer,
)

__version__ = "0.2.0"
__author__ = "Lalit"
__all__ = [
    "analyze",
    "analyze_batch",
    "transliterate",
    "detect_language",
    "detect_emotion",
    "is_sarcastic",
    "HinglishAnalysis",
    "HinglishAnalyzer",
]