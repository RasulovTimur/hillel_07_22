class UnexpectedTypeException(Exception):
    pass



def expected(func):
    def inner(text):
        if isinstance(text,str):
            print(f"{text}")
        else:
            raise UnexpectedTypeException("Was expecting types: str")
        return func
    return inner

@expected
def func():
    pass

func(None)
