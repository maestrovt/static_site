class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag if tag is not None else ''
        self.value = value if value is not None else ''
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    def props_to_html(self):
        props_list = [f'{key}="{value}"' for key, value in self.props.items()]
        return ' ' + ' '.join(props_list) if props_list else ''
    def __repr__(self):
        props_list = [f'{key}="{value}"' for key, value in self.props.items()]
        return f"HTMLNode(tag = {self.tag}, value = {self.value}, " + "children = " + ', '.join(self.children) + ", props = " + ' '.join(props_list)+")"
