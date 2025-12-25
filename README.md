# Content-Based-E-Commerce-Product-Recommendation-System
STREAMLIT WEB APP LINK- https://h7fah9oyobhfcpaccjrvrw.streamlit.app/
This project implements a content-based e-commerce product recommendation system that suggests relevant products based on user search text and price preferences. The system intelligently handles exact price, price range, and budget-based searches, ensuring accurate and meaningful recommendations similar to real-world e-commerce platforms.


⬇️Project Objective⬇️

Recommend products based on content similarity

Handle price-aware searches like:

nike shoes 10000

running shoes under 5000

nike shoes 8000-10000

Avoid irrelevant results across categories

Deploy the model as an interactive web application



👇Recommendation Approach👇

This project uses a Content-Based Filtering approach with:

TF-IDF Vectorization for text representation

Cosine Similarity for measuring relevance

Regex-based query parsing for price extraction

Keyword-based pre-filtering to avoid cross-category noise



✅Dataset Description✅

The dataset contains structured e-commerce product information.

Features Used
Feature Name	Description
product_name	Product title
category	Product category
brand	Brand name
description	Product details
price	Product price (numeric)


✅Engineered Feature✅

combined_text
→ Combination of product name, category, brand, and description
→ Used as input for TF-IDF

⬇️Input & Output⬇️
🔹 Input

User search query (text + price)

Example: nike shoes 8000-10000

🔹 Output

Top-N recommended products with:

Product name

Price

Similarity score


✅Model Persistence✅

The trained TF-IDF model and processed dataset are saved using Pickle, allowing the system to:

Avoid retraining on every run

Load models instantly during deployment

Maintain consistent recommendations

Saved Files

tfidf.pkl – trained TF-IDF vectorizer

products.pkl – cleaned dataset


🌐Deployment (Streamlit)

The recommendation system is deployed as a Streamlit web app, allowing users to:

Enter search queries

Apply price constraints

View real-time recommendations
