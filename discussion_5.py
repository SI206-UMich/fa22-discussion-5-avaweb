import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in range(len(sentence)):
		if sentence[i] == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		tempVal = self.items[0].stock
		tempItem = self.items[0]
		for i in self.items:
			if i.stock > tempVal:
				tempVal = i.stock
				tempItem = i
		return tempItem


	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		tempVal = self.items[0].price
		tempItem = self.items[0]
		for i in self.items:
			if i.price > tempVal:
				tempVal = i.price 
				tempItem = i
		return tempItem



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a('a'), 1)
		self.assertEqual(count_a('abc'), 1)
		self.assertEqual(count_a('a a a'), 3)
		self.assertEqual(count_a('hello world'), 0)
		self.assertEqual(count_a('my name is ava'), 3)
		self.assertEqual(count_a('sea'), 1)


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		items_list = [self.item1, self.item2, self.item3, self.item4]
		warehouse = Warehouse(items_list)
		warehouse.add_item(self.item5)
		self.assertEqual(warehouse.items[4], self.item5)
		items_list2 = []
		warehouse2 = Warehouse(items_list2)
		warehouse2.add_item(self.item1)
		warehouse2.add_item(self.item2)
		self.assertEqual(warehouse2.items[0], self.item1)
		self.assertEqual(warehouse2.items[1], self.item2)

	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		items_list = [self.item1, self.item2, self.item3, self.item4, self.item5]
		warehouse = Warehouse(items_list)
		self.assertEqual(warehouse.get_max_stock(), self.item3)
		items_list2 = [self.item1]
		warehouse2 = Warehouse(items_list2)
		self.assertEqual(warehouse2.get_max_stock(), self.item1)



	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		items_list = [self.item1, self.item2, self.item3, self.item4, self.item5]
		warehouse = Warehouse(items_list)
		self.assertEqual(warehouse.get_max_price(), self.item1)
		items_list2 = [self.item3]
		warehouse2 = Warehouse(items_list2)
		self.assertEqual(warehouse2.get_max_price(), self.item3)
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()