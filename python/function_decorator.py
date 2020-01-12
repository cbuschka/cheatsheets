class MyFuncDecorator:
  def __init__(self, function):
    self.function = function

  def __call__(self, *args, **kvargs):
    return ">>>> {} <<<<".format(self.function(*args, **kvargs))

@MyFuncDecorator
def say_hello(name, ending="!"):
  return "huhu {}{}".format(name, ending)

if __name__ == '__main__':
  print(say_hello("conni", "!!!"))
