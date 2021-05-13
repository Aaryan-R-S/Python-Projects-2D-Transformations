import unittest
import numpy as np
from unittest.mock import patch
import a3 as my

tolerance = 0

class TestPolygon(unittest.TestCase):
	# P1 is the square and P2 a pentagon
	inp = np.array([[1.0, 1.0, 1.0], [1.0, 5.0, 1.0], [5.0, 5.0, 1.0], [5.0, 1.0, 1.0]])
	P1 = my.Polygon(inp)
	inp2 = np.array([[2.0, 1.0, 1.0], [4.0, 1.0, 1.0], [5.0, 2.0, 1.0], [3.0, 3.0, 1.0], [1.0, 2.0, 1.0]])
	P2 = my.Polygon(inp2)
	inp3 = np.array([[0.0, 0.0, 1.0], [4.0, 0.0, 1.0], [4.0, 4.0, 1.0], [0.0, 4.0, 1.0]])
	P3 = my.Polygon(inp3)
	
	def test_1(self):
		
		user_output = self.P1.rotate(90)
		exp_output = (np.array([1.0, 5.0, 5.0, 1.0]), np.array([-1.0, -1.0, -5.0, -5.0]))
		np.testing.assert_allclose(exp_output, user_output, atol=tolerance)

	def test_2(self):

		user_output = self.P1.translate(2, 2)
		exp_output = (np.array([3.0, 7.0, 7.0, 3.0]), np.array([1.0, 1.0, -3.0, -3.0]))
		np.testing.assert_allclose(exp_output, user_output, atol=tolerance)

	def test_3(self):

		user_output = self.P1.scale(3, 2)
		exp_output = (np.array([-1.0, 11.0, 11.0, -1.0]), np.array([3.0, 3.0, -5.0, -5.0]))
		np.testing.assert_allclose(exp_output, user_output, atol=tolerance)

	def test_4(self):
		user_output = self.P2.scale(-2, -2)
		exp_output = (np.array([5.0, 1.0, -1.0, 3.0, 7.0]), np.array([3.4, 3.4, 1.4, -0.6, 1.4]))
		np.testing.assert_allclose(exp_output, user_output, atol=tolerance)

	def test_5(self):
		user_output = self.P2.rotate(-45)
		exp_output = (np.array([1.13, -1.7, -1.7, 2.55, 3.96]), np.array([5.94, 3.11, 0.28, 1.7, 5.94]))
		np.testing.assert_allclose(exp_output, user_output, atol=tolerance)

	def test_6(self):
		user_output = self.P2.scale(0.5, 0.3)
		exp_output = (np.array([0.99, -0.43, -0.43, 1.7, 2.4]), np.array([4.16, 3.31, 2.46, 2.89, 4.16]))
		np.testing.assert_allclose(exp_output, user_output, atol=tolerance)

	def test_7(self):

		user_output = self.P3.rotate(45, 2, 2)
		exp_output = (np.array([-0.83, 2.0, 4.83, 2.0]), np.array([2.0, -0.83, 2.0, 4.83]))
		np.testing.assert_allclose(exp_output, user_output, atol=tolerance)

class TestCircle(unittest.TestCase):

	C1 = my.Circle(2.0, 2.0, 3.0) # 2,2 is center and 3 is radius
	C2 = my.Circle(2.0, 2.0, 3.0) # 2,2 is center and 3 is radius
	
	def test_1(self):
		
		user_output = self.C1.rotate(45)
		print(user_output)
		exp_output = (2.83, 0.0, 3)
		np.testing.assert_allclose(exp_output, user_output, atol=tolerance)

	def test_2(self):

		user_output = self.C1.scale(0.5)
		print(user_output)
		exp_output = (2.83, 0.0, 1.5)
		np.testing.assert_allclose(exp_output, user_output, atol=tolerance)

	def test_3(self):

		user_output = self.C1.translate(-3, 3)
		print(user_output)
		exp_output = (-0.17, 3.0, 1.5)
		np.testing.assert_allclose(exp_output, user_output, atol=tolerance)
		
	def test_4(self):

		user_output = self.C2.rotate(45, 4, 4)
		exp_output = (1.17, 4, 3)
		print(user_output)
		np.testing.assert_allclose(exp_output, user_output, atol=tolerance)

if __name__ == '__main__':
	unittest.main()
