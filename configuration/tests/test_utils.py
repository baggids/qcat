from django.db.models import Q

from configuration.utils import (
    get_configuration_query_filter,
)
from qcat.tests import TestCase


class GetConfigurationQureyFilterTest(TestCase):

    def test_returns_configuration_query(self):
        query_filter = get_configuration_query_filter('foo')
        self.assertIsInstance(query_filter, Q)
        attrs = query_filter.children
        self.assertEqual(len(attrs), 1)
        self.assertEqual(attrs[0][0], 'configurations__code')
        self.assertEqual(attrs[0][1], 'foo')

    def test_returns_combined_query_for_wocat(self):
        query_filter = get_configuration_query_filter('wocat')
        self.assertIsInstance(query_filter, Q)
        attrs = query_filter.children
        self.assertEqual(len(attrs), 2)
        self.assertEqual(attrs[0][0], 'configurations__code')
        self.assertEqual(attrs[0][1], 'wocat')
        self.assertEqual(attrs[1][0], 'configurations__code')
        self.assertEqual(attrs[1][1], 'unccd')
        self.assertEqual(query_filter.connector, 'OR')
