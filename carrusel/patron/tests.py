from django.test import TestCase
from patron.models import Carousel
from patron.views import *

class ArmarCarruselHTMLTestCase(TestCase):

    def setUp(self):
        Carousel.objects.create(count=2, title="Nuevo")

    def armarCarruselHTML_test(self):
        carousel = Carousel.objects.get(title="Nuevo")
        data = {
            'duration': carousel.timer * 1000,
            'automatic': carousel.auto,
            'circular': carousel.circular,
            'title': carousel.title,
            'elements': carousel.content_set.all().values()
        }
        dic = armarCarruselHTML(data)
        self.assertNotEqual(dic,None)

    def test_armarCarruselHTML_1(self):
        carousel = Carousel.objects.get(title="Nuevo")
        data = {
            'duration': carousel.timer * 1000,
            'automatic': carousel.auto,
            'circular': carousel.circular,
            'title': carousel.title,
            'elements': carousel.content_set.all().values()
        }
        dic = armarCarruselHTML(None)
        self.assertEqual(dic,None)

    def test_armarCarruselHTML_2(self):
        carousel = Carousel.objects.get(title="Nuevo")
        data = {
            'duration': carousel.timer * 1000,
            'automatic': carousel.auto,
            'circular': carousel.circular,
            'title': carousel.title,
            'elements': carousel.content_set.all().values()
        }
        dic = armarCarruselHTML(data)
        self.assertNotEqual(dic['file'], None)

    def test_armarCarruselHTML_3(self):
        carousel = Carousel.objects.get(title="Nuevo")
        data = {
            'duration': carousel.timer * 1000,
            'automatic': carousel.auto,
            'circular': carousel.circular,
            'title': carousel.title,
            'elements': carousel.content_set.all().values()
        }
        dic = armarCarruselHTML(data)
        self.assertNotEqual(dic['code'], None)

    def test_armarCarruselHTML_4(self):
        carousel = Carousel.objects.get(title="Nuevo")
        data = {
            'duration': carousel.timer * 1000,
            'automatic': carousel.auto,
            'circular': carousel.circular,
            'title': carousel.title,
            'elements': carousel.content_set.all().values()
        }
        dic = armarCarruselHTML(data)
        self.assertNotEqual(dic['file'], "")

    def test_armarCarruselHTML_5(self):
        carousel = Carousel.objects.get(title="Nuevo")
        data = {
            'duration': carousel.timer * 1000,
            'automatic': carousel.auto,
            'circular': carousel.circular,
            'title': carousel.title,
            'elements': carousel.content_set.all().values()
        }
        dic = armarCarruselHTML(data)
        self.assertNotEqual(dic['code'], "")

    def test_armarCarruselCSS(self):
        carousel = Carousel.objects.get(title="Nuevo")
        data = {
            'duration': carousel.timer * 1000,
            'automatic': carousel.auto,
            'circular': carousel.circular,
            'title': carousel.title,
            'elements': carousel.content_set.all().values()
        }
        string = armarCarruselCSS()
        self.maxDiff = None
        self.assertEqual(string,"""
* {
  box-sizing: border-box;
}
.code{
  height: 300px;
  overflow-y: auto;
}
.slider {
  width: 100%;
  max-width: 700px;
}
.slides {
  background: #ccc;
}
.slide {
  display: flex !important;
  justify-content: center;
  align-items: center;
  background: #fff;
  height: 400px;
  width: 700px;
  outline: 0 !important;
  color: #ccc;
  font-size: 40px;
}
.controls {
  display: flex;
  width: 100%;
}
.captions {
  flex: 1;
  width: 100px;
  padding: 10px;
  margin-top: 2px;
  color: #7b7b7b;
  background: #fff;
}
.caption {
  outline: 0 !important;
}
.pagination {
  display: flex;
  margin-top: 2px;
}
.pagination__button {
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #ccc;
  background: #fff;
  width: 40px;
  height: 40px;
  margin-left: 2px;
}
.pagination__button:hover {
  color: #fff;
  background: #2aa1c0;
}
.pagination__button.slick-disabled {
  cursor: not-allowed;
  background: #ccc;
  color: #fff;
}
""")