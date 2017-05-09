=======
CHANGES
=======

4.0.0 (2017-05-09)
------------------

- Add support for Python 3.4, 3.5, 3.6 and PyPy.

- Fix the ``evolve`` view to use independent transactions instead of
  committing or aborting the thread-local current transaction.

- Drop dependency on ``zope.app.renderer``.

- Drop test dependency on ``zope.app.testing``, ``zope.app.zcmlfiles``
  and others.


3.7.1 (2012-01-23)
------------------

- Replaced an undeclared test dependency on ``zope.app.authentication`` with
  ``zope.password``.


3.7.0 (2010-09-18)
------------------

- Depends now on the extracted ``zope.generations``.


3.6.0 (2010-09-17)
------------------

- ``zope.app.generations`` depended on ``zope.app.applicationcontrol`` but
  did not declare it. Modernized dependecy to ``zope.applicationcontrol`` as
  the needed interface has been moved there.

- Using python's ``doctest`` module instead of deprecated
  ``zope.testing.doctest[unit]``.

- Replaced a testing dependency on ``zope.app.securitypolicy`` with one on
  ``zope.securitypolicy``.


3.5.1 (2010-01-08)
------------------

- Depend on new ``zope.processlifetime`` interfaces instead of using
  BBB imports from ``zope.app.appsetup``.

- Fix ftesting.zcml due to ``zope.securitypolicy`` update.

- Fix tests using a newer zope.publisher that requires zope.login.

3.5.0 (2009-04-05)
------------------

- Moved ``getRootFolder`` utility method from
  ``zope.app.zopeappgenerations`` to ``zope.app.generations.utility``.

- Removed not necessary install dependency on ``zope.app.testing``.


3.4.2 (2009-01-27)
------------------

- Provide more logging output for the various stages and actions of evolving a
  database.

- Fixed bug: A failing last generation would allow starting an app server
  without having evolved to the minimum generation.

- Substitute zope.app.zapi by direct calls to its wrapped apis. See
  bug 219302.

- Corrected author email and home page address.


3.4.1 (2007-10-31)
------------------

- Resolve ``ZopeSecurityPolicy`` deprecation warning.


3.4.0 (2007-10-24)
------------------

- Initial release independent of the main Zope tree.
