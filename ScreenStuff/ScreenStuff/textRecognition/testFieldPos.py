import getFieldPos2 as fp
import cv2
import unittest


class test_FieldPos(unittest.TestCase):

    def setUp(self):
        pass

    def test_fp_1(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/1.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 23)

    def test_fp_2(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/2.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 38)

    def test_fp_3(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/3.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 41)

    def test_fp_4(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/4.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 22)

    def test_fp_5(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/5.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 16)

    def test_fp_6(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/6.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 45)

    def test_fp_7(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/7.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 31)

    def test_fp_8(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/8.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 48)

    def test_fp_9(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/9.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 20)

    def test_fp_10(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/10.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 4)

    def test_fp_11(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/11.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 24)

    def test_fp_12(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/12.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 43)

    def test_fp_13(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/13.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 49)

    def test_fp_14(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/14.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 41)

    def test_fp_15(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/15.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 2)

    def test_fp_16(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/16.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 37)

    def test_fp_17(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/17.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 26)

    def test_fp_18(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/18.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 31)

    def test_fp_19(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/19.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 8)

    def test_fp_20(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/20.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 24)

    def test_fp_21(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/21.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 37)

    def test_fp_22(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/22.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 30)

    def test_fp_23(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/23.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 29)

    def test_fp_24(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/24.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 20)

    def test_fp_25(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/25.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 36)

    def test_fp_26(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/26.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 19)

    def test_fp_27(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/27.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 20)

    def test_fp_28(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/28.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 34)

    def test_fp_29(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/29.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 32)

    def test_fp_30(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/30.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 26)

    def test_fp_31(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/31.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 4)

    def test_fp_32(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/32.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 3)

    def test_fp_33(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/33.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 37)

    def test_fp_34(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/34.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 30)

    def test_fp_35(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/35.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 25)

    def test_fp_36(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/36.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 11)

    def test_fp_37(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/37.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 6)

    def test_fp_38(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/38.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 45)

    def test_fp_39(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/39.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 23)

    def test_fp_40(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/40.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 19)

    def test_fp_41(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/41.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 43)

    def test_fp_42(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/42.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 46)

    def test_fp_43(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/43.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 39)

    def test_fp_44(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/44.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 26)

    def test_fp_45(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/45.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 26)

    def test_fp_46(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/46.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 25)

    def test_fp_47(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/47.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 22)

    def test_fp_48(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/48.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 42)

    def test_fp_49(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/49.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 44)

    def test_fp_50(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/50.png")
        computer = "152.1.138.159"
        self.assertEqual(fp.getFieldPos(frame, computer), 41)

    def test_fp_51(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/0.png")
        computer = "152.1.138.160"
        self.assertEqual(fp.getFieldPos(frame, computer), 25)

    def test_fp_52(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/1.png")
        computer = "152.1.138.160"
        self.assertEqual(fp.getFieldPos(frame, computer), 28)

    def test_fp_53(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/2.png")
        computer = "152.1.138.160"
        self.assertEqual(fp.getFieldPos(frame, computer), 28)

    def test_fp_54(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/3.png")
        computer = "152.1.138.160"
        self.assertEqual(fp.getFieldPos(frame, computer), 34)

    def test_fp_55(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/4.png")
        computer = "152.1.138.160"
        self.assertEqual(fp.getFieldPos(frame, computer), 29)

    def test_fp_56(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/5.png")
        computer = "152.1.138.160"
        self.assertEqual(fp.getFieldPos(frame, computer), 44)

    def test_fp_57(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/6.png")
        computer = "152.1.138.160"
        self.assertEqual(fp.getFieldPos(frame, computer), 47)

    def test_fp_58(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/7.png")
        computer = "152.1.138.160"
        self.assertEqual(fp.getFieldPos(frame, computer), 46)

    def test_fp_59(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/8.png")
        computer = "152.1.138.160"
        self.assertEqual(fp.getFieldPos(frame, computer), 33)

    def test_fp_60(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/9.png")
        computer = "152.1.138.160"
        self.assertEqual(fp.getFieldPos(frame, computer), 21)

    def test_fp_61(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/10.png")
        computer = "152.1.138.160"
        self.assertEqual(fp.getFieldPos(frame, computer), 18)

    def test_fp_62(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/11.png")
        computer = "152.1.138.160"
        self.assertEqual(fp.getFieldPos(frame, computer), 5)

    def test_fp_63(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/12.png")
        computer = "152.1.138.160"
        self.assertEqual(fp.getFieldPos(frame, computer), 2)

    def test_fp_64(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/13.png")
        computer = "152.1.138.160"
        self.assertEqual(fp.getFieldPos(frame, computer), 25)

    def test_fp_65(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/14.png")
        computer = "152.1.138.160"
        self.assertEqual(fp.getFieldPos(frame, computer), 29)

if __name__ == "__main__":
    unittest.main()
