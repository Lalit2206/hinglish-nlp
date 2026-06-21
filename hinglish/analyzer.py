from dataclasses import dataclass
from typing import Dict, List, Any
import re


@dataclass
class HinglishAnalysis:
    mood: str                    # positive, negative, neutral, mixed
    intensity: float             # 0.0 to 1.0
    confidence: float
    emoji: str
    sentiment: str
    key_phrases: List[str]
    sarcasm: bool
    language_mix: Dict[str, float]
    category: str                # casual, complaint, praise, suggestion, angry, etc.
    summary: str


class HinglishAnalyzer:
    
    # Hinglish Lexicon (aap isko baad mein bahut bada kar sakte ho)
    POSITIVE = {"mast", "badiya", "zabardast", "awesome", "suprb", "love", "best", "perfect", "great", "achha", "accha", "nice"}
    NEGATIVE = {"bakwaas", "bekar", "kharaab", "worst", "faltu", "garbage", "disappoint", "boring", "time waste", "bekaar"}
    INTENSIFIERS = {"bahut", "bohot", "bht", "very", "super", "ekdum", "bilkul", "sabse"}
    SARCASM_INDICATORS = {"achha", "great yaar", "mast hai na", "bahut accha", "wow"}
    
    def analyze(self, text: str) -> HinglishAnalysis:
        if not text or not text.strip():
            return self._neutral_result()
        
        text_lower = text.lower()
        words = re.findall(r'\w+', text_lower)
        
        # Count
        pos_count = sum(1 for w in words if w in self.POSITIVE)
        neg_count = sum(1 for w in words if w in self.NEGATIVE)
        intens_count = sum(1 for w in words if w in self.INTENSIFIERS)
        
        # Intensity
        intensity = min(1.0, (pos_count + neg_count) * 0.25 + intens_count * 0.15 + len(words) * 0.02)
        intensity = round(intensity, 2)
        
        # Mood
        if pos_count > neg_count + 1:
            mood = "positive"
            emoji = "😊"
            category = "praise"
        elif neg_count > pos_count + 1:
            mood = "negative"
            emoji = "😠"
            category = "complaint"
        elif pos_count > 0 and neg_count > 0:
            mood = "mixed"
            emoji = "🤨"
            category = "mixed"
        else:
            mood = "neutral"
            emoji = "😐"
            category = "casual"
        
        sarcasm = any(ind in text_lower for ind in self.SARCASM_INDICATORS)
        
        return HinglishAnalysis(
            mood=mood,
            intensity=intensity,
            confidence=round(0.65 + min(0.35, (pos_count + neg_count) * 0.1), 2),
            emoji=emoji,
            sentiment=mood,
            key_phrases=self._extract_key_phrases(text),
            sarcasm=sarcasm,
            language_mix={"hinglish": 0.75, "english": 0.25},
            category=category,
            summary=self._generate_summary(text, mood)
        )
    
    def _neutral_result(self):
        return HinglishAnalysis(
            mood="neutral", intensity=0.0, confidence=0.5, emoji="😐",
            sentiment="neutral", key_phrases=[], sarcasm=False,
            language_mix={"hinglish": 0.5, "english": 0.5},
            category="casual", summary="Empty or neutral text"
        )
    
    def _extract_key_phrases(self, text: str) -> List[str]:
        # Simple implementation (aap ise improve kar sakte ho)
        sentences = re.split(r'[.!?]', text)
        return [s.strip()[:60] for s in sentences if s.strip()][:3]
    
    def _generate_summary(self, text: str, mood: str) -> str:
        if len(text) < 50:
            return text
        return f"User expressed {mood} sentiment in Hinglish."


# Main public API
def analyze(text: str) -> Dict[str, Any]:
    """Main function to analyze Hinglish text"""
    analyzer = HinglishAnalyzer()
    result = analyzer.analyze(text)
    return result.__dict__