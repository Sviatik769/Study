# arr = [1,2,3]
# iterator = iter(arr)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# for elem in iterator:
#     print(elem)
# for elem in iterator:
#     print(elem)
#
# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#
#     def __iter__(self):
#         self.i = 0
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
#
#
# count = Counter(5)
# for elem in count:
#     print(elem)
#
#

# def raise_to_the_degrees(number, max_degree):
#     i = 0
#     for _ in  range(max_degree):
#         yield number ** i
#         i += 1
#
#
# res = raise_to_the_degrees(10,100)
# print(res)
# for _ in res:
#     print(_)




# class Helper:
#     def __init__(self, work):
#         self.work = work
#
#     def __call__(self, work):
#         return f"Will help you with your {self.work}. AfterwardsI I will help you with {work}"
#
# helper = Helper('Homework')
# print(helper("Clearning"))


# def helper(work):
#     work_in_memory = work
#
#
#     def helper(work):
#         return f"I will help you with your {work_in_memory}.Afterwards I will help you with {work}"
#     return helper
#
# helper = helper('Homework')
# print(helper("clearning"))
# print(helper("driving"))


# def checker(function, *args, **kwargs):
#     try:
#         result = function(*args, **kwargs)
#     except Exception as  exc:
#         print(f"We have a problem {exc}")
#     else:print(f"No problems. Result - {result}")
#
#
# def calculate(expresion):
#     return eval(expresion)
#
# checker(calculate, '2+2')


def checker(*exc_types):
    def checker(funtions):

        def checker(*args, **kwargs):
            try:
                result = funtions(*args, **kwargs)
            except (exc_types) as exc:
                print(f"We have a probles {exc}")
            else:
                print(f"No problems. Result - {result}")
        return checker
    return checker


@checker(NameError,TypeError,SyntaxError,ZeroDivisionError)
def calculate(expression):
    return eval(expression)

calculate('2+2')
