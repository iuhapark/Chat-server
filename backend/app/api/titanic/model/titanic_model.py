from dataclasses import dataclass

#deprecated
# @dataclass
# class TitanicModel:
#     def __init__(self):
#         self.context = None  # java에서 클래스 만든 뒤 new instance한 것과 같음
#         self.train = None
#         self.test = None
#         self.fname = ''
#         self.id = 0
#         self.label = 0

@dataclass
class TitanicModel:
    context: str
    fname: str
    train: object
    test: object
    id: str
    label: str
    
    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> object: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> object: return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, label): self._label = label

    


