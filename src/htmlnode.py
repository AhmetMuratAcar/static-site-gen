class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""

        stringified = ""
        for key, value in self.props.items():
            stringified += f' {key}="{value}"'

        return stringified

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return NotImplemented

        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def __repr__(self):
        return f"tag = {self.tag}\nvalue = {self.value}\nchildren = {self.children}\nprops = {self.props}"
