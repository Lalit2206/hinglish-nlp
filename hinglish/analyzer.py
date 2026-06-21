from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
import re


#  LEXICON
POSITIVE_WORDS = {
    # General positive
    "mast", "badiya", "zabardast", "awesome", "superb", "love", "best",
    "perfect", "great", "achha", "accha", "nice", "kamaal", "shandaar",
    "dhamaka", "bindaas", "jhakaas", "wah", "waah", "solid", "killer",
    "dope", "lit", "fire", "too good", "ekdum sahi", "full mast",
    "khush", "khushi", "maza", "party", "celebrate", "lajawaab",
    "shaandaar", "gazab", "jalwa", "badhiya", "outstanding", "excellent",
    "wonderful", "fantastic", "brilliant", "amazing", "superb", "fabulous",
    "incredible", "marvelous", "splendid", "terrific", "spectacular",
    "magnificent", "glorious", "superb", "lovely", "beautiful", "gorgeous",
    "stunning", "charming", "delightful", "enjoyable", "fun", "exciting",
    "thrilling", "refreshing", "satisfying", "pleasing", "impressive",
    "remarkable", "extraordinary", "phenomenal", "exceptional", "top",
    "sahi", "bilkul sahi", "dum", "dum hai", "kya baat", "ekdum",
    "maja", "maja aaya", "mst", "bdhiya", "zbrdsst", "kmaal",
    "happy", "glad", "joyful", "cheerful", "content", "pleased",
    "grateful", "thankful", "blessed", "fortunate", "lucky",
    "proud", "confident", "hopeful", "optimistic", "positive",
    "energetic", "enthusiastic", "passionate", "motivated", "inspired",
    "relaxed", "peaceful", "calm", "comfortable", "satisfied",
}

NEGATIVE_WORDS = {
    # General negative
    "bakwaas", "bekar", "kharaab", "worst", "faltu", "garbage",
    "disappoint", "boring", "time waste", "bekaar", "ganda", "bura",
    "kharab", "wahiyat", "forma", "forma", "useless", "pathetic",
    "terrible", "horrible", "awful", "dreadful", "atrocious", "abysmal",
    "disgusting", "revolting", "repulsive", "nasty", "vile", "foul",
    "lousy", "poor", "inferior", "substandard", "inadequate", "deficient",
    "flawed", "faulty", "broken", "damaged", "ruined", "destroyed",
    "failed", "failure", "disaster", "catastrophe", "tragedy", "mess",
    "problem", "issue", "trouble", "difficulty", "challenge", "obstacle",
    "frustrating", "annoying", "irritating", "aggravating", "infuriating",
    "disappointing", "unsatisfying", "dissatisfying", "displeasing",
    "sad", "unhappy", "miserable", "depressed", "gloomy", "melancholy",
    "upset", "distressed", "troubled", "worried", "anxious", "stressed",
    "angry", "furious", "enraged", "outraged", "livid", "irate",
    "disgusted", "repelled", "appalled", "horrified", "shocked",
    "bored", "dull", "tedious", "monotonous", "repetitive", "bland",
    "nahi", "mat", "bandh", "band", "chup", "shut",
}

INTENSIFIERS = {
    "bahut", "bohot", "bht", "very", "super", "ekdum", "bilkul",
    "sabse", "itna", "utna", "kitna", "zyada", "boht", "bhot",
    "extremely", "incredibly", "absolutely", "totally", "completely",
    "utterly", "highly", "deeply", "strongly", "severely", "greatly",
    "tremendously", "enormously", "immensely", "vastly", "profoundly",
}

