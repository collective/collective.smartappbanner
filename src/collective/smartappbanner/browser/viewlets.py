# -*- encoding: utf-8 -*-
from collective.smartappbanner import _
from collective.smartappbanner.browser.interfaces import ISmartappbannerBaseSettings  # noqa
from plone import api
from plone.app.layout.viewlets import ViewletBase
from plone.registry.interfaces import IRegistry
from zope.component import ComponentLookupError
from zope.component import getUtility

import json


DAYS_HIDDEN = 15
DAYS_REMINDER = 90


class SmartappbannerViewlet(ViewletBase):

    script = u''
    meta_tags = None

    def update(self):
        # Reset the class defaults, to prevent accidentally leaking
        # data between calls.  Probably not needed, but I like to make sure.
        self.meta_tags = {}
        self.script = u''
        try:
            self.settings = getUtility(
                IRegistry).forInterface(ISmartappbannerBaseSettings)  # noqa
        except (ComponentLookupError, KeyError):
            return
        # Do we have an ID for at least one platform?
        platforms = {}
        android_id = self.settings.android_id
        if android_id:
            platforms[u'android'] = android_id
        ios_id = self.settings.ios_id
        if ios_id:
            platforms[u'ios'] = ios_id
        windows_id = self.settings.windows_id
        if windows_id:
            platforms[u'windows'] = windows_id
        if not platforms:
            return

        price_tag = self.settings.price or u''
        store = {}
        price = {}
        for platform, pid in platforms.items():
            # We currently have the same price per platform.
            # We expect the app to be free in most cases.
            price[platform] = price_tag
            if platform == u'ios':
                store[platform] = api.portal.translate(_(u'on the App Store'))
                self.meta_tags[u'apple-itunes-app'] = u'app-id={0}'.format(pid)
            elif platform == u'android':
                store[platform] = api.portal.translate(_(u'in Google Play'))
                self.meta_tags[u'google-play-app'] = u'app-id={0}'.format(pid)
            elif platform == u'windows':
                store[platform] = api.portal.translate(_(u'in Windows Store'))
                self.meta_tags[u'msApplication-ID'] = u'app-id={0}'.format(pid)

        # If we only have information for ios, then the meta tag is enough.
        # We do not need the script or any other options.
        if len(platforms) == 1 and 'ios' in platforms:
            return

        # Get the options for the javascript.
        options = self.generate_options()
        options['store'] = store
        options['price'] = price

        self.script = u'new SmartBanner({0});'.format(json.dumps(options))

    def generate_options(self):
        # We add all options, even those who are empty.
        # Make sure to not add None, as that may lead to javasript errors.
        language = api.portal.get_current_language()
        # For more information about options, see
        # https://github.com/kudago/smart-app-banner
        options = {
            # days to hide banner after close button is clicked:
            'daysHidden': DAYS_HIDDEN,
            # days to hide banner after "VIEW" button is clicked:
            'daysReminder': DAYS_REMINDER,
            # language code for the App Store:
            'appStoreLanguage': language,
            'title': self.settings.app_title or u'',
            'author': self.settings.author or u'',
            'button': self.settings.button_text or u'',
            # put platform type ('ios', 'android', etc.) here to force
            # a single theme on all devices:
            # theme: '',
        }

        # Get icon url
        icon = self.settings.icon or u''
        if icon and not icon.startswith(u'http'):
            nav_root = api.portal.get_navigation_root(self.context)
            if not icon.startswith(u'/'):
                icon = u'/' + icon
            icon = nav_root.absolute_url() + icon
        if icon:
            # full path to icon image if not using website icon image
            options['icon'] = icon

        # Maybe force showing as if we look from a certain platform.
        force = self.request.get('force_platform')
        if force:
            # Emulate a platform (ios/android/windows).
            options['force'] = force

        return options
