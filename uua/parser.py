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
        self.line_number = 0
        self.keys = [
            'message_id',
            'newsgroup',
            'path',
            'timestamp',
            'subject'
        ]
        self.reset()

    @classmethod
    def accept(cls, first_line):
        return cls.accept_pattern.match(first_line)

    def parse(self, line):
        if self.line_number < len(self.keys):
            self.parse_header(line)
        else:
            self.parse_body(line)
        self.line_number += 1

    def get_post(self):
        post = self.post
        post['body'] = post['body'][:-1]
        self.reset()
        return post

    def reset(self):
        self.line_number = 0
        self.post = { 'body': '' }

    def parse_header(self, line):
        key = self.keys[self.line_number]
        self.post[key] = line

    def parse_body(self, line):
        self.post['body'] = self.post['body'] + line + '\n'
    