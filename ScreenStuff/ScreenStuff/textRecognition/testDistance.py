import getDistance2 as gd
import cv2
import unittest


class test_getDistance(unittest.TestCase):

    def setUp(self):
        pass

    def test_distance_1(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/1.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_2(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/2.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 3)

    def test_distance_3(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/3.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_4(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/4.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_5(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/5.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 16)

    def test_distance_6(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/6.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_7(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/7.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 2)

    def test_distance_8(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/8.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_9(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/9.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_10(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/10.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 2)

    def test_distance_11(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/11.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 4)

    def test_distance_12(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/12.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 8)

    def test_distance_13(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/13.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 2)

    def test_distance_14(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/14.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 1)

    def test_distance_15(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/15.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 0)

    def test_distance_16(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/16.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_17(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/17.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_18(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/18.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_19(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/19.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 4)

    def test_distance_20(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/20.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 17)

    def test_distance_21(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/21.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_22(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/22.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_23(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/23.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 1)

    def test_distance_24(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/24.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_25(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/25.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 0.5)

    def test_distance_26(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/26.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 22)

    def test_distance_27(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/27.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_28(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/28.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 17)

    def test_distance_29(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/29.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 7)

    def test_distance_30(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/30.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 9)

    def test_distance_31(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/31.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 0)

    def test_distance_32(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/32.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_33(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/33.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 6)

    def test_distance_34(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/34.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_35(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/35.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 6)

    def test_distance_36(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/36.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_37(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/37.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 0)

    def test_distance_38(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/38.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_39(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/39.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_40(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/40.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_41(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/41.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 8)

    def test_distance_42(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/42.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_43(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/43.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_44(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/44.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 18)

    def test_distance_45(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/45.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 8)

    def test_distance_46(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/46.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 5)

    def test_distance_47(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/47.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_48(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/48.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)

    def test_distance_49(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/49.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 0.5)

    def test_distance_50(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/50.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDistance(frame, computer), 10)


if __name__ == "__main__":
    unittest.main()
