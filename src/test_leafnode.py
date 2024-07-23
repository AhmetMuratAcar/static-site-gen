import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_no_props_to_html(self):
        answer = "<p>This is a paragraph of text.</p>"
        node = LeafNode(tag="p", value="This is a paragraph of text.")
        self.assertEqual(answer, node.to_html())

    def test_with_props_to_html(self):
        answer = '<a href="https://www.google.com">Click me!</a>'
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(answer, node.to_html())

    def test_no_value_to_html(self):
        # answer = ValueError("LeafNode must have a value")
        node = LeafNode(tag="p", props={"href": "https://www.google.com"})
        self.assertRaises(ValueError, node.to_html)

    def test_children_presence(self):
        children = None
        node = LeafNode()
        self.assertEqual(children, node.children)


if __name__ == "__main__":
    unittest.main()
