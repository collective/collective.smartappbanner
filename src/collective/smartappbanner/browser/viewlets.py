# -*- encoding: utf-8 -*-
from collective.smartappbanner.browser.interfaces import ISmartappbannerBaseSettings  # noqa
from plone.app.layout.viewlets import ViewletBase
from plone.registry.interfaces import IRegistry
from zope.component import ComponentLookupError
from zope.component import getUtility


class smartappbannerViewlet(ViewletBase):

    def meta_tags(self):
        try:
            self.settings = getUtility(
                IRegistry).forInterface(ISmartappbannerBaseSettings)  # noqa
        except (ComponentLookupError, KeyError):
            return
        tags = {}

        tags['smartbanner:title'] = self.settings.smartbannerTitle
        tags['smartbanner:author'] = self.settings.smartbannerAuthor
        tags['smartbanner:price'] = self.settings.smartbannerPrice
        tags['smartbanner:price-suffix-apple'] = 'On the App Store'
        tags['smartbanner:price-suffix-google'] = 'In Google Play'
        tags['smartbanner:icon-apple'] = self.settings.smartbannerIcon
        tags['smartbanner:icon-google'] = self.settings.smartbannerIcon
        tags['smartbanner:button'] = 'VIEW'
        tags['smartbanner:button-url-apple'] = self.settings.smartbannerIOSurl
        tags['smartbanner:button-url-google'] = \
            self.settings.smartbannerAndroidUrl
        tags['smartbanner:enabled-platforms'] = \
            self.settings.smartbannerPlatforms

        return tags
