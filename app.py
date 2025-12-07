import os
from flask import Flask, render_template, request
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static"


def generate_meme(image_path, top_text, bottom_text, output_path):

    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    width, height = image.size

    font_size = int(height / 25)

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    def draw_centered_text(text, y_pos):
        text = text.upper()  

        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        x = (width - text_width) / 2

        draw.text((x, y_pos), text, font=font, fill="white")

    if top_text:
        draw_centered_text(top_text, 25)

    if bottom_text:
        draw_centered_text(bottom_text, height - font_size - 25)

    image.save(output_path)


@app.route("/", methods=["GET", "POST"])
def index():
    generated_filename = None

    if request.method == "POST":
        file = request.files.get("image")
        top_text = request.form.get("top_text", "")
        bottom_text = request.form.get("bottom_text", "")

        if file:
            input_path = os.path.join(app.config["UPLOAD_FOLDER"], "uploaded_image.jpg")
            output_path = os.path.join(app.config["UPLOAD_FOLDER"], "generated_meme.jpg")

            file.save(input_path)

            generate_meme(input_path, top_text, bottom_text, output_path)

            generated_filename = "generated_meme.jpg"

    return render_template("index.html", meme_filename=generated_filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
