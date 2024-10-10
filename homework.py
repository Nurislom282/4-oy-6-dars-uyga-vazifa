#1
# class SimpleIterator:
#     def __init__(self):
#         self.current = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current > 10:
#             raise StopIteration
#         else:
#             number = self.current
#             self.current += 1
#             return number
# iterator = SimpleIterator()
# for number in iterator:
#     print(number)
#2
# my_list = [1, 2, 3, 4, 5]
# iterator = iter(my_list)
# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break
#3
# class ReverseIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index -= 1
#         return self.data[self.index]
# my_list = [1, 2, 3, 4, 5]
# reverse_iter = ReverseIterator(my_list)
# for item in reverse_iter:
#     print(item)
#4
# def print_each_character(string):
#     for char in string:
#         print(char)
#
# my_string = "Salom, dunyo!"
# print_each_character(my_string)
#5
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))
