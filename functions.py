import json

def reading_posts():
    with open('posts.json', 'r', encoding="utf-8") as file:
        posts_data_json = json.load(file)
    return posts_data_json

def getting_all_tags():
    posts_list = reading_posts()
    tag_list = []
    for post in posts_list:
        content_words = post["content"].split(" ")
        for word in content_words:
            if word.startswith("#"):
                if not "!" in word:
                    tag_list.append(word[1:])
                else:
                    tag_list.append(word[1:].rstrip("!"))
    return tag_list

def getting_post_by_tag(tag_name):
    posts_list = reading_posts()
    matching_posts = []
    for post in posts_list:
        content_words = post["content"].split(" ")
        for word in content_words:
            if tag_name in word:
                matching_posts.append(post)
    return matching_posts






