html_tag_paragraph = "p"
html_tag_link = "a"
from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("Value is required for LeafNode")
        super().__init__(tag, value, [], props)
    def to_html(self):
        props_html = self.props_to_html()
        if self.tag == html_tag_paragraph:
            return f"<p {props_html}>{self.value}</p>" if props_html else f"<p>{self.value}</p>"
        elif self.tag == html_tag_link:
            return f"<a {props_html}>{self.value}</a>" if props_html else f"<a>{self.value}</a>"
        else:
            return self.value
