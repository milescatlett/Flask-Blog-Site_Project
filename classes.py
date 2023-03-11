

class Tag:
    def __init__(self, tag_name):
        self.tag_name = tag_name
        self.full_tag = f"<{self.tag_name}></{self.tag_name}>"

    def add(self, item, val):
        lst = self.full_tag.split("<" + self.tag_name)
        lst.insert(1, f"<{self.tag_name} {item}='{val}'")
        self.full_tag = "".join(lst)

    def add_class(self, cls=[]):
        lst = list()
        cls = " ".join(cls)
        if "class" not in self.full_tag:
            lst = self.full_tag.split("<" + self.tag_name)
            lst.insert(1, f"<{self.tag_name} class='{cls}'")
        if "class" in self.full_tag:
            lst = self.full_tag.split("class='")
            lst.insert(1, f"class='{cls} ")
        self.full_tag = "".join(lst)

    def add_innerHTML(self, innerHTML):
        lst = self.full_tag.split("></")
        lst.insert(1, f">{innerHTML}</")
        self.full_tag = "".join(lst)

    def display(self):
        return self.full_tag

