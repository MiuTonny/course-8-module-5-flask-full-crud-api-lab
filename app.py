from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]
#assign a unique id
def next_id():
    return max((e.id for e in events), default=0) +1

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json() or {}
    title = data.get("title")
    if not title:
        return jsonify({"error": "title is required"}), 400

    new_event = Event(next_id(), title)
    events.append(new_event)
    return jsonify(new_event.to_dict()), 201 # TODO: Task 4 - Return and Handle Results
    

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    data = request.get_json() or {}

    for e in events:
        if e.id == event_id:
            if "title" not in data:
                return jsonify({"error": "title is required"}), 400
            e.title = data["title"]
            return jsonify(e.to_dict()), 200

    return jsonify({"error": "Event not found"}), 404
    
# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    for i, e in enumerate(events):
        if e.id == event_id:
            del events[i]
            return "", 204  # No Content 

    return jsonify({"error": "Event not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
