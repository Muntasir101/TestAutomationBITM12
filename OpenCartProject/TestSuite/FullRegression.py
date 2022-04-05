import unittest

from OpenCartProject.Registration.test_registration import Registration
from OpenCartProject.Login.test_login import Login
from OpenCartProject.AddToCart.test_addToCart import Addtocart

registration_test = unittest.TestLoader().loadTestsFromTestCase(Registration)
login_test = unittest.TestLoader().loadTestsFromTestCase(Login)
add_to_cart_test = unittest.TestLoader().loadTestsFromTestCase(Addtocart)

regression = unittest.TestSuite([registration_test, login_test, add_to_cart_test])
unittest.TextTestRunner(verbosity=2).run(regression)
