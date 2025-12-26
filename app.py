from flask import Flask, request, redirect, abort, render_template
from models import db, URL
import string
import random

app = Flask(__name__)

# ----------------------
# Database Configuration
# ----------------------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///urls.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# ----------------------
# Utility: Short Code Generator
# ----------------------
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# ----------------------
# Home Route
# ----------------------
@app.route("/", methods=["GET", "POST"])
def home():
    short_url = None
    error = None

    if request.method == "POST":
        original_url = request.form.get("url")

        if not original_url or not original_url.strip():
            error = "Please enter a URL"
        elif not original_url.startswith(("http://", "https://")):
            error = "Please enter a valid URL (http/https)"
        else:
            existing = URL.query.filter_by(original_url=original_url).first()
            if existing:
                short_url = f"http://127.0.0.1:5000/{existing.short_code}"
            else:
                while True:
                    short_code = generate_short_code()
                    if not URL.query.filter_by(short_code=short_code).first():
                        break

                new_url = URL(
                    original_url=original_url,
                    short_code=short_code
                )
                db.session.add(new_url)
                db.session.commit()

                short_url = f"http://127.0.0.1:5000/{short_code}"

    return render_template("index.html", short_url=short_url, error=error)


# ----------------------
# Create Short URL
# ----------------------
@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()

    # Edge Case: missing or empty URL
    if not data or "url" not in data or not data["url"].strip():
        return {"error": "URL is required"}, 400

    original_url = data["url"].strip()

    # Edge Case: invalid URL format
    if not original_url.startswith(("http://", "https://")):
        return {"error": "Invalid URL format"}, 400

    # Edge Case: duplicate long URL
    existing = URL.query.filter_by(original_url=original_url).first()
    if existing:
        return {
            "original_url": existing.original_url,
            "short_code": existing.short_code,
            "short_url": f"http://127.0.0.1:5000/{existing.short_code}"
        }, 200

    # Edge Case: short code collision prevention
    while True:
        short_code = generate_short_code()
        if not URL.query.filter_by(short_code=short_code).first():
            break

    new_url = URL(
        original_url=original_url,
        short_code=short_code
    )

    db.session.add(new_url)
    db.session.commit()

    return {
        "original_url": new_url.original_url,
        "short_code": new_url.short_code,
        "short_url": f"http://127.0.0.1:5000/{new_url.short_code}"
    }, 201

# ----------------------
# Redirect Short URL
# ----------------------
@app.route("/<short_code>")
def redirect_to_url(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first()

    if not url_entry:
        abort(404)

    return redirect(url_entry.original_url)

# ----------------------
# Run App
# ----------------------
if __name__ == "__main__":
    app.run(debug=True)
