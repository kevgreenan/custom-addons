import sys

class Stack:
	def __init__(self, size):
		self.a = [""]*size
		self.b = -1
		self.c = size
		self.EmptyStackException = "ERROR: The stack is empty!"
		self.SmallStackException = "ERROR: The stack is too small to peek more than once!"
		self.LargeStackException = "ERROR: The stack has exceeded the maximum height!"
		self.StackSizeMultiplierWarning = "WARNING: The stack size will triple."
		self.StackSizeAdditionWarning = "WARNING: The stack size will increase by 10,000,000."
		self.ToStringTimeLength = "WARNING: This may take some time; over 1,000,000 items on the stack."

	def IsEmpty(self):
		return self.b == -1

	def Count(self):
		return self.b + 1

	def Clear(self):
		self.b = -1

	def RemoveAll(self, item):
		notDone = True
		while notDone:
			if item in self.a:
				self.a.remove(item)
			else:
				notDone = False

	def Contains(self, item):
		if item in self.a:
			return True
		else:
			return False

	def IncreaseSize(self):
		if self.c < 177147:
			print(self.StackSizeMultiplierWarning)
			i = 0
			while i < self.c*2:
				self.a.append("")
				i += 1
			self.c = len(self.a)
		elif self.c >= 177147:
			print(self.StackSizeAdditionWarning)
			i = 0
			while i < 10000000:
				self.a.append("")
				i += 1
			self.c = len(self.a)
		else:
			print(self.LargeStackException)

	def Peek(self):
		if self.IsEmpty() == False:
			return self.a[self.b]
		else:
			return self.EmptyStackException

	def PeekNext(self):
		if self.Count() >= 2:
			return self.a[self.b + 1]
		elif self.Count() >= 1:
			return self.SmallStackException
		else:
			return self.EmptyStackException

	def Push(self, value):
		if self.Count() < self.c:
			self.a[self.Count()] = value
			self.b += 1
		else:
			self.IncreaseSize()
			self.a[self.Count()] = value
			self.b += 1

	def Pop(self):
		if self.IsEmpty() == False:
			self.b -= 1
			return self.a[self.b + 1]
		else:
			return self.EmptyStackException

	def Purge(self, size):
		self.Clear()
		self.a = [""]*size
		self.c = size

	def ToString(self):
		if self.IsEmpty() == False and self.c < 1000000:
			ret = ""
			i = 0
			while i < self.Count():
				ret += str(self.a[i])
				ret += "\n"
				i += 1
			return ret
		elif self.IsEmpty() == False and self.c >= 1000000:
			print(self.ToStringTimeLength)
			ret = ""
			i = 0
			while i < self.Count():
				ret += str(self.a[i])
				ret += "\n"
				i += 1
			return ret
		else:
			return self.EmptyStackException
