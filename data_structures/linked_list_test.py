import unittest
import linked_list

class TestLinkedList(unittest.TestCase):
	def test_node_get_data(self):
		node = linked_list.Node(10)
		self.assertTrue(node.get_data(), 10)

	def test_list_creation(self):
		my_list = linked_list.List(linked_list.Node(2))
		self.assertEqual(my_list.get_head().get_data(), 2)
		self.assertEqual(my_list.get_tail().get_data(), 2)

	def test_append(self):
		my_list = linked_list.List(linked_list.Node(5))
		node = linked_list.Node(7)
		my_list.append(node)
		self.assertEqual(my_list.get_tail().get_data(),7)
		self.assertEqual(my_list.get_head().get_next().get_data(),7)

	def test_remove_head(self):
		my_list = linked_list.List(linked_list.Node(5))
		node = linked_list.Node(7)
		my_list.append(node)
		my_list.remove(linked_list.Node(5))
		self.assertEqual(my_list.get_head().get_data(),7)

	def test_remove_tail(self):
		my_list = linked_list.List(linked_list.Node(5))
		node = linked_list.Node(7)
		my_list.append(node)
		my_list.remove(node)
		self.assertEqual(my_list.get_tail().get_data(),5)

	def test_remove_node(self):
		my_list = linked_list.List(linked_list.Node(5))
		node = linked_list.Node(7)
		my_list.append(node)
		my_list.append(linked_list.Node(9))
		my_list.remove(node)
		self.assertEqual(my_list.get_head().get_data(),5)
		self.assertEqual(my_list.get_head().get_next().get_data(),9)
		self.assertEqual(my_list.get_tail().get_data(),9)

if __name__ == '__main__':
	unittest.main()		
