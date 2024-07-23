import unittest

from htmlnode import HTMLNode

test_props = {
    "href": "https://www.google.com",
    "target": "_blank",
}


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="p", value="ijinnamo", children=None, props=test_props)
        node2 = HTMLNode(tag="p", value="ijinnamo", children=None, props=test_props)
        self.assertEqual(node, node2)

    def test_ineq(self):
        node = HTMLNode(tag="p", value="ijinnamo", children=None, props=test_props)
        node2 = HTMLNode(tag="p", value="ijinnamo", children=None, props=None)
        self.assertNotEqual(node, node2)

    def test_defaults(self):
        node = HTMLNode(tag="p", value="ijinnamo", props=test_props)
        node2 = HTMLNode(tag="p", value="ijinnamo", children=None, props=test_props)
        self.assertEqual(node.children, node2.children)


if __name__ == "__main__":
    unittest.main()
