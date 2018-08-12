# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Open each of the samples
with open("Sample1.txt") as sample:
    Sample1 = sample.read()

with open("Sample2.txt") as sample:
    Sample2 = sample.read()

with open("Sample3.txt") as sample:
    Sample3 = sample.read()

# Store each sample in a tuple
samples = (Sample1, Sample2, Sample3)

# Loop through Each Sample
for sample in samples:

    # Run Vader Analysis on each Sample
    compound = analyzer.polarity_scores(sample)["compound"]
    pos = analyzer.polarity_scores(sample)["pos"]
    neu = analyzer.polarity_scores(sample)["neu"]
    neg = analyzer.polarity_scores(sample)["neg"]

    # Print Samples and Analysis
    print(sample)
    print(f"Compound Score: {compound}")
    print(f"Positive Score: {pos}")
    print(f"Neutral Score: {neu}")
    print(f"Negative Score: {neg}")
    print("")
