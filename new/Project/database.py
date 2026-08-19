import sqlite3


def save_news(df):

    conn=sqlite3.connect(
        "news.db"
    )

    df.to_sql(
        "news",
        conn,
        if_exists="replace"
    )

    conn.close()