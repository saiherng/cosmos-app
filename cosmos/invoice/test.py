
from invoice.models import *

print("Starting test")
c1 = Customer(name="Sai", phone_number=111, address="U Chit MG")
c1.save()

p1 = Product(name="SK", price=50, quantity=2)
p2 = Product(name="RM", price=60, quantity=3)
p3 = Product(name="FL", price=70, quantity=4)

p1.save()
p2.save()
p3.save()

i1 = Invoice(customer=c1,payment="K", payment_id=1)
i1.save()



