# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import sys

import firestore as firestore_live
import firestore_stub

from flask import current_app, flash, Flask, Markup, redirect, render_template
from flask import request, url_for
from google.cloud import error_reporting
import google.cloud.logging
import storage

STUB_FIRESTORE = False


def firestore():
    if STUB_FIRESTORE:
        return firestore_stub
    else:
        return firestore_live


def upload_image_file(img):
    """
    Upload the user-uploaded file to Google Cloud Storage and retrieve its
    publicly-accessible URL.
    """
    if not img:
        return None

    public_url = storage.upload_file(
        img.read(),
        img.filename,
        img.content_type
    )

    current_app.logger.info(
        'Uploaded file %s as %s.', img.filename, public_url)

    return public_url


app = Flask(__name__)
app.config.update(
    SECRET_KEY='secret',
    MAX_CONTENT_LENGTH=8 * 1024 * 1024,
    ALLOWED_EXTENSIONS=set(['png', 'jpg', 'jpeg', 'gif'])
)

app.debug = False
app.testing = False

# Configure logging
if not app.testing:
    logging.basicConfig(level=logging.INFO)
    client = google.cloud.logging.Client()
    # Attaches a Google Stackdriver logging handler to the root logger
    client.setup_logging()


@app.route('/')
def list_items():
    start_after = request.args.get('start_after', None)
    recipes, last_name = firestore().next_page(start_after=start_after)
    return render_template('list.html', recipes=recipes, last_name=last_name, size=len(recipes))


@app.route('/recipe/<recipe_id>')
def view(recipe_id):
    recipe_header, ingredient_list, directions = firestore().read(recipe_id)
    return render_template('view.html', recipe=recipe_header, ingredients=ingredient_list, directions=directions, len=len(directions))


@app.route('/recipe/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)

        # If an image was uploaded, update the data to point to the new image.
        image_url = upload_image_file(request.files.get('image'))

        if image_url:
            data['imageUrl'] = image_url

        book = firestore().create(data)

        return redirect(url_for('.view', book_id=book['id']))

    return render_template('form.html', action='Add', book={})


@app.route('/recipe/<recipe_id>/edit-directions', methods=['GET', 'POST'])
def edit_directions(recipe_id):
    recipe_name, directions = firestore().read_directions(recipe_id)
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        print(data)
        return view(recipe_id)

    return render_template('directions.html', action='Edit', recipe_name=recipe_name, directions=directions, size=len(directions))


@app.route('/recipe/<recipe_id>/edit', methods=['GET', 'POST'])
def edit(recipe_id):
    book = firestore().read(recipe_id)

    if request.method == 'POST':
        data = request.form.to_dict(flat=True)

        # If an image was uploaded, update the data to point to the new image.
        #image_url = upload_image_file(request.files.get('image'))

        #if image_url:
        #    data['imageUrl'] = image_url

        #book = firestore.update(data, book_id)

        return
        #return redirect(url_for('.view', book_id=book['id']))

    return render_template('form.html', action='Edit', book=book)


@app.route('/recipe/<recipe_id>/delete')
def delete(recipe_id):
    firestore().delete(recipe_id)
    return redirect(url_for('.list'))


@app.route('/logs')
def logs():
    logging.info('Hey, you triggered a custom log entry. Good job!')
    flash(Markup('''You triggered a custom log entry. You can view it in the
        <a href="https://console.cloud.google.com/logs">Cloud Console</a>'''))
    return redirect(url_for('.list'))


@app.route('/errors')
def errors():
    raise Exception('This is an intentional exception.')


# Add an error handler that reports exceptions to Stackdriver Error
# Reporting. Note that this error handler is only used when debug
# is False
@app.errorhandler(500)
def server_error(e):
    error_client = error_reporting.Client()
    error_client.report_exception(
        http_context=error_reporting.build_flask_context(request))
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


# This is only used when running locally. When running live, gunicorn runs
# the application.
if __name__ == '__main__':
    for arg in sys.argv[1:]:
        if arg == "--stub-firestore":
            STUB_FIRESTORE = True

    app.run(host='127.0.0.1', port=8080, debug=True)
