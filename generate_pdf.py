from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Preformatted,
    HRFlowable, Table, TableStyle, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT

OUTPUT = "/mnt/user-data/outputs/Chatbot_NLP_Code.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    leftMargin=1.8*cm, rightMargin=1.8*cm,
    topMargin=2*cm, bottomMargin=2*cm,
    title="NLP Chatbot — Python Source Code",
    author="PyBot"
)

W, H = A4
styles = getSampleStyleSheet()

# ── Custom styles ──────────────────────────────────────────
DARK   = colors.HexColor("#1a1a2e")
BLUE   = colors.HexColor("#2196F3")
GREEN  = colors.HexColor("#4CAF50")
ORANGE = colors.HexColor("#FF9800")
BG     = colors.HexColor("#f0f4f8")
CODE_BG= colors.HexColor("#1e1e2e")
CODE_FG= colors.HexColor("#cdd6f4")

title_style = ParagraphStyle(
    "TitleStyle", parent=styles["Title"],
    fontSize=22, textColor=colors.white,
    fontName="Helvetica-Bold", alignment=TA_CENTER,
    spaceAfter=4
)
subtitle_style = ParagraphStyle(
    "SubTitle", parent=styles["Normal"],
    fontSize=11, textColor=colors.HexColor("#aab4be"),
    alignment=TA_CENTER, spaceAfter=2
)
h1_style = ParagraphStyle(
    "H1", parent=styles["Heading1"],
    fontSize=14, textColor=DARK,
    fontName="Helvetica-Bold",
    borderPad=4, spaceBefore=14, spaceAfter=6,
    leftIndent=0
)
h2_style = ParagraphStyle(
    "H2", parent=styles["Heading2"],
    fontSize=11, textColor=BLUE,
    fontName="Helvetica-Bold",
    spaceBefore=10, spaceAfter=4
)
body_style = ParagraphStyle(
    "Body", parent=styles["Normal"],
    fontSize=9.5, textColor=DARK,
    leading=15, spaceAfter=6
)
code_style = ParagraphStyle(
    "Code",
    fontName="Courier",
    fontSize=7.8,
    textColor=CODE_FG,
    backColor=CODE_BG,
    leading=12,
    leftIndent=10, rightIndent=10,
    spaceBefore=4, spaceAfter=4,
    borderPad=8,
)
bullet_style = ParagraphStyle(
    "Bullet", parent=body_style,
    leftIndent=16, bulletIndent=6,
    spaceAfter=3
)

def section_divider(color=BLUE):
    return HRFlowable(width="100%", thickness=1.5, color=color, spaceAfter=6, spaceBefore=2)

def code_block(code_text):
    """Render a dark-themed code block."""
    return Preformatted(code_text, code_style)

def bullet(text):
    return Paragraph(f"• {text}", bullet_style)

# ── Story ──────────────────────────────────────────────────
story = []

# ── COVER BANNER ──────────────────────────────────────────
cover_data = [[
    Paragraph("<font color='white'><b>🤖  NLP Chatbot — Python Source Code</b></font>", title_style),
]]
cover_table = Table(cover_data, colWidths=[W - 3.6*cm])
cover_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), DARK),
    ("ROUNDEDCORNERS", [8]),
    ("TOPPADDING",    (0,0), (-1,-1), 18),
    ("BOTTOMPADDING", (0,0), (-1,-1), 18),
    ("LEFTPADDING",   (0,0), (-1,-1), 20),
    ("RIGHTPADDING",  (0,0), (-1,-1), 20),
]))
story.append(cover_table)
story.append(Spacer(1, 8))
story.append(Paragraph("Built with Python • NLTK • spaCy", subtitle_style))
story.append(Spacer(1, 14))

# ── INFO TABLE ────────────────────────────────────────────
info_data = [
    ["Language", "Python 3.x"],
    ["Libraries", "NLTK, spaCy (en_core_web_sm)"],
    ["Techniques", "Tokenization, Lemmatization, NER, Intent Matching"],
    ["Features", "Math eval, Time/Date, Capitals, Jokes, Facts, Motivation"],
    ["Interface", "Interactive terminal chatbot"],
]
info_table = Table(info_data, colWidths=[4.5*cm, 11.5*cm])
info_table.setStyle(TableStyle([
    ("BACKGROUND",   (0,0), (0,-1), colors.HexColor("#e3f2fd")),
    ("BACKGROUND",   (1,0), (1,-1), colors.white),
    ("TEXTCOLOR",    (0,0), (0,-1), DARK),
    ("FONTNAME",     (0,0), (0,-1), "Helvetica-Bold"),
    ("FONTSIZE",     (0,0), (-1,-1), 9),
    ("GRID",         (0,0), (-1,-1), 0.5, colors.HexColor("#c8d8e8")),
    ("ROWBACKGROUNDS",(0,0),(-1,-1),[colors.white, colors.HexColor("#f9fbfd")]),
    ("TOPPADDING",   (0,0), (-1,-1), 5),
    ("BOTTOMPADDING",(0,0), (-1,-1), 5),
    ("LEFTPADDING",  (0,0), (-1,-1), 8),
]))
story.append(info_table)
story.append(Spacer(1, 16))

