from wtforms import form, fields
from flask_admin.form import Select2Widget
from flask_admin.contrib.pymongo import ModelView, filters
from flask_admin.model.fields import InlineFormField, InlineFieldList


# User admin
class InnerForm(form.Form):
    name = fields.StringField('Name')
    test = fields.StringField('Test')


class UserForm(form.Form):
    username = fields.StringField('Username')
    fullname = fields.StringField('Fullname')
    email = fields.StringField('Email')
    password = fields.StringField('Password')
    gender = fields.StringField('Gender')
    issuperuser = fields.StringField('Is_superuser')
    # Inner form
    inner = InlineFormField(InnerForm)
    # Form list
    form_list = InlineFieldList(InlineFormField(InnerForm))


class UserView(ModelView):
    column_list = ('username', 'fullname', 'password', 'gender', 'email', 'issuperuser')
    column_sortable_list = ('username', 'fullname', 'password', 'gender', 'email', 'issuperuser')
    form = UserForm


# Question admin
class QuestionForm(form.Form):
    ID = fields.StringField('_id')
    Question = fields.StringField('question')

    # Inner form
    inner = InlineFormField(InnerForm)
    # Form list
    form_list = InlineFieldList(InlineFormField(InnerForm))


class QuestionView(ModelView):
    column_list = ('_id', 'Question')
    column_sortable_list = ('_id', 'Question')
    form = QuestionForm


# Answr admin
class AnswerForm(form.Form):
    ID = fields.StringField('_id')
    Answer = fields.StringField('answer')

    # Inner form
    inner = InlineFormField(InnerForm)
    # Form list
    form_list = InlineFieldList(InlineFormField(InnerForm))


class AnswerView(ModelView):
    column_list = ('_id', 'Answer')
    column_sortable_list = ('_id', 'Answer')
    form = AnswerForm


# Category admin
class CategoryForm(form.Form):
    ID = fields.StringField('_id')
    NameCategory = fields.StringField('namecategory')
    Description = fields.StringField('description')

    # Inner form
    inner = InlineFormField(InnerForm)
    # Form list
    form_list = InlineFieldList(InlineFormField(InnerForm))


class CategoryView(ModelView):
    column_list = ('_id', 'Name Category', 'Description')
    column_sortable_list = ('_id', 'Name Category', 'Description')
    form = CategoryForm


# MBTI admin
class MBTIForm(form.Form):
    ID = fields.StringField('_id')
    ID_Question_Answer = fields.StringField('idquestionanswer')
    ID_Category = fields.StringField('idcategory')
    Score = fields.StringField('score')
    # Inner form
    inner = InlineFormField(InnerForm)
    # Form list
    form_list = InlineFieldList(InlineFormField(InnerForm))


class MBTIView(ModelView):
    column_list = ('_id', 'ID_Question_Answer', 'ID_Category', 'Score')
    column_sortable_list = ('_id', 'ID_Question_Answer', 'ID_Category', 'Score')
    form = MBTIForm


# Holland admin
class HollandForm(form.Form):
    ID = fields.StringField('_id')
    ID_Question_Answer = fields.StringField('idquestionanswer')
    ID_Category = fields.StringField('idcategory')
    Score = fields.StringField('score')
    # Inner form
    inner = InlineFormField(InnerForm)
    # Form list
    form_list = InlineFieldList(InlineFormField(InnerForm))


class HollandView(ModelView):
    column_list = ('_id', 'ID_Question_Answer', 'ID_Category', 'Score')
    column_sortable_list = ('_id', 'ID_Question_Answer', 'ID_Category', 'Score')
    form = HollandForm


# Question-Answer admin
class QuestionAnswerForm(form.Form):
    ID = fields.StringField('_id')
    IDQuestion = fields.StringField('idquestion')
    IDAnswer = fields.StringField('idanswer')
    # Inner form
    inner = InlineFormField(InnerForm)
    # Form list
    form_list = InlineFieldList(InlineFormField(InnerForm))


class QuestionAnswerView(ModelView):
    column_list = ('_id', 'IDQuestion', 'IDAnswer')
    column_sortable_list = ('_id', 'IDQuestion', 'IDAnswer')
    form = QuestionAnswerForm


# Execrise admin
class ExecriseForm(form.Form):
    ID = fields.StringField('_id')
    Orginal_Title = fields.StringField('orginaltitle')
    URL = fields.StringField('url')
    # Inner form
    inner = InlineFormField(InnerForm)
    # Form list
    form_list = InlineFieldList(InlineFormField(InnerForm))


class ExecriseView(ModelView):
    column_list = ('_id', 'Orginal_Title', 'URL')
    column_sortable_list = ('_id', 'Orginal_Title', 'URL')
    form = ExecriseForm
