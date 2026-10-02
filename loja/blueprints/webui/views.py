from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from loja.model import User, Product

def index():
    products = Product.query.all()
    return render_template("index.html", products=products)

def product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template("product.html", product=product)

def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('admin.index'))
        
        flash('Usuário ou senha inválidos.')

    return '''
        <div style="max-width: 300px; margin: 50px auto; font-family: sans-serif;">
            <h2>Login Administrativo</h2>
            <form method="post">
                <p><input type="text" name="username" placeholder="Usuário" required style="width: 100%; padding: 8px;"></p>
                <p><input type="password" name="password" placeholder="Senha" required style="width: 100%; padding: 8px;"></p>
                <p><button type="submit" style="padding: 8px 15px;">Entrar</button></p>
            </form>
        </div>
    '''

def admin_logout():
    logout_user()
    return redirect(url_for('webui.admin_login'))