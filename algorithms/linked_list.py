class Element(object):
	"""this class is implenting element of linked list"""
	def __init__(self, value, NextElement = None, PreviousElement = None):
		self.value = value
		self.PreviousElement = PreviousElement
		self.NextElement = NextElement

class LinkedList(object):
	"""this class is implenting linked list"""
	"""variable "vault" implenting memory and acess to it"""
	def __init__(self):
		self.vault = []
		self.head = None
		self.tail = None

	def add(self, element:Element):
		if len(self.vault) == 0:
			self.vault.append(element)
			self.head = element
			self.tail = element
			return 1

		else:
			elem = self.head
			while elem.NextElement is not None:
				elem = elem.NextElement
			self.vault.append(element)
			elem.NextElement = element
			self.tail = element
			return 1

	def delete(self, value):
		if len(self.vault) == 0:
			return 0
		else:
			elem = self.head
			while 1:
				if elem.value == value:
					elem.PreviousElement.NextElement = element.NextElement
					vault.remove(elem)
					return 1
			return 0

	def read(self, value):
		if len(self.vault) == 0:
			return 0
		else:
			elem = self.head
			while 1:
				if elem.value == value:
					return elem
				elif elem == self.tail:
					return 0
				elem = elem.NextElement
			return 0


AwesomeList = LinkedList()
a = Element(23)
b = Element(24)
a.NextElement = b
AwesomeList.add(a)
AwesomeList.add(b)
 
print(AwesomeList.read(23).NextElement.value)