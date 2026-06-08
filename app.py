import os
import re
import cv2
import joblib
import pytesseract
import numpy as np
import spacy

from flask import Flask, render_template, request
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


app = Flask(__name__)


nlp = spacy.load("en_core_web_sm")

model = joblib.load("model/fake_profile_model.pkl")

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def convert_to_number(text):

    text = text.upper().replace(",", "").strip()

    try:

        if "M" in text:
            return int(float(text.replace("M", "")) * 1000000)

        elif "K" in text:
            return int(float(text.replace("K", "")) * 1000)

        else:
            return int(float(text))

    except:
        return 0

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "profile_image" not in request.files:
        return "No File Uploaded"

    file = request.files["profile_image"]

    if file.filename == "":
        return "No Selected File"


    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    img = cv2.imread(filepath)

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    gray = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    gray = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    kernel = np.array([
        [-1, -1, -1],
        [-1,  9, -1],
        [-1, -1, -1]
    ])

    gray = cv2.filter2D(
        gray,
        -1,
        kernel
    )


    processed_path = (
        "static/uploads/processed.png"
    )

    cv2.imwrite(
        processed_path,
        gray
    )


    image = Image.open(processed_path)

    custom_config = r'--oem 3 --psm 11'

    extracted_text = pytesseract.image_to_string(
        image,
        config=custom_config
    )


    cleaned_text = "\n".join(
        line.strip()
        for line in extracted_text.splitlines()
        if line.strip()
    )

    print("\n===== OCR TEXT =====\n")
    print(cleaned_text)


    doc = nlp(cleaned_text)

    tokens = [token.text for token in doc]

    print("\n===== NLP TOKENS =====\n")
    print(tokens)



    posts = 0
    followers = 0
    following = 0



    posts_match = re.search(
        r'([\d.,]+[MK]?)\s*posts',
        cleaned_text,
        re.IGNORECASE
    )

    if posts_match:
        posts = convert_to_number(
            posts_match.group(1)
        )


    followers_match = re.search(
        r'([\d.,]+[MK]?)\s*followers',
        cleaned_text,
        re.IGNORECASE
    )

    if followers_match:
        followers = convert_to_number(
            followers_match.group(1)
        )


    following_match = re.search(
        r'([\d.,]+[MK]?)\s*following',
        cleaned_text,
        re.IGNORECASE
    )

    if following_match:
        following = convert_to_number(
            following_match.group(1)
        )



    username = tokens[0] if len(tokens) > 0 else "unknown"

    fullname_words = len(cleaned_text.split())

    digit_ratio = (
        sum(c.isdigit() for c in username)
        / max(len(username), 1)
    )

    name_equals_username = 1 if username.lower() == username else 0

    description_length = len(cleaned_text)

    external_url = (
        1 if ".com" in cleaned_text.lower()
        else 0
    )

    private_account = (
        1 if "private" in cleaned_text.lower()
        else 0
    )

    engagement_ratio = (
        followers / (following + 1)
    )

    trust_score = 100

    if posts < 5:
        trust_score -= 20

    if followers < 50:
        trust_score -= 20

    if following > followers * 3:
        trust_score -= 20

    if private_account:
        trust_score += 5

    trust_score = max(0, min(100, trust_score))

    bot_probability = 0

    if following > followers * 3:
        bot_probability += 40

    if posts < 3:
        bot_probability += 30

    if followers < 20:
        bot_probability += 20

    bot_probability = min(bot_probability, 100)
    
    digit_count = sum(
    c.isdigit()
    for c in username
)

    username_risk = "Low"

    if digit_count >= 3:
        username_risk = "Medium"

    if digit_count >= 6:
        username_risk = "High"


    scam_keywords = [
        "crypto",
        "bitcoin",
        "investment",
        "giveaway",
        "lottery",
        "winner",
        "earn money",
        "free money"
    ]


    bio_risk = "Safe"

    for word in scam_keywords:
        if word in cleaned_text.lower():
            bio_risk = "Suspicious"
            break

    reasons = []

    if posts < 5:
        reasons.append(
            "Very low post count"
        )

    if following > followers * 3:
        reasons.append(
            "High following ratio"
        )

    if username_risk == "High":
        reasons.append(
            "Suspicious username pattern"
        )

    if bio_risk == "Suspicious":
        reasons.append(
            "Potential scam keywords detected"
        )

    if private_account:
        reasons.append(
            "Private account detected"
        )
     

    features = np.array([[
        1,                     
        digit_ratio,
        fullname_words,
        digit_ratio,
        name_equals_username,
        description_length,
        external_url,
        private_account,
        posts,
        followers,
        following
    ]])


    prediction = model.predict(features)[0]

    probability = model.predict_proba(
        features
    )[0]

    confidence = round(
        max(probability) * 100,
        2
    )

    result = (
        "Fake Profile"
        if prediction == 1
        else "Real Profile"
    )


    if prediction == 1:

        if confidence >= 90:
            risk_level = "Highly Suspicious"

        elif confidence >= 70:
            risk_level = "Suspicious"

        else:
            risk_level = "Moderate Risk"

    else:
        risk_level = "Likely Genuine"


    print("\n===== DETECTED VALUES =====\n")

    print("Posts:", posts)
    print("Followers:", followers)
    print("Following:", following)

    print("\n===== AI RESULT =====\n")

    print(result)
    print(confidence)

    return render_template(
    "result.html",
    image_path=filepath.replace("\\", "/"),
    extracted_text=cleaned_text,
    posts=posts,
    followers=followers,
    following=following,
    prediction=result,
    confidence=confidence,
    risk_level=risk_level,

    trust_score=trust_score,
    bot_probability=bot_probability,
    username_risk=username_risk,
    bio_risk=bio_risk,
    reasons=reasons
)

if __name__ == "__main__":
    app.run(debug=True)