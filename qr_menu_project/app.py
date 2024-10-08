from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

menu = {
    "Appetizers": ["Salad", "Soup", "Bruschetta"],
    "Main Courses": ["Pasta", "Steak", "Fish"],
    "Desserts": ["Ice Cream", "Cake", "Fruit Platter"]
}

@app.route('/')
def home():
    return render_template('menu.html', menu=menu)

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    url = request.url_root
    
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    
    return send_file(buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)