from inline_markdown import extract_markdown_images, extract_markdown_links

text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
print(extract_markdown_images(text))
# [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]

text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
print(extract_markdown_links(text))
# [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]

text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)"
image_list = extract_markdown_images(text)
for image in image_list:
    print(image[0])
    print(image[1])
    print(text.split(f"![{image[0]}]({image[1]})", 1))

