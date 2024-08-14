#Task 1: Keyword Highlighter
reviews = ["This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]
key_words = ["good", "excellent", "poor", "bad", "average"]
for review in reviews:
    for key_word in key_words:
        if key_word in review.lower():
            print(str(key_word))

#Task 2: Sentiment Tally

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

x = len(positive_words)
y = len(negative_words)
print(x, y)

#Task 3: Review Summary

txt = "This product is really good. I'm impressed with its quality."
print(txt[0:32])

