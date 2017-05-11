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

        tags['smartbanner:title'] = self.settings.title
        tags['smartbanner:author'] = self.settings.author
        tags['smartbanner:price'] = self.settings.price
        tags['smartbanner:price-suffix-apple'] = 'On the App Store'
        tags['smartbanner:price-suffix-google'] = 'In Google Play'
        tags['smartbanner:icon-apple'] = self.settings.icon
        tags['smartbanner:icon-google'] = self.settings.icon
        tags['smartbanner:button'] = 'VIEW'
        tags['smartbanner:button-url-apple'] = self.settings.ios_url
        tags['smartbanner:button-url-google'] = self.settings.android_url
        tags['smartbanner:enabled-platforms'] = self.settings.platforms

        return tags
