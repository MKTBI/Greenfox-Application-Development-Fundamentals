class BlogPost:
    def __init__(self, authorName, title, text, publicationDate):
        self.authorName = authorName
        self.title = title
        self.text = text
        self.publicationDate = publicationDate

post1 = BlogPost("John Doe", "Lorem Ipsum", "Lorem ipsum dolor sit amet.", "2000.05.04.")
post2 = BlogPost("Tim Urban", "Wait but why", "A popular long-form, stick-figure-illustrated blog about almost everything.", "2010.10.10.")
post3 = BlogPost("William Turton", "One Engineer Is Trying to Get IBM to Reckon With Trump", "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing.", "2017.03.28.")

print(post1.title)
print(post3.publicationDate)

class Blog:
    def __init__(self):
        self.listOfPosts = []
        
    def add(self, post):
        self.listOfPosts.append(post)
        
    def delete(self, index):
        self.listOfPosts.pop(index)
        
    def update(self, index, post):
        self.listOfPosts[index] = post
    

blog = Blog()

blog.add(post1)
blog.add(post2)
blog.add(post3)

blog.delete(1)

new_post = BlogPost("Jane Smith", "The power of mindfulness", "Learn how to live in the present moment.", "2022.01.01.")
blog.update(0, new_post)

for post in blog.listOfPosts:
    print("Title: " + post.title)
    print("Author: " + post.authorName)
    print("Publication Date: " + post.publicationDate)
    print("Text: " + post.text)
    print("\n")
