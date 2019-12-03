from src.model import TypeDecorator, VARBINARY

class my_varbinary(TypeDecorator):
    impl = VARBINARY

    def result_processor(self, dialect, coltype):
        def process(value):
            result = ''
            if isinstance(value, bytes):
                result = str(value)
            else:
                result = value
            return result
        return process
