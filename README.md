# python-mini-project
Supermarket Management System
Overview
This Python-based supermarket management system simulates a shopping experience for users. It includes functionalities such as browsing available products, selecting items for purchase, applying offers or discounts, generating a bill, and handling product stock levels.

Features
Product Management: Products are organized into categories such as fruits, vegetables, dairy, groceries, snacks, beverages, home essentials, stationary, and personal care. Each product has attributes such as name, quantity, price, category, and unit.
User Interaction: Users can interact with the system by selecting products they wish to purchase and specifying the desired quantity. The system validates user input and ensures that requested quantities are available in stock.
Offers and Discounts: The system supports predefined offers and discounts for certain products, such as buy-one-get-one-free offers, free items with a minimum purchase quantity, and other promotional deals.
Bill Generation: After completing their shopping, users receive a detailed bill summarizing their purchases, including purchased items, quantities, prices, any free items received through offers, and the total bill amount.
Error Handling: The project includes error handling mechanisms to handle invalid user input, out-of-stock products, and other potential issues that may arise during the shopping process.
Scalability and Modularity: The project is designed to be modular and scalable, allowing for easy expansion of the product list, addition of new features, and integration with other systems or modules.
Getting Started
To run the supermarket management system:

Ensure you have Python installed on your system.
Clone this repository to your local machine.
Navigate to the project directory.
Run the main Python script
python supermarket.py
Files Included
supermarket.py: Main Python script containing the implementation of the supermarket management system.
products.csv: CSV file containing the list of products used in the supermarket management system.
read_products.py: Python script to read the product information from the products.csv file.
Dependencies
Python 3.x
pandas library
License
This project is licensed under the MIT License.
