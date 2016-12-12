# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.smartappbanner


class CollectiveSmartappbannerLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.smartappbanner)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.smartappbanner:default')


COLLECTIVE_SMARTAPPBANNER_FIXTURE = CollectiveSmartappbannerLayer()


COLLECTIVE_SMARTAPPBANNER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_SMARTAPPBANNER_FIXTURE,),
    name='CollectiveSmartappbannerLayer:IntegrationTesting'
)


COLLECTIVE_SMARTAPPBANNER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_SMARTAPPBANNER_FIXTURE,),
    name='CollectiveSmartappbannerLayer:FunctionalTesting'
)


COLLECTIVE_SMARTAPPBANNER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_SMARTAPPBANNER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveSmartappbannerLayer:AcceptanceTesting'
)
