import warnings
# try:
#     try:
#         print('Start')
#         print(10/0)
#         print('No errors')
#     except SyntaxError:
#         print("Wrong errors")
# except (NameError, ZeroDivisionError) as error:
#     print(error)
#
#
# print('Next error')


# try:
#     print('Start')
#
# except (NameError) as error:
#     print(error)
# else:
#     print('no problems')
#
# finally:
#     print('Finally code')
#
# print('Next error')


# def checker(a):
#     if type(a) != str:
#         raise TypeError(f"Sorry, we can`t work with {type(a)},"f"we need class str")
#     else:
#         return a
#
#
#
#
# var = 10
# checker(var)

warnings.simplefilter('ignore', SyntaxWarning)
warnings.simplefilter('always', ImportWarning)

warnings.warn('Warning, no code here', SyntaxWarning)
try:
    warnings.warn('Warning, module not import', ImportWarning)
except:
    print("Warning progressed")
