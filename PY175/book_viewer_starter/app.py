from flask import Flask, render_template, g, redirect, request
import re

app = Flask(__name__)

@app.before_request
def load_contents():
    with open("book_viewer/data/toc.txt", "r") as file:
        g.contents = file.readlines()

@app.template_filter('in_paragraphs')
def in_paragraphs(text):
    return text.split("\n\n")

@app.template_filter('highlight')
def highlight(text, term):
    return text.replace(term, f'<strong>{term}</strong>')

@app.route("/")
def index():
    return render_template("home.html", contents=g.contents)

@app.route('/chapters/<page_num>')
def chapter(page_num):
    if page_num.isdigit() and (1 <= int(page_num) <= len(g.contents)):
        chapter_name = g.contents[int(page_num) - 1]
        chapter_title = f"Chapter {page_num}: {chapter_name}"

        with open(f"book_viewer/data/chp{page_num}.txt") as file:
            chapter_content = file.read()

        return render_template('chapter.html',
                              chapter_title=chapter_title,
                              chapter=chapter_content,
                              contents=g.contents)
    else:
        return redirect("/")

@app.route('/search')
def search():
    query = request.args.get('query', '')
    chapters_dict = {}

    if query:
        for num, ch_title in enumerate(g.contents):
            file_name = f"book_viewer/data/chp{str(num + 1)}.txt"
            with open(file_name) as file:
                chapter_content = file.read()

            matching_paragraphs = {}
            for para_index, paragraph in enumerate(chapter_content.split("\n\n")):
                if query.lower() in paragraph.lower():
                    matching_paragraphs[para_index] = paragraph

            if matching_paragraphs:
                chapters_dict[ch_title] = {
                    'number': num + 1,
                    'paragraphs': matching_paragraphs
                }
            
    return render_template('search.html', query=query, found_chapters=chapters_dict)

@app.errorhandler(404)
def some_path(_error):
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5003)

