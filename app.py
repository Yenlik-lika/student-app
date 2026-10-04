from flask import Flask, jsonify

app = Flask(__name__)

STUDENT = {
    "name": "Demo Student",
    "group": "IS-41",
    "program": "Information Systems",
    "course": 4,
}

GRADES = [
    {"subject": "DevOps Engineering", "score": 92},
    {"subject": "Database Systems", "score": 85},
    {"subject": "Information Security", "score": 78},
]


def average_score(grades):
    """Return the average score of a list of grades (0 for an empty list)."""
    if not grades:
        return 0
    return round(sum(item["score"] for item in grades) / len(grades), 1)


@app.route("/")
def index():
    return "Student Personal Account"


@app.route("/profile")
def profile():
    return jsonify(STUDENT)


@app.route("/grades")
def grades():
    return jsonify({"grades": GRADES, "average": average_score(GRADES)})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
