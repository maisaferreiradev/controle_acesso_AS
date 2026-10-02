from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user
from flask import redirect, url_for, request
from loja.ext.database import db
from loja.model import Product, User

class SecureAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('webui.admin_login', next=request.url))

class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('webui.admin_login', next=request.url))

def init_app(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'webui.admin_login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    admin = Admin(app, name='Painel Admin', template_mode='bootstrap4', index_view=SecureAdminIndexView())
    admin.add_view(SecureModelView(Product, db.session))
    admin.add_view(SecureModelView(User, db.session))