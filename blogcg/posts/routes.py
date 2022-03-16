from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from blogcg import db
from blogcg.models import Post
from blogcg.posts.forms import PostForm

posts=Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET','POST'])
@login_required
def new_post():
    form=PostForm()
    if form.validate_on_submit():
        post=Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Su post ha sido creado!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='Nuevo Post', form=form, legend='Nuevo post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post=Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@posts.route("/post/<int:post_id>/update", methods=['GET','POST'])
@login_required
def update_post(post_id):
    post=Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form=PostForm()
    if form.validate_on_submit():
        post.title=form.title.data
        post.content=form.content.data
        db.session.commit()
        flash('Su post ha sido actualizado!','success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data=post.title
        form.content.data=post.content
    return render_template('create_post.html', title='Actualizar Post', form=form, legend='Actualizar post')

@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post=Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Su post ha sido eliminado!','success')
    return redirect(url_for('main.home'))


