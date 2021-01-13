from flask import redirect, render_template, url_for
from flask import views
from data import *

class Index(views.MethodView):
	def get(self):
		return render_template("index.html", data=get_news())

	def post(self):
		return "Method Not allowed"