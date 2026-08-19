import streamlit as st
from news_api import get_news
from sentiment import analyze_sentiment
from database import save_news

st.set_page_config(
    page_title="Trending News Analyzer",
    page_icon="📰",
    layout="wide"
)

# ---------------- Sidebar ----------------

st.sidebar.title("⚙️ Settings")

countries = {
    "🇺🇸 United States": "us",
    "🇬🇧 United Kingdom": "gb",
    "🇨🇦 Canada": "ca",
    "🇦🇺 Australia": "au",
    "🇮🇳 India": "in",
    "🇵🇰 Pakistan": "pk",
    "🇫🇷 France": "fr",
    "🇩🇪 Germany": "de",
    "🇯🇵 Japan": "jp",
    "🇮🇹 Italy": "it",
    "ru russia": "ru",
}

selected_country = st.sidebar.selectbox(
    "🌍 Select Country",
    list(countries.keys())
)

# ---------------- Header ----------------

st.markdown(
    """
    <h1 style='text-align:center;color:#ff4b4b;'>
    📰 AI Trending News Analyzer
    </h1>

    <p style='text-align:center;font-size:18px;color:gray;'>
    Fetch the latest news, analyze sentiment using AI, and visualize the results.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------------- Button ----------------

if st.button("🚀 Analyze News", use_container_width=True):

    with st.spinner("Fetching latest news..."):
        df = get_news(countries[selected_country])

    df["Sentiment"] = df["title"].apply(analyze_sentiment)

    save_news(df)

    positive = (df["Sentiment"] == "Positive").sum()
    negative = (df["Sentiment"] == "Negative").sum()
    neutral = (df["Sentiment"] == "Neutral").sum()

    c1, c2, c3 = st.columns(3)

    c1.metric("😊 Positive", positive)
    c2.metric("😐 Neutral", neutral)
    c3.metric("😡 Negative", negative)

    st.divider()

    st.subheader("📰 Latest Headlines")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("📊 Sentiment Distribution")

    st.bar_chart(df["Sentiment"].value_counts())

    st.success("✅ Analysis Completed Successfully")