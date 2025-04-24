
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Step 1: Load texts
with open("emil.txt", "r", encoding="utf-8") as f:
    emil_text = f.read()

with open("mushroom.txt", "r", encoding="utf-8") as f:
    mushroom_text = f.read()

# Step 2: Expanded custom stopwords
custom_stopwords = set(STOPWORDS)
custom_stopwords.update([
    # General filler words or letters
    "t", "s", "u", "n", "m", "ll", "ve", "re",
    # Dialogue or storytelling words
    "say", "saying", "told", "asked", "tells", "says",
    # General vague terms
    "thing", "something", "anything", "everything", "nothing",
    # Common narrative verbs
    "come", "get", "go", "want", "make", "give", "took", "put", "told", "know",
    # Names or characters
    "gustav", "grandma", "professor", "hans", "mushroom", 
    "boy", "girl", "man", "woman", "children", "child", "one", "two", "young", "old",
    # Other
    "will", "may", "could", "would", "should", "well", "let",
    "see", "even", "much", "many", "also", "still", "back", "came", "thing", "said","now","don"
])

# Step 3: Generate word clouds
emil_wc = WordCloud(width=800, height=400, background_color="white",
                    stopwords=custom_stopwords, collocations=False).generate(emil_text)

mushroom_wc = WordCloud(width=800, height=400, background_color="white",
                        stopwords=custom_stopwords, collocations=False).generate(mushroom_text)

# Step 4: Plot them side by side
plt.figure(figsize=(16, 8))

plt.subplot(1, 2, 1)
plt.imshow(emil_wc, interpolation="bilinear")
plt.title("Emil and the Detectives\n (Emil und die Detektive)\n 1929", fontsize=16)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(mushroom_wc, interpolation="bilinear")
plt.title("The Poisonous Mushroom\n (Der Giftpilz)\n 1938", fontsize=16)
plt.axis("off")

plt.tight_layout()
plt.show()
