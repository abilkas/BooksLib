from booksite.celery import app

from .tesseract import image_to_text


@app.task
def quote_text(path):
	image_to_text(path)