import unittest
import numpy as np
from unittest.mock import patch
#import a3Precise as my
#import a3 as my
import a3 as my
#import a3Double as my

atolerance, rtolerance = 0.011, 0.00


class TestPolygon(unittest.TestCase):
    square_inp = np.array([[0.0, 0.0, 1.0], [0.0, 4.0, 1.0],
                    [4.0, 4.0, 1.0], [4.0, 0.0, 1.0]])
    P1Square = my.Polygon(square_inp)
    square_inp2 = np.array([[0.0, 0.0, 1.0], [0.0, 4.0, 1.0],
                     [4.0, 4.0, 1.0], [4.0, 0.0, 1.0]])
    P2Square = my.Polygon(square_inp2)
    square_inp3 = np.array([[0.0, 0.0, 1.0], [0.0, 4.0, 1.0],
                     [4.0, 4.0, 1.0], [4.0, 0.0, 1.0]])
    P3Square = my.Polygon(square_inp3)
    square_inp4 = np.array([[0.0, 0.0, 1.0], [0.0, 4.0, 1.0],
                     [4.0, 4.0, 1.0], [4.0, 0.0, 1.0]])
    P4Square = my.Polygon(square_inp4)

    pentagon_inp = np.array([[2.0, 0.0, 1.0], [0.76, 3.8, 1.0],
                    [4.0, 6.15, 1.0], [7.24, 3.8, 1.0], [6.0, 0.0, 1.0]])
    P1Pentagon = my.Polygon(pentagon_inp)
    pentagon_inp2 = np.array([[2.0, 0.0, 1.0], [0.76, 3.8, 1.0],
                    [4.0, 6.15, 1.0], [7.24, 3.8, 1.0], [6.0, 0.0, 1.0]])
    P2Pentagon = my.Polygon(pentagon_inp2)
    pentagon_inp3 = np.array([[2.0, 0.0, 1.0], [0.76, 3.8, 1.0],
                    [4.0, 6.15, 1.0], [7.24, 3.8, 1.0], [6.0, 0.0, 1.0]])
    P3Pentagon = my.Polygon(pentagon_inp3)
    pentagon_inp4 = np.array([[2.0, 0.0, 1.0], [0.76, 3.8, 1.0],
                    [4.0, 6.15, 1.0], [7.24, 3.8, 1.0], [6.0, 0.0, 1.0]])
    P4Pentagon = my.Polygon(pentagon_inp4)

    def test_01(self):
        print('test_01 starts')
        user_output = self.P1Square.scale(2, 2)
        exp_output = (np.array([-2.0, -2.0, 6.0, 6.0]),
                      np.array([-2.0, 6.0, 6.0, -2.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_01 ends')

    def test_02(self):
        print('test_02 starts')
        user_output = self.P2Square.rotate(90)
        exp_output = (np.array([0.0, 4.0, 4.0, 0.0]),
                      np.array([0.0, 0.0, -4.0, -4.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_02 ends')

    def test_03(self):
        print('test_03 starts')
        user_output = self.P3Square.translate(4, 4)
        exp_output = (np.array([4.0, 4.0, 8.0, 8.0]),
                      np.array([4.0, 8.0, 8.0, 4.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_03 ends')

    def test_04(self):
        print('test_04 starts')
        user_output = self.P4Square.rotate(180)
        exp_output = (np.array([0.0, 0.0, -4.0, -4.0]),
                      np.array([0.0, -4.0, -4.0, 0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_04 ends')

    def test_05(self):
        print('test_05 starts')
        user_output = self.P4Square.translate(0, -4)
        exp_output = (np.array([0.0, 0.0, -4.0, -4.0]),
                      np.array([-4.0, -8.0, -8.0, -4.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_05 ends')

    def test_06(self):
        print('test_06 starts')
        user_output = self.P4Square.rotate(180)
        exp_output = (np.array([0.0, 0.0, 4.0, 4.0]),
                      np.array([4.0, 8.0, 8.0, 4.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_06 ends')

    def test_07(self):
        print('test_07 starts')
        user_output = self.P4Square.rotate(90, 0, 6)
        exp_output = (np.array([-2.0, 2.0, 2.0, -2.0]),
                      np.array([6.0, 6.0, 2.0, 2.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_07 ends')

    def test_08(self):
        print('test_08 starts')
        user_output = self.P4Square.translate(0, -4)
        exp_output = (np.array([-2.0, 2.0, 2.0, -2.0]),
                      np.array([2.0, 2.0, -2.0, -2.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_08 ends')

    def test_09(self):
        print('test_09 starts')
        user_output = self.P4Square.scale(2, 2)
        exp_output = (np.array([-4.0, 4.0, 4.0, -4.0]),
                      np.array([4.0, 4.0, -4.0, -4.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_09 ends')

    def test_10(self):
        print('test_10 starts')
        user_output = self.P4Square.rotate(180, 4, 4)
        exp_output = (np.array([12.0, 4.0, 4.0, 12.0]),
                      np.array([4.0, 4.0, 12.0, 12.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_10 ends')

    def test_11(self):
        print('test_11 starts')
        user_output = self.P4Square.rotate(-180)
        exp_output = (np.array([-12.0, -4.0, -4.0, -12.0]),
                      np.array([-4.0, -4.0, -12.0, -12.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_11 ends')

    def test_12(self):
        print('test_12 starts')
        user_output = self.P4Square.scale(2, 3)
        exp_output = (np.array([-16.0, 0.0, 0.0, -16.0]),
                      np.array([4.0, 4.0, -20.0, -20.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_12 ends')

    # pentagon
    def test_13(self):
        print('test_13 starts')
        user_output = self.P1Pentagon.scale(2, 2)
        exp_output = (np.array([0.0, -2.48, 4.0, 10.48, 8.0]),
                      np.array([-2.75, 4.85, 9.55, 4.85, -2.75]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_13 ends')
    
    def test_14(self):
        print('test_13 starts')
        user_output = self.P2Pentagon.rotate(90)
        exp_output = (np.array([0.0, 3.8, 6.15, 3.8, 0]),
                      np.array([-2.0, -0.76, -4.0, -7.24, -6.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_14 ends')

    def test_15(self):
        print('test_15 starts')
        user_output = self.P3Pentagon.translate(4, 4)
        exp_output = (np.array([6.0, 4.76, 8, 11.24, 10]),
                      np.array([4.0, 7.8, 10.15, 7.8, 4.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_15 ends')

    def test_16(self):
        print('test_16 starts')
        user_output = self.P4Pentagon.rotate(180)
        exp_output = (np.array([-2, -0.76, -4.0, -7.24, -6]),
                      np.array([0.0, -3.8, -6.15, -3.8, 0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_16 ends')

    def test_17(self):
        print('test_17 starts')
        user_output = self.P4Pentagon.translate(0, -4)
        exp_output = (np.array([-2, -0.76, -4.0, -7.24, -6]),
                      np.array([-4.0, -7.8, -10.15, -7.8, -4]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_17 ends')

    def test_18(self):
        print('test_18 starts')
        user_output = self.P4Pentagon.rotate(180)
        exp_output = (np.array([2, 0.76, 4.0, 7.24, 6]),
                      np.array([4.0, 7.8, 10.15, 7.8, 4]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_18 ends')

    def test_19(self):
        print('test_19 starts')
        user_output = self.P4Pentagon.rotate(90, 0, 6)
        exp_output = (np.array([-2, 1.8, 4.15, 1.8, -2]),
                      np.array([4.0, 5.24, 2.0, -1.24, 0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_19 ends')

    def test_20(self):
        print('test_20 starts')
        user_output = self.P4Pentagon.translate(0, -4)
        exp_output = (np.array([-2.0, 1.8, 4.15, 1.80, -2.0]),
                      np.array([0.0, 1.24, -2.0, -5.24, -4.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_20 ends')

    def test_21(self):
        print('test_21 starts')
        user_output = self.P4Pentagon.scale(2, 2)
        exp_output = (np.array([-4.75, 2.85, 7.55, 2.85, -4.75]),
                      np.array([2.0, 4.48, -2.0, -8.48, -6.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_21 ends')

    def test_22(self):
        print('test_22 starts')
        user_output = self.P4Pentagon.rotate(180, 4, 4)
        exp_output = (np.array([12.75, 5.15, 0.45, 5.15, 12.75]),
                      np.array([6.0, 3.52, 10.0, 16.48, 14.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_22 ends')

    def test_23(self):
        print('test_23 starts')
        user_output = self.P4Pentagon.rotate(-180)
        exp_output = (np.array([-12.75, -5.15, -0.45, -5.15, -12.75]),
                      np.array([-6.0, -3.52, -10.0, -16.48, -14.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_23 ends')

    def test_24(self):
        print('test_24 starts')
        user_output = self.P4Pentagon.scale(2, 3)
        exp_output = (np.array([-18.25, -3.05, 6.35, -3.05, -18.25]),
                      np.array([2.0, 9.44, -10.0, -29.44, -22.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(
            exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_24 ends')

class TestCircle(unittest.TestCase):

    C1 = my.Circle(2.0, 2.0, 3.0)
    C2 = my.Circle(2.0, 2.0, 3.0)
    C3 = my.Circle(2.0, 2.0, 3.0)
    C4 = my.Circle(2.0, 2.0, 3.0)
    C5 = my.Circle(-2.0, -3.0, 5.0)

    def test_1(self):
        print('test_1 starts')
        user_output = self.C1.scale(2)
        exp_output = (2.0, 2.0, 6.0)
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_1 ends')

    def test_2(self):
        print('test_2 starts')
        user_output = self.C2.rotate(90)
        exp_output = (2.0, -2.0, 3.0)
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_2 ends')

    def test_3(self):
        print('test_3 starts')
        user_output = self.C3.translate(4, 4)
        exp_output = (6.0, 6.0, 3.0)
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_3 ends')

    def test_4(self):
        print('test_4 starts')
        user_output = self.C3.scale(0.2)
        exp_output = (6.0, 6.0, 0.6)
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_4 ends')

    def test_5(self):
        print('test_5 starts')
        user_output = self.C3.rotate(90, 2, 2)
        exp_output = (6.0, -2.0, 0.6)
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_5 ends')

    def test_6(self):
        print('test_6 starts')
        user_output = self.C3.rotate(-45, 3, 3)
        exp_output = (8.66, 1.59, 0.6)
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_6 ends')

    def test_7(self):
        print('test_7 starts')
        user_output = self.C3.translate(-3, -3)
        exp_output = (5.66, -1.41, 0.6)
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_7 ends')

    def test_8(self):
        print('test_8 starts')
        user_output = self.C3.rotate(90)
        exp_output = (-1.41, -5.66, 0.6)
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_8 ends')

    def test_9(self):
        print('test_9 starts')
        user_output = self.C3.scale(10)
        exp_output = (-1.41, -5.66, 6.0)
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_9 ends')

    def test_10(self):
        print('test_10 starts')
        user_output = self.C5.scale(0.01)
        exp_output = (-2.0, -3.0, 0.05)
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_10 ends')

    def test_11(self):
        print('test_11 starts')
        user_output = self.C5.translate(2, 3)
        exp_output = (0.0, 0.0, 0.05)
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_11 ends')

    def test_12(self):
        print('test_12 starts')
        user_output = self.C5.rotate(90, 0.1, 0.1)
        exp_output = (0.0, 0.2, 0.05)
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_12 ends')

    def test_13(self):
        print('test_13 starts')
        user_output = self.C5.translate(0.01, 0.01)
        exp_output = (0.01, 0.21, 0.05)
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_13 ends')

    def test_14(self):
        print('test_14 starts')
        user_output = self.C5.rotate(-0.1, 2, 2)
        exp_output = (0.01, 0.21, 0.05)
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_14 ends')

    # def test_4(self):
    #     print('test_4 starts')
    #     user_output = self.C4.translate(4, 4)
    #     exp_output = (6.0, 6.0, 3.0)
    #     print(f'returned value {user_output}')
    #     print(f'expected value {exp_output}')
    #     np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
    #     print('test_4 ends')


if __name__ == '__main__':
	unittest.main()
