from django.test import TestCase
from paginacion.paginator import *

class PaginationTestCase(TestCase):
	def setUp(self):
		self.paginator = None
		
	def test_crearPaginador(self):
		lista = ['asd', 'bobba', 'foo', 'bar' , 'dsa', 'sad', 'ninesoft']
		
		#Caso trivial
		self.paginator = TUIsDPaginator(lista, 2)
		self.assertNotEqual(self.paginator, None)
		self.paginator = None
		
		#Caso borde
		self.paginator = TUIsDPaginator([], 2)
		self.assertNotEqual(self.paginator, None)
		self.paginator = None
		
		#Casos en que deberia fallar
		with self.assertRaises(ValueError):
			self.paginator = TUIsDPaginator([], -1)
		self.paginator = None
		
		with self.assertRaises(ValueError):
			self.paginator = TUIsDPaginator([], 0)
		self.paginator = None
		
	def test_seleccionarPagina(self):
		lista = ['asd', 'bobba', 'foo', 'bar' , 'dsa', 'sad', 'ninesoft']
		self.paginator = TUIsDPaginator(lista, 3)
		
		#Caso trivial
		elems = self.paginator.get_elems_from_page(1).object_list
		self.assertEquals(elems, ['asd', 'bobba', 'foo'])
		
		#Casos borde
		elems = self.paginator.get_elems_from_page(3).object_list
		self.assertEquals(elems, ['ninesoft'])
		
		#Casos en que deberia fallar
		elems = self.paginator.get_elems_from_page(-1).object_list
		self.assertEquals(elems, ['ninesoft'])
		
		elems = self.paginator.get_elems_from_page(5).object_list
		self.assertEquals(elems, ['ninesoft'])
		
		elems = self.paginator.get_elems_from_page(2.9).object_list
		self.assertEquals(elems, ['asd', 'bobba', 'foo'])
