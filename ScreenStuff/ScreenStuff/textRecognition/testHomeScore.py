import getHomeScore2 as hs
import cv2
import unittest


class test_HomeScore(unittest.TestCase):

    def setUp(self):
        pass

    def test_hs_1(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/1.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_2(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/2.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_3(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/3.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 33)

    def test_hs_4(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/4.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_5(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/5.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_6(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/6.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 17)

    def test_hs_7(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/7.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 14)

    def test_hs_8(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/8.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_9(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/9.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 19)

    def test_hs_10(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/10.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_11(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/11.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 3)

    def test_hs_12(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/12.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_13(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/13.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 59)

    def test_hs_14(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/14.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 30)

    def test_hs_15(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/15.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 6)

    def test_hs_16(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/16.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 27)

    def test_hs_17(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/17.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_18(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/18.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_19(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/19.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 3)

    def test_hs_20(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/20.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 19)

    def test_hs_21(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/21.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 10)

    def test_hs_22(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/22.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 17)

    def test_hs_23(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/23.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 14)

    def test_hs_24(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/24.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_25(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/25.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 14)

    def test_hs_26(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/26.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 21)

    def test_hs_27(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/27.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_28(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/28.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_29(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/29.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_30(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/30.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 3)

    def test_hs_31(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/31.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 30)

    def test_hs_32(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/32.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 10)

    def test_hs_33(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/33.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 17)

    def test_hs_34(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/34.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_35(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/35.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 14)

    def test_hs_36(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/36.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_37(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/37.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_38(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/38.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_39(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/39.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 31)

    def test_hs_40(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/40.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 17)

    def test_hs_41(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/41.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_42(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/42.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 31)

    def test_hs_43(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/43.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_44(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/44.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 14)

    def test_hs_45(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/45.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 19)

    def test_hs_46(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/46.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 10)

    def test_hs_47(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/47.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_48(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/48.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 17)

    def test_hs_49(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/49.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 17)

    def test_hs_50(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/50.png")
        computer = "152.1.138.159"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_51(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/0.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_52(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/1.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_53(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/2.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_54(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/3.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_55(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/4.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_56(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/5.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_57(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/6.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_58(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/7.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_59(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/8.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_60(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/9.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_61(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/10.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_62(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/11.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 0)

    def test_hs_63(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/12.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 6)

    def test_hs_64(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/13.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_65(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/14.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_66(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/15.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_67(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/16.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_68(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/17.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_69(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/18.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_70(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/19.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_71(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/20.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_72(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/21.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_73(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/22.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_74(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/23.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_75(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/24.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_76(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/25.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_77(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/26.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_78(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/27.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_79(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/28.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_80(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/29.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_81(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/30.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_82(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/31.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_83(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/32.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_84(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/33.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_85(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/34.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_86(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/35.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_87(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/36.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_88(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/37.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_89(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/38.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_90(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/39.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_91(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/40.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_92(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/41.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_93(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/42.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_94(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/43.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_95(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/44.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_96(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/45.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_97(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/46.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 7)

    def test_hs_98(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/47.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 13)

    def test_hs_99(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/48.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 14)

    def test_hs_100(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/49.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 14)

    def test_hs_101(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/50.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 14)

    def test_hs_102(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/51.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 14)

    def test_hs_103(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/52.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 14)

    def test_hs_104(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/53.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_105(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/54.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_106(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/55.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_107(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/56.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_108(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/57.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_109(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/58.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_110(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/59.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_111(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/60.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_112(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/61.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_113(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/62.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_114(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/63.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_115(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/64.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_116(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/65.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_117(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/66.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_118(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/67.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_119(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/68.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_120(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/69.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_121(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/70.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_122(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/71.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_123(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/72.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_124(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/73.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_125(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/74.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_126(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/75.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_127(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/76.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_has_128(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/77.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_129(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/78.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_130(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/79.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_131(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/80.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_132(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/81.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_133(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/82.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_134(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/83.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_135(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/84.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_136(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/85.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_137(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/86.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_138(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/87.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_139(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/88.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_140(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/89.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_141(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/90.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_142(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/91.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

    def test_hs_143(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/92.png")
        computer = "152.1.138.160"
        self.assertEqual(hs.getHomeScore(frame, computer), 20)

if __name__ == "__main__":
    unittest.main()
