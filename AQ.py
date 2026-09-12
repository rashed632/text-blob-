from textblob import TextBlob


def choose(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    if sentiment.polarity > 0 :
        return "happy" , sentiment.polarity
    elif sentiment.polarity < 0 :
        return "sad" , sentiment.polarity
    else :
        return "normal" , sentiment.polarity


text = input("Enter you : ")
mood , polarity = choose(text)
print(f'res : {mood}')
print(f'res : {polarity}')


features_blob = TextBlob(text)
print(f"res words count :  {len(features_blob.words)}")