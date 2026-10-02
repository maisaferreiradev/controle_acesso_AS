from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from loja.ext.database import db, SerializerMixin, mapped_column, Mapped

class Product(db.Model, SerializerMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(unique=True)
    price: Mapped[float]


class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(nullable=False)

    def set_password(self, password: str):
        
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

def populate_db():
    products = [
        Product(id=1, description="Resistor 470 ohms", price=0.05),
        Product(id=2, description="Arduino Nano R3", price=50.00),
        Product(id=3, description="Raspberry PI 3", price=200.00),
    ]

    db.session.add_all(products)

    
    if not User.query.filter_by(username="admin").first():
        admin_user = User(username="admin")
        admin_user.set_password("admin123")  
        db.session.add(admin_user)

    db.session.commit()