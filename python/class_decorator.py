class MyProxy:
  def __init__(self, target):
    self.target = target

  def __getattr__(self, attr):
    print("__getattr__({}, {})".format(self, attr))
    method = getattr(self.target, attr)
    def wrapped_method(*args, **kwargs):
      print("wrapped_method {}({}, {})".format(method, args, kwargs))
      return method(*args, **kwargs)
    return wrapped_method


class MyClassDecorator:
  def __init__(self, clazz, *args, **kwargs):
    print("__init__ {}, {}, {} {}".format(self, clazz, args, kwargs))
    self.clazz = clazz

  def __call__(self, method, *args, **kwargs):
    print("__call__ {}, {}, {} {}".format(self, method, args, kwargs))
    self.instance = MyProxy(self.clazz(*args, *kwargs))
    return self.instance


@MyClassDecorator
class Message:
  def __init__(self, text, ending="!"):
    self.text  = text
    self.ending = ending

  def getit(self):
    return "{}{}".format(self.text, self.ending)

if __name__ == '__main__':
  m = Message("hello", ending="!!!")
  print(m.getit())
