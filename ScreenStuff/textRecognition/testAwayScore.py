import getAwayScore2 as awayS
import cv2
import unittest


class test_AwayScore(unittest.TestCase):

    def setUp(self):
        pass

    def test_as_1(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/1.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_2(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/2.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_3(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/3.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 19)

    def test_as_4(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/4.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 7)

    def test_as_5(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/5.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 7)

    def test_as_6(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/6.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 17)

    def test_as_7(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/7.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_8(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/8.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 21)

    def test_as_9(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/9.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 14)

    def test_as_10(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/10.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_11(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/11.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 7)

    def test_as_12(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/12.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_13(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/13.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 14)

    def test_as_14(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/14.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 12)

    def test_as_15(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/15.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 31)

    def test_as_16(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/16.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 7)

    def test_as_17(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/17.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_18(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/18.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 14)

    def test_as_19(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/19.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 21)

    def test_as_20(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/20.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 14)

    def test_as_21(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/21.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_22(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/22.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 7)

    def test_as_23(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/23.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 7)

    def test_as_24(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/24.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 7)

    def test_as_25(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/25.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_26(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/26.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 21)

    def test_as_27(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/27.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_28(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/28.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_29(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/29.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 21)

    def test_as_30(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/30.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_31(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/31.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 12)

    def test_as_32(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/32.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_33(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/33.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 17)

    def test_as_34(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/34.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 14)

    def test_as_35(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/35.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 7)

    def test_as_36(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/36.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_37(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/37.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_38(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/38.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 14)

    def test_as_39(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/39.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 9)

    def test_as_40(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/40.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_41(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/41.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_42(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/42.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 14)

    def test_as_43(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/43.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_44(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/44.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 7)

    def test_as_45(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/45.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 14)

    def test_as_46(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/46.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_47(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/47.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_48(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/48.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 7)

    def test_as_49(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/49.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_50(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/50.png")
        computer = "152.1.138.159"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_51(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/0.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_52(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/1.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_53(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/2.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_54(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/3.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_55(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/4.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_56(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/5.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_57(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/6.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_58(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/7.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_59(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/8.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_60(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/9.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_61(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/10.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_62(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/11.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_63(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/12.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_64(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/13.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_65(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/14.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_66(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/15.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_67(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/16.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_68(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/17.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_69(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/18.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_70(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/19.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_71(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/20.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_72(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/21.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_73(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/22.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_74(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/23.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_75(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/24.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_76(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/25.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_77(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/26.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_78(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/27.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_79(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/28.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_80(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/29.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_81(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/30.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_82(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/31.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_83(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/32.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_84(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/33.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_85(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/34.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 0)

    def test_as_86(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/35.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_87(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/36.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_88(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/37.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_89(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/38.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_90(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/39.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_91(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/40.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_92(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/41.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_93(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/42.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_94(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/43.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_95(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/44.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_96(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/45.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_97(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/46.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_98(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/47.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_99(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/48.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_100(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/49.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_101(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/50.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_102(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/51.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_103(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/52.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_104(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/53.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_105(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/54.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_106(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/55.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_107(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/56.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_108(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/57.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_109(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/58.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_110(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/59.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_111(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/60.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_112(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/61.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_113(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/62.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_114(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/63.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_115(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/64.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_116(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/65.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_117(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/66.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_118(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/67.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_119(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/68.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 3)

    def test_as_120(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/69.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 9)

    def test_as_121(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/70.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_122(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/71.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_123(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/72.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_124(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/73.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_125(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/74.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_126(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/75.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_127(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/76.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_128(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/77.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_129(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/78.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_130(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/79.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_131(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/80.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_132(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/81.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_133(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/82.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_134(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/83.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_135(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/84.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_136(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/85.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_137(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/86.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_138(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/87.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_139(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/88.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_140(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/89.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_141(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/90.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_142(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/91.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)

    def test_as_143(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/92.png")
        computer = "152.1.138.160"
        self.assertEqual(awayS.getAwayScore(frame, computer), 10)


if __name__ == "__main__":
    unittest.main()
