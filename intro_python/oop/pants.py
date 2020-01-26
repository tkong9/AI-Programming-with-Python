### TODO:
#   - code a Pants class with the following attributes
#   - color (string) eg 'red', 'yellow', 'orange'
#   - waist_size (integer) eg 8, 9, 10, 32, 33, 34
#   - length (integer) eg 27, 28, 29, 30, 31
#   - price (float) eg 9.28
class Pants:
    def __init__(self, color, waist_size, length, price):
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price


### TODO: Declare the Pants Class

### TODO: write an __init__ function to initialize the attributes

### TODO: write a change_price method:
#    Args:
#        new_price (float): the new price of the shirt
#    Returns:
#        None
    def change_price(self, new_price):
        self.price = new_price

### TODO: write a discount method:
#    Args:
#        discount (float): a decimal value for the discount.
#            For example 0.05 for a 5% discount.
    def discount(self, discount):
        self.price = self.price * (1 - discount)
#
#    Returns:
#        float: the discounted price
        return self.price

def check_results():
    pants = Pants('red', 35, 36, 15.12)
    assert pants.color == 'red'
    assert pants.waist_size == 35
    assert pants.length == 36
    assert pants.price == 15.12

    pants.change_price(10) == 10
    assert pants.price == 10

    assert pants.discount(.1) == 9

    print('You made it to the end of the check. Nice job!')

check_results()

### TODO:
#   Code a SalesPerson class with the following attributes
#   - first_name (string), the first name of the salesperson
#   - last_name (string), the last name of the salesperson
#   - employee_id (int), the employee ID number like 5681923
#   - salary (float), the monthly salary of the employee
#   - pants_sold (list of Pants objects),
#            pants that the salesperson has sold
#   - total_sales (float), sum of sales of pants sold
class SalesPerson:


### TODO: Declare the SalesPerson Class

### TODO: write an __init__ function to initialize the attributes
###    Input Args for the __init__ function:
#        first_name (str)
#        last_name (str)
#        employee_id (int)
# .      salary (float)

    def __init__(self, first_name, last_name, employee_id, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
#
# You can initialize pants_sold as an empty list
# You can initialize total_sales to zero.
#
###
        self.pants_sold = []
        self.total_sales = 0

### TODO: write a sell_pants method:
#
#    This method receives a Pants object and appends
#    the object to the pants_sold attribute list
#
#    Args:
#        pants (Pants object): a pants object
#    Returns:
#        None
    def sell_pants(self, pant):
        self.pants_sold.append(pant)

### TODO: write a display_sales method:
#
#    This method has no input or outputs. When this method
#    is called, the code iterates through the pants_sold list
#    and prints out the characteristics of each pair of pants
#    line by line. The print out should look something like this
#
#   color: blue, waist_size: 34, length: 34, price: 10
#   color: red, waist_size: 36, length: 30, price: 14.15
#
#
#
###
    def display_sales(self):
        for pant in self.pants_sold:
            print("color: {}, waist_size: {}, length: {}, price: {}".format(pant.color, pant.waist_size, pant.length, pant.price))

### TODO: write a calculate_sales method:
#      This method calculates the total sales for the sales person.
#      The method should iterate through the pants_sold attribute list
#      and sum the prices of the pants sold. The sum should be stored
#      in the total_sales attribute and then return the total.
#
#      Args:
#        None
#      Returns:
#        float: total sales
#
###
    def calculate_sales(self):
        for pant in self.pants_sold:
            self.total_sales += pant.price
        return self.total_sales

### TODO: write a calculate_commission method:
#
#   The salesperson receives a commission based on the total
#   sales of pants. The method receives a percentage, and then
#   calculate the total sales of pants based on the price,
#   and then returns the commission as (percentage * total sales)
#
#    Args:
#        percentage (float): comission percentage as a decimal
#
#    Returns:
#        float: total commission
#
#
###
    def calculate_commission(self, comission):
        return self.total_sales * comission


def check_results():
    pants_one = Pants('red', 35, 36, 15.12)
    pants_two = Pants('blue', 40, 38, 24.12)
    pants_three = Pants('tan', 28, 30, 8.12)

    salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)

    assert salesperson.first_name == 'Amy'
    assert salesperson.last_name == 'Gonzalez'
    assert salesperson.employee_id == 2581923
    assert salesperson.salary == 40000
    assert salesperson.pants_sold == []
    assert salesperson.total_sales == 0

    salesperson.sell_pants(pants_one)
    salesperson.pants_sold[0] == pants_one.color

    salesperson.sell_pants(pants_two)
    salesperson.sell_pants(pants_three)

    assert len(salesperson.pants_sold) == 3
    assert round(salesperson.calculate_sales(), 2) == 47.36
    assert round(salesperson.calculate_commission(.1), 2) == 4.74


    print('Great job, you made it to the end of the code checks!')


check_results()
