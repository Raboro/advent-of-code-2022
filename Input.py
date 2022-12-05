class Input:

    @classmethod
    def get_input_of_file(cls, filename: str) -> list:
        with open(filename, "r") as file:
            return file.readlines()