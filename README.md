# Python Flask Payment

This is a sample project demonstrating how to create a simple web application using **Flask** to simulate a payment method similar to PIX (a Brazilian electronic payment system). Here are the key components of the project:

## Description

The goal of this project is to simulate an electronic payment system inspired by PIX, using the Flask framework. It includes features such as QR code generation for payments, data storage in an SQLite database, and asynchronous communication with WebSockets to wait for payment confirmation.

## Main Files

1. **app.py**: This file serves as the entry point of the application. It contains the main logic for handling routes, authentication, and payment processing.
2. **requirements.txt**: Lists the Python dependencies required to run the application.
3. **instance**: A folder that can contain environment-specific configurations (development, testing, production).
4. **models**: Contains the data models used in the application.
5. **templates**: This folder holds the HTML files for rendering the application pages.
6. **static**: Here, you can store static files such as CSS, JavaScript, and images.

## How to Run

1. Make sure you have Python installed on your machine.
2. Clone this repository: `git clone https://github.com/LuizHumphries/Python_Flask_Payment.git`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python app.py`
5. Access the application in your browser at `http://localhost:5000`

## Features

1. **QR Code Generation**: The application allows generating QR codes for payments, simulating the functionality of PIX payments.
2. **Data Storage**: Payment data is stored in an SQLite database.
3. **Asynchronous Communication**: The use of WebSockets allows the application to wait for payment confirmation asynchronously.

## Contribution

Feel free to contribute with improvements, bug fixes, or new features. Just open an **issue** or submit a **pull request**.

## License

This project is licensed under the MIT License.

---

If you have any questions or need further information, feel free to ask! 🚀
