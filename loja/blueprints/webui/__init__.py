from flask import Blueprint
from .views import index, product, admin_login, admin_logout

bp = Blueprint('webui', __name__, template_folder='templates',
               url_prefix="/main/v1",
              )

bp.add_url_rule("/", view_func=index)
bp.add_url_rule(
    "/product/<product_id>", view_func=product, endpoint="productview",
)
bp.add_url_rule(
    "/admin-login", view_func=admin_login, methods=["GET", "POST"], endpoint="admin_login"
)
bp.add_url_rule(
    "/admin-logout", view_func=admin_logout, endpoint="admin_logout"
)

def init_app(app):
    app.register_blueprint(bp)