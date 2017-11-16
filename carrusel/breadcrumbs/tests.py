from django.test import TestCase
from breadcrumbs.models import *
from breadcrumbs.views import *

class ArmarBreadcrumbslHTMLTestCase(TestCase):

    def setUp(self):
        BreadcrumbsLevels.objects.create(niveles=4)

    def test_armarBreadcrumbsHTML(self):
        levels = BreadcrumbsLevels.objects.get(niveles=4)
        breadcrumbs = BreadcrumbsContent.objects.filter(breadcrumb=levels.pk).values()
        data = {
            'elements': BreadcrumbsContent.objects.filter(breadcrumb=levels.pk).values()
        }
        dic = armarBreadcrumbsHTML(data)
        self.assertNotEqual(dic,None)

    def test_armarBreadcrumbsHTML_2(self):
        levels = BreadcrumbsLevels.objects.get(niveles=4)
        data = {
            'elements': BreadcrumbsContent.objects.filter(breadcrumb=levels.pk).values()
        }
        dic = armarBreadcrumbsHTML(data)
        self.assertNotEqual(dic['file'], None)

    def test_armarBreadcrumbsHTML_3(self):
        levels = BreadcrumbsLevels.objects.get(niveles=4)
        data = {
            'elements': BreadcrumbsContent.objects.filter(breadcrumb=levels.pk).values()
        }
        dic = armarBreadcrumbsHTML(data)
        self.assertNotEqual(dic['code'], None)

    def test_armarBreadcrumbsHTML_4(self):
        levels = BreadcrumbsLevels.objects.get(niveles=4)
        data = {
            'elements': BreadcrumbsContent.objects.filter(breadcrumb=levels.pk).values()
        }
        dic = armarBreadcrumbsHTML(data)
        self.assertNotEqual(dic['file'], "")

    def test_armarBreadcrumbsHTML_5(self):
        levels = BreadcrumbsLevels.objects.get(niveles=4)
        data = {
            'elements': BreadcrumbsContent.objects.filter(breadcrumb=levels.pk).values()
        }
        dic = armarBreadcrumbsHTML(data)
        self.assertNotEqual(dic['code'], "")