EMOTION_LEXICON = {
    "anger": {
        "gussa", "ghussa", "pagal", "bakwas", "beizzati", "insult",
        "angry", "furious", "rage", "mad", "irritated", "annoyed",
        "frustrated", "outraged", "livid", "enraged", "irate",
        "aggressive", "hostile", "violent", "hateful", "resentful",
        "jalega", "jala", "jalao", "maar", "marunga", "toot",
    },
    "joy": {
        "khushi", "maza", "party", "celebrate", "mast", "khush",
        "happy", "joyful", "cheerful", "delighted", "elated", "ecstatic",
        "thrilled", "excited", "glad", "pleased", "content", "satisfied",
        "blissful", "euphoric", "overjoyed", "jubilant", "radiant",
        "maja", "maja aaya", "bindaas", "dhamaal", "moj", "masti",
    },
    "sadness": {
        "dukh", "rona", "bura", "miss", "akela", "dard", "toot",
        "sad", "unhappy", "miserable", "depressed", "gloomy", "melancholy",
        "sorrowful", "heartbroken", "devastated", "grief", "mourning",
        "lonely", "isolated", "abandoned", "rejected", "hurt", "pain",
        "cry", "tears", "weep", "sob", "lament", "grieve",
        "roya", "rote", "aansu", "tadap", "bichar",
    },
    "surprise": {
        "kya", "seriously", "matlab", "no way", "sach", "sachchi",
        "surprised", "shocked", "astonished", "amazed", "stunned",
        "bewildered", "dumbfounded", "flabbergasted", "astounded",
        "unexpected", "unbelievable", "incredible", "wow", "omg",
        "arre", "arrey", "oye", "yaar sach", "are bhai",
    },
    "fear": {
        "dar", "darr", "tension", "problem", "mushkil", "dara",
        "afraid", "scared", "frightened", "terrified", "horrified",
        "anxious", "nervous", "worried", "stressed", "panicked",
        "dread", "terror", "phobia", "paranoid", "threatened",
        "darr gaya", "darta hun", "daro mat",
    },
    "disgust": {
        "yuck", "chhi", "ganda", "ulti", "bura laga", "nafrat",
        "disgusting", "revolting", "repulsive", "nasty", "vile",
        "gross", "horrible", "awful", "terrible", "dreadful",
        "loathsome", "abhorrent", "detestable", "despicable",
        "hate", "hatred", "abhor", "detest", "despise", "loathe",
    },
}

SARCASM_PATTERNS = [
    r"bahut\s+acch[ao]\s+hai\s*na",
    r"haan\s+bilkul",
    r"wah\s+kya\s+baat",
    r"!{2,}",
    r"(?:oh\s+)?sure\s+yaar",
    r"bilkul\s+sahi\s+(?:hai|tha|thi)",
    r"kitna\s+(?:accha|mast|badiya)\s+(?:hai|tha|thi)\s*(?:na|yaar)?",
    r"great\s+yaar",
    r"very\s+nice\s+(?:yaar|bhai)",
]

HINGLISH_WORDS = {
    "yaar", "bhai", "mein", "hai", "toh", "kya", "nahi", "haan",
    "abhi", "kal", "aaj", "phir", "kab", "kahan", "kyun", "kaisa",
    "accha", "achha", "theek", "sahi", "matlab", "samjha", "dekho",
    "suno", "bolo", "jao", "aao", "ruko", "chalo", "batao",
    "mast", "badiya", "zabardast", "bindaas", "dhamaka", "kamaal",
    "bilkul", "ekdum", "bahut", "bohot", "itna", "zyada",
    "ghar", "dost", "paisa", "kaam", "time", "baat", "cheez",
    "log", "aadmi", "ladka", "ladki", "bachha", "mama", "papa",
    "khana", "pani", "chai", "coffee", "movie", "gana", "game",
    "phone", "laptop", "net", "wifi", "app", "online",
    "arre", "arrey", "oye", "yaar", "bhai", "boss", "dude",
}

