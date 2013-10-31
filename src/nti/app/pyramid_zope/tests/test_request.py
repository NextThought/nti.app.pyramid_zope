#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""


$Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

#disable: accessing protected members, too many methods
#pylint: disable=W0212,R0904


from hamcrest import assert_that
from hamcrest import is_
from hamcrest import has_key
from hamcrest import has_entry

from nti.testing import base
from nti.testing import matchers

from nti.testing.matchers import verifiably_provides
from nti.testing.matchers import validly_provides

from zope.publisher.interfaces.browser import IBrowserRequest
from pyramid.interfaces import IRequest
from pyramid.request import Request

setUpModule = lambda: base.module_setup( set_up_packages=(__name__,) )
tearDownModule = base.module_teardown

def test_adapts():

	request = Request.blank('/')

	zrequest = IBrowserRequest( request )
	assert_that( zrequest, verifiably_provides(IBrowserRequest) )
	# and it's still a valid pyramid request
	assert_that( zrequest, verifiably_provides(IRequest) )
