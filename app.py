from flask import Flask
from index import Index

app = Flask(__name__)


app.add_url_rule("/", view_func=Index.as_view("index"))