# ══════════════════════════════════════════════════════════
# SECTION 1 — INSTALL
# ══════════════════════════════════════════════════════════
story.append(Paragraph("1.  Installation", h1_style))
story.append(section_divider(BLUE))
story.append(code_block(
"""# Install required libraries
pip install nltk spacy

# Download spaCy English model
python -m spacy download en_core_web_sm"""
))
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════════
# SECTION 2 — IMPORTS
# ══════════════════════════════════════════════════════════
story.append(Paragraph("2.  Imports &amp; Setup", h1_style))
story.append(section_divider(BLUE))
story.append(code_block(
"""import re
import random
import string
import warnings
warnings.filterwarnings('ignore')

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import spacy

# Download required NLTK data
nltk.download('punkt',     quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet',   quiet=True)

# Load spaCy English model
nlp = spacy.load('en_core_web_sm')"""
))
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════════
# SECTION 3 — KNOWLEDGE BASE
# ══════════════════════════════════════════════════════════
story.append(Paragraph("3.  Knowledge Base", h1_style))
story.append(section_divider(BLUE))
story.append(Paragraph(
    "The knowledge base is a Python dictionary mapping <b>intents</b> to "
    "pattern lists and response lists. Dynamic intents (time, date, math, "
    "capitals) use a sentinel string that the response generator handles at runtime.",
    body_style
))
story.append(code_block(
"""KNOWLEDGE_BASE = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "good morning", "good evening",
                     "good afternoon", "howdy", "what's up", "sup", "greetings"],
        "responses": [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! Great to see you. What do you need help with?",
            "Greetings! How may I assist you?",
        ]
    },
    "farewell": {
        "patterns": ["bye", "goodbye", "see you", "take care", "later",
                     "quit", "exit", "cya", "farewell", "good night"],
        "responses": [
            "Goodbye! Have a great day!",
            "See you later! Take care!",
            "Bye! Feel free to come back anytime.",
            "Farewell! It was nice chatting with you.",
        ]
    },
    "thanks": {
        "patterns": ["thank you", "thanks", "thank", "appreciate",
                     "grateful", "cheers", "thx"],
        "responses": [
            "You're welcome!",
            "Happy to help!",
            "Anytime! Let me know if you need anything else.",
            "Glad I could assist!",
        ]
    },
    "name": {
        "patterns": ["what is your name", "who are you", "what are you called",
                     "what should i call you", "your name", "tell me your name"],
        "responses": [
            "I'm PyBot, your intelligent Python-powered assistant!",
            "My name is PyBot. Nice to meet you!",
            "You can call me PyBot -- here to help!",
        ]
    },
    "age": {
        "patterns": ["how old are you", "what is your age", "when were you born",
                     "your age", "how long have you existed"],
        "responses": [
            "I was created recently, so I'm quite young in bot years!",
            "Age is just a number for a bot like me.",
            "I don't age like humans do -- I just keep getting smarter!",
        ]
    },
    "weather": {
        "patterns": ["weather", "forecast", "temperature", "raining",
                     "sunny", "hot outside", "cold outside", "climate"],
        "responses": [
            "I don't have live weather data. Try weather.com or Google Weather!",
            "For real-time weather, I'd recommend AccuWeather or Weather Underground.",
        ]
    },
    "time":     {"patterns": ["what time is it", "current time",
                               "what's the time", "time now"],
                 "responses": ["__TIME__"]},   # dynamic

    "date":     {"patterns": ["what is today's date", "what day is it",
                               "current date", "today's date"],
                 "responses": ["__DATE__"]},   # dynamic

    "math":     {"patterns": ["calculate", "math", "plus", "minus",
                               "multiply", "divide", "sum"],
                 "responses": ["__MATH__"]},   # dynamic

    "capital":  {"patterns": ["capital of india", "capital of france",
                               "capital of usa",  "capital of japan"],
                 "responses": ["__CAPITAL__"]},# dynamic

    "help": {
        "patterns": ["help", "what can you do", "capabilities",
                     "features", "how do you work"],
        "responses": [
            ("I can help you with:\\n"
             "  - General conversation\\n"
             "  - Time & date queries\\n"
             "  - Python & programming tips\\n"
             "  - Math calculations\\n"
             "  - Fun facts & jokes\\n"
             "  - Motivational quotes\\n"
             "  - World capitals\\n"
             "Just type your question!")
        ]
    },
    "python": {
        "patterns": ["python", "programming", "coding", "code",
                     "developer", "software", "script"],
        "responses": [
            "Python is a fantastic language! Known for simplicity and readability.",
            "Python tip: use list comprehensions -- [x*2 for x in range(10)]",
            "Fun fact: Python was named after Monty Python, not the snake!",
        ]
    },
    "ai": {
        "patterns": ["artificial intelligence", "machine learning",
                     "deep learning", "neural network", "nlp", "ai", "ml"],
        "responses": [
            "AI is transforming every industry!",
            "NLP allows me to understand your text!",
            "Deep learning uses multi-layer neural networks.",
        ]
    },
    "joke": {
        "patterns": ["joke", "funny", "make me laugh", "tell me a joke"],
        "responses": [
            "Why do programmers prefer dark mode? Light attracts bugs!",
            "A SQL query walks into a bar and asks two tables: 'Can I JOIN you?'",
            "Why did the Python programmer wear glasses? They couldn't C!",
        ]
    },
    "fact": {
        "patterns": ["fun fact", "interesting fact", "fact",
                     "did you know", "trivia"],
        "responses": [
            "Honey never spoils -- archaeologists found 3000-year-old honey!",
            "A group of flamingos is called a 'flamboyance'!",
            "Bananas are berries, but strawberries are not!",
        ]
    },
    "motivation": {
        "patterns": ["motivate me", "motivation", "inspire me",
                     "quote", "i feel sad", "feeling down"],
        "responses": [
            "'The only way to do great work is to love what you do.' -- Steve Jobs",
            "'Believe you can and you're halfway there.' -- Roosevelt",
        ]
    },
    "creator": {
        "patterns": ["who made you", "who created you", "who built you"],
        "responses": [
            "I was built using Python, NLTK, and spaCy!",
            "A Python developer crafted me with NLP libraries and caffeine.",
        ]
    },
    "default": {
        "responses": [
            "I'm not sure I understand. Could you rephrase that?",
            "Hmm, interesting! Try asking about Python, jokes, or facts.",
            "I don't have an answer yet, but I'm always learning!",
        ]
    }
}

CAPITALS = {
    "india": "New Delhi",     "france": "Paris",
    "usa": "Washington D.C.", "japan": "Tokyo",
    "uk": "London",           "germany": "Berlin",
    "australia": "Canberra",  "canada": "Ottawa",
    "china": "Beijing",       "brazil": "Brasilia",
    "italy": "Rome",          "spain": "Madrid",
    "russia": "Moscow",       "mexico": "Mexico City",
    "egypt": "Cairo",         "pakistan": "Islamabad",
}"""
))
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════════
# SECTION 4 — NLP PROCESSOR
# ══════════════════════════════════════════════════════════
story.append(Paragraph("4.  NLP Processor Class", h1_style))
story.append(section_divider(GREEN))
story.append(Paragraph(
    "Handles tokenization, lemmatization, stopword removal, named-entity "
    "recognition (via spaCy), and intent matching via pattern overlap scoring.",
    body_style
))
story.append(code_block(
"""class NLPProcessor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def preprocess(self, text):
        \"\"\"Lowercase, strip punctuation, tokenize, lemmatize.\"\"\"
        text = text.lower().strip()
        text = re.sub(r'[^\\w\\s]', '', text)
        tokens = word_tokenize(text)
        tokens = [self.lemmatizer.lemmatize(t) for t in tokens
                  if t not in self.stop_words]
        return tokens

    def extract_entities(self, text):
        \"\"\"Named-entity recognition via spaCy.\"\"\"
        doc = nlp(text)
        return [(ent.text, ent.label_) for ent in doc.ents]

    def get_intent(self, text):
        \"\"\"Match user input to the best-fitting intent.\"\"\"
        tokens    = set(self.preprocess(text))
        text_lower = text.lower()

        best_intent = None
        best_score  = 0

        for intent, data in KNOWLEDGE_BASE.items():
            if intent == "default":
                continue
            for pattern in data.get("patterns", []):
                # Full phrase match (highest priority)
                if pattern in text_lower:
                    score = len(pattern.split()) * 2
                else:
                    # Token-overlap score
                    pattern_tokens = set(self.preprocess(pattern))
                    score = len(tokens & pattern_tokens)

                if score > best_score:
                    best_score  = score
                    best_intent = intent

        return best_intent if best_score > 0 else "default" """
))
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════════
# SECTION 5 — MATH EVALUATOR
# ══════════════════════════════════════════════════════════
story.append(Paragraph("5.  Safe Math Evaluator", h1_style))
story.append(section_divider(ORANGE))
story.append(code_block(
"""def safe_math(expression):
    \"\"\"Safely evaluate a numeric expression extracted from user input.\"\"\"
    try:
        expr = re.sub(r'[^0-9+\\-*/().\\s]', '', expression).strip()
        if not expr:
            return None
        result = eval(expr, {"__builtins__": {}})   # no builtins = safe
        return result
    except Exception:
        return None"""
))
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════════
# SECTION 6 — RESPONSE GENERATOR
# ══════════════════════════════════════════════════════════
story.append(Paragraph("6.  Response Generator Class", h1_style))
story.append(section_divider(BLUE))
story.append(code_block(
"""class ResponseGenerator:
    def __init__(self):
        self.processor = NLPProcessor()

    def get_response(self, user_input):
        from datetime import datetime

        intent   = self.processor.get_intent(user_input)
        data     = KNOWLEDGE_BASE.get(intent, KNOWLEDGE_BASE["default"])
        response = random.choice(data["responses"])

        # Dynamic: current time
        if response == "__TIME__":
            now = datetime.now().strftime("%I:%M %p")
            return f"The current time is {now}."

        # Dynamic: current date
        if response == "__DATE__":
            today = datetime.now().strftime("%A, %B %d, %Y")
            return f"Today is {today}."

        # Dynamic: math expression
        if response == "__MATH__":
            result = safe_math(user_input)
            if result is not None:
                return f"The answer is: {result}"
            return "Please give me a math expression like '15 * 4' or '100 / 5'."

        # Dynamic: world capitals
        if response == "__CAPITAL__":
            text_lower = user_input.lower()
            for country, capital in CAPITALS.items():
                if country in text_lower:
                    return f"The capital of {country.title()} is {capital}."
            return "Try asking: 'capital of France' or 'capital of Japan'."

        return response"""
))
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════════
# SECTION 7 — CHATBOT CLASS
# ══════════════════════════════════════════════════════════
story.append(Paragraph("7.  ChatBot Class", h1_style))
story.append(section_divider(BLUE))
story.append(code_block(
"""class ChatBot:
    def __init__(self, name="PyBot"):
        self.name         = name
        self.generator    = ResponseGenerator()
        self.chat_history = []

    def chat(self, user_input):
        user_input = user_input.strip()
        if not user_input:
            return "Please say something! I'm here to help."
        response = self.generator.get_response(user_input)
        self.chat_history.append({"user": user_input, "bot": response})
        return response

    def show_history(self):
        if not self.chat_history:
            print("No chat history yet.")
            return
        print("\\n--- Chat History ---")
        for i, entry in enumerate(self.chat_history, 1):
            print(f"[{i}] You : {entry['user']}")
            print(f"     Bot : {entry['bot']}")
        print("--------------------\\n")

    def run(self):
        print("=" * 55)
        print(f"  Welcome to {self.name} -- NLP-Powered Chatbot")
        print("=" * 55)
        print("  Type 'help'    to see what I can do.")
        print("  Type 'history' to view chat history.")
        print("  Type 'bye'     to quit.")
        print("=" * 55)

        farewell_words = {"bye", "goodbye", "exit", "quit",
                          "cya", "farewell", "see you", "later"}

        while True:
            try:
                user_input = input("\\nYou: ").strip()
                if not user_input:
                    continue
                if user_input.lower() == "history":
                    self.show_history()
                    continue
                response = self.chat(user_input)
                print(f"\\n{self.name}: {response}")
                if any(w in user_input.lower() for w in farewell_words):
                    break
            except KeyboardInterrupt:
                print(f"\\n\\n{self.name}: Goodbye! Have a great day!")
                break"""
))
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════════
# SECTION 8 — ENTRY POINT
# ══════════════════════════════════════════════════════════
story.append(Paragraph("8.  Main Entry Point", h1_style))
story.append(section_divider(GREEN))
story.append(code_block(
"""if __name__ == "__main__":
    bot = ChatBot(name="PyBot")
    bot.run()"""))
