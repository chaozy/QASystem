from app.app import app
print("enter wsgi.py")
if __name__ == "__main__":
    app.run(debug=True, port=5000)