TRANSLITERATION_MAP = {
    "mera": "मेरा", "tera": "तेरा", "uska": "उसका", "hamara": "हमारा",
    "naam": "नाम", "ghar": "घर", "dost": "दोस्त", "pyaar": "प्यार",
    "khushi": "खुशी", "dukh": "दुःख", "zindagi": "ज़िंदगी",
    "yaar": "यार", "bhai": "भाई", "kya": "क्या", "hai": "है",
    "nahi": "नहीं", "haan": "हाँ", "accha": "अच्छा", "achha": "अच्छा",
    "bahut": "बहुत", "bohot": "बहुत", "mast": "मस्त",
    "badiya": "बढ़िया", "zabardast": "ज़बरदस्त", "kamaal": "कमाल",
    "theek": "ठीक", "sahi": "सही", "galat": "गलत",
    "khana": "खाना", "pani": "पानी", "chai": "चाय",
    "aaj": "आज", "kal": "कल", "abhi": "अभी",
    "main": "मैं", "mein": "में", "toh": "तो",
    "kaam": "काम", "paisa": "पैसा", "time": "टाइम",
    "phone": "फ़ोन", "movie": "मूवी", "gana": "गाना",
    "dil": "दिल", "aankhein": "आँखें", "haath": "हाथ",
    "gussa": "गुस्सा", "dar": "डर", "khauf": "ख़ौफ़",
    "hasna": "हँसना", "rona": "रोना", "bolna": "बोलना",
    "sunna": "सुनना", "dekhna": "देखना", "jaana": "जाना",
    "aana": "आना", "karna": "करना", "rehna": "रहना",
}


#  DATACLASS
@dataclass
class HinglishAnalysis:
    mood: str
    intensity: float
    confidence: float
    emoji: str
    sentiment: str
    key_phrases: List[str]
    sarcasm: bool
    sarcasm_confidence: float
    language_mix: Dict[str, float]
    category: str
    summary: str
    emotions: Dict[str, float]
    word_count: int
    positive_words_found: List[str]
    negative_words_found: List[str]
    transliteration: Optional[str] = None