story.append(Spacer(1, 14))

# ══════════════════════════════════════════════════════════
# SECTION 9 — SAMPLE SESSION
# ══════════════════════════════════════════════════════════
story.append(Paragraph("9.  Sample Session", h1_style))
story.append(section_divider(ORANGE))
story.append(code_block(
"""=======================================================
  Welcome to PyBot -- NLP-Powered Chatbot
=======================================================
  Type 'help' to see what I can do.
  Type 'history' to view chat history.
  Type 'bye' to quit.
=======================================================

You: hello
PyBot: Hi there! What can I do for you?

You: what is your name
PyBot: I'm PyBot, your intelligent Python-powered assistant!

You: tell me a joke
PyBot: Why do programmers prefer dark mode? Light attracts bugs!

You: what is 25 * 4
PyBot: The answer is: 100

You: capital of france
PyBot: The capital of France is Paris.

You: what time is it
PyBot: The current time is 07:45 PM.

You: fun fact
PyBot: A group of flamingos is called a 'flamboyance'!

You: motivate me
PyBot: 'Believe you can and you're halfway there.' -- Roosevelt

You: history
--- Chat History ---
[1] You : hello      |  Bot : Hi there! What can I do for you?
[2] You : tell me a joke  |  Bot : Why do programmers prefer dark mode?
...
--------------------

You: bye
PyBot: Goodbye! Have a great day!"""))
story.append(Spacer(1, 14))

