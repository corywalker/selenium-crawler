# Global modules
import unittest
# Local modules
from seleniumcrawler.handle import handle_url

class TestHandlers(unittest.TestCase):

    def test_forbes(self):
        r = handle_url('http://www.forbes.com/sites/abrambrown/2013/04/22/netflixs-profit-picture-clears-q1s-big-beat-surprises-wall-street/')
        self.assertEqual(r['handler'], 'forbes')
        self.assertTrue('You need to go back to 2011, to shortly before the Qwikster')

    def test_hnews(self):
        r = handle_url('https://news.ycombinator.com/item?id=5612912')
        self.assertEqual(r['handler'], 'hnews')
        self.assertTrue('Wolfe, Cockrell and the rest of the team got a couple of Nexus')

    def test_reddit(self):
        r = handle_url('http://www.reddit.com/r/technology/comments/1d5ptg/the_force_of_fiber_google_fiber_is_pressuring/')
        self.assertEqual(r['handler'], 'reddit')
        self.assertTrue('that there is no public data that paints a complete picture')

    def test_hackaday(self):
        r = handle_url('http://hackaday.com/2013/04/26/old-led-marquee-turned-embedded-video-player/')
        self.assertEqual(r['handler'], 'hackaday')
        self.assertTrue('A better look at the industrial PC.')

if __name__ == '__main__':
    unittest.main()
