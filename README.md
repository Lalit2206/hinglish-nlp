# hinglish-nlp 🇮🇳

A powerful NLP toolkit for **Hinglish** (Roman Hindi + English) text analysis.

[![PyPI version](https://badge.fury.io/py/hinglish-nlp.svg)](https://badge.fury.io/py/hinglish-nlp)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Installation

```bash
pip install hinglish-nlp
```

---

## Features

| Feature | Description |
|--------|-------------|
| ✅ Sentiment Analysis | Positive / Negative / Neutral / Mixed |
| ✅ Emotion Detection | Joy, Anger, Sadness, Fear, Surprise, Disgust |
| ✅ Sarcasm Detection | Pattern + contradiction based |
| ✅ Language Mix Detection | Hinglish vs English ratio |
| ✅ Transliteration | Roman Hindi → Devanagari |
| ✅ Batch Processing | Multiple texts at once |
| ✅ Key Phrase Extraction | Important phrases from text |
| ✅ Intensity Score | 0.0 to 1.0 scale |
| ✅ Confidence Score | How sure the model is |

---

## Usage

### Basic Sentiment Analysis
```python
from hinglish import analyze

result = analyze("yaar bahut mast movie thi!")
print(result["mood"])        # positive
print(result["emoji"])       # 😊
print(result["intensity"])   # 0.45
print(result["confidence"])  # 0.75
```

### Emotion Detection
```python
from hinglish import detect_emotion

emotions = detect_emotion("mujhe bahut gussa aa raha hai!")
print(emotions)  # {'anger': 0.35}

emotions = detect_emotion("aaj bahut khushi hui yaar!")
print(emotions)  # {'joy': 0.7}
```

### Sarcasm Detection
```python
from hinglish import is_sarcastic

result = is_sarcastic("haan bilkul, bahut accha hai na!!")
print(result)
# {'is_sarcastic': True, 'confidence': 0.6}
```

### Language Mix Detection
```python
from hinglish import detect_language

mix = detect_language("yaar ye movie bahut boring thi")
print(mix)
# {'hinglish': 0.5, 'english': 0.33, 'unknown': 0.17}
```

### Transliteration (Roman → Devanagari)
```python
from hinglish import transliterate

text = transliterate("mera naam lalit hai")
print(text)  # मेरा नाम ललित है
```

### Batch Processing
```python
from hinglish import analyze_batch

texts = [
    "yaar mast movie thi!",
    "bilkul bakwaas tha yaar",
    "theek thak tha, kuch khaas nahi"
]

results = analyze_batch(texts)
for r in results:
    print(r["mood"], r["emoji"])
# positive 😊
# negative 😠
# neutral  😐
```

### Full Analysis
```python
from hinglish import analyze

result = analyze("Phone ki battery toh bekar hai but camera mast hai")
print(result)
# {
#   'mood': 'mixed',
#   'intensity': 0.3,
#   'confidence': 0.75,
#   'emoji': '🤨',
#   'sentiment': 'mixed',
#   'key_phrases': ['Phone ki battery toh bekar hai but camera mast hai'],
#   'sarcasm': False,
#   'sarcasm_confidence': 0.0,
#   'language_mix': {'hinglish': 0.36, 'english': 0.55, 'unknown': 0.09},
#   'category': 'mixed',
#   'summary': 'A detailed Hinglish message expressing mixed sentiment...',
#   'emotions': {'disgust': 0.35},
#   'word_count': 11,
#   'positive_words_found': ['mast'],
#   'negative_words_found': ['bekar'],
#   'transliteration': 'Phone की battery तो bekar है but camera मस्त है'
# }
```

---

## Output Fields

| Field | Type | Description |
|-------|------|-------------|
| `mood` | str | positive / negative / neutral / mixed |
| `intensity` | float | 0.0 – 1.0 |
| `confidence` | float | 0.0 – 1.0 |
| `emoji` | str | Visual mood indicator |
| `sentiment` | str | Same as mood |
| `key_phrases` | list | Important phrases |
| `sarcasm` | bool | Is text sarcastic? |
| `sarcasm_confidence` | float | Sarcasm confidence score |
| `language_mix` | dict | hinglish / english / unknown ratio |
| `category` | str | praise / complaint / casual / mixed |
| `summary` | str | Short summary of the text |
| `emotions` | dict | Detected emotions with scores |
| `word_count` | int | Total word count |
| `positive_words_found` | list | Positive words detected |
| `negative_words_found` | list | Negative words detected |
| `transliteration` | str | Roman → Devanagari |

---

## Author

**Lalit** — [lalitpal2206](https://pypi.org/user/lalitpal2206/)

## License

MIT License