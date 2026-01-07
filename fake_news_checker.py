# Fake News Checker - Keyword Based

suspicious_keywords = [
    "shocking",
    "breaking",
    "unbelievable",
    "miracle",
    "guaranteed",
    "click here",
    "must see",
    "viral",
    "leaked",
    "cure",
    "free",
    "won",
    "urgent",
    "secret"
]

print("---- Fake News Checker ----")

news = input("Enter a news headline or sentence: ").lower()

flag = False
found_words = []

for word in suspicious_keywords:
    if word in news:
        flag = True
        found_words.append(word)

if flag:
    print("\n⚠️ This news is POSSIBLY FAKE.")
    print("Suspicious words found:", ", ".join(found_words))
else:
    print("\n✅ This news seems more LIKELY REAL (but always verify).")

print("\nNote: This is a simple keyword-based checker, not a real AI model.")