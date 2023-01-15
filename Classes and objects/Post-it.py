class PostIt:
    def __init__(self, background_color, text, text_color):
        self.background_color = background_color
        self.text = text
        self.text_color = text_color

postit1 = PostIt("orange", "Idea 1", "blue")
postit2 = PostIt("pink", "Awesome", "black")
postit3 = PostIt("yellow", "Superb!", "green")

print(postit1.background_color) 
print(postit2.text) 
print(postit3.text_color) 
