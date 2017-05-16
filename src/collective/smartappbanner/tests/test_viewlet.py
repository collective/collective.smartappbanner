# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.smartappbanner.testing import COLLECTIVE_SMARTAPPBANNER_INTEGRATION_TESTING  # noqa

import unittest


class TestViewlet(unittest.TestCase):
    """Test the viewlet."""

    layer = COLLECTIVE_SMARTAPPBANNER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']

    def test_viewlet_no_show(self):
        # By default the viewlet does not show anything.
        self.assertNotIn('smartbanner', self.portal())

    def test_viewlet_show(self):
        from collective.smartappbanner.browser.interfaces import ISmartappbannerBaseSettings  # noqa
        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility
        settings = getUtility(
            IRegistry).forInterface(ISmartappbannerBaseSettings)  # noqa for plone.api alternative
        settings.app_title = u'Gardening for knights'
        settings.author = u'The knights who say Ni'
        settings.icon = u'shrubbery.png'
        self.assertNotIn('smartbanner', self.portal())

        # Add ios settings.
        settings.ios_id = u'1234567890'
        home = self.portal()
        # We expect
        # <meta content="app-id=1234567890" name="apple-itunes-app">
        # but the order of the meta tag properties may be the
        # other way around.
        self.assertIn('content="app-id=1234567890"', home)
        self.assertIn('name="apple-itunes-app"', home)
        # apple does not need the javascript code
        self.assertNotIn('new SmartBanner', home)
        self.assertNotIn('name="google-play-app"', home)
        self.assertNotIn('name="msApplication-ID"', home)

        # Add android settings
        settings.android_id = u'org-example-app'
        home = self.portal()
        self.assertIn('new SmartBanner', home)
        self.assertIn('name="apple-itunes-app"', home)
        self.assertIn('name="google-play-app"', home)
        self.assertNotIn('name="msApplication-ID"', home)
        self.assertIn('content="app-id=1234567890"', home)
        self.assertIn('content="app-id=org-example-app"', home)

        # Add windows settings
        settings.windows_id = u'org-windows-example-app'
        home = self.portal()
        self.assertIn('new SmartBanner', home)
        self.assertIn('name="apple-itunes-app"', home)
        self.assertIn('name="google-play-app"', home)
        self.assertIn('name="msApplication-ID"', home)
        self.assertIn('content="app-id=1234567890"', home)
        self.assertIn('content="app-id=org-example-app"', home)
        self.assertIn('content="app-id=org-windows-example-app"', home)
