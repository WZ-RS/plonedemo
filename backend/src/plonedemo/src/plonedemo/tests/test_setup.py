"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plonedemo.testing import PLONEDEMO_INTEGRATION_TESTING  # noqa: E501
from Products.CMFPlone.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonedemo is properly installed."""

    layer = PLONEDEMO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.setup = self.portal.portal_setup
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if plonedemo is installed."""
        self.assertTrue(self.installer.is_product_installed("plonedemo"))

    def test_browserlayer(self):
        """Test that IPLONEDEMOLayer is registered."""
        from plone.browserlayer import utils
        from plonedemo.interfaces import IPLONEDEMOLayer

        self.assertIn(IPLONEDEMOLayer, utils.registered_layers())

    def test_latest_version(self):
        """Test latest version of default profile."""
        self.assertEqual(
            self.setup.getLastVersionForProfile("plonedemo:default")[0],
            "20221021001",
        )


class TestUninstall(unittest.TestCase):

    layer = PLONEDEMO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("plonedemo")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if plonedemo is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("plonedemo"))

    def test_browserlayer_removed(self):
        """Test that IPLONEDEMOLayer is removed."""
        from plone.browserlayer import utils
        from plonedemo.interfaces import IPLONEDEMOLayer

        self.assertNotIn(IPLONEDEMOLayer, utils.registered_layers())
