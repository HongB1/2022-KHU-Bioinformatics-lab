class Vector():
    '''Vector class를 구현해봅시다.'''
    def __init__(self, x, y, z): # ! *args 언패킹을 해주기 -> 세련된 방법. 잘 만든 소스보기
        '''Create a vector, example : v = Vector(5, 10)'''
        self._x, self._y, self._z = x, y, z

    def __repr__(self):
        '''Return the information of the vector'''
        return 'Vector(%r, %r, %r)' % (self._x, self._y, self._z) # %r : 객체표현으로 출력해줌 raw string
        
    def __add__(self, other):
        '''Return the vector addition of self and other'''
        return Vector(self._x + other._x, self._y + other._y, self._z + other._z) # other은 다른 인스턴스

    def __mul__(self, scalar):
        '''Return the vector multiplication of self and scalar'''
        return Vector(self._x * scalar, self._y * scalar, self._z * scalar)

    def __bool__(self): # (0, 0)인지를 확인하는 메소드
        return bool(max(self._x, self._y, self._z))
