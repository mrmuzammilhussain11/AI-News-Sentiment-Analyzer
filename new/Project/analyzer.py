from sklearn.feature_extraction.text import CountVectorizer


def trending_topics(data):


    text=" ".join(data["title"])


    vectorizer=CountVectorizer(
        stop_words="english"
    )


    words=vectorizer.fit_transform([text])


    frequency=sum(words.toarray())


    result=pd.DataFrame(
        {
        "Word":vectorizer.get_feature_names_out(),
        "Count":frequency
        }
    )


    result=result.sort_values(
        by="Count",
        ascending=False
    )


    return result.head(10)