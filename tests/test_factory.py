from unittest import TestCase
from rectpack.packer import newPacker, PackingMode, PackingBin
import random


class TestFactory(TestCase):
    
    def setUp(self):
        self.rectangles = [(w, h) for w in range(8,50, 8) for h in range(8,50, 8)]

    def _prepare(self, mode, bin_algo, width, height):
        print('newPacker', mode, bin_algo)
        p = newPacker(mode, bin_algo)
        print('add_factory', width, height)
        p.add_factory(width, height)
        print('add_rect', sep='', end='')
        for r in self.rectangles:
            print('.', sep='', end='')
            p.add_rect(*r)
        print()
        if mode == PackingMode.Offline:
            print('pack')
            p.pack()
        print('done')
        return p

    def test_Offline_BNF_50(self):
        p = self._prepare(PackingMode.Offline, PackingBin.BNF, 50, 50)
        # check that bins were created
        self.assertGreater(len(p.bin_list()), 0)
        # check that all of the rectangles made it in
        self.assertEqual(len(p.rect_list()), len(self.rectangles))

    def test_Offline_BNF_5(self):
        p = self._prepare(PackingMode.Offline, PackingBin.BNF, 5, 5)
        # check that none of the rectangles made it in
        self.assertEqual(len(p.rect_list()), 0)

    def test_Offline_BFF_50(self):
        p = self._prepare(PackingMode.Offline, PackingBin.BFF, 50, 50)
        # check that bins were created
        self.assertGreater(len(p.bin_list()), 0)
        # check that all of the rectangles made it in
        self.assertEqual(len(p.rect_list()), len(self.rectangles))

    def test_Offline_BFF_5(self):
        p = self._prepare(PackingMode.Offline, PackingBin.BFF, 5, 5)
        # check that none of the rectangles made it in
        self.assertEqual(len(p.rect_list()), 0)

    def test_Offline_BBF_50(self):
        p = self._prepare(PackingMode.Offline, PackingBin.BBF, 50, 50)
        # check that bins were created
        self.assertGreater(len(p.bin_list()), 0)
        # check that all of the rectangles made it in
        self.assertEqual(len(p.rect_list()), len(self.rectangles))

    def test_Offline_BBF_5(self):
        p = self._prepare(PackingMode.Offline, PackingBin.BBF, 5, 5)
        # check that none of the rectangles made it in
        self.assertEqual(len(p.rect_list()), 0)

# TODO:  The following test isn't working, len(p.rect_list()) is 0.
##    def test_Offline_Global_50(self):
##        p = self._prepare(PackingMode.Offline, PackingBin.Global, 50, 50)
##        # check that bins were created
##        self.assertGreater(len(p.bin_list()), 0)
##        # check that all of the rectangles made it in
##        self.assertEqual(len(p.rect_list()), len(self.rectangles))

    def test_Offline_Global_5(self):
        p = self._prepare(PackingMode.Offline, PackingBin.Global, 5, 5)
        # check that none of the rectangles made it in
        self.assertEqual(len(p.rect_list()), 0)


def helper():
    """create a bunch of tests to copy and paste above"""
    for mode in PackingMode:
        for bin_algo in PackingBin:
            for size in '50', '5':
                name = '_'.join(('test', mode, bin_algo, size))
                print("""\
    def %s(self):
        p = self._prepare(PackingMode.%s, PackingBin.%s, %s, %s)""" %
                      (name, mode, bin_algo, size, size))
                if size == '50':
                    print("""\
        # check that bins were created
        self.assertGreater(len(p.bin_list()), 0)
        # check that all of the rectangles made it in
        self.assertEqual(len(p.rect_list()), len(self.rectangles))
""")
                else:
                    print("""\
        # check that none of the rectangles made it in
        self.assertEqual(len(p.rect_list()), 0)
""")
