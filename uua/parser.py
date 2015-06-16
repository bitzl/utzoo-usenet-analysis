import re

class Parser:
    @classmethod
    def accept(cls, first_line):
        raise NotImplementedError()

    def parse(self, line):
        raise NotImplementedError()

    def get_post(self):
        raise NotImplementedError()

    def parse_lines(self, lines):
        for line in lines:
            self.parse(line)


class FirstFileFormatParser(Parser):
    accept_pattern = re.compile('\\w+\\.\\d+')

    def __init__(self):
        self.post = { 'body': '' }
        self.line_number = 0
        self.keys = [
            'message_id',
            'newsgroup',
            'path',
            'timestamp',
            'subject'
        ]

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
        return post

    def parse_header(self, line):
        key = self.keys[self.line_number]
        self.post[key] = line

    def parse_body(self, line):
        self.post['body'] = self.post['body'] + line + '\n'


class SecondFileFormatParser(Parser):

    def __init__(self):
        self.post = { 'body': '' }
        self.new_line_count = 0

    @classmethod
    def accept(cls, first_line):
        return first_line.startswith('Path: ')

    def parse(self, line):
        if self.new_line_count < 3:
            if line == '':
                self.new_line_count += 1
            else:
                self.parse_header(line)
        else:
            self.parse_body(line)

    def get_post(self):
        post = self.post
        post['body'] = post['body'][:-1]
        return post

    def parse_header(self, line):
        key, value = line.split(': ', 1)
        key = key.replace('-', '_')
        key = key.replace('Date', 'timestamp')
        self.post[key.lower()] = value

    def parse_body(self, line):
        self.post['body'] = self.post['body'] + line + '\n'
    