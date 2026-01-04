from flask import Flask, request, jsonify
from flask_cors import CORS
from app import get_enhanced_reddit_posts
from datetime import datetime

# === Initialize Flask App ===
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/search", methods=["POST"])
def search():
    data = request.json or {}

    # Extract request data
    keywords = data.get("keywords", "")
    subreddits = data.get("subreddits", [])
    fuzzy_threshold = data.get("fuzzy_threshold", 80)
    comment_filter = data.get("comment_filter", None)

    start_date_str = data.get("start_date")
    end_date_str = data.get("end_date")

    # Make dates optional
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d") if start_date_str else None
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d") if end_date_str else None

    # Fetch posts using your existing logic
    posts = get_enhanced_reddit_posts(
        keywords,
        start_date=start_date,
        end_date=end_date,
        subreddits=subreddits,
        comment_filter=comment_filter,
        fuzzy_threshold=fuzzy_threshold
    )

    return jsonify(posts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
