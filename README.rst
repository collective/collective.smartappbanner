.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

=========================
collective.smartappbanner
=========================

Customisable smart app banners on Plone for iOS and Android.

.. image:: https://img.shields.io/travis/collective/collective.smartappbanner/master.svg
    :target: http://travis-ci.org/collective/collective.smartappbanner


Features
--------

- Uses `smart-app-banner.js <https://github.com/kudago/smart-app-banner>`_ from Diva Yv / Kudago.  (Thanks!)

- Adds meta tags, which are handled by the javascript to show a banner for your app when viewed on a mobile device.


..  Examples
    --------

    This add-on can be seen in action at the following sites:
    - Is there a page on the internet where everybody can see the features?


Translations
------------

This product has been translated into

- Dutch (Maurits van Rees)


Installation
------------

Install collective.smartappbanner by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.smartappbanner


and then running ``bin/buildout``

After you start your Plone Site, you can install it in the add-ons control panel.
This adds a control panel where you can configure the app name, urls, supported platforms, etcetera.

We only create meta tags if at least one of the App Store or Google Play urls is filled in.

.. TODO This is still on bitbucket.

    Contribute
    ----------

    - Issue Tracker: https://github.com/collective/collective.smartappbanner/issues
    - Source Code: https://github.com/collective/collective.smartappbanner


Support
-------

If you are having issues, please let us know by using the issue tracker.



License
-------

The project is licensed under the GPLv2.
