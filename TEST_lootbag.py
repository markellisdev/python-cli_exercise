import unittest
from lootbag import *

class TestBag(unittest.TestCase):

	def test_toy_can_be_added_to_bag(self):
		bag = LootBag()
		toy = 'transformer'
		child = 'Ken'

		# Add toy to bag
		bag.add_toy_for_child(toy, child) #Here we're agreeing this function will be created
		print('A ' + bag.toy + ' was added to the toy bag')

		# Get child's toys
		ken_toys = bag.get_toy_by_child(child) #Here we're agreeing this function will be created

		# Verify toy was added
		self.assertIn(toy, ken_toys)

	def test_toy_can_be_removed_for_child(self):
		bag = LootBag() #This is the only instance within this scope
		toy = 'monkey'
		child = 'Ken'

		# Add toy to bag
		bag.add_toy_for_child(toy, child)
		print(bag.toy)

		# Get child's toys
		ken_toys = bag.get_toy_by_child(child)

		# Verify toy was added -needed before removal would be possible
		self.assertIn(toy, ken_toys)

		# Remove toy from bag
		updated_toys = bag.remove_toy_from_child(toy, child)

		# Verify toy was removed
		self.assertNotIn(toy, updated_toys)

	def test_can_list_children_receiving_toys(self):
		bag = LootBag()
		bag.add_toy_for_child('Duct Tape', "Ben")
		bag.add_toy_for_child('Hair accessories', 'Drew')
		bag.add_toy_for_child('Google course', 'Trent')
		bag.add_toy_for_child('Ninjago Zane', 'Kahnu')

		#Verify toys in bag
		good_children = bag.list_good_children()

		self.assertGreater(len(good_children), 0) #Does list have items?
		self.assertIn('Ben', good_children) #Is Jimmy in it?
		self.assertIn('Drew', good_children) #Is Wes in it?
		self.assertIn('Trent', good_children) #Is Anne in it?
		self.assertIn('Kahnu', good_children) #Is Kahnu in it?

	def test_Can_list_single_child_toys(self):
		bag = LootBag()
		bag.add_toy_for_child('tank', 'Tim')
		bag.add_toy_for_child('robot', 'Tim')
		bag.add_toy_for_child('doll', 'Anne')
		bag.add_toy_for_child('Ninjago Zane', 'Kahnu')

		single_child_list = bag.get_toy_by_child('Tim')

		self.assertGreater(len(single_child_list), 0)

	def test_toys_can_be_delivered_to_child(self):
		bag = LootBag()
		bag.add('tank', 'Tim')
		bag.add('robot', 'Tim')
		bag.add('doll', 'Anne')
		bag.add('Ninjago Zane', 'Kahnu')

		self.assertFalse(bag.is_child_happy('Tim'))	#Make sure child isn't already happy(toys delivered)
		bag.deliver_toys_to_child('Tim') #method to reflect an action
		self.assertTrue(bag.is_child_happy('Tim'))













if __name__ == '__main__':
	unittest.main()
