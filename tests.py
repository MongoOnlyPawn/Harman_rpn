import unittest
import rpn_calc


def reset_stack(func):
    def wrapper(self, *args, **kwargs):
        rpn_calc.stack = []  # Reset the stack before each test function
        func(self, *args, **kwargs)
        rpn_calc.stack = []  # Reset the stack after each test function

    return wrapper


class TestRPNCalculator(unittest.TestCase):
    @reset_stack
    def setUp(self):
        pass

    def test_addition(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("3 4 +"), 7)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("-3 4 +"), 1)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("0 4 +"), 4)

    def test_subtraction(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("3 4 -"), -1)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("4 3 -"), 1)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("-3 -4 -"), 1)

    def test_multiplication(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("3 4 *"), 12)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("-3 4 *"), -12)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("-3 -4 *"), 12)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("0 4 *"), 0)

    def test_division(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("12 4 /"), 3)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("-12 4 /"), -3)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("12 -4 /"), -3)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("0 4 /"), 0)
        self.setUp()
        self.assertIsNone(rpn_calc.evaluate_rpn("4 0 /"))

    def test_factorial(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("5 !"), 120)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("0 !"), 1)
        self.setUp()
        self.assertIsNone(rpn_calc.evaluate_rpn("-5 !"))

    def test_not_equal(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("5 5 !="), 0)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("5 6 !="), 1)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("pi pi !="), 0)

    def test_modulus(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("10 3 %"), 1)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("17 5 %"), 2)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("20 7 %"), 6)

    def test_increment_decrement(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("5 ++"), 6)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("5 --"), 4)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("0 --"), -1)

    def test_pi_e_rand(self):
        self.setUp()
        self.assertAlmostEqual(rpn_calc.evaluate_rpn("pi"), 3.141592653589793)
        self.setUp()
        self.assertAlmostEqual(rpn_calc.evaluate_rpn("e"), 2.718281828459045)
        self.setUp()

    def test_invalid_expression(self):
        self.setUp()
        self.assertIsNone(rpn_calc.evaluate_rpn("3 + 4"))
        self.setUp()
        self.assertIsNone(rpn_calc.evaluate_rpn("3 4 5 +"))
        self.setUp()
        self.assertIsNone(rpn_calc.evaluate_rpn("3 4 + *"))
        self.setUp()
        self.assertIsNone(rpn_calc.evaluate_rpn("3 a + 4 *"))

    def test_ceil(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("3.2 ceil"), 4)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("3.7 ceil"), 4)

    def test_floor(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("3.2 floor"), 3)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("3.7 floor"), 3)

    def test_round(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("3.2 round"), 3)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("3.7 round"), 4)

    def test_ip(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("3.2 ip"), 3)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("3.7 ip"), 3)

    def test_fp(self):
        self.setUp()
        self.assertAlmostEqual(rpn_calc.evaluate_rpn("3.2 fp"), 0.2)
        self.setUp()
        self.assertAlmostEqual(rpn_calc.evaluate_rpn("3.7 fp"), 0.7)

    def test_sign(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("3 sign"), 1)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("-3 sign"), -1)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("0 sign"), None)

    def test_abs(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("-3 abs"), 3)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("3 abs"), 3)

    def test_max(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("3 4 max"), 4)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("-3 -4 max"), -3)

    def test_min(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("3 4 min"), 3)
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("-3 -4 min"), -4)

    def test_bitwise_and_zero(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("0 5 &"), 0)

    def test_bitwise_or_zero(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("0 5 |"), 5)

    def test_bitwise_xor_zero(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("0 5 ^"), 5)

    def test_bitwise_not_zero(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("0 ~"), -1)

    def test_bitwise_shift_left_zero(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("0 2 <<"), 0)

    def test_bitwise_shift_right_zero(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("0 1 >>"), 0)

    def test_bitwise_shift_left_large(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("255 3 <<"), 2040)

    def test_bitwise_shift_right_large(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("255 3 >>"), 31)

    def test_bitwise_not_large(self):
        self.setUp()
        self.assertEqual(rpn_calc.evaluate_rpn("255 ~"), -256)


if __name__ == "__main__":
    unittest.main()
