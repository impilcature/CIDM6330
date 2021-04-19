from datetime import datetime

from flask import Flask, jsonify, request
from barkylib.domain import commands
from barkylib.api import views
from barkylib import bootstrap

app = Flask(__name__)
bus = bootstrap.bootstrap()

@app.route('/')
def index():
    return f'Barky API'

@app.route('/add_bookmark', methods=['POST'])
def add_confirm_and_remove_bookmark():

    # id: int
    # title: str
    # url: str
    # # data["date_added"] = datetime.utcnow().isoformat()
    # date_added: str
    # date_edited: str
    # notes: Optional[str] = None

    # title, url, notes, date_added, date_edited
    id = request.json["id"]
    title = request.json["title"]
    url = request.json["url"]
    date_added = request.json["date_added"]
    date_edited = request.json["date_edited"]
    notes = request.json["notes"]

    cmd = commands.AddBookmarkCommand(
            id, title, url, date_added, date_edited, notes,
    )
    bus.handle(cmd)
    return "OK", 201


@app.route("/bookmarks/<title>", methods=['GET'])
def get_bookmark_by_title(title):
    result = views.bookmarks_view(title, bus.uow)
    if not result:
         return "not found", 404
    return jsonify(result), 200

def get_bookmark_by_id( title):
    pass

def delete(bookmark):
    pass

def update(bookmark):
    pass

if __name__ == "__main__":
    app.run()