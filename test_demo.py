import pytest


@pytest.fixture(scope='class')
def start():
    print('888888888')
    c = 3
    yield c
    print('aaaaaaaaaa')


class Test_Demo():

    @pytest.mark.parametrize('a,b', [(1, 2), (2, 2), (1, 3)], ids=['1', '2', '3'])
    def test_one(self, a, b,start):
        print('1111')
        assert a + b == start


if __name__ == '__main__':
    pytest.main('-s,-v')
