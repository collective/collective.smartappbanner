# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.smartappbanner.testing import COLLECTIVE_SMARTAPPBANNER_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.smartappbanner is properly installed."""

    layer = COLLECTIVE_SMARTAPPBANNER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.smartappbanner is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.smartappbanner'))

    def test_browserlayer(self):
        """Test that ICollectiveSmartappbannerLayer is registered."""
        from collective.smartappbanner.interfaces import (
            ICollectiveSmartappbannerLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveSmartappbannerLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_SMARTAPPBANNER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.smartappbanner'])

    def test_product_uninstalled(self):
        """Test if collective.smartappbanner is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.smartappbanner'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveSmartappbannerLayer is removed."""
        from collective.smartappbanner.interfaces import \
            ICollectiveSmartappbannerLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           ICollectiveSmartappbannerLayer,
           utils.registered_layers())
