from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/upload")
def upload_file():
    return render_template("upload.html")


# 메소드 명이 같으면 에러가나네...
@app.route("/uploader", methods=["POST"])
def uploader_file():
    f = request.files["file"]
    f.save(f.filename)
    return "file uploaded successfully"


if __name__ == "__main__":
    app.run(debug=True)
