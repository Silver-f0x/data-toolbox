import typing as t


class BaseModule:
    '''Base module class.'''

    def __iter__(self) -> t.Generator[list[str], None, None]:
        '''Implements the basic iterator interface.'''
        return self.generator()

    def generator(self) -> t.Generator[list[str], None, None]:
        '''
        Should yield dialogue turns that will be used in the model's training /
        validation / test splits.
        '''
        raise NotImplementedError