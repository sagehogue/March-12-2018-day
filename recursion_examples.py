from datetime import datetime
#
#
# def fibo(n):
#     # print('n == {}'.format(n))
#     if n == 1 or n == 2:
#         # print('end recursion')
#         return 1
#     # print('start new recursion...')
#
#     return fibo(n-1) + fibo(n-2)
#
# class Memoize:
#  def __init__(self, fn):
#   self.fn = fn
#   self.memo = {}
#  def __call__(self, arg):
#   if arg not in self.memo:
#    self.memo[arg] = self.fn(arg)
#    return self.memo[arg]
#
# @Memoize
# def fib(n):
#  a,b = 1,1
#  for i in range(n-1):
#   a,b = b,a+b
#  return a

# start = datetime.now()
# print(fib(1000))
# end = datetime.now()
#
# print(end - start)
