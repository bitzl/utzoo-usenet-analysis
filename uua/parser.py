import re

class Parser:
    @classmethod
    def accept(cls, first_line):
        raise NotImplementedError()

    def parse(self, line):
        raise NotImplementedError()

    def get_post(self):
        raise NotImplementedError()


class FirstFileFormatParser(Parser):
    accept_pattern = re.compile('\\w+\\.\\d+')

    def __init__(self):
        self.post = {}

    @classmethod
    def accept(cls, first_line):
        return cls.accept_pattern.match(first_line)

    def parse(self, line):
        if line_number < 4:
            self.parse_header(line)
        else:
            self.parse_body(line)
        self.line_number += 1

    def get_post(self):
        pass

    def reset(self):
        self.line_number = 0
        self.post = {}

    def parse_header(self, line):
        pass
        
    def parse_body(self, line):
        self.post['body'] = self.post['body'] + line
    