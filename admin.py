import os
from flask import Blueprint, render_template, session, redirect, url_for, request, send_from_directory
from werkzeug.utils import secure_filename
from models import Page
from forms import PageForm
from passenger_wsgi import db

admin = Blueprint('admin', __name__, url_prefix='/admin')
project_root = os.path.dirname(os.path.abspath(__file__))
upload_path = os.path.join(project_root, 'uploads')


@admin.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(upload_path, filename)


@admin.route("/", methods=['GET', 'POST'])
def dashboard():
    if 'loggedin' not in session:
        return redirect(url_for('auth.login'))
    else:
        form = PageForm()
        if form.validate_on_submit():
            image_path = ''
            if form.image.data:
                file = request.files[form.image.name]
                filename = secure_filename(file.filename)
                file.save(os.path.join(upload_path, filename))
                image_path = "/uploads/"+filename
            slug = form.title.data
            slug = slug.lower()
            slug = slug.replace(" ", "-")
            page = Page.query.filter_by(slug=slug).first()
            if page:
                page = page.slug
                last = page.split("-")[-1]
                if last.isdigit():
                    slug = slug + "-" + str(int(last) + 1)
                else:
                    slug = slug + "-1"
            new_page = Page(
                slug=slug,
                author=session['name'],
                title=form.title.data,
                text=form.text.data,
                image_path=image_path,
                emgithub=form.emgithub.data,
                youtube=form.youtube.data,
                type=form.type.data,
                keywords=form.keywords.data
            )
            db.session.add(new_page)
            db.session.commit()
        return render_template("index.html", form=form)
