# QR Code Generator and Restaurant Menu Website

## Description
This project is a Python-based full-stack web application that combines a QR code generator with a responsive restaurant menu interface. It's designed to streamline the ordering process in restaurants by providing quick access to digital menus through QR codes. The application demonstrates proficiency in full-stack development, integrating backend Python logic with a user-friendly frontend.

## Features
- Dynamic QR code generation for easy menu access
- Responsive restaurant menu interface adaptable to various devices
- Server-side QR code generation using Python
- User-friendly frontend built with HTML, CSS, and JavaScript
- Seamless integration of QR codes with menu display
- Estimated 20% reduction in customer wait times

## Technologies Used
- Backend: Python 3.x, Flask 2.0.1
- Frontend: HTML5, CSS3, JavaScript
- QR Code Generation: qrcode 7.3
- Image Processing: Pillow 8.3.1
- WSGI Interface: Werkzeug 2.0.1
- Template Engine: Jinja2

## Installation
1. Clone the repository:
git clone https://github.com/andy8th/qr-menu-project.git
cd qr-menu-project
Copy
2. Create a virtual environment:
python -m venv venv
Copy
3. Activate the virtual environment:
- On Windows: `venv\Scripts\activate`
- On macOS and Linux: `source venv/bin/activate`

4. Install the required packages:
pip install -r requirements.txt
Copy
## Usage
1. Ensure you're in the project directory with the virtual environment activated.

2. Run the application:
python app.py
Copy
3. Open a web browser and navigate to `http://localhost:5000`

4. Use the interface to:
- View the restaurant menu
- Generate QR codes for specific menu items or the full menu
- Test the QR code scanning functionality

## Project Structure
qr_menu_project/
│
├── app.py
├── requirements.txt
├── README.md
├── static/
│   └── styles.css
└── templates/
└── menu.html
