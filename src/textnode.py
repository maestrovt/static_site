class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        if not url:
            self.url = None
        self.url = url