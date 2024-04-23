import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        #print(f"\nOld Node: {old_node.text}")
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        image_list = extract_markdown_images(old_node.text)
        #print(f"\nImage List: {image_list}")
        if len(image_list) == 0:
            new_nodes.append(old_node)
            continue
        text_list = []
        temp = old_node.text
        for img, url in image_list:
            item = temp.split(f"![{img}]({url})", 1)
            #print(f"\nSplit Item List: {item}")
            if len(item) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            text_list.append(item[0])
            temp = item[1]
        #print(f"\nText List: {text_list}")
        for i, image_tup in enumerate(image_list):
            if text_list[i] != "":
                new_nodes.append(TextNode(text_list[i], text_type_text))
            new_nodes.append(TextNode(image_tup[0], text_type_image, image_tup[1]))
        if temp != "":
            new_nodes.append(TextNode(temp, text_type_text))
    return new_nodes
def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        link_list = extract_markdown_links(old_node.text)
        if len(link_list) == 0:
            new_nodes.append(old_node)
            continue
        text_list = []
        temp = old_node.text
        for lnk, url in link_list:
            item = temp.split(f"[{lnk}]({url})", 1)
            if len(item) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            text_list.append(item[0])
            temp = item[1]
        for i, link_tup in enumerate(link_list):
            if text_list[i] != "":
                new_nodes.append(TextNode(text_list[i], text_type_text))
            new_nodes.append(TextNode(link_tup[0], text_type_link, link_tup[1]))
        if temp != "":
            new_nodes.append(TextNode(temp, text_type_text))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    
def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)