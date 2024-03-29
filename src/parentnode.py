html_tag_paragraph = "p"
html_tag_link = "a"
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, "", children, props)
        if tag is None:
            raise ValueError("tag is required")
        if children is None:
            raise ValueError("children are required")
    def to_html(self):
        # Ensure the node has a tag
        if not self.tag:
            raise ValueError("Tag is required")

        # Ensure there are children
        if not self.children:
            raise ValueError("At least one child is required")

        # Start the HTML string with the opening tag
        html = f"<{self.tag}>"
        html += self.props_to_html()

        # Iterate through the children and recursively call to_html on each
        for child in self.children:
           html += child.to_html()
        # Close the tag
        html += f"</{self.tag}>"

        return html
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
        