import getTime2 as gt
import cv2
import unittest


class test_getDistance(unittest.TestCase):

    def setUp(self):
        pass

    def test_time_1(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/1.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 477)

    def test_time_2(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/2.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 348)

    def test_time_3(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/3.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 67)

    def test_time_4(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/4.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 86)

    def test_time_5(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/5.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 480)

    def test_time_6(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/6.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 24)

    def test_time_7(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/7.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 158)

    def test_time_8(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/8.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 30)

    def test_time_9(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/9.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 87)

    def test_time_10(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/10.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 231)

    def test_time_11(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/11.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 459)

    def test_time_12(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/12.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 237)

    def test_time_13(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/13.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 50)

    def test_time_14(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/14.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 301)

    def test_time_15(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/15.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 480)

    def test_time_16(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/16.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 59)

    def test_time_17(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/17.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 328)

    def test_time_18(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/18.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 72)

    def test_time_19(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/19.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 84)

    def test_time_20(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/20.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 267)

    def test_time_21(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/21.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 409)

    def test_time_22(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/22.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 43)

    def test_time_23(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/23.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 316)

    def test_time_24(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/24.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 469)

    def test_time_25(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/25.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 279)

    def test_time_26(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/26.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 364)

    def test_time_27(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/27.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 202)

    def test_time_28(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/28.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 82)

    def test_time_29(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/29.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 407)

    def test_time_30(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/30.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 63)

    def test_time_31(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/31.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 172)

    def test_time_32(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/32.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 53)

    def test_time_33(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/33.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 109)

    def test_time_34(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/34.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 290)

    def test_time_35(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/35.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 461)

    def test_time_36(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/36.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 93)

    def test_time_37(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/37.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 281)

    def test_time_38(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/38.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 218)

    def test_time_39(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/39.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 120)

    def test_time_40(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/40.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 173)

    def test_time_41(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/41.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 261)

    def test_time_42(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/42.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 327)

    def test_time_43(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/43.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 413)

    def test_time_44(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/44.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 49)

    def test_time_45(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/45.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 182)

    def test_time_46(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/46.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 18)

    def test_time_47(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/47.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 478)

    def test_time_48(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/48.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 77)

    def test_time_49(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/49.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 150)

    def test_time_50(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/50.png")
        computer = "152.1.138.159"
        self.assertEqual(gt.getTime(frame, computer), 345)


if __name__ == "__main__":
    unittest.main()
