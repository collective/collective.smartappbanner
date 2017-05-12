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
            IRegistry).forInterface(ISmartappbannerBaseSettings)
        settings.app_title = u'Gardening for knights'
        settings.author = u'The knights who say Ni'
        settings.icon = u'shrubbery.png'
        self.assertNotIn('smartbanner', self.portal())
        settings.ios_url = u'some-ios-url'
        home = self.portal()
        self.assertIn('smartbanner', home)
        self.assertIn('<meta content="Gardening for knights" name="smartbanner:title">', home)  # noqa
        self.assertIn('<meta content="http://nohost/plone/shrubbery.png" name="smartbanner:icon-apple">', home)  # noqa
        self.assertIn('<meta content=" On the App Store" name="smartbanner:price-suffix-apple">', home)  # noqa
        self.assertIn('<meta content="ios" name="smartbanner:enabled-platforms">', home)  # noqa
        settings.android_url = u'some-android-url'
        home = self.portal()
        self.assertIn('<meta content="android,ios" name="smartbanner:enabled-platforms">', home)  # noqa
