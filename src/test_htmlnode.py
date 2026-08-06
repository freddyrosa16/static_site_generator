import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_HTML_tag_children(self):
        node = HTMLNode(tag="div", children="p")
        node.props_to_html()

    def test_HTML(self):
        node = HTMLNode(
            tag="p",
            value="I like boot.dev",
            children="a",
            props={"href": "boot.dev"},
        )
        node.props_to_html()
