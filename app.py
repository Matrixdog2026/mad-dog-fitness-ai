from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Mad Dog Fitness AI is running"

@app.route("/generate-plan", methods=["POST"])
def generate_plan():
    data = request.json

    goal = data.get("goal", "muscle_gain")

    workout = ["Bench Press", "Squats", "Deadlifts"]
    meals = ["Chicken", "Rice", "Eggs"]

    return jsonify({
        "goal": goal,
        "workout": workout,
        "meals": meals
    })

if __name__ == "__main__":
    app.run()
