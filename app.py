import streamlit as st #creates web UI
import pickle #loads saved model & dataset
import re #handles price extraction
from sklearn.metrics.pairwise import cosine_similarity#calculates relevance score

#Load Pickle Files (MOST IMPORTANT)
tfidf = pickle.load(open("tfidf.pkl", "rb"))
df = pickle.load(open("products.pkl", "rb"))

#Helper Functions (Same Logic as Training)
def extract_price(query):
    query = query.lower()

    range_match = re.search(r'(\d+)\s*-\s*(\d+)', query)
    if range_match:
        return int(range_match.group(1)), int(range_match.group(2))

    under_match = re.search(r'(under|below)\s*(\d+)', query)
    if under_match:
        return 0, int(under_match.group(2))

    exact_match = re.search(r'\b(\d{3,6})\b', query)
    if exact_match:
        price = int(exact_match.group(1))
        return price - 500, price + 500

    return None, None

def clean_query(query):
    return re.sub(r'\d+', '', query).strip().lower()
# ---------------------------
# RECOMMENDER
def recommend_products(user_query, top_n=10):

    min_price, max_price = extract_price(user_query)
    keywords = clean_query(user_query)

    # Keyword filtering (fixes headphones issue)
    keyword_mask = df['combined_text'].str.lower().str.contains(
        '|'.join(keywords.split()), regex=True
    )

    filtered_df = df[keyword_mask]

    # Price filtering
    if min_price is not None and max_price is not None:
        filtered_df = filtered_df[
            (filtered_df['price'] >= min_price) &
            (filtered_df['price'] <= max_price)
        ]

    if filtered_df.empty:
        return None

    # TF-IDF similarity
    filtered_vectors = tfidf.transform(filtered_df['combined_text'])
    query_vector = tfidf.transform([keywords])

    scores = cosine_similarity(query_vector, filtered_vectors).flatten()
    filtered_df = filtered_df.copy()
    filtered_df['score'] = scores

    return filtered_df.sort_values(
        by='score', ascending=False
    ).head(top_n)
# ---------------------------
#Streamlit UI

st.title("🛒 E-Commerce Product Recommendation System")

query = st.text_input(
    "Search product (example: smartphones, laptops ,sneakers shoes 8000-10000)"
)

if st.button("Recommend"):
    results = recommend_products(query)

    if results is None:
        st.warning("No products found for your search.")
    else:
        for _, row in results.iterrows():
            st.write(
                f"**{row['product_name']}** | ₹{row['price']}"
            )

