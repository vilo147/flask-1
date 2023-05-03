from flask import render_template, redirect, url_for

from . import app, db
from .forms import NewsForm
from .models import Category, News

@app.route('/', methods=['GET', 'POST'])
def index():
    news = News.query.all()
    category = Category.query.all()
    form = FeedbackForm()
    feedbacks = Feedback.query.all()
    print(news)
    if form.validate_on_submit():
        feedback = Feedback(
            name=form.name.data,
            text=form.text.data,
            email=form.email.data,
            rating=form.rating.data
        )
        db.session.add(feedback)
        db.session.commit()
        return redirect('/')
    return render_template('index.html', form=form, feedback=feedbacks, category=category, news=news)


@app.route('/news_detail/<int:id>')
def news_detail(id):
    category = Category.query.all()
    new_deta = News.query.get(id)
    return render_template('news_detail.html', category=category, news=new_deta)


@app.route('/add_news', methods=['GET', 'POST'])
def add_news():
    category = Category.query.all()
    form = NewsForm()
    if form.validate_on_submit():
        news = News()
        news.title = form.title.data
        news.text = form.text.data
        db.session.add(news)
        db.session.commit()
        return redirect(url_for('news_detail', id=news.id))
    return render_template('add_news.html', category=category,
                           form=form)
