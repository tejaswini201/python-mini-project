{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "70fc6a79-3094-460a-af6d-8f7cf00dd0ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Product  Quantity  Price         Category   Unit\n",
      "0          Apple       200   1.50            Fruit     kg\n",
      "1         Banana       300   0.75            Fruit     kg\n",
      "2         Orange       240   2.00            Fruit     kg\n",
      "3           Milk        20   3.00            Dairy  liter\n",
      "4          Bread       100   1.50           Bakery   pack\n",
      "5         Carrot       160   1.00        Vegetable     kg\n",
      "6         Tomato       180   0.75        Vegetable     kg\n",
      "7        Spinach       140   1.25        Vegetable     kg\n",
      "8      Chocolate        50   2.50            Snack   pack\n",
      "9        Cookies        60   1.75            Snack   pack\n",
      "10        Grapes       120   2.50            Fruit     kg\n",
      "11      Broccoli       100   1.80        Vegetable     kg\n",
      "12        Potato       150   0.50        Vegetable     kg\n",
      "13         Onion       200   0.75        Vegetable     kg\n",
      "14          Rice        80   4.00            Grain     kg\n",
      "15       Chicken       100   5.00             Meat     kg\n",
      "16          Soap       150   2.00  Home Essentials   unit\n",
      "17  Toilet Paper       100   3.50  Home Essentials   pack\n",
      "18     Detergent        80   6.00  Home Essentials   pack\n",
      "19           Pen        50   1.00       Stationary   unit\n",
      "20      Notebook        60   2.50       Stationary   unit\n",
      "21        Pencil        70   0.50       Stationary   unit\n",
      "22        Eraser        80   0.25       Stationary   unit\n",
      "23     Sharpener        90   0.75       Stationary   unit\n",
      "24    Toothpaste       100   1.80    Personal Care   unit\n",
      "25       Shampoo        80   4.50    Personal Care   unit\n",
      "26   Conditioner        70   5.00    Personal Care   unit\n",
      "27         Towel        50   8.00  Home Essentials   unit\n",
      "28        Cheese        30   2.75            Dairy     kg\n",
      "29        Yogurt        40   1.50            Dairy   pack\n",
      "30         Sugar       100   2.00        Groceries     kg\n",
      "31          Salt       120   1.00        Groceries     kg\n",
      "32      Biscuits        60   2.50            Snack   pack\n",
      "33           Tea        90   3.00         Beverage   pack\n",
      "34        Coffee       110   4.00         Beverage   pack\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Read product information from CSV file\n",
    "df_products = pd.read_csv('products.csv')\n",
    "\n",
    "# Display the product DataFrame\n",
    "print(df_products)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b32d5cf-c1b2-434b-8d62-dd24f65cf29a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "anaconda-panel-2023.05-py310",
   "language": "python",
   "name": "conda-env-anaconda-panel-2023.05-py310-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
