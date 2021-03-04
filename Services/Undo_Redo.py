class Operations:
    def __init__(self, operation, reverse_operation):
        self.__apply_operations = operation
        self.__apply_reverse_operation = reverse_operation

    def apply_action(self):
        self.__apply_operations()

    def apply_reverse_action(self):
        self.__apply_reverse_operation()
