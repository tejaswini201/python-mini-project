#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

# Define initial products and their quantities
initial_products = {
    'Product': ['Apple', 'Banana', 'Orange', 'Milk', 'Bread', 'Carrot', 'Tomato', 'Spinach', 'Chocolate', 'Cookies',
                'Grapes', 'Broccoli', 'Potato', 'Onion', 'Rice', 'Chicken', 'Soap', 'Toilet Paper', 'Detergent',
                'Pen', 'Notebook', 'Pencil', 'Eraser', 'Sharpener', 'Toothpaste', 'Shampoo', 'Conditioner', 'Towel', 'Cheese', 
                'Yogurt', 'Sugar', 'Salt', 'Biscuits', 'Tea', 'Coffee'],
    'Quantity': [200, 300, 240, 20, 100, 160, 180, 140, 50, 60, 120, 100, 150, 200, 80, 100, 150, 100, 80, 50, 60, 70, 80, 90, 100,80, 70, 50, 30, 40, 100, 120, 60, 90, 110],
    'Price': [1.50, 0.75, 2.00, 3.00, 1.50, 1.00, 0.75, 1.25, 2.50, 1.75, 2.50, 1.80, 0.50, 0.75, 4.00, 5.00, 2.00, 3.50, 6.00,
              1.00, 2.50, 0.50, 0.25, 0.75, 1.80, 4.50, 5.00, 8.00, 2.75, 1.50, 2.00, 1.00, 2.50, 3.00, 4.00],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Dairy', 'Bakery', 'Vegetable', 'Vegetable', 'Vegetable', 'Snack', 'Snack',
                 'Fruit', 'Vegetable', 'Vegetable', 'Vegetable', 'Grain', 'Meat', 'Home Essentials', 'Home Essentials', 'Home Essentials',
                 'Stationary', 'Stationary', 'Stationary', 'Stationary', 'Stationary', 'Personal Care', 'Personal Care', 'Personal Care', 'Home Essentials', 'Dairy', 'Dairy', 'Groceries', 'Groceries', 'Snack', 'Groceries', 'Groceries'],
    'Unit': ['kg', 'kg', 'kg', 'liter', 'pound', 'kg', 'kg', 'kg', 'pack', 'pack',
             'kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'pack', 'pack', 'pack', 'unit',
             'unit', 'unit', 'unit', 'unit', 'unit', 'liter', 'liter', 'unit', 'kg', 'pack', 'kg', 'kg', 'pack', 'kg', 'kg']
}

# Create DataFrame for products
df_products = pd.DataFrame(initial_products)

# Fixing price per kg for applicable items
df_products.loc[df_products['Product'].isin(['Apple', 'Banana', 'Orange', 'Grapes']), 'Price'] /= 1.5
df_products.loc[df_products['Product'].isin(['Potato', 'Onion']), 'Price'] /= 0.5

# Define offers
offers = {
   import pandas as pd

# Define initial products and their quantities
initial_products = {
    'Product': ['Apple', 'Banana', 'Orange', 'Milk', 'Bread', 'Carrot', 'Tomato', 'Spinach', 'Chocolate', 'Cookies',
                'Grapes', 'Broccoli', 'Potato', 'Onion', 'Rice', 'Chicken', 'Soap', 'Toilet Paper', 'Detergent',
                'Pen', 'Notebook', 'Pencil', 'Eraser', 'Sharpener', 'Toothpaste', 'Shampoo', 'Conditioner', 'Towel', 'Cheese', 
                'Yogurt', 'Sugar', 'Salt', 'Biscuits', 'Tea', 'Coffee'],
    'Quantity': [200, 300, 240, 20, 100, 160, 180, 140, 50, 60, 120, 100, 150, 200, 80, 100, 150, 100, 80, 50, 60, 70, 80, 90, 100,80, 70, 50, 30, 40, 100, 120, 60, 90, 110],
    'Price': [1.50, 0.75, 2.00, 3.00, 1.50, 1.00, 0.75, 1.25, 2.50, 1.75, 2.50, 1.80, 0.50, 0.75, 4.00, 5.00, 2.00, 3.50, 6.00,
              1.00, 2.50, 0.50, 0.25, 0.75, 1.80, 4.50, 5.00, 8.00, 2.75, 1.50, 2.00, 1.00, 2.50, 3.00, 4.00],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Dairy', 'Bakery', 'Vegetable', 'Vegetable', 'Vegetable', 'Snack', 'Snack',
                 'Fruit', 'Vegetable', 'Vegetable', 'Vegetable', 'Grain', 'Meat', 'Home Essentials', 'Home Essentials', 'Home Essentials',
                 'Stationary', 'Stationary', 'Stationary', 'Stationary', 'Stationary', 'Personal Care', 'Personal Care', 'Personal Care', 'Home Essentials', 'Dairy', 'Dairy', 'Groceries', 'Groceries', 'Snack', 'Groceries', 'Groceries'],
    'Unit': ['kg', 'kg', 'kg', 'liter', 'pound', 'kg', 'kg', 'kg', 'pack', 'pack',
             'kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'pack', 'pack', 'pack', 'unit',
             'unit', 'unit', 'unit', 'unit', 'unit', 'liter', 'liter', 'unit', 'kg', 'pack', 'kg', 'kg', 'pack', 'kg', 'kg']
}

