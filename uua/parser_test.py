from uua.parser import FirstFileFormatParser, SecondFileFormatParser
from unittest import TestCase, main


raw_post_using_first_file_format = """Acbosg.129
net.general
utzoo!decvax!duke!mhtsa!harpo!cbosg!mark
Thu Aug 27 08:28:10 1981
Re: UUCP gateway
First line of message body.

Here is some text
which may span multiple lines.
"""

raw_post_using_second_file_format = """Path: utzoo!utgpu!news-server.csri.toronto.edu
From: dtj@sumac.cray.com (Dean Johnson)
Newsgroups: sci.virtual-worlds
Subject: Re: Japanese Symposium on Artificial Reality, 9-10 July 1991, Tokyo
Message-ID: <1991Jun21.055051.28165@milton.u.washington.edu>
Date: 21 Jun 91 02:56:59 GMT
Sender: hlab@milton.u.washington.edu (Human Int. Technology Lab)
Organization: University of Washington
Lines: 3
Approved: cyberoid@milton.u.washington.edu



This is a test for the body.

A second paragraph.
"""


class FirstFileFormatParserTest(TestCase):
	def setUp(self):
		self.parser = FirstFileFormatParser()
		self.lines = raw_post_using_first_file_format.split('\n')

	def test_accept(self):
		self.assertTrue(FirstFileFormatParser.accept('Autzoo.101'))

	def test_accept_rejects_wrong_format(self):
		self.assertFalse(self.parser.accept('Path: utzoo!telly!attcan!utgpu!news-server.csri.toronto.edu!' + 
			'bonnie.concordia.ca!uunet!looking!xenitec!sco!timr'))

	def test_parse_gets_message_id(self):
		self.parser.parse_lines(self.lines)
		post = self.parser.get_post()
		self.assertEquals(post['message_id'], '<1991Jun21.055051.28165@milton.u.washington.edu>')

	def test_parse_gets_newsgroup(self):
		self.parser.parse_lines(self.lines)
		post = self.parser.get_post()
		self.assertEquals(post['newsgroup'], 'net.general')


	def test_parse_gets_path(self):
		self.parser.parse_lines(self.lines)
		post = self.parser.get_post()
		self.assertEquals(post['path'], 'utzoo!decvax!duke!mhtsa!harpo!cbosg!mark')


	def test_parse_gets_timestamp(self):
		self.parser.parse_lines(self.lines)
		post = self.parser.get_post()
		self.assertEquals(post['timestamp'], 'Thu Aug 27 08:28:10 1981')

	def test_parse_gets_subject(self):
		self.parser.parse_lines(self.lines)
		post = self.parser.get_post()
		self.assertEquals(post['subject'], 'Re: UUCP gateway')

	def test_parse_gets_message_id(self):
		self.parser.parse_lines(self.lines)
		post = self.parser.get_post()
		self.assertEquals(post['body'], """First line of message body.

Here is some text
which may span multiple lines.
""")



class SecondFileFormatParserTest(TestCase):
	def setUp(self):
		self.parser = SecondFileFormatParser()
		self.lines = raw_post_using_second_file_format.split('\n')

	def test_accept(self):
		self.assertTrue(SecondFileFormatParser.accept('Path: utzoo!telly!attcan!utgpu'))

	def test_accept_rejects_wrong_format(self):
		self.assertFalse(self.parser.accept('Autzoo.101'))

	def test_parse_gets_message_id(self):
		self.parser.parse_lines(self.lines)
		post = self.parser.get_post()
		self.assertEquals(post['message_id'], '<1991Jun21.055051.28165@milton.u.washington.edu>')

	def test_parse_gets_newsgroups(self):
		self.parser.parse_lines(self.lines)
		post = self.parser.get_post()
		self.assertEquals(post['newsgroups'], 'sci.virtual-worlds')

	def test_parse_gets_path(self):
		self.parser.parse_lines(self.lines)
		post = self.parser.get_post()
		self.assertEquals(post['path'], 'utzoo!utgpu!news-server.csri.toronto.edu')

	def test_parse_gets_subject(self):
		self.parser.parse_lines(self.lines)
		post = self.parser.get_post()
		self.assertEquals(post['subject'], 'Re: UUCP gateway')

	def test_parse_gets_timestamp(self):
		self.parser.parse_lines(self.lines)
		post = self.parser.get_post()
		self.assertEquals(post['timestamp'], '21 Jun 91 02:56:59 GMT')

	def test_parse_gets_subject(self):
		self.parser.parse_lines(self.lines)
		post = self.parser.get_post()
		self.assertEquals(post['subject'], 'Re: Japanese Symposium on Artificial Reality, 9-10 July 1991, Tokyo')

	def test_parse_gets_body(self):
		self.parser.parse_lines(self.lines)
		post = self.parser.get_post()
		self.assertEquals(post['body'], """This is a test for the body.

A second paragraph.
""")


if __name__ == '__main__':
	main()