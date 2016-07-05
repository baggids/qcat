from unittest.mock import patch

from configuration.cache import get_configuration
from configuration.configuration import QuestionnaireConfiguration
from qcat.tests import TestCase
from questionnaire.serializers import QuestionnaireSerializer

from .test_models import get_valid_questionnaire


class SerializerTest(TestCase):

    fixtures = ['sample.json', 'sample_global_key_values.json']

    def setUp(self):
        self.questionnaire = get_valid_questionnaire()
        linked_questionnaire = get_valid_questionnaire()
        self.questionnaire.add_link(linked_questionnaire)
        self.questionnaire.save()
        self.serialized = QuestionnaireSerializer(self.questionnaire).data  # noqa
        self.expected = {
            'original_locale': 'en',
            'flags': [],
            'code': 'sample_0',
            'name': {'en': 'Unknown name'},
            'data': {'foo': 'bar'},
            'compilers': [{'name': 'bar foo', 'id': 1}],
            'list_data': {},
            'editors': [],
            'links': [
                {'en': {
                    'url': '/en/sample/view/sample_1/',
                    'code': 'sample_1',
                    'name': 'Unknown name',
                    'configuration': 'sample'}
                },
                {'es': {
                    'url': '/es/sample/view/sample_1/',
                    'code': 'sample_1',
                    'name': 'Unknown name',
                    'configuration': 'sample'}
                },
                {'fr': {
                    'url': '/fr/sample/view/sample_1/',
                    'code': 'sample_1',
                    'name': 'Unknown name',
                    'configuration': 'sample'}
                }],
            'url': '/en/sample/view/sample_0/',
            'serializer_config': 'sample',
            'translations': ['en'],
            'status': ['draft', 'Draft'],
            'configurations': ['sample']
        }

    def test_init_with_config(self):
        configuration = QuestionnaireConfiguration(self.questionnaire.code)
        serializer = QuestionnaireSerializer(
            instance=self.questionnaire, config=configuration
        )
        self.assertEqual(serializer.config, configuration)

    def test_init_without_config(self):
        config = self.questionnaire.questionnaireconfiguration_set.filter(
            original_configuration=True
        ).first()
        original_config = get_configuration(config.configuration.code)

        serializer = QuestionnaireSerializer(
            instance=self.questionnaire
        )

        self.assertEqual(serializer.config.keyword, original_config.keyword)

    def test_get_links_serialize(self):
        self.assertListEqual(self.serialized['links'], self.questionnaire.links_property)

    def test_get_links_to_native(self):
        deserialized = QuestionnaireSerializer(data=self.serialized)
        self.assertTrue(deserialized.is_valid())
        self.assertListEqual(
            deserialized.validated_data['links'], self.questionnaire.links_property
        )

    def test_url(self):
        native = QuestionnaireSerializer(data=self.serialized)
        self.assertTrue(native.is_valid())
        self.assertEqual(
            self.questionnaire.get_absolute_url(), native.validated_data['url']
        )

    def test_complete_serialization(self):
        data = self.serialized
        # datetimes are not relevant to the structure.
        del data['created']
        del data['updated']

        self.assertDictEqual(data, self.expected)

    def test_complete_to_native(self):
        native = QuestionnaireSerializer(data=self.serialized)
        native.is_valid()

        # datetimes are not relevant to the structure.
        del native.validated_data['created']
        del native.validated_data['updated']

        self.assertEqual(native.validated_data, self.expected)