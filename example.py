from hinglish import analyze

texts = [
    "Yaar ye movie bahut bakwaas thi",
    "Bhai aaj mood bahut mast hai, party karte hain!",
    "Phone ki battery toh bekar hai but camera mast hai"
]

for text in texts:
    print(f"\nText: {text}")
    result = analyze(text)
    print(result)