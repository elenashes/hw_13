import json
from flask import Flask, request, render_template, send_from_directory
from functions import getting_all_tags, getting_post_by_tag

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    tag_list = getting_all_tags()
    return render_template('index.html', tag_list=tag_list)


@app.route("/tag")
def page_tag():
    tag_name = request.args.get("tag")
    matching_posts = getting_post_by_tag(tag_name)
    return render_template('post_by_tag.html', posts=matching_posts, tag=tag_name)


@app.route("/post", methods=["GET"])
def page_post_form():
    return render_template('post_form.html')


@app.route("/post", methods=["POST"])
def page_post_create():
    picture = request.files.get("picture")
    content = request.values.get("content")

    if not picture:
        return "Ошибка загрузки"

    filename = picture.filename
    path = "./"+UPLOAD_FOLDER+"/"+filename
    picture.save(path)

    picture_url = "/"+UPLOAD_FOLDER+"/"+filename

    data_dict = {"pic": picture_url, "content": content}

    with open('posts.json', 'a', encoding="utf-8") as file:
        json.dump(data_dict, file, ensure_ascii=False)

    return render_template('post_uploaded.html', picture=picture_url, content=content)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

