from uua.parser import FirstFileFormatParser
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


class FirstFileFormatParserTest(TestCase):
	def setUp(self):
		self.parser = FirstFileFormatParser()

	def test_accept(self):
		self.assertTrue(FirstFileFormatParser.accept('Autzoo.101'))

	def test_accept_rejects_wrong_format(self):
		self.assertFalse(self.parser.accept('Path: utzoo!telly!attcan!utgpu!news-server.csri.toronto.edu!' + 
			'bonnie.concordia.ca!uunet!looking!xenitec!sco!timr'))

	def test_parse(self):

		for line in raw_post_using_first_file_format.split('\n'):
			self.parser.parse(line)

		post = self.parser.get_post()
		self.assertEquals(post.message_id, 'Acbosg.129')
		self.assertEquals(post.newsgroup, 'Acbosg.129')
		self.assertEquals(post.path, 'Acbosg.129')
		self.assertEquals(post.timestamp, 'Acbosg.129')
		self.assertEquals(post.subject, 'Acbosg.129')
		self.assertEquals(post.content, 'Acbosg.129')


if __name__ == '__main__':
	main()