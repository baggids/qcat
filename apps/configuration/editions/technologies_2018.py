import copy

from django.utils.translation import ugettext_lazy as _

from .base import Edition, Operation


class Technologies(Edition):
    """
    Questionnaire updates for carbon benefit.
    """
    code = 'technologies'
    edition = 2018

    all_configuration_editions = [
        'technologies_2018', 'technologies', 'approaches', 'cca', 'watershed']

    @property
    def operations(self):
        return [
            Operation(
                transform_configuration=self.add_option_user_resourceperson_type,
                release_note=_('1.2: Added option "co-compiler" to "Key resource persons".')
            ),
            Operation(
                transform_configuration=self.remove_person_address_questions,
                transform_questionnaire=self.delete_person_address_data,
                release_note=_('1.2: Removed "Address", "Phone" and "E-Mail" of "Key resource persons".')
            ),
            Operation(
                transform_configuration=self.remove_subcategory_1_6,
                release_note=''
            ),
            Operation(
                transform_configuration=self.do_nothing,
                # This happened in self.merge_subcategory_3_5_into_2_5 ...
                release_note=_('2.5: Integrated questions about "Spread of the Technology" (previously in 3.5).')
            ),
            Operation(
                transform_configuration=self.do_nothing,
                # This happened in self.merge_subcategory_3_5_into_2_5 ...
                release_note=_('2.5: Added new question "If precise area is known, please specify".')
            ),
            Operation(
                transform_configuration=self.add_tech_location_protected,
                release_note=_('2.5: Added new question "Is/are the technology site(s) located in a permanently protected area?"')
            ),
            Operation(
                transform_configuration=self.add_tech_lu_mixed,
                transform_questionnaire=self.remove_tech_lu_mixed,
                release_note=_('3.2: Added separate question about "Mixed land use".')
            ),
            Operation(
                transform_configuration=self.add_questions_tech_lu_cropland,
                release_note=_('3.2: Added additional questions about crops, intercropping and crop rotation to land use type "Cropland".'),
            ),
            Operation(
                transform_configuration=self.remove_tech_lu_cropland_specify,
                transform_questionnaire=self.delete_tech_lu_cropland_specify_data,
                release_note=_('3.2: Removed text question "Main crops" of land use type "Cropland".')
            ),
            Operation(
                transform_configuration=self.add_questions_tech_lu_grazingland,
                release_note=_('3.2: Added additional questions about grazing land (animal type, crop-livestock management practices, products and services).')
            ),
            Operation(
                transform_configuration=self.remove_tech_lu_grazingland_specify,
                transform_questionnaire=self.delete_tech_lu_grazingland_specify,
                release_note=_('3.2: Removed text question "Main animal species and products" of land use type "Grazing land".')
            ),
            Operation(
                transform_configuration=self.add_tech_livestock_population,
                release_note=_('3.2: Added additional question "Livestock population" for land use type "Grazing land"')
            ),
            Operation(
                transform_configuration=self.rename_tech_lu_grazingland_pastoralism,
                release_note=_('3.2: Renamed option "semi-nomadism" of land use type "Grazing land" to "semi-nomadic pastoralism".')
            ),
            Operation(
                transform_configuration=self.add_option_tech_lu_grazingland_transhumant,
                release_note=_('3.2: Added option "transhumant pastoralism" to land use type "Grazing land".')
            ),
            Operation(
                transform_configuration=self.add_questions_tech_lu_woodlands,
                release_note=_('3.2: Added optional questions about forest type and trees for land use type "Forest/ woodlands".')
            ),
            Operation(
                transform_configuration=self.remove_tech_lu_change,
                transform_questionnaire=self.delete_tech_lu_change,
                release_note=_('3.2: Removed text question "If land use has changed due to the implementation of the Technology, indicate land use before implementation of the Technology". This information can now be entered in 3.3.')
            ),
            Operation(
                transform_configuration=self.add_subcategory_initial_landuse,
                release_note=_('3.3 (new): Added new subcategory about initial land use')
            ),
            Operation(
                transform_configuration=self.move_tech_growing_seasons,
                transform_questionnaire=self.delete_tech_growing_seasons,
                release_note=_('3.4 (previously 3.3): Moved question "Number of growing seasons per year" to 3.2 - land use type "Cropland". Data was only migrated automatically, if land use type "Cropland" was selected.')
            ),
            Operation(
                transform_configuration=self.remove_tech_livestock_density,
                transform_questionnaire=self.delete_tech_livestock_density,
                release_note=_('3.4 (previously 3.3): Removed question "Livestock density (if relevant). Use "Comments" of "3.2 Current land use type(s)".')
            ),
            Operation(
                transform_configuration=self.merge_subcategory_3_5_into_2_5,
                transform_questionnaire=self.delete_tech_spread_tech_comments,
                release_note=_('3.5: Previous questions of "3.5 Spread of the Technology" were integrated into "2.5 Country/ region/ locations where the Technology has been applied and which are covered by this assessment".')
            ),
            Operation(
                transform_configuration=self.do_nothing,
                # This happened in self.merge_subcategory_3_5_into_2_5 ...
                release_note=_('3.5: Question "Comments" about "Spread of the Technology" (previously 3.5) was removed, its content needs to be merged with "Comments" of 2.5.')
            ),
            Operation(
                transform_configuration=self.add_question_tech_agronomic_tillage,
                release_note=_('3.6: Added new question "Differentiate tillage systems" when selecting agronomic measure "A3: Soil surface treatment".')
            ),
            Operation(
                transform_configuration=self.add_option_a6_residue_management,
                release_note=_('3.6: Added new option "A6: Residue Management" to "agronomic measures".')
            ),
            Operation(
                transform_configuration=self.rename_option_a6_others,
                release_note=_('3.6 Renamed option "A6: Others" of "agronomic measures" to "A7: Others".')
            ),
            Operation(
                transform_configuration=self.add_question_tech_residue_management,
                release_note=_('3.6: Added new question "Specify residue management" when selecting agronomic measure "A6: residue management".')
            ),
            Operation(
                transform_configuration=self.do_nothing,
                release_note=_('4: Updated numbering (4.2 was removed).')
            ),
            Operation(
                transform_configuration=self.move_technical_specification,
                transform_questionnaire=self.delete_technical_specification,
                release_note=_('4.1: Previous question "4.2 Technical specifications" is now integrated into "4.1 Technical drawing".')
            ),
            Operation(
                transform_configuration=self.remove_tech_est_type,
                transform_questionnaire=self.delete_tech_est_type,
                release_note=_('4.3 (previously 4.4): Removed "Type of measure" from Establishment activities.')
            ),
            Operation(
                transform_configuration=self.add_question_tech_input_est_total_costs_usd,
                release_note=_('4.4 (previously 4.5): Added question "Total costs for establishment of the Technology in USD" (automatically calculated).')
            ),
            Operation(
                transform_configuration=self.remove_tech_maint_type,
                transform_questionnaire=self.delete_tech_maint_type,
                release_note=_('4.5 (previously 4.6): Removed "Type of measure" from Maintenance activities.')
            ),
            Operation(
                transform_configuration=self.add_question_tech_input_maint_total_costs_usd,
                release_note=_('4.6 (previously 4.7): Added question "Total costs for maintenance of the Technology in USD" (automatically calculated).')
            ),
            Operation(
                transform_configuration=self.move_tech_input_est_total_estimation,
                release_note='',
            ),
            Operation(
                transform_configuration=self.rename_tech_input_est_total_estimation,
                release_note='',
            ),
            Operation(
                transform_configuration=self.move_tech_input_maint_total_estimation,
                release_note='',
            ),
            Operation(
                transform_configuration=self.rename_tech_input_maint_total_estimation,
                release_note='',
            ),
            Operation(
                transform_configuration=self.rename_tech_individuals,
                release_note='',
            ),
            Operation(
                transform_configuration=self.rename_us_dollars,
                release_note=''
            ),
            Operation(
                transform_configuration=self.add_question_tech_traditional_rights,
                release_note='5.8: Added new question about traditional land use rights'
            ),
        ]

    def add_question_tech_input_maint_total_costs_usd(self, **data) -> dict:

        # Create a new question
        k_keyword = 'tech_input_maint_total_costs_usd'
        self.create_new_question(
            keyword=k_keyword,
            translation={
                'label': {
                    'en': 'Total costs for maintenance of the Technology in USD'
                }
            },
            question_type='float',
            configuration={
                'form_options': {
                    'label': 'placeholder',
                    'field_options': {
                        'min': 0,
                        'decimals': 2,
                        'readonly': 'readonly',
                        'data-local-currency-calculation': 'tech_qg_164|tech_input_exchange_rate|tech_qg_223|tech_input_maint_total_costs'
                    }
                }
            }
        )

        # Create new questiongroup and add the question to it.
        qg_keyword = 'tech_qg_233'
        self.create_new_questiongroup(
            keyword=qg_keyword, translation=None)
        qg_configuration = {
            'keyword': qg_keyword,
            'questions': [
                {
                    'keyword': k_keyword
                }
            ]
        }

        subcat_path = ('section_specifications', 'tech__4', 'tech__4__7')
        subcat_data = self.find_in_data(path=subcat_path, **data)

        # Update table grouping options
        subcat_data['view_options']['table_grouping'][1] += [qg_keyword]

        # Add the questiongroup
        questiongroups = subcat_data['questiongroups']

        questiongroups.insert(8, qg_configuration)
        subcat_data['questiongroups'] = questiongroups

        data = self.update_config_data(
            path=subcat_path, updated=subcat_data, **data)

        return data

    def add_question_tech_input_est_total_costs_usd(self, **data) -> dict:

        # Create a new question
        k_keyword = 'tech_input_est_total_costs_usd'
        self.create_new_question(
            keyword=k_keyword,
            translation={
                'label': {
                    'en': 'Total costs for establishment of the Technology in USD'
                }
            },
            question_type='float',
            configuration={
                'form_options': {
                    'label': 'placeholder',
                    'field_options': {
                        'min': 0,
                        'decimals': 2,
                        'readonly': 'readonly',
                        'data-local-currency-calculation': 'tech_qg_164|tech_input_exchange_rate|tech_qg_222|tech_input_est_total_costs'
                    }
                }
            }
        )

        # Create new questiongroup and add the question to it.
        qg_keyword = 'tech_qg_232'
        self.create_new_questiongroup(
            keyword=qg_keyword, translation=None)
        qg_configuration = {
            'keyword': qg_keyword,
            'questions': [
                {
                    'keyword': k_keyword
                }
            ]
        }

        subcat_path = ('section_specifications', 'tech__4', 'tech__4__5')
        subcat_data = self.find_in_data(path=subcat_path, **data)

        # Update table grouping options
        subcat_data['view_options']['table_grouping'][1] += [qg_keyword]

        # Add the questiongroup
        questiongroups = subcat_data['questiongroups']
        questiongroups.insert(8, qg_configuration)
        subcat_data['questiongroups'] = questiongroups

        data = self.update_config_data(
            path=subcat_path, updated=subcat_data, **data)

        return data

    def delete_tech_spread_tech_comments(self, **data) -> dict:
        return self.update_data('tech_qg_4', 'tech_spread_tech_comments', None, **data)

    def merge_subcategory_3_5_into_2_5(self, **data) -> dict:

        old_subcat_path = ('section_specifications', 'tech__3', 'tech__3__5')
        old_subcat_data = self.find_in_data(path=old_subcat_path, **data)

        questiongroup = old_subcat_data['questiongroups'][0]  # There is only 1

        # Remove the entire old subcategory
        old_cat_path = ('section_specifications', 'tech__3')
        old_cat_data = self.find_in_data(path=old_cat_path, **data)
        old_cat_data['subcategories'] = [
            s for s in old_cat_data['subcategories']
            if s['keyword'] != 'tech__3__5'
        ]
        data = self.update_config_data(
            path=old_cat_path, updated=old_cat_data, **data)

        # Delete comments question of questiongroup
        questiongroup['questions'] = [
            q for q in questiongroup['questions'] if
            q['keyword'] != 'tech_spread_tech_comments']

        # Update translation of previous question about categorized area
        self.update_translation(
            update_pk=1311,
            **{
                "label": {
                    "en": "If precise area is not known, indicate approximate area covered"
                }
            }
        )

        # Add new question
        q_keyword = 'tech_spread_area_precise'
        self.create_new_question(
            keyword=q_keyword,
            translation={
                'label': {
                    'en': 'If the Technology is evenly spread over an area, specify area covered (in km2)'
                }
            },
            question_type='float',
            configuration={
                'summary': {
                    'types': ['full'],
                    'default': {
                        'field_name': 'location_spread_area_precise'
                    }
                }
            }
        )
        question_configuration = {
            'keyword': q_keyword,
            'form_options': {
                'field_options': {
                    'min': 0
                },
                'question_condition': 'tech_spread_area',
            }
        }

        new_questions = questiongroup['questions']
        new_questions.insert(1, question_configuration)
        questiongroup['questions'] = new_questions

        new_subcat_path = ('section_specifications', 'tech__2', 'tech__2__5')
        new_subcat_data = self.find_in_data(path=new_subcat_path, **data)

        # Add to questiongroups of new subcategory
        new_questiongroups = new_subcat_data['questiongroups']
        new_questiongroups.insert(3, questiongroup)
        new_subcat_data['questiongroups'] = new_questiongroups

        data = self.update_config_data(
            path=new_subcat_path, updated=new_subcat_data, **data)

        return data

    def add_question_tech_traditional_rights(self, **data) -> dict:

        q_keyword = 'tech_traditional_rights'
        self.create_new_question(
            keyword=q_keyword,
            translation={
                'label': {
                    'en': 'Are land use rights based on a traditional legal system?'
                }
            },
            question_type='bool'
        )
        question_configuration = {
            'keyword': q_keyword,
            'form_options': {
                'question_conditions': [
                    '=="1"|tech_traditional_rights_specify'
                ]
            }
        }

        q_keyword_specify = 'tech_traditional_rights_specify'
        self.create_new_question(
            keyword=q_keyword_specify,
            translation={
                'label': {
                    'en': 'Specify'
                }
            },
            question_type='text'
        )
        question_specify_configuration = {
            'keyword': q_keyword_specify,
            'form_options': {
                'question_condition': 'tech_traditional_rights_specify'
            }
        }

        qg_path = ('section_specifications', 'tech__5', 'tech__5__8', 'tech_qg_73')
        qg_data = self.find_in_data(path=qg_path, **data)
        qg_data['questions'] += [question_configuration, question_specify_configuration]

        return self.update_config_data(path=qg_path, updated=qg_data, **data)

    def move_technical_specification(self, **data) -> dict:

        # Add tech_specifications to 4.1
        qg_path = (
            'section_specifications', 'tech__4', 'tech__4__1', 'tech_qg_185')
        qg_data = self.find_in_data(path=qg_path, **data)
        qg_data['questions'].insert(1, {'keyword': 'tech_specifications'})
        # Adjust template
        qg_data['form_options'].update({
            'template': 'columns_custom',
            'columns_custom': [['12'], ['12'], ['6', '6']]
        })
        data = self.update_config_data(path=qg_path, updated=qg_data, **data)

        # Update translation of tech_specifications (insert helptext previously
        # in subcategory)
        self.update_translation(
            update_pk=1036,
            **{
                "label": {
                    "en": "Technical specifications (related to technical drawing)"
                },
                "helptext": {
                    "en": "<p>Summarize technical specifications, e.g.:</p><ul><li>Dimensions (height, depth, width, length) of structures or vegetative elements;</li><li>Spacing between structures or plants/ vegetative measures</li><li>Vertical intervals structures or vegetative measures</li><li>Slope angle (before and after implementation of the Technology)</li><li>Lateral gradient of structures</li><li>Capacity of dams, ponds, etc.</li><li>Catchment area and beneficial area of dams, ponds, other water harvesting systems</li><li>Construction material used</li><li>Species used</li><li>Quantity/ density of plants (per ha)</li></ul>"
                }
            }
        )

        # Remove 4.2
        cat_path = (
            'section_specifications', 'tech__4')
        cat_data = self.find_in_data(path=cat_path, **data)
        new_subcats = []
        for subcat in cat_data['subcategories']:
            # Exclude 4.2
            if subcat['keyword'] == 'tech__4__2':
                continue

            # Update numbering
            if subcat['keyword'] != 'tech__4__1':
                old_numbering = subcat['form_options']['numbering']
                new_numbering = str(round(float(old_numbering) - 0.1, 1))
                subcat['form_options']['numbering'] = new_numbering

            new_subcats.append(subcat)
        cat_data['subcategories'] = new_subcats
        data = self.update_config_data(path=cat_path, updated=cat_data, **data)

        # Update helptexts of new subcategories 4.4 and 4.6 (pointing to
        # previous subcategories where numbering has changed)
        self.update_translation(
            update_pk=2792,
            **{
                "label": {
                    "en": "Costs and inputs needed for establishment"
                },
                "helptext": {
                    "en": "<p><strong>Note</strong>: Costs and inputs specified in this question should refer to the technology area/ technology unit defined in 4.2 and to the activities listed in 4.3. Use the currency indicated in 4.2.</p>"
                }
            }
        )
        self.update_translation(
            update_pk=2793,
            **{
                "label": {
                    "en": "Costs and inputs needed for maintenance/ recurrent activities (per year)"
                },
                "helptext": {
                    "en": "<strong>Note</strong>: Costs and inputs specified in this question should refer to the technology area/ technology unit defined in 4.2, and to the activities listed in 4.5. Use the currency indicated in 4.2."
                }
            }
        )

        return data

    def delete_technical_specification(self, **data) -> dict:
        if 'tech_qg_161' in data:
            del data['tech_qg_161']
        return data

    def add_tech_location_protected(self, **data) -> dict:
        qg_keyword = 'tech_qg_234'
        self.create_new_questiongroup(
            keyword=qg_keyword,
            translation=None
        )
        question_keyword = 'tech_location_protected'
        self.create_new_question(
            keyword=question_keyword,
            translation={
                'label': {
                    'en': 'Is/are the technology site(s) located in a permanently protected area?'
                },
                'helptext': {
                    'en': 'I.e. national reserve/ national park'
                }
            },
            question_type='bool',
            configuration={
                'summary': {
                    'types': ['full'],
                    'default': {
                        'field_name': 'location_protected_area'
                    }
                }
            }
        )
        specify_keyword = 'tech_location_protected_specify'
        self.create_new_question(
            keyword=specify_keyword,
            translation={
                'label': {
                    'en': 'If yes, specify'
                }
            },
            question_type='text',
            configuration={
                'summary': {
                    'types': ['full'],
                    'default': {
                        'field_name': 'location_protected_area_specify'
                    }
                }
            }
        )
        qg_configuration = {
            'keyword': qg_keyword,
            'questions': [
                {
                    'keyword': question_keyword,
                    'form_options': {
                        'question_conditions': [
                            f"=='1'|{specify_keyword}"
                        ],
                        'helptext_position': 'tooltip'
                    }
                },
                {
                    'keyword': specify_keyword,
                    'form_options': {
                        'question_condition': specify_keyword
                    }
                }
            ]
        }
        subcat_path = ('section_specifications', 'tech__2', 'tech__2__5')
        subcat_data = self.find_in_data(path=subcat_path, **data)
        questiongroups = subcat_data['questiongroups']
        questiongroups.insert(3, qg_configuration)
        subcat_data['questiongroups'] = questiongroups
        return self.update_config_data(path=subcat_path, updated=subcat_data, **data)

    def remove_tech_lu_mixed(self, **data) -> dict:

        # Migrate values of tech_landuse to tech_landuse_2018 (tech_qg_9)
        new_landuse_qg = []
        for landuse_qg in data.get('tech_qg_9', []):
            new_lu_values = [
                v for v in landuse_qg.get('tech_landuse', [])
                if v != 'tech_lu_mixed']
            landuse_qg['tech_landuse_2018'] = new_lu_values
            del landuse_qg['tech_landuse']
            new_landuse_qg.append(landuse_qg)
        data['tech_qg_9'] = new_landuse_qg

        # Remove entire questiongroup tech_qg_13
        if 'tech_qg_13' in data:
            del data['tech_qg_13']

        return data

    def add_tech_lu_mixed(self, **data) -> dict:

        subcat_path = ('section_specifications', 'tech__3', 'tech__3__2')
        subcat_data = self.find_in_data(path=subcat_path, **data)

        # Remove tech_lu_mixed from questiongroup_conditions
        subcat_data['form_options']['questiongroup_conditions'] = [
            c for c in subcat_data['form_options']['questiongroup_conditions']
            if c != "=='tech_lu_mixed'|tech_qg_13"
        ]

        # Remove questiongroup tech_qg_13 (lu_mixed)
        subcat_data['questiongroups'] = [
            qg for qg in subcat_data['questiongroups']
            if qg['keyword'] != 'tech_qg_13'
        ]
        data = self.update_config_data(
            path=subcat_path, updated=subcat_data, **data)

        # Remove tech_lu_mixed from questiongroup_conditions (of tech_qg_9)
        old_cond_qg_path = (
            'section_specifications', 'tech__3', 'tech__3__2', 'tech_qg_9')
        old_cond_qg_data = self.find_in_data(path=old_cond_qg_path, **data)
        old_cond_qg_data['questions'][0]['form_options']['questiongroup_conditions'] = [
            c for c in old_cond_qg_data['questions'][0]['form_options']['questiongroup_conditions']
            if c != "=='tech_lu_mixed'|tech_qg_13"
        ]

        # Instead of removing value "tech_lu_mixed" of question "tech_landuse",
        # create a new question "tech_landuse_2018". Just deleting the value
        # from the existing question would mean that technologies in the
        # previous edition would also automatically have this value removed,
        # which is not correct behaviour.
        old_question = self.get_question(keyword='tech_landuse')
        old_configuration = old_question.configuration
        old_configuration['form_options']['field_options']['data-cb-max-choices'] = 3
        new_keyword = 'tech_landuse_2018'
        self.create_new_question(
            keyword=new_keyword,
            translation={
                "label": {
                    "en": "Select land use type"
                },
                "label_view": {
                    "en": "Land use type"
                }
            },
            question_type='image_checkbox',
            values=[
                self.get_value(keyword='tech_lu_cropland'),
                self.get_value(keyword='tech_lu_grazingland'),
                self.get_value(keyword='tech_lu_forest'),
                self.get_value(keyword='tech_lu_settlements'),
                self.get_value(keyword='tech_lu_waterways'),
                self.get_value(keyword='tech_lu_mines'),
                self.get_value(keyword='tech_lu_unproductive'),
                self.get_value(keyword='tech_lu_other'),
            ],
            configuration=old_configuration,
        )
        old_cond_qg_data['questions'][0]['keyword'] = new_keyword
        data = self.update_config_data(
            path=old_cond_qg_path, updated=old_cond_qg_data, **data)

        # Add new question about mixed land use at the beginning of the
        # subcategory

        # Update the translations of the values
        self.update_translation(
            update_pk=1512,
            **{
                'label': {
                    'en': 'Agroforestry'
                },
                'helptext': {
                    'en': '<strong>Mf: Agroforestry</strong>: cropland and trees.<br>Select "Cropland" and "Forest/ woodlands" below and fill out the relevant sections.'
                }
            }
        )
        self.update_translation(
            update_pk=1513,
            **{
                'label': {
                    'en': 'Agro-pastoralism (incl. integrated crop-livestock)'
                },
                'helptext': {
                    'en': '<strong>Mp: Agro-pastoralism</strong>: cropland and grazing land (including seasonal change between crops and livestock).<br>Select "Cropland" and "Grazing land" below and fill out the relevant sections.'
                }
            }
        )
        self.update_translation(
            update_pk=1514,
            **{
                'label': {
                    'en': 'Agro-silvopastoralism'
                },
                'helptext': {
                    'en': '<strong>Ma: Agro-silvopastoralism</strong>: cropland, grazing land and trees (including seasonal change between crops and livestock).<br>Select "Cropland", "Grazing land" and "Forest/ woodlands" below and fill out the relevant sections.'
                }
            }
        )
        self.update_translation(
            update_pk=1515,
            **{
                'label': {
                    'en': 'Silvo-pastoralism'
                },
                'helptext': {
                    'en': '<strong>Ms: Silvo-pastoralism</strong>: forest and grazing land.<br>Select "Grazing land" and "Forest/ woodlands" below and fill out the relevant sections.'
                }
            }
        )
        new_mixed_keyword = 'tech_lu_mixed'
        self.create_new_question(
            keyword=new_mixed_keyword,
            translation={
                'label': {
                    'en': 'Is land use mixed within the same land unit (e.g. agroforestry)?'
                },
                'helptext': {
                    'en': 'A mixture of crops, grazing and trees within the same land unit, e.g. agroforestry, agro-silvopastoralism.'
                }
            },
            question_type='bool'
        )

        new_mixed_keyword_specify = 'tech_lu_mixed_select'
        self.create_new_question(
            keyword=new_mixed_keyword_specify,
            translation={
                'label': {
                    'en': 'Specify mixed land use (crops/ grazing/ trees)'
                },
            },
            question_type='radio',
            values=[
                self.get_value('lu_mixed_mf'),
                self.get_value('lu_mixed_mp'),
                self.get_value('lu_mixed_ma'),
                self.get_value('lu_mixed_ms'),
            ]
        )

        new_qg_keyword = 'tech_qg_235'
        self.create_new_questiongroup(
            keyword=new_qg_keyword,
            translation=None
        )

        subcat_data = self.find_in_data(path=subcat_path, **data)
        subcat_data['questiongroups'] = [
            {
                'keyword': new_qg_keyword,
                'questions': [
                    {
                        'keyword': new_mixed_keyword,
                        'form_options': {
                            'question_conditions': [
                                f"=='1'|{new_mixed_keyword_specify}"
                            ],
                            'helptext_position': 'tooltip',
                        }
                    },
                    {
                        'keyword': new_mixed_keyword_specify,
                        'form_options': {
                            'question_condition': new_mixed_keyword_specify,
                        }
                    }
                ]
            }
        ] + subcat_data['questiongroups']
        subcat_data['form_options']['template'] = 'tech_lu_2018'

        self.update_translation(
            update_pk=2781,
            **{
                "label": {
                    "en": "Current land use type(s) where the Technology is applied"
                },
                "helptext": {
                    "en": "<p><strong>Land use</strong>: human activities which are directly related to land, making use of its resources or having an impact upon it.<br><strong>Land cover</strong>: Vegetation (natural or planted) or man-made structures (buildings, etc.) that cover the earth’s surface.</p>"
                }
            }
        )

        data = self.update_config_data(
            path=subcat_path, updated=subcat_data, **data)

        return data

    def add_questions_tech_lu_woodlands(self, **data) -> dict:

        qg_path = (
            'section_specifications', 'tech__3', 'tech__3__2', 'tech_qg_12'
        )
        qg_data = self.find_in_data(path=qg_path, **data)

        # Update the "other" question to have the label appear as placeholder
        qg_data['questions'][2]['form_options']['label_position'] = 'placeholder'
        del qg_data['questions'][2]['form_options']['row_class']

        # Update the conditions of the sub checkbox questions
        qg_data['questions'][0]['form_options']['question_condition'] = 'tech_lu_forest_natural'
        qg_data['questions'][1]['form_options']['question_condition'] = 'tech_lu_forest_plantation'

        # Update the translations of these questions
        self.update_translation(
            update_pk=1339,
            **{
                'label': {
                    'en': '(Semi-)natural forests/ woodlands: Specify management type'
                }
            }
        )
        self.update_translation(
            update_pk=1240,
            **{
                'label': {
                    'en': 'Tree plantation, afforestation: Specify origin and composition of species'
                }
            }
        )

        # Create a new first checkbox question which triggers the conditions
        forest_question_keyword = 'tech_lu_forest_type'
        forest_value_natural = 'lu_forest_natural'
        forest_value_plantation = 'lu_forest_plantation'
        self.create_new_question(
            keyword=forest_question_keyword,
            translation={},
            question_type='checkbox',
            values=[
                self.create_new_value(
                    keyword=k,
                    translation={
                        'label': {
                            'en': l
                        },
                        'helptext': {
                            'en': h
                        }
                    }
                )
                for i, (k, l, h) in enumerate([
                    (forest_value_natural, '(Semi-)natural forests/ woodlands', '<strong>Fn: Natural or semi-natural</strong>: forests mainly composed of indigenous trees, not planted by man'),
                    (forest_value_plantation, 'Tree plantation, afforestation', '<strong>Fp: Plantations, afforestations:</strong>: forest stands established by planting or/ and seeding in the process of afforestation or reforestation'),
                ])
            ]
        )
        qg_data['questions'] += [
            {
                'keyword': forest_question_keyword,
                'form_options': {
                    'template': 'no_label',
                    'question_conditions': [
                        f"=='{forest_value_natural}'|tech_lu_forest_natural",
                        f"=='{forest_value_plantation}'|tech_lu_forest_plantation",
                    ]
                },
                'view_options': {
                    'label_position': 'none'
                }
            }
        ]
        data = self.update_config_data(path=qg_path, updated=qg_data, **data)

        # Add new question about type of forest (natural)
        type_natural_keyword = 'tech_lu_forest_natural_type'
        data = self._create_land_use_subquestions(
            qg_path=qg_path,
            keyword=type_natural_keyword,
            label='(Semi-)natural forests/ woodlands: Search type of forest',
            values_list=[
                ('natural_forest_1715', 'Boreal coniferous forest natural vegetation'),
                ('natural_forest_1716', 'Boreal mountain systems natural vegetation'),
                ('natural_forest_1717', 'Boreal tundra woodland natural vegetation'),
                ('natural_forest_1750', 'Subtropical desert natural vegetation'),
                ('natural_forest_1751', 'Subtropical dry forest natural vegetation'),
                ('natural_forest_1752', 'Subtropical humid forest natural vegetation'),
                ('natural_forest_1753', 'Subtropical mountain systems natural vegetation'),
                ('natural_forest_1754', 'Subtropical steppe natural vegetation'),
                ('natural_forest_1758', 'Temperate continental forest natural vegetation'),
                ('natural_forest_1759', 'Temperate desert natural vegetation'),
                ('natural_forest_1760', 'Temperate mountain systems natural vegetation'),
                ('natural_forest_1761', 'Temperate oceanic forest natural vegetation'),
                ('natural_forest_1762', 'Temperate steppe natural vegetation'),
                ('natural_forest_1765', 'Tropical desert natural vegetation'),
                ('natural_forest_1766', 'Tropical dry forest natural vegetation'),
                ('natural_forest_1767', 'Tropical moist deciduous forest natural vegetation'),
                ('natural_forest_1768', 'Tropical mountain systems natural vegetation'),
                ('natural_forest_1769', 'Tropical rain forest natural vegetation'),
                ('natural_forest_1770', 'Tropical shrubland natural vegetation'),
            ],
            other_label='If type of forest is not listed above, specify other type',
            conditional_value=None,
            question_condition_keyword='tech_lu_forest_natural',
            **data
        )

        # Add new question about type of forest (plantation)
        type_plantation_keyword = 'tech_lu_forest_plantation_type'
        data = self._create_land_use_subquestions(
            qg_path=qg_path,
            keyword=type_plantation_keyword,
            label='Tree plantation, afforestation: Search type of forest',
            values_list=[
                ('plantation_forest_1773', 'Boreal coniferous forest plantation'),
                ('plantation_forest_1774', 'Boreal mountain systems plantation'),
                ('plantation_forest_1775', 'Boreal tundra woodland plantation'),
                ('plantation_forest_1776', 'Subtropical dry forest plantation'),
                ('plantation_forest_1777', 'Subtropical dry forest plantation - Eucalyptus spp.'),
                ('plantation_forest_1779', 'Subtropical dry forest plantation - broadleaf'),
                ('plantation_forest_1780', 'Subtropical dry forest plantation - Pinus spp.'),
                ('plantation_forest_1781', 'Subtropical dry forest plantation - Tectona grandis'),
                ('plantation_forest_1782', 'Subtropical humid forest plantation - broadleaf'),
                ('plantation_forest_1783', 'Subtropical humid forest plantation - Eucalyptus spp.'),
                ('plantation_forest_1784', 'Subtropical humid forest plantation'),
                ('plantation_forest_1786', 'Subtropical humid forest plantation - Pinus spp.'),
                ('plantation_forest_1787', 'Subtropical humid forest plantation - Tectona grandis'),
                ('plantation_forest_1788', 'Subtropical mountain systems plantation - broadleaf'),
                ('plantation_forest_1789', 'Subtropical mountain systems plantation - Eucalyptus spp.'),
                ('plantation_forest_1790', 'Subtropical mountain systems plantation'),
                ('plantation_forest_1792', 'Subtropical mountain systems plantation - Pinus spp.'),
                ('plantation_forest_1793', 'Subtropical mountain systems plantation - Tectona grandis'),
                ('plantation_forest_1794', 'Subtropical steppe plantation'),
                ('plantation_forest_1795', 'Subtropical steppe plantation - broadleaf'),
                ('plantation_forest_1796', 'Subtropical steppe plantation - coniferous'),
                ('plantation_forest_1797', 'Subtropical steppe plantation - Eucalyptus spp.'),
                ('plantation_forest_1799', 'Subtropical steppe plantation - Pinus spp.'),
                ('plantation_forest_1800', 'Subtropical steppe plantation - Tectona grandis'),
                ('plantation_forest_1801', 'Temperate continental forest plantation'),
                ('plantation_forest_1802', 'Temperate mountain systems plantation'),
                ('plantation_forest_1803', 'Temperate oceanic forest plantation'),
                ('plantation_forest_1804', 'Tropical dry forest plantation - broadleaf'),
                ('plantation_forest_1805', 'Tropical dry forest plantation - Eucalyptus spp.'),
                ('plantation_forest_1806', 'Tropical dry forest plantation'),
                ('plantation_forest_1808', 'Tropical dry forest plantation - Pinus spp.'),
                ('plantation_forest_1809', 'Tropical dry forest plantation - Tectona grandis'),
                ('plantation_forest_1810', 'Tropical moist deciduous forest plantation - broadleaf'),
                ('plantation_forest_1811', 'Tropical moist deciduous forest plantation - Eucalyptus spp.'),
                ('plantation_forest_1812', 'Tropical moist deciduous forest plantation'),
                ('plantation_forest_1814', 'Tropical moist deciduous forest plantation - Pinus spp.'),
                ('plantation_forest_1815', 'Tropical moist deciduous forest plantation - Tectona grandis'),
                ('plantation_forest_1816', 'Tropical mountain systems plantation - broadleaf'),
                ('plantation_forest_1817', 'Tropical mountain systems plantation - Eucalyptus spp.'),
                ('plantation_forest_1818', 'Tropical mountain systems plantation'),
                ('plantation_forest_1820', 'Tropical mountain systems plantation - Pinus spp.'),
                ('plantation_forest_1821', 'Tropical mountain systems plantation - Tectona grandis'),
                ('plantation_forest_1822', 'Tropical rain forest plantation'),
                ('plantation_forest_1823', 'Tropical rain forest plantation - broadleaf'),
                ('plantation_forest_1824', 'Tropical rain forest plantation - Eucalyptus spp.'),
                ('plantation_forest_1827', 'Tropical rain forest plantation - Pinus spp.'),
                ('plantation_forest_1828', 'Tropical rain forest plantation - Tectona grandis'),
                ('plantation_forest_1829', 'Tropical shrubland plantation'),
                ('plantation_forest_1830', 'Tropical shrubland plantation - broadleaf'),
                ('plantation_forest_1831', 'Tropical shrubland plantation - Eucalyptus spp.'),
                ('plantation_forest_1833', 'Tropical shrubland plantation - Pinus spp.'),
            ],
            other_label='If type of forest is not listed above, specify other type',
            conditional_value=None,
            question_condition_keyword='tech_lu_forest_plantation',
            **data
        )

        # Add new question about type of trees
        type_tree_keyword = 'tech_lu_forest_tree_type'
        data = self._create_land_use_subquestions(
            qg_path=qg_path,
            keyword=type_tree_keyword,
            label='Search type of tree',
            values_list=[
                ('tree_type_1700', 'Acacia albida'),
                ('tree_type_1701', 'Acacia auriculiformis'),
                ('tree_type_1702', 'Acacia mearnsii'),
                ('tree_type_1703', 'Acacia mellifera'),
                ('tree_type_1704', 'Acacia nilotica'),
                ('tree_type_1705', 'Acacia senegal'),
                ('tree_type_1706', 'Acacia seyal'),
                ('tree_type_1707', 'Acacia species'),
                ('tree_type_1708', 'Acacia tortilis'),
                ('tree_type_1709', 'Ailanthus excelsa'),
                ('tree_type_1710', 'Ailanthus species'),
                ('tree_type_1711', 'Araucaria angustifolia'),
                ('tree_type_1712', 'Araucaria cunninghamii'),
                ('tree_type_1713', 'Balanites aegyptiaca'),
                ('tree_type_1714', 'Bamboo bamboo'),
                ('tree_type_1718', 'Casuarina equisetifolia'),
                ('tree_type_1719', 'Casuarina junghuhniana'),
                ('tree_type_1720', 'Cordia alliadora'),
                ('tree_type_1721', 'Cupressus lusitanica'),
                ('tree_type_1722', 'Cupressus species'),
                ('tree_type_1723', 'Dalbergia sissoo'),
                ('tree_type_1724', 'Eucalyptus camaldulensis'),
                ('tree_type_1725', 'Eucalyptus deglupta'),
                ('tree_type_1726', 'Eucalyptus globulus'),
                ('tree_type_1727', 'Eucalyptus grandis'),
                ('tree_type_1728', 'Eucalyptus robusta'),
                ('tree_type_1729', 'Eucalyptus saligna'),
                ('tree_type_1730', 'Eucalyptus species'),
                ('tree_type_1731', 'Eucalyptus urophylla'),
                ('tree_type_1732', 'Abies species (fir)'),
                ('tree_type_1733', 'Gmelina arborea'),
                ('tree_type_1734', 'Hevea brasiliensis'),
                ('tree_type_1735', 'Khaya species'),
                ('tree_type_1736', 'Larix species (larch)'),
                ('tree_type_1737', 'Leucaena leucocephala'),
                ('tree_type_1738', 'Mimosa scabrella'),
                ('tree_type_1739', 'Pinus species (pine)'),
                ('tree_type_1740', 'Pinus caribaea v. caribaea'),
                ('tree_type_1741', 'Pinus caribaea v. hondurensis'),
                ('tree_type_1742', 'Pinus oocarpa'),
                ('tree_type_1743', 'Pinus patula'),
                ('tree_type_1744', 'Pinus radiata'),
                ('tree_type_1747', 'Populus species'),
                ('tree_type_1748', 'Sclerocarya birrea'),
                ('tree_type_1749', 'Picea species (spruce)'),
                ('tree_type_1755', 'Swietenia macrophylla'),
                ('tree_type_1756', 'Tectona grandis'),
                ('tree_type_1757', 'Tectona species'),
                ('tree_type_1763', 'Terminalia ivorensis'),
                ('tree_type_1764', 'Terminalia superba'),
                ('tree_type_1771', 'Xylia xylocapa'),
                ('tree_type_1772', 'Ziziphus mauritiana'),
                ('tree_type_1834', 'Azadirachta indica'),
                ('tree_type_1835', 'Grevillea robusta'),
            ],
            other_label='If type of tree is not listed above, specify other type',
            conditional_value=None,
            **data
        )

        # Add new question about decidiuous or evergreen trees
        deciduous_trees_keyword = 'tech_lu_forest_deciduous'
        self.create_new_question(
            keyword=deciduous_trees_keyword,
            translation={
                'label': {
                    'en': 'Are the trees specified above deciduous or evergreen?'
                }
            },
            question_type='radio',
            values=[
                self.create_new_value(
                    keyword=k,
                    translation={
                        'label': {
                            'en': l
                        }
                    },
                    order_value=i
                )
                for i, (k, l) in enumerate([
                    ('trees_deciduous', 'deciduous'),
                    ('trees_deciduous_mixed', 'mixed deciduous/ evergreen'),
                    ('trees_evergreen', 'evergreen'),
                ])
            ]
        )
        qg_data = self.find_in_data(path=qg_path, **data)
        qg_data['questions'] += [
            {
                'keyword': deciduous_trees_keyword,
                'form_options': {
                    'row_class': 'top-margin',
                }
            }
        ]

        # Rearrange order of questions
        order = [
            forest_question_keyword,
            'tech_lu_sub_other',
            'tech_lu_forest_natural',
            type_natural_keyword,
            f'{type_natural_keyword}_other',
            'tech_lu_forest_plantation',
            type_plantation_keyword,
            f'{type_plantation_keyword}_other',
            type_tree_keyword,
            f'{type_tree_keyword}_other',
            deciduous_trees_keyword,
            'tech_lu_forest_products',
            'tech_lu_forest_other',
        ]
        qg_data['questions'] = sorted(
            qg_data['questions'], key=lambda q: order.index(q['keyword']))

        data = self.update_config_data(path=qg_path, updated=qg_data, **data)

        return data

    def add_questions_tech_lu_grazingland(self, **data) -> dict:
        qg_path = (
            'section_specifications', 'tech__3', 'tech__3__2', 'tech_qg_11'
        )

        # Search animal type
        data = self._create_land_use_subquestions(
            qg_path=qg_path,
            keyword='tech_lu_grazingland_animals',
            label='Search animal type',
            values_list=[
                ('animals_50', 'Dairy Cattle'),
                ('animals_51', 'Non-Dairy Beef Cattle'),
                ('animals_52', 'Non-Dairy Working Cattle'),
                ('animals_53', 'Buffalo'),
                ('animals_54', 'Swine'),
                ('animals_55', 'Goats'),
                ('animals_56', 'Camels'),
                ('animals_57', 'Horses'),
                ('animals_58', 'Mules and Asses'),
                ('animals_59', 'Sheep'),
                ('animals_60', 'Poultry'),
                ('animals_61', 'Rabbits and similar mammals'),
                ('animals_wildlife_large', 'Wildlife – large herbivours'),
                ('animals_wildlife_small', 'Wildlife – small herbivours'),
            ],
            other_label='If animal type is not listed above, specify other animal',
            conditional_value=None,
            **data
        )

        # Crop-livestock management
        crop_livestock_keyword = 'tech_crop_livestock_management'
        crop_livestock_specify_keyword = 'tech_crop_livestock_management_specify'
        self.create_new_question(
            keyword=crop_livestock_keyword,
            translation={
                'label': {
                    'en': 'Is crop-livestock management practiced?'
                }
            },
            question_type='bool'
        )
        self.create_new_question(
            keyword=crop_livestock_specify_keyword,
            translation={
                'label': {
                    'en': 'If yes, specify'
                }
            },
            question_type='text'
        )
        qg_data = self.find_in_data(path=qg_path, **data)
        qg_data['questions'] = qg_data['questions'] + [
            {
                'keyword': crop_livestock_keyword,
                'form_options': {
                    'question_conditions': [
                        f"=='1'|{crop_livestock_specify_keyword}"
                    ],
                    'row_class': 'top-margin',
                }
            },
            {
                'keyword': crop_livestock_specify_keyword,
                'form_options': {
                    'question_condition': crop_livestock_specify_keyword
                }
            },
        ]

        # Products and services
        data = self._create_land_use_subquestions(
            qg_path=qg_path,
            keyword='tech_lu_grazingland_products',
            label='Search products and services',
            values_list=[
                ('prod_service_meat', 'meat'),
                ('prod_service_milk', 'milk'),
                ('prod_service_eggs', 'eggs'),
                ('prod_service_whool', 'whool'),
                ('prod_service_skins', 'Skins / hides'),
                ('prod_service_transport', 'Transport/  draught'),
            ],
            other_label='If product or service is not listed above, specify other product or service',
            conditional_value=None,
            **data
        )

        return data

    def add_tech_livestock_population(self, **data) -> dict:

        subcat_path = ('section_specifications', 'tech__3', 'tech__3__2')
        subcat_data = self.find_in_data(path=subcat_path, **data)

        # Create new questions
        keyword_species = 'tech_lu_grazingland_pop_species'
        keyword_count = 'tech_lu_grazingland_pop_count'
        self.create_new_question(
            keyword=keyword_species,
            translation={
                'label': {
                    'en': 'Species'
                }
            },
            question_type='select_type',
            values=[
                self.get_value('animals_50'),
                self.get_value('animals_51'),
                self.get_value('animals_52'),
                self.get_value('animals_53'),
                self.get_value('animals_54'),
                self.get_value('animals_55'),
                self.get_value('animals_56'),
                self.get_value('animals_57'),
                self.get_value('animals_58'),
                self.get_value('animals_59'),
                self.get_value('animals_60'),
                self.get_value('animals_61'),
                self.get_value('animals_wildlife_large'),
                self.get_value('animals_wildlife_small'),
            ]
        )
        self.create_new_question(
            keyword=keyword_count,
            translation={
                'label': {
                    'en': 'Count'
                }
            },
            question_type='int',
            configuration={
                'form_options': {
                    'field_options': {
                        'min': 0,
                    }
                }
            }
        )

        qg_keyword = 'tech_qg_236'
        self.create_new_questiongroup(
            keyword=qg_keyword,
            translation={
                'label': {
                    'en': 'Livestock population',
                }
            },
        )

        questiongroups = subcat_data['questiongroups']
        questiongroups.insert(4, {
            'keyword': qg_keyword,
            'form_options': {
                'questiongroup_condition': qg_keyword,
                'max_num': 5,
                'template': 'table1',
                'column_widths': ['70%', '30%'],
            },
            'view_options': {
                'conditional_question': 'tech_lu_grazingland',
            },
            'questions': [
                {
                    'keyword': keyword_species,
                },
                {
                    'keyword': keyword_count,
                }
            ]
        })
        subcat_data['questiongroups'] = questiongroups

        # Add conditions
        condition = f"=='tech_lu_grazingland'|{qg_keyword}"
        subcat_data['form_options']['questiongroup_conditions'] += [condition]
        subcat_data['questiongroups'][1]['questions'][0]['form_options'][
            'questiongroup_conditions'] += [condition]

        # Update template used for subcategory details
        subcat_data['view_options']['template'] = 'image_questiongroups_2018'

        data = self.update_config_data(
            path=subcat_path, updated=subcat_data, **data)

        return data

    def remove_tech_lu_grazingland_specify(self, **data) -> dict:
        qg_path = ('section_specifications', 'tech__3', 'tech__3__2', 'tech_qg_11')
        qg_data = self.find_in_data(path=qg_path, **data)
        qg_data['questions'] = [
            q for q in qg_data['questions']
            if q['keyword'] != 'tech_lu_grazingland_specify'
        ]
        return self.update_config_data(path=qg_path, updated=qg_data, **data)

    def delete_tech_lu_grazingland_specify(self, **data) -> dict:
        return self.update_data(
            'tech_qg_11', 'tech_lu_grazingland_specify', None, **data)

    def remove_tech_lu_cropland_specify(self, **data) -> dict:
        qg_path = ('section_specifications', 'tech__3', 'tech__3__2', 'tech_qg_10')
        qg_data = self.find_in_data(path=qg_path, **data)
        qg_data['questions'] = [
            q for q in qg_data['questions']
            if q['keyword'] != 'tech_lu_cropland_specify'
        ]
        return self.update_config_data(path=qg_path, updated=qg_data, **data)

    def delete_tech_lu_cropland_specify_data(self, **data) -> dict:
        return self.update_data(
            'tech_qg_10', 'tech_lu_cropland_specify', None, **data)

    def add_questions_tech_lu_cropland(self, **data) -> dict:
        qg_path = (
            'section_specifications', 'tech__3', 'tech__3__2', 'tech_qg_10'
        )

        # Annual cropping list of crops
        data = self._create_land_use_subquestions(
            qg_path=qg_path,
            keyword='tech_lu_cropland_annual_cropping_crops',
            label='Annual cropping - Select crops',
            values_list=[
                ('annual_crops_453', 'Fibre crops - other'),
            ],
            other_label='If crop type is not listed above, specify other crop',
            conditional_value='lu_cropland_ca',
            **data
        )

        # Search cropping system
        cropping_system_keyword = 'tech_lu_cropland_cropping_system'
        self.create_new_question(
            keyword=cropping_system_keyword,
            translation={
                'label': {
                    'en': 'If data will be linked to CBP (simple assessment), specify annual cropping system'
                }
            },
            question_type='select_type',
            values=self.create_new_values_list([
                ('cropping_system_401', 'Continuous wheat/barley/oats/upland rice'),
                ('cropping_system_402', 'Fallow - wheat/barley/oats/upland rice'),
                ('cropping_system_403', 'Continuous maize/sorghum/millet'),
                ('cropping_system_404', 'Fallow - maize/sorghum/millet'),
                ('cropping_system_405', 'Maize/sorghum/millet legume'),
                ('cropping_system_406', 'Maize/sorghum/millet intercropped with legume'),
                ('cropping_system_407', 'Fallow - maize/sorghum/millet intercropped with legume'),
                ('cropping_system_408', 'Continuous wetland rice'),
                ('cropping_system_409', 'Wetland rice - wheat'),
                ('cropping_system_410', 'Continuous vegetables'),
                ('cropping_system_411', 'Vegetables - wheat/barley/oat/upland rice'),
                ('cropping_system_412', 'Continuous cotton/tobacco'),
                ('cropping_system_413', 'Vegetable - cotton/tobacco'),
                ('cropping_system_414', 'Continuous root crop'),
                ('cropping_system_415', 'Cassava/potato/manioc - vegetable'),
                ('cropping_system_416', 'Cassava/potato/manioc - wheat/barley/oat'),
                ('cropping_system_417', 'Cassava/potato/manioc - maize/sorghum/millet'),
                ('cropping_system_418', 'Hay'),
                ('cropping_system_419', 'Wheat or similar rotation with hay/pasture'),
                ('cropping_system_420', 'Maize or similar rotation with hay/pasture'),
            ])
        )
        cropping_system_configuration = {
            'keyword': cropping_system_keyword,
            'form_options': {
                'question_condition': 'tech_lu_cropland_annual_cropping_crops',
            }
        }
        qg_data = self.find_in_data(path=qg_path, **data)
        qg_data['questions'] = qg_data['questions'] + [
            cropping_system_configuration]
        data = self.update_config_data(path=qg_path, updated=qg_data, **data)

        # Perennial cropping list of crops
        data = self._create_land_use_subquestions(
            qg_path=qg_path,
            keyword='tech_lu_cropland_perennial_cropping_crops',
            label='Perennial (non-woody) cropping - Select crops',
            values_list=[
                ('perennial_crops_502', 'banana/plantain/abaca'),
                ('perennial_crops_520', 'agave / sisal'),
                ('perennial_crops_521', 'areca'),
                ('perennial_crops_522', 'berries'),
                ('perennial_crops_sugar_cane', 'Sugar cane'),
                ('perennial_crops_pineapple', 'Pineapple'),
                ('perennial_crops_flower_crops', 'Perennial flower crops'),
                ('perennial_crops_medicinal', 'Perennial  medicinal, aromatic, pesticidal'),
            ],
            other_label='If crop type is not listed above, specify other crop',
            conditional_value='lu_cropland_cp',
            **data
        )

        # Tree and shrub cropping list of crops
        data = self._create_land_use_subquestions(
            qg_path=qg_path,
            keyword='tech_lu_cropland_tree_shrub_cropping_crops',
            label='Tree and shrub cropping - Select crops',
            values_list=[
                ('tree_shrub_501', 'avocado'),
                ('tree_shrub_503', 'citrus'),
                ('tree_shrub_504', 'cacao'),
                ('tree_shrub_505', 'coconut (fruit, coir, leaves, etc.)'),
                ('tree_shrub_506', 'coffee, open grown'),
                ('tree_shrub_507', 'coffee, shade grown'),
                ('tree_shrub_508', 'dates'),
                ('tree_shrub_509', 'mango, mangosteen, guava'),
                ('tree_shrub_510', 'oil palm'),
                ('tree_shrub_511', 'papaya'),
                ('tree_shrub_512', 'pome fruits (apples, pears, quinces, etc.)'),
                ('tree_shrub_513', 'rubber'),
                ('tree_shrub_514', 'stone fruits (peach, apricot, cherry, plum, etc)'),
                ('tree_shrub_515', 'tea'),
                ('tree_shrub_516', 'tree nuts (brazil nuts, pistachio, walnuts, almonds, etc.)'),
                ('tree_shrub_517', 'wolfberries'),
                ('tree_shrub_523', 'carob'),
                ('tree_shrub_524', 'cashew'),
                ('tree_shrub_525', 'cinnamon'),
                ('tree_shrub_528', 'figs'),
                ('tree_shrub_529', 'fruits, other'),
                ('tree_shrub_530', 'grapes'),
                ('tree_shrub_531', 'gums'),
                ('tree_shrub_532', 'jojoba'),
                ('tree_shrub_533', 'kapok'),
                ('tree_shrub_534', 'karite (sheanut)'),
                ('tree_shrub_535', 'olive'),
                ('tree_shrub_537', 'tallowtree'),
                ('tree_shrub_540', 'tung'),
                ('tree_shrub_fodder', 'Fodder trees'),

            ],
            other_label='If crop type is not listed above, specify other crop',
            conditional_value='lu_cropland_ct',
            **data
        )

        # Add questions about intercropping and crop rotation
        intercropping_keyword = 'tech_intercropping'
        intercropping_specify_keyword = 'tech_intercropping_specify'
        self.create_new_question(
            keyword=intercropping_keyword,
            translation={
                'label': {
                    'en': 'Is intercropping practiced?'
                }
            },
            question_type='bool'
        )
        self.create_new_question(
            keyword=intercropping_specify_keyword,
            translation={
                'label': {
                    'en': 'If yes, specify which crops are intercropped'
                }
            },
            question_type='text'
        )
        croprotation_keyword = 'tech_crop_rotation'
        croprotation_specify_keyword = 'tech_crop_rotation_specify'
        self.create_new_question(
            keyword=croprotation_keyword,
            translation={
                'label': {
                    'en': 'Is crop rotation practiced?'
                }
            },
            question_type='bool'
        )
        self.create_new_question(
            keyword=croprotation_specify_keyword,
            translation={
                'label': {
                    'en': 'If yes, specify'
                },
                'helptext': {
                    'en': 'E.g. sequence of crops, fallow periods, green manuring'
                }
            },
            question_type='text'
        )
        qg_path = qg_path
        qg_data = self.find_in_data(path=qg_path, **data)
        qg_data['questions'] = qg_data['questions'] + [
            {
                'keyword': intercropping_keyword,
                'form_options': {
                    'question_conditions': [
                        f"=='1'|{intercropping_specify_keyword}"
                    ],
                    'row_class': 'top-margin',
                }
            },
            {
                'keyword': intercropping_specify_keyword,
                'form_options': {
                    'question_condition': intercropping_specify_keyword
                }
            },
            {
                'keyword': croprotation_keyword,
                'form_options': {
                    'question_conditions': [
                        f"=='1'|{croprotation_specify_keyword}"
                    ],
                    'row_class': 'top-margin',
                }
            },
            {
                'keyword': croprotation_specify_keyword,
                'form_options': {
                    'question_condition': croprotation_specify_keyword,
                    'helptext_position': 'tooltip'
                }
            }
        ]
        data = self.update_config_data(path=qg_path, updated=qg_data, **data)
        return data

    def delete_tech_growing_seasons(self, **data) -> dict:

        moved_questions = {}
        for qg_data in data.get('tech_qg_19', []):
            old_data = {}
            for key, value in qg_data.items():
                if key in [
                    'tech_growing_seasons', 'tech_growing_seasons_specify'
                ]:
                    moved_questions[key] = value
                else:
                    old_data[key] = value
            if old_data:
                data['tech_qg_19'] = [old_data]

        if moved_questions:
            # Only move data if the corresponding conditional value
            # (tech_lu_cropland of tech_qg_9.tech_landuse_2018) is selected.
            # Otherwise, do not move the data (as this would block the form from
            # being submitted)
            cond_question_values = data.get('tech_qg_9', [{}])[0].get(
                'tech_landuse_2018', [])
            if 'tech_lu_cropland' in cond_question_values:
                new_data = data.get('tech_qg_10', [{}])
                new_data[0].update(moved_questions)
                data['tech_qg_10'] = new_data

        return data

    def remove_tech_lu_change(self, **data) -> dict:
        qg_path = ('section_specifications', 'tech__3', 'tech__3__2', 'tech_qg_7')
        qg_data = self.find_in_data(path=qg_path, **data)
        qg_data['questions'] = [
            q for q in qg_data['questions']
            if q['keyword'] != 'tech_lu_change'
        ]
        return self.update_config_data(path=qg_path, updated=qg_data, **data)

    def add_subcategory_initial_landuse(self, **data) -> dict:
        cat_path = ('section_specifications', 'tech__3')
        cat_data = self.find_in_data(path=cat_path, **data)

        # New subcategory 3.3
        subcat_keyword = 'tech__3__3__initial_landuse'
        self.create_new_category(
            keyword=subcat_keyword,
            translation={
                'label': {
                    'en': 'Has land use changed due to the implementation of the Technology?'
                },
                'helptext': {
                    'en': 'This section is not relevant for traditional systems'
                }
            }
        )

        # New question about whether land use has changed
        qg_keyword = 'tech_qg_237'
        self.create_new_questiongroup(
            keyword=qg_keyword,
            translation=None
        )
        q_keyword = 'tech_initial_landuse_changed'
        self.create_new_question(
            keyword=q_keyword,
            translation={
                'label': {
                    'en': 'Has land use changed due to the implementation of the Technology?'
                }
            },
            question_type='radio',
            values=self.create_new_values_list([
                ('initial_landuse_changed_yes', 'Yes (Please fill out the questions below with regard to the land use before implementation of the Technology)'),
                ('initial_landuse_changed_no', 'No (Continue with question 3.4)')
            ])
        )

        # Basically copy subcategory 3.2
        original_subcat_path = ('section_specifications', 'tech__3', 'tech__3__2')
        original_subcat_data = self.find_in_data(path=original_subcat_path, **data)
        original_qgs = copy.deepcopy(original_subcat_data['questiongroups'])

        # Re-map the questiongroups to ones newly created
        qg_mapping = {
            'tech_qg_235': 'tech_qg_238',  # mixed landuse?
            'tech_qg_9': 'tech_qg_239',    # main checkbox about land use
            'tech_qg_10': 'tech_qg_240',   # cropland (details)
            'tech_qg_11': 'tech_qg_241',   # grazingland (details)
            'tech_qg_236': 'tech_qg_242',  # grazingland (details, population)
            'tech_qg_12': 'tech_qg_243',   # forest (details)
            'tech_qg_14': 'tech_qg_244',   # settlements (details)
            'tech_qg_15': 'tech_qg_245',   # waterways (details)
            'tech_qg_16': 'tech_qg_246',   # mines (details)
            'tech_qg_17': 'tech_qg_247',   # unproductive (details)
            'tech_qg_18': 'tech_qg_248',   # other (details)
            'tech_qg_7': 'tech_qg_249',    # comments
        }
        # Re-map conditions
        questiongroup_conditions = [
            "=='tech_lu_cropland'|tech_qg_240",
            "=='tech_lu_grazingland'|tech_qg_241",
            "=='tech_lu_forest'|tech_qg_243",
            "=='tech_lu_settlements'|tech_qg_244",
            "=='tech_lu_waterways'|tech_qg_245",
            "=='tech_lu_mines'|tech_qg_246",
            "=='tech_lu_unproductive'|tech_qg_247",
            "=='tech_lu_other'|tech_qg_248",
            "=='tech_lu_grazingland'|tech_qg_242"
        ]

        new_qgs = []
        for qg in original_qgs:
            # Create a new questiongroup, use previous translation
            new_qg_keyword = qg_mapping[qg['keyword']]
            original_qg = self.get_questiongroup(qg['keyword'])
            self.create_new_questiongroup(
                keyword=new_qg_keyword,
                translation=original_qg.translation
            )
            qg['keyword'] = new_qg_keyword

            # Update questiongroup_condition where relevant
            if new_qg_keyword in [
                'tech_qg_240',
                'tech_qg_241',
                'tech_qg_243',
                'tech_qg_244',
                'tech_qg_245',
                'tech_qg_246',
                'tech_qg_247',
                'tech_qg_248',
                'tech_qg_242',
            ]:
                qg['form_options']['questiongroup_condition'] = new_qg_keyword

            # Update conditions of subquestions
            for question in qg['questions']:
                question_conditions = question.get('form_options', {}).get('question_conditions', [])
                if question_conditions:
                    question['form_options']['question_conditions'] = [
                        f'{cond}_initial' for cond in question_conditions
                    ]
                question_condition = question.get('form_options', {}).get('question_condition')
                if question_condition:
                    question['form_options']['question_condition'] = f'{question_condition}_initial'

            # Add questiongroup conditions to land use question
            if qg['questions'][0]['keyword'] == 'tech_landuse_2018':
                qg['questions'][0]['form_options']['questiongroup_conditions'] = questiongroup_conditions

            new_qgs.append(qg)

        # Configuration of new subcategory
        subcategory_data = {
            'keyword': subcat_keyword,
            'form_options': {
                'numbering': '3.3',
                'questiongroup_conditions': questiongroup_conditions,
                'template': 'tech_lu_2018'
            },
            'view_options': {
                'raw_questions': True,
                'template': 'image_questiongroups_2018'
            },
            'questiongroups': [
                {
                    'keyword': qg_keyword,
                    'form_options': {
                        'helptext_position': 'bottom',
                    },
                    'questions': [
                        {
                            'keyword': q_keyword,
                        }
                    ]
                }
            ] + new_qgs
        }
        # Insert at correct position
        subcategories = cat_data['subcategories']
        subcategories.insert(2, subcategory_data)
        cat_data['subcategories'] = subcategories
        data = self.update_config_data(path=cat_path, updated=cat_data, **data)

        # Update numbering of following subcategories (3.5 was removed,
        # therefore numbering of 3.6 and following stays the same)
        subcat_path = ('section_specifications', 'tech__3', 'tech__3__3')
        subcat_data = self.find_in_data(path=subcat_path, **data)
        subcat_data['form_options']['numbering'] = '3.4'
        data = self.update_config_data(
            path=subcat_path, updated=subcat_data, **data)

        subcat_path = ('section_specifications', 'tech__3', 'tech__3__4')
        subcat_data = self.find_in_data(path=subcat_path, **data)
        subcat_data['form_options']['numbering'] = '3.5'
        data = self.update_config_data(
            path=subcat_path, updated=subcat_data, **data)

        # Update translation of 3.4 (previously Further information about land
        # use)
        self.update_translation(
            update_pk=2788,
            **{
                'label': {
                    'en': 'Water supply'
                }
            }
        )

        return data

    def delete_tech_lu_change(self, **data) -> dict:
        return self.update_data('tech_qg_7', 'tech_lu_change', None, **data)

    def remove_tech_livestock_density(self, **data) -> dict:
        qg_path = ('section_specifications', 'tech__3', 'tech__3__3', 'tech_qg_19')
        qg_data = self.find_in_data(path=qg_path, **data)
        qg_data['questions'] = [
            q for q in qg_data['questions']
            if q['keyword'] != 'tech_livestock_density'
        ]
        return self.update_config_data(path=qg_path, updated=qg_data, **data)

    def delete_tech_livestock_density(self, **data) -> dict:
        return self.update_data(
            'tech_qg_19', 'tech_livestock_density', None, **data)

    def move_tech_growing_seasons(self, **data) -> dict:

        # Remove questions from old questiongroup
        old_qg_path = (
            'section_specifications', 'tech__3', 'tech__3__3', 'tech_qg_19')
        old_qg_data = self.find_in_data(path=old_qg_path, **data)
        old_qg_data['questions'] = [
            q for q in old_qg_data['questions']
            if q['keyword'] not in [
                'tech_growing_seasons', 'tech_growing_seasons_specify'
            ]
        ]
        data = self.update_config_data(
            path=old_qg_path, updated=old_qg_data, **data)

        # Add questions to new questiongroup
        new_qg_path = (
            'section_specifications', 'tech__3', 'tech__3__2', 'tech_qg_10')
        new_qg_data = self.find_in_data(path=new_qg_path, **data)

        questions = new_qg_data['questions']
        position = 9
        questions.insert(position, {
            'keyword': 'tech_growing_seasons_specify'
        })
        questions.insert(position, {
            'keyword': 'tech_growing_seasons',
            'form_options': {
                'row_class': 'top-margin',
            }
        })
        new_qg_data['questions'] = questions
        data = self.update_config_data(path=new_qg_path, updated=new_qg_data, **data)
        return data

    def add_question_tech_agronomic_tillage(self, **data) -> dict:
        # Create key and values
        q_keyword = 'tech_agronomic_tillage'
        self.create_new_question(
            keyword=q_keyword,
            translation={
                'label': {
                    'en': 'A3: Differentiate tillage systems'
                }
            },
            question_type='select',
            values=[
                self.create_new_value(
                    keyword='tillage_no',
                    translation={
                        'label': {
                            'en': 'A 3.1: No tillage'
                        }
                    },
                    order_value=1,
                ),
                self.create_new_value(
                    keyword='tillage_reduced',
                    translation={
                        'label': {
                            'en': 'A 3.2: Reduced tillage (> 30% soil cover)'
                        }
                    },
                    order_value=2,
                ),
                self.create_new_value(
                    keyword='tillage_full',
                    translation={
                        'label': {
                            'en': 'A 3.3: Full tillage (< 30% soil cover)'
                        }
                    },
                    order_value=3,
                ),
            ]
        )

        # Prepare configuration (with condition)
        question_configuration = {
            'keyword': q_keyword,
            'form_options': {
                'question_condition': q_keyword
            }
        }

        qg_path = (
            'section_specifications', 'tech__3', 'tech__3__6', 'tech_qg_21')
        qg_data = self.find_in_data(path=qg_path, **data)

        # Add question
        qg_data['questions'] = qg_data['questions'] + [
            question_configuration]

        # Add condition to the first question
        new_condition = f"=='measures_agronomic_a3'|{q_keyword}"
        question_conditions = qg_data['questions'][0]['form_options'].get(
            'question_conditions', [])
        question_conditions.append(new_condition)
        qg_data['questions'][0]['form_options'][
            'question_conditions'] = question_conditions

        data = self.update_config_data(path=qg_path, updated=qg_data, **data)
        return data

    def rename_option_a6_others(self, **data) -> dict:
        self.update_translation(
            update_pk=1516,
            **{
                'label': {
                    'en': 'A7: Others'
                }
            }
        )
        return data

    def add_option_a6_residue_management(self, **data) -> dict:
        self.add_new_value(
            question_keyword='tech_measures_agronomic_sub',
            value=self.create_new_value(
                keyword='measures_agronomic_a6_residue_management',
                translation={
                    'label': {
                        'en': 'A6: Residue management'
                    }
                },
                order_value=6,
            ),
            order_value=6,
        )
        return data

    def add_question_tech_residue_management(self, **data) -> dict:
        # Create key and values
        q_keyword = 'tech_residue_management'
        self.create_new_question(
            keyword=q_keyword,
            translation={
                'label': {
                    'en': 'A6: Specify residue management'  # If this text changes, also adapt the release notes above
                }
            },
            question_type='select',
            values=[
                self.create_new_value(
                    keyword='residue_management_burned',
                    translation={
                        'label': {
                            'en': 'A 6.1: burned'
                        }
                    },
                    order_value=1,
                ),
                self.create_new_value(
                    keyword='residue_management_grazed',
                    translation={
                        'label': {
                            'en': 'A 6.2: grazed'
                        }
                    },
                    order_value=2,
                ),
                self.create_new_value(
                    keyword='residue_management_collected',
                    translation={
                        'label': {
                            'en': 'A 6.3: collected'
                        }
                    },
                    order_value=3,
                ),
                self.create_new_value(
                    keyword='residue_management_retained',
                    translation={
                        'label': {
                            'en': 'A 6.4: retained'
                        }
                    },
                    order_value=4,
                ),
            ]
        )

        # Prepare configuration (with condition)
        question_configuration = {
            'keyword': q_keyword,
            'form_options': {
                'question_condition': q_keyword
            }
        }

        qg_path = (
            'section_specifications', 'tech__3', 'tech__3__6', 'tech_qg_21')
        qg_data = self.find_in_data(path=qg_path, **data)

        # Add question
        qg_data['questions'] = qg_data['questions'] + [
            question_configuration]

        # Add condition to the first question
        new_condition = f"=='measures_agronomic_a6_residue_management'|{q_keyword}"
        question_conditions = qg_data['questions'][0]['form_options'].get(
            'question_conditions', [])
        question_conditions.append(new_condition)
        qg_data['questions'][0]['form_options'][
            'question_conditions'] = question_conditions

        data = self.update_config_data(path=qg_path, updated=qg_data, **data)
        return data

    def remove_subcategory_1_6(self, **data) -> dict:
        cat_path = ('section_general_information', 'tech__1')
        cat_data = self.find_in_data(path=cat_path, **data)
        cat_data['subcategories'] = [
            subcat for subcat in cat_data['subcategories']
            if subcat['keyword'] != 'tech__1__6'
        ]
        data = self.update_config_data(path=cat_path, updated=cat_data, **data)
        return data

    def remove_person_address_questions(self, **data) -> dict:
        qg_path = (
            'section_general_information', 'tech__1', 'tech__1__2',
            'tech_qg_184')
        remove_questions = [
            'person_address',
            'person_phone_1',
            'person_phone_2',
            'person_email_1',
            'person_email_2',
        ]
        qg_data = self.find_in_data(path=qg_path, **data)
        qg_data['questions'] = [
            q for q in qg_data['questions']
            if q['keyword'] not in remove_questions]
        # Also update the view template
        qg_data['view_options']['template'] = 'select_user_2018'
        data = self.update_config_data(path=qg_path, updated=qg_data, **data)
        return data

    def delete_person_address_data(self, **data) -> dict:
        delete_questions = [
            'person_address',
            'person_phone_1',
            'person_phone_2',
            'person_email_1',
            'person_email_2',
        ]
        for question in delete_questions:
            data = self.update_data('tech_qg_184', question, None, **data)
        return data

    def add_option_user_resourceperson_type(self, **data) -> dict:
        self.add_new_value(
            question_keyword='user_resourceperson_type',
            value=self.create_new_value(
                keyword='resourceperson_cocompiler',
                translation={
                    'label': {
                        'en': 'co-compiler'
                    }
                },
                order_value=3,
                configuration_editions=self.all_configuration_editions
            ),
        )
        return data

    def rename_tech_individuals(self, **data) -> dict:
        # Add option to show helptext as tooltip. Then add tooltip.
        qg_path = (
            'section_specifications', 'tech__5', 'tech__5__6', 'tech_qg_71')
        qg_data = self.find_in_data(path=qg_path, **data)
        questions = []
        for question in qg_data['questions']:
            if question['keyword'] == 'tech_individuals':
                question['form_options'] = {'helptext_position': 'tooltip'}
            questions.append(question)
        qg_data['questions'] = questions
        data = self.update_config_data(path=qg_path, updated=qg_data, **data)
        self.update_translation(
            update_pk=1139,
            **{
                'label': {
                    'en': 'Individuals or groups'
                },
                'helptext': {
                    'en': 'Indicate if land users apply the technology as individuals or as members of a specific group/ company.'
                }
            }
        )
        return data

    def rename_tech_input_maint_total_estimation(self, **data) -> dict:
        self.update_translation(
            update_pk=1321,
            **{
                'label': {
                    'en': 'If you are unable to break down the costs in the table above, give an estimation of the total costs of maintaining the Technology'
                }
            }
        )
        return data

    def move_tech_input_maint_total_estimation(self, **data) -> dict:
        qg_path = (
            'section_specifications', 'tech__4', 'tech__4__7', 'tech_qg_50')
        qg_data = self.find_in_data(path=qg_path, **data)
        del qg_data['form_options']
        del qg_data['view_options']
        data = self.update_config_data(path=qg_path, updated=qg_data, **data)
        return data

    def rename_tech_input_est_total_estimation(self, **data) -> dict:
        self.update_translation(
            update_pk=1319,
            **{
                'label': {
                    'en': 'If you are unable to break down the costs in the table above, give an estimation of the total costs of establishing the Technology'
                }
            }
        )
        return data

    def move_tech_input_est_total_estimation(self, **data) -> dict:
        qg_path = (
            'section_specifications', 'tech__4', 'tech__4__5', 'tech_qg_42')
        qg_data = self.find_in_data(path=qg_path, **data)
        del qg_data['form_options']
        del qg_data['view_options']
        data = self.update_config_data(path=qg_path, updated=qg_data, **data)
        return data

    def remove_tech_maint_type(self, **data) -> dict:
        qg_path = (
            'section_specifications', 'tech__4', 'tech__4__6', 'tech_qg_43')
        qg_data = self.find_in_data(path=qg_path, **data)
        qg_data['questions'] = [
            q for q in qg_data['questions'] if q['keyword'] != 'tech_maint_type']
        data = self.update_config_data(path=qg_path, updated=qg_data, **data)
        return data

    def delete_tech_maint_type(self, **data) -> dict:
        return self.update_data('tech_qg_43', 'tech_maint_type', None, **data)

    def remove_tech_est_type(self, **data) -> dict:
        qg_path = (
            'section_specifications', 'tech__4', 'tech__4__4', 'tech_qg_165')
        qg_data = self.find_in_data(path=qg_path, **data)
        qg_data['questions'] = [
            q for q in qg_data['questions'] if q['keyword'] != 'tech_est_type']
        data = self.update_config_data(path=qg_path, updated=qg_data, **data)
        return data

    def delete_tech_est_type(self, **data: dict) -> dict:
        return self.update_data('tech_qg_165', 'tech_est_type', None, **data)

    def add_option_tech_lu_grazingland_transhumant(self, **data) -> dict:
        self.add_new_value(
            question_keyword='tech_lu_grazingland_extensive',
            value=self.create_new_value(
                keyword='lu_grazingland_transhumant',
                translation={
                    'label': {
                        'en': 'Transhumant pastoralism'
                    }
                },
                order_value=4
            ),
        )
        return data

    def rename_tech_lu_grazingland_pastoralism(self, **data) -> dict:
        self.update_translation(
            update_pk=1759,
            **{
                'label': {
                    'en': 'Semi-nomadic pastoralism'
                },
                'helptext': {
                    'en': '<strong>Semi-nomadic pastoralism</strong>: animal owners have a permanent place of residence where supplementary cultivation is practiced. Herds are moved to distant grazing grounds.'
                }
            }
        )
        return data

    def rename_us_dollars(self, **data) -> dict:
        self.update_translation(
            update_pk=1904,
            **{
                "label": {
                    "en": "USD"
                }
            }
        )
        return data

    def do_nothing(self, **data) -> dict:
        return data

    def _create_land_use_subquestions(
            self, qg_path: tuple, keyword: str, label: str, values_list: list,
            other_label: str, conditional_value: str or None,
            question_condition_keyword: str or None=None, **data) -> dict:

        if question_condition_keyword is None:
            question_condition_keyword = keyword

        # Create question
        self.create_new_question(
            keyword=keyword,
            translation={
                'label': {
                    'en': label
                }
            },
            question_type='multi_select',
            values=self.create_new_values_list(values_list),
        )
        question_configuration = {
            'keyword': keyword,
            'form_options': {
                'question_condition': question_condition_keyword,
                'row_class': 'top-margin'
            }
        }

        # Create "other" question
        other_keyword = f'{keyword}_other'
        self.create_new_question(
            keyword=other_keyword,
            translation={
                'label': {
                    'en': other_label
                }
            },
            question_type='char'
        )
        other_configuration = {
            'keyword': other_keyword,
            'form_options': {
                'question_condition': question_condition_keyword,
                'template': 'checkbox_other',
                'label_position': 'placeholder',
                'label_class': 'input-full-width'
            },
            'view_options': {
                'template': 'checkbox_other',
            }
        }

        # Add configuration
        qg_data = self.find_in_data(path=qg_path, **data)
        qg_data['questions'] = qg_data['questions'] + [
            question_configuration, other_configuration]
        if conditional_value:
            new_condition = f"=='{conditional_value}'|{keyword}"
            question_conditions = qg_data['questions'][0]['form_options'].get(
                'question_conditions', [])
            question_conditions += [new_condition]
            qg_data['questions'][0]['form_options'][
                'question_conditions'] = question_conditions

        return self.update_config_data(path=qg_path, updated=qg_data, **data)
