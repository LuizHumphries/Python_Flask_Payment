from repository.database import db

class Payment(db.Model):
    # id, value, paid_or_not, bank_payment_id, qr_code, expiration_date
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)
    paid = db.Column(db.Boolean, default=False)
    bank_paid_id = db.Column(db.Integer, nullable=True)
    qr_code = db.Column(db.String, nullable=True)
    expiration_date = db.Column(db.DateTime)