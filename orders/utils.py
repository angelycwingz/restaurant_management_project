import secrets
import string
from .models import Order # assuming coupon_code field exists in Order model

def generate_coupon_code(length=10):
    """
    Generate a unique alphanumeric coupon code of given length
    Ensures uniqueness  by checking against the Order model's coupon_code field.
    """

    alphabet = string.ascii_uppercase + string.digits

    while True:
        # Create a random code
        code = "".join(secrets.choice(alphabet) for _ in range(length))


        # check if it already exists in DB
        if not Order.objects.filter(coupon_code=code).exists()
            return code
            