# Create DataFrame for products
df_products = pd.DataFrame(initial_products)

# Fixing price per kg for applicable items
df_products.loc[df_products['Product'].isin(['Apple', 'Banana', 'Orange', 'Grapes']), 'Price'] /= 1.5
df_products.loc[df_products['Product'].isin(['Potato', 'Onion']), 'Price'] /= 0.5

# Define offers
offers = {
    global df_products
    index = df_products[df_products['Product'] == product].index
    if len(index) == 0:
        print("Sorry, that product is not available.")
        return bill_df_purchased, bill_df_free, 0
    current_quantity = df_products.loc[index, 'Quantity'].values[0]
    if current_quantity < quantity:
        print("Sorry, there is not enough stock for your request.")
        return bill_df_purchased, bill_df_free, 0
    df_products.loc[index, 'Quantity'] -= quantity
    price_per_unit = df_products.loc[index, 'Price'].values[0]
    total_price = price_per_unit * quantity
    print(f"You have successfully bought {quantity} {df_products.loc[index, 'Unit'].values[0]} of {product} for ${total_price:.2f}.")

    # Apply offer if applicable
    bill_df_purchased, bill_df_free = apply_offer(product, quantity, bill_df_purchased, bill_df_free)

    bill_df_purchased = pd.concat([bill_df_purchased, pd.DataFrame({'Product': [product], 'Quantity': [quantity], 'Total Price': [total_price]})], ignore_index=True)
    return bill_df_purchased, bill_df_free, total_price

def update_stock(product, quantity):
    """Update stock for a product."""
    global df_products
    index = df_products[df_products['Product'] == product].index
    if len(index) == 0:
        print("Sorry, that product is not available.")
        return
    df_products.loc[index, 'Quantity'] += quantity
    if df_products.loc[index, 'Quantity'].values[0] < 20:
        print(f"Warning: Stock for {product} is low. Please restock.")
    else:
        print(f"Stock for {product} has been updated by {quantity}.")

def simulate_purchase():
    """Simulate a purchase."""
    display_products()
    total_bill = 0
    bill_df_purchased = pd.DataFrame(columns=['Product', 'Quantity', 'Total Price'])
    bill_df_free = pd.DataFrame(columns=['Product', 'Quantity', 'Total Price'])
    while True:
        product = input("Enter the product you want to buy (or type 'done' to finish): ")
        if product.lower() == 'done':
            break
        if product not in df_products['Product'].tolist():
            print("Invalid product! Please choose a product from the list.")
            continue
        try:
            quantity = float(input(f"Enter the quantity of {product}: "))
        except ValueError:
            print("Invalid input! Quantity must be a number.")
            continue
        if quantity <= 0:
            print("Invalid input! Quantity must be greater than zero.")
            continue    
        bill_df_purchased, bill_df_free, product_price = buy_product(product, quantity, bill_df_purchased, bill_df_free)
        total_bill += product_price
    if not bill_df_purchased.empty:
        print("\nPurchased Items:")
        print(bill_df_purchased)
    else:
        print("No items purchased.")
    if not bill_df_free.empty:
        print("\nFree Items:")
        print(bill_df_free)
    if not bill_df_purchased.empty:
        print(f"\nTotal bill for purchased items: ${total_bill:.2f}")
    print()

def simulate_stock_update():
    """Simulate updating stock."""
    display_products()
    product = input("Enter the product you want to update: ")
    quantity = int(input(f"Enter the quantity you want to add ({df_products.loc[df_products['Product'] == product, 'Unit'].values[0]}): "))
    update_stock(product, quantity)
    print()
    display_products()

def main():
    """Main function to run the supermarket simulation."""
    while True:
        print("1. Buy Product")
        print("2. Update Stock")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            simulate_purchase()
        elif choice == '2':
            simulate_stock_update()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
        print()

if __name__ == "__main__":
    main()


# In[ ]:




