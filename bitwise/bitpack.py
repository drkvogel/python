


class BitPack:
  the_num = 1 # NameError: name 'the_num' is not defined

  def __init__(self):
    super().__init__()
    # self.the_num = 1
    # print(f'the_num: {the_num}') # NameError: name 'the_num' is not defined
    print(f'the_num: {self.the_num}')

  def reset(self):
    self.the_num = 0

  def show(self):
    print(f'the_num: {the_num}')

  def put_a(self):
    pass

  def put_b(self):
    pass

  def get_a(self):
    pass

  def get_b(self):
    pass


  def print_bin(self, num):
    print('{0:b}'.format(num))
    # e.g. s'1000011100001'

# TODO min (0), max (depends on bits available) check
# TODO more than two - use subscript for n divisions

# instruction_id = 4321
# client_id = 12

# bs = BitPack()