# ══════════════════════════════════════════════════════════
# SECTION 10 — CAPABILITIES TABLE
# ══════════════════════════════════════════════════════════
story.append(Paragraph("10.  Chatbot Capabilities", h1_style))
story.append(section_divider(BLUE))

cap_data = [
    ["Feature", "Example Input", "How It Works"],
    ["Greetings",      "hello / hey / good morning",     "Pattern match + random response"],
    ["Farewells",      "bye / exit / goodbye",            "Pattern match + exits loop"],
    ["Name / Age",     "what is your name",               "Intent: name"],
    ["Current Time",   "what time is it",                 "datetime.now() at runtime"],
    ["Current Date",   "what day is it",                  "datetime.now() at runtime"],
    ["Math",           "what is 56 / 8",                  "safe_math() via eval()"],
    ["World Capitals", "capital of Japan",                "CAPITALS dict lookup"],
    ["Python Tips",    "tell me about Python",            "Intent: python"],
    ["AI / ML Info",   "what is machine learning",        "Intent: ai"],
    ["Jokes",          "tell me a joke",                  "Intent: joke"],
    ["Fun Facts",      "fun fact / did you know",         "Intent: fact"],
    ["Motivation",     "motivate me / I feel sad",        "Intent: motivation"],
    ["Help Menu",      "help / what can you do",          "Intent: help"],
    ["Chat History",   "history",                         "show_history() method"],
    ["NER (spaCy)",    "Any named entity in text",        "extract_entities()"],
]
col_w = [(W-3.6*cm)*x for x in [0.22, 0.38, 0.40]]
cap_table = Table(cap_data, colWidths=col_w)
cap_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),  (-1,0),  DARK),
    ("TEXTCOLOR",     (0,0),  (-1,0),  colors.white),
    ("FONTNAME",      (0,0),  (-1,0),  "Helvetica-Bold"),
    ("FONTSIZE",      (0,0),  (-1,-1), 8.5),
    ("GRID",          (0,0),  (-1,-1), 0.4, colors.HexColor("#c8d8e8")),
    ("ROWBACKGROUNDS",(0,1),  (-1,-1), [colors.white, colors.HexColor("#f0f4f8")]),
    ("TOPPADDING",    (0,0),  (-1,-1), 5),
    ("BOTTOMPADDING", (0,0),  (-1,-1), 5),
    ("LEFTPADDING",   (0,0),  (-1,-1), 7),
    ("VALIGN",        (0,0),  (-1,-1), "MIDDLE"),
]))
story.append(cap_table)
story.append(Spacer(1, 18))

# ── FOOTER NOTE ───────────────────────────────────────────
footer_data = [[
    Paragraph(
        "<font color='white'><b>Save this file as chatbot.py and run:</b>  "
        "python chatbot.py</font>",
        ParagraphStyle("footer", fontName="Courier", fontSize=9,
                       textColor=colors.white, alignment=TA_CENTER)
    )
]]
footer_table = Table(footer_data, colWidths=[W - 3.6*cm])
footer_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), colors.HexColor("#1565C0")),
    ("TOPPADDING",    (0,0), (-1,-1), 10),
    ("BOTTOMPADDING", (0,0), (-1,-1), 10),
]))
story.append(footer_table)

# ── BUILD ─────────────────────────────────────────────────
doc.build(story)
print(f"PDF saved to: {OUTPUT}")
