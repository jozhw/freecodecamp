
class Demo:
  name = "squirrel"

  def get_name(self):
    print(self.name)

  @classmethod
  def change_name(cls, new_name: str):
    cls.name = new_name
    return cls()

demo = Demo()
demo.get_name()
demo_change = demo.change_name("cat")
demo_change.get_name()