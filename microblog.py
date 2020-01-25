from app import app

if __name__ == "__main__":
	app.run(debug=app.debug, port=5000, threaded=True)
