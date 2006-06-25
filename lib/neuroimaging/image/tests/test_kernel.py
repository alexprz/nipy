import unittest

from neuroimaging.image import Image
from neuroimaging.image.kernel_smooth import LinearFilter
from neuroimaging.data import Repository
from neuroimaging.visualization import viewer

class KernelTest(unittest.TestCase):
    def test_smooth(self):
        rho = Image('../../tests/data/rho.img', datasource=Repository("."))
        smoother = LinearFilter(rho.grid)

        srho = smoother.smooth(rho)
        view = viewer.BoxViewer(rho)
        view.draw()

        sview = viewer.BoxViewer(srho)
        sview.m = view.m
        sview.M = view.M
        sview.draw()

def suite():
    suite = unittest.makeSuite(KernelTest)
    return suite

        
if __name__ == '__main__':
    unittest.main()
