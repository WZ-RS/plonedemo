from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE

import plonedemo


class PLONEDEMOLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=plonedemo)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "plonedemo:default")
        applyProfile(portal, "plonedemo:initial")


PLONEDEMO_FIXTURE = PLONEDEMOLayer()


PLONEDEMO_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONEDEMO_FIXTURE,),
    name="PLONEDEMOLayer:IntegrationTesting",
)


PLONEDEMO_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONEDEMO_FIXTURE, WSGI_SERVER_FIXTURE),
    name="PLONEDEMOLayer:FunctionalTesting",
)


PLONEDEMOACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONEDEMO_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name="PLONEDEMOLayer:AcceptanceTesting",
)
