from hinglish import (
    analyze,
    analyze_batch,
    transliterate,
    detect_language,
    detect_emotion,
    is_sarcastic,
)

print("=" * 55)
print("       hinglish-nlp — Feature Demo")
print("=" * 55)

# ── 1. Basic Analysis ──────────────────────────────
print("\n📌 1. BASIC SENTIMENT ANALYSIS")
texts = [
    "Yaar ye movie bahut bakwaas thi",
    "Bhai aaj mood bahut mast hai, party karte hain!",
    "Phone ki battery toh bekar hai but camera mast hai",
    "haan bilkul, bahut accha hai na!!",
]
for text in texts:
    r = analyze(text)
    print(f"\n  Text      : {text}")
    print(f"  Mood      : {r['mood']} {r['emoji']}")
    print(f"  Intensity : {r['intensity']}  |  Confidence: {r['confidence']}")
    print(f"  Category  : {r['category']}")

# ── 2. Emotion Detection ───────────────────────────
print("\n" + "=" * 55)
print("📌 2. EMOTION DETECTION")
emotion_texts = [
    "mujhe bahut gussa aa raha hai!",
    "aaj bahut khushi hui yaar!",
    "dil toot gaya bhai, bahut dukh hai",
    "seriously?! yeh sach mein hua?",
]
for text in emotion_texts:
    emotions = detect_emotion(text)
    print(f"\n  Text    : {text}")
    print(f"  Emotions: {emotions}")

# ── 3. Sarcasm Detection ───────────────────────────
print("\n" + "=" * 55)
print("📌 3. SARCASM DETECTION")
sarcasm_texts = [
    "haan bilkul, bahut accha hai na!!",
    "yaar mast movie thi ekdum!",
    "great yaar, bilkul sahi kiya",
]
for text in sarcasm_texts:
    result = is_sarcastic(text)
    print(f"\n  Text      : {text}")
    print(f"  Sarcastic : {result['is_sarcastic']}  |  Confidence: {result['confidence']}")

# ── 4. Language Detection ──────────────────────────
print("\n" + "=" * 55)
print("📌 4. LANGUAGE MIX DETECTION")
lang_texts = [
    "yaar ye movie bahut boring thi",
    "This movie was absolutely fantastic and amazing",
    "bhai the battery is bekar but camera is mast",
]
for text in lang_texts:
    mix = detect_language(text)
    print(f"\n  Text : {text}")
    print(f"  Mix  : {mix}")

# ── 5. Transliteration ─────────────────────────────
print("\n" + "=" * 55)
print("📌 5. TRANSLITERATION (Roman → Devanagari)")
roman_texts = [
    "mera naam lalit hai",
    "yaar bahut mast movie thi",
    "aaj bahut khushi hui",
]
for text in roman_texts:
    dev = transliterate(text)
    print(f"\n  Roman     : {text}")
    print(f"  Devanagari: {dev}")

# ── 6. Batch Processing ────────────────────────────
print("\n" + "=" * 55)
print("📌 6. BATCH PROCESSING")
batch = [
    "yaar mast movie thi!",
    "bilkul bakwaas tha yaar",
    "theek thak tha, kuch khaas nahi",
    "bahut gussa aa raha hai mujhe",
]
results = analyze_batch(batch)
print()
for text, r in zip(batch, results):
    print(f"  {r['emoji']}  [{r['mood']:8s}]  {text}")

print("\n" + "=" * 55)
print("✅ Demo complete!")