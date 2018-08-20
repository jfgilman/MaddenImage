import getDown2 as gd
import cv2
import unittest


class test_GetDown(unittest.TestCase):

    def setUp(self):
        pass

    def test_down_1(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/1.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_2(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/2.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 4)

    def test_down_3(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/3.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_4(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/4.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_5(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/5.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_6(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/6.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_7(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/7.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 3)

    def test_down_8(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/8.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_9(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/9.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_10(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/10.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 4)

    def test_down_11(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/11.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_12(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/12.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 3)

    def test_down_13(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/13.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_14(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/14.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_15(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/15.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_16(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/16.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_17(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/17.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_18(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/18.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_19(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/19.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_20(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/20.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_21(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/21.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_22(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/22.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_23(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/23.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_24(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/24.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_25(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/25.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 3)

    def test_down_26(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/26.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 3)

    def test_down_27(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/27.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_28(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/28.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 4)

    def test_down_29(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/29.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_30(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/30.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_31(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/31.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_32(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/32.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_33(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/33.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 4)

    def test_down_34(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/34.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_35(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/35.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 3)

    def test_down_36(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/36.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_37(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/37.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_38(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/38.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_39(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/39.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_40(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/40.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 4)

    def test_down_41(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/41.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_42(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/42.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_43(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/43.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_44(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/44.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_45(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/45.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 3)

    def test_down_46(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/46.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 3)

    def test_down_47(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/47.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_48(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/48.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_49(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/49.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_50(self):
        frame = cv2.imread("ScreenStuff/images/comp4Images/50.png")
        computer = "152.1.138.159"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_51(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/0.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_52(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/1.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_53(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/2.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 3)

    def test_down_54(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/3.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 4)

    def test_down_55(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/4.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_56(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/5.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_57(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/6.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_58(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/7.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 3)

    def test_down_59(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/8.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_60(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/9.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_61(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/10.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_62(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/11.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    # def test_down_63(self):
    #     frame = cv2.imread("ScreenStuff/images/comp3Images/12.png")
    #     computer = "152.1.138.160"
    #     self.assertEqual(gd.getDown(frame, computer), 0)

    def test_down_64(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/13.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_65(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/14.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_66(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/15.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_67(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/16.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_68(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/17.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_69(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/18.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_70(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/19.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_71(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/20.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_72(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/21.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_73(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/22.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_74(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/23.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_75(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/24.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_76(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/25.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 3)

    def test_down_77(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/26.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 4)

    def test_down_78(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/27.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_79(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/28.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_80(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/29.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 3)

    def test_down_81(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/30.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_82(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/31.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_83(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/32.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_84(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/33.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 3)

    def test_down_85(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/34.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 4)

    def test_down_86(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/35.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_87(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/36.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_88(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/37.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_89(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/38.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_90(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/39.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_91(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/40.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_92(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/41.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_93(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/42.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 3)

    def test_down_94(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/43.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_95(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/44.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_96(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/45.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_97(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/46.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 3)

    # def test_down_98(self):
    #     frame = cv2.imread("ScreenStuff/images/comp3Images/47.png")
    #     computer = "152.1.138.160"
    #     self.assertEqual(gd.getDown(frame, computer), 0)

    def test_down_99(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/48.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_100(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/49.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_101(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/50.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 3)

    def test_down_102(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/51.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 4)

    def test_down_103(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/52.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    # def test_down_104(self):
    #     frame = cv2.imread("ScreenStuff/images/comp3Images/53.png")
    #     computer = "152.1.138.160"
    #     self.assertEqual(gd.getDown(frame, computer), 0)

    def test_down_105(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/54.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_106(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/55.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_107(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/56.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_108(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/57.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_109(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/58.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 3)

    def test_down_110(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/59.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 4)

    def test_down_111(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/60.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_112(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/61.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_113(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/62.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_114(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/63.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_115(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/64.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_116(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/65.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_117(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/66.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_118(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/67.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 3)

    def test_down_119(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/68.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 4)

    # def test_down_120(self):
    #     frame = cv2.imread("ScreenStuff/images/comp3Images/69.png")
    #     computer = "152.1.138.160"
    #     self.assertEqual(gd.getDown(frame, computer), 0)

    def test_down_121(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/70.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_122(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/71.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_123(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/72.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_124(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/73.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_125(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/74.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_126(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/75.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_127(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/76.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 3)

    def test_down_128(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/77.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_129(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/78.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_130(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/79.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_131(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/80.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_132(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/81.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 3)

    def test_down_133(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/82.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 4)

    def test_down_134(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/83.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_135(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/84.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_as_136(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/85.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_137(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/86.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_138(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/87.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_139(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/88.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 3)

    def test_down_140(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/89.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 1)

    def test_down_141(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/90.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 2)

    def test_down_142(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/91.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 3)

    def test_down_143(self):
        frame = cv2.imread("ScreenStuff/images/comp3Images/92.png")
        computer = "152.1.138.160"
        self.assertEqual(gd.getDown(frame, computer), 4)

if __name__ == "__main__":
    unittest.main()