#  MAIN ANALYZER
class HinglishAnalyzer:

    # ── Language Detection ──────────────────
    def detect_language_mix(self, text: str) -> Dict[str, float]:
        words = re.findall(r'\w+', text.lower())
        if not words:
            return {"hinglish": 0.5, "english": 0.5, "unknown": 0.0}

        hinglish_count = sum(1 for w in words if w in HINGLISH_WORDS)
        # simple English heuristic: words NOT in hinglish set, length > 2
        english_count = sum(
            1 for w in words
            if w not in HINGLISH_WORDS and len(w) > 2 and w.isalpha()
        )
        total = len(words)
        unknown = max(0, total - hinglish_count - english_count)

        return {
            "hinglish": round(hinglish_count / total, 2),
            "english": round(english_count / total, 2),
            "unknown": round(unknown / total, 2),
        }

    # ── Sarcasm Detection ───────────────────
    def detect_sarcasm(self, text: str) -> Dict[str, Any]:
        text_lower = text.lower()
        matched = [p for p in SARCASM_PATTERNS if re.search(p, text_lower)]

        # Contradiction: positive word + negative context
        words = set(re.findall(r'\w+', text_lower))
        has_positive = bool(words & POSITIVE_WORDS)
        has_negative = bool(words & NEGATIVE_WORDS)
        contradiction = has_positive and has_negative

        score = len(matched) * 0.3 + (0.2 if contradiction else 0)
        score = min(1.0, score)
        return {"is_sarcastic": score > 0.3, "confidence": round(score, 2)}

    # ── Emotion Detection ───────────────────
    def detect_emotions(self, words: List[str]) -> Dict[str, float]:
        word_set = set(words)
        scores = {}
        for emotion, lexicon in EMOTION_LEXICON.items():
            matches = len(word_set & lexicon)
            if matches:
                scores[emotion] = round(min(1.0, matches * 0.35), 2)
        return scores if scores else {"neutral": 1.0}

    # ── Confidence ──────────────────────────
    def calculate_confidence(self, pos: int, neg: int, total: int) -> float:
        signal = (pos + neg) / max(total, 1)
        if signal > 0.3:
            return 0.92
        elif signal > 0.15:
            return 0.75
        elif signal > 0.05:
            return 0.60
        return 0.45

    # ── Transliteration ─────────────────────
    def transliterate(self, text: str) -> str:
        words = text.split()
        result = []
        for word in words:
            clean = re.sub(r'[^\w]', '', word.lower())
            result.append(TRANSLITERATION_MAP.get(clean, word))
        return " ".join(result)

    # ── Key Phrases ─────────────────────────
    def extract_key_phrases(self, text: str) -> List[str]:
        sentences = re.split(r'[.!?,]', text)
        phrases = []
        for s in sentences:
            s = s.strip()
            if len(s) > 3:
                phrases.append(s[:80])
        return phrases[:4]

    # ── Summary ─────────────────────────────
    def generate_summary(self, text: str, mood: str, emotions: Dict) -> str:
        top_emotion = max(emotions, key=emotions.get) if emotions else "neutral"
        length = "short" if len(text.split()) < 6 else "detailed"
        return (
            f"A {length} Hinglish message expressing {mood} sentiment "
            f"with primary emotion: {top_emotion}."
        )

    # ── Main Analyze ────────────────────────
    def analyze(self, text: str) -> HinglishAnalysis:
        if not text or not text.strip():
            return self._neutral_result()

        text_lower = text.lower()
        words = re.findall(r'\w+', text_lower)

        pos_found = [w for w in words if w in POSITIVE_WORDS]
        neg_found = [w for w in words if w in NEGATIVE_WORDS]
        intens_count = sum(1 for w in words if w in INTENSIFIERS)

        pos_count = len(pos_found)
        neg_count = len(neg_found)

        # Intensity
        intensity = min(
            1.0,
            (pos_count + neg_count) * 0.20
            + intens_count * 0.15
            + len(words) * 0.01
        )
        intensity = round(intensity, 2)

        # Mood & category
        if pos_count > neg_count + 1:
            mood, emoji, category = "positive", "😊", "praise"
        elif neg_count > pos_count + 1:
            mood, emoji, category = "negative", "😠", "complaint"
        elif pos_count > 0 and neg_count > 0:
            mood, emoji, category = "mixed", "🤨", "mixed"
        else:
            mood, emoji, category = "neutral", "😐", "casual"

        sarcasm_result = self.detect_sarcasm(text)
        emotions = self.detect_emotions(words)
        lang_mix = self.detect_language_mix(text)
        confidence = self.calculate_confidence(pos_count, neg_count, len(words))
        key_phrases = self.extract_key_phrases(text)
        summary = self.generate_summary(text, mood, emotions)
        transliteration = self.transliterate(text)

        return HinglishAnalysis(
            mood=mood,
            intensity=intensity,
            confidence=confidence,
            emoji=emoji,
            sentiment=mood,
            key_phrases=key_phrases,
            sarcasm=sarcasm_result["is_sarcastic"],
            sarcasm_confidence=sarcasm_result["confidence"],
            language_mix=lang_mix,
            category=category,
            summary=summary,
            emotions=emotions,
            word_count=len(words),
            positive_words_found=list(set(pos_found)),
            negative_words_found=list(set(neg_found)),
            transliteration=transliteration,
        )

    def _neutral_result(self) -> HinglishAnalysis:
        return HinglishAnalysis(
            mood="neutral", intensity=0.0, confidence=0.5, emoji="😐",
            sentiment="neutral", key_phrases=[], sarcasm=False,
            sarcasm_confidence=0.0,
            language_mix={"hinglish": 0.5, "english": 0.5, "unknown": 0.0},
            category="casual", summary="Empty or neutral text.",
            emotions={"neutral": 1.0}, word_count=0,
            positive_words_found=[], negative_words_found=[],
            transliteration="",
        )


#  PUBLIC API
_analyzer = HinglishAnalyzer()


def analyze(text: str) -> Dict[str, Any]:
    """Analyze a single Hinglish text."""
    return _analyzer.analyze(text).__dict__


def analyze_batch(texts: List[str]) -> List[Dict[str, Any]]:
    """Analyze multiple Hinglish texts at once."""
    return [analyze(t) for t in texts]


def transliterate(text: str) -> str:
    """Convert Roman Hinglish to Devanagari script."""
    return _analyzer.transliterate(text)


def detect_language(text: str) -> Dict[str, float]:
    """Detect language mix in text."""
    return _analyzer.detect_language_mix(text)


def detect_emotion(text: str) -> Dict[str, float]:
    """Detect emotions in text."""
    words = re.findall(r'\w+', text.lower())
    return _analyzer.detect_emotions(words)


def is_sarcastic(text: str) -> Dict[str, Any]:
    """Check if text is sarcastic."""
    return _analyzer.detect_sarcasm(text)