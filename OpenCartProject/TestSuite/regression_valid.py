import unittest

from OpenCartProject.Registration.test_registration import Registration
from OpenCartProject.Login.test_login import Login
from OpenCartProject.AddToCart.test_addToCart import Addtocart

registration_test = unittest.TestLoader().loadTestsFromTestCase(Registration)
login_test = unittest.TestLoader().loadTestsFromTestCase(Login)


regression_valid = unittest.TestSuite([registration_test, login_test])
unittest.TextTestRunner(verbosity=2).run(regression_valid)