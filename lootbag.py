import sys
import sqlite3

def main(args):
	print(args, " main arguments")

class LootBag():


	def __init__(self, toy = None, child = None):
		self.good_children = dict()
		self.toy = toy
		self.child = child

	def add_toy_for_child(self, toy, child):
		children = set()
		children.add(child)
		self.toy = toy

		with sqlite3.connect('lootbag.db') as conn:
			c = conn.cursor()

			try:
				c.execute("INSERT INTO Child VALUES (?, ?, ?)",
					(None, child, 0))
			except sqlite3.OperationalError:
				pass

			c.execute("select ChildId FROM Child WHERE Name='{}'".format(child)) #need single '' around {} because it is string
			# [(1)]
			results = c.fetchall() #returns tuples (or each row) within table

			try:
				c.execute("INSERT INTO Toy VALUES (?, ?, ?)",
					(None, toy, results[0][0]))
			except sqlite3.OperationalError:
				pass

 # This was code to make test pass -----------------------------------------
	# 	try:
	# 		self.good_children[child].append(toy) #Trying to append, if not key error

	# 	except KeyError:
	# 		self.good_children[child] = dict()
	# 		self.good_children[child]['delivered'] = False
	# 		self.good_children[child] = list()
	# 		self.good_children[child].append(toy)

	def remove_toy_from_child(self, toy, child):

		with sqlite3.connect('lootbag.db') as conn:
			c = conn.cursor()

			c.execute("select ChildId FROM Child WHERE Name='{}'".format(child)) #need single '' around {} because it is string
			# [(1)]
			results = c.fetchall()

			try:
				c.execute("DELETE FROM toy WHERE ChildId={} AND Name='{}'".format(results[0][0], toy))
			except sqlite3.OperationalError:
				pass


# This was code to make test pass ------------------------------------------
# 		try:
# 			self.good_children[child].remove(toy)
# 		except KeyError:
# 			pass

	def get_toy_by_child(self, child):
		with sqlite3.connect('lootbag.db') as conn:
			c = conn.cursor()

# --- Enclosing in three " enables writing multi-line string ---
			c.execute("""SELECT t.Name
				FROM Toy t, Child c
				WHERE c.Name='{}'
				AND c.ChildId = t.ChildId
			""".format(child))

			toys = c.fetchall()

			print(toys)

 # This was code to make test pass ----------------------------------
	# 	return [child for child in self.good_children.keys()]

	# def get_child(self):
	# 	return self.toy

	def list_all_children(self):

		with sqlite3.connect('lootbag.db') as conn:
			c = conn.cursor()

			c.execute("""SELECT c.Name
				FROM Child c, Toy t
				WHERE t.ToyId
				AND c.ChildId = t.ChildId
			""")
			results = c.fetchall()

			print(results) #This works but repeats name. Change to set to only have one

# Original code to pass test
# 		return [kid for kid in self.good_children.keys()] #returning list of all (keys) children


if __name__ == "__main__":
	bag = LootBag()
	print(sys.argv)
	if sys.argv[1] == "add":
		bag.add_toy_for_child(sys.argv[2], sys.argv[3])
		print(bag.get_toy_by_child(sys.argv[3]))
	elif sys.argv[1] == "remove":
		bag.remove_toy_from_child(sys.argv[2], sys.argv[3])
		print(bag.get_toy_by_child(sys.argv[3]))
	elif sys.argv[1] == "ls":
		bag.get_toy_by_child(sys.argv[2])
	elif sys.argv[1] == "ls_all":
		bag.list_all_children()

