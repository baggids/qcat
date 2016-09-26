COUNTRY_MAPPING = {
    'country_GRE': 'country_GRC',
    'country_SPA': 'country_ESP',
    'country_AS': 'country_AFG',
    'country_SWI': 'country_CHE',
    'country_ZIM': 'country_ZWE',
    'country_RSA': 'country_ZAF',
    'country_TAJ': 'country_TJK',
    'country_KYR': 'country_KGZ',
    'country_TUM': 'country_TKM',
    'country_COS': 'country_CRI',
    'country_CHA': 'country_TCD',
    'country_CAM': 'country_CMR',
    'country_BOT': 'country_BWA',
    'country_BAN': 'country_BGD',
    'country_TOG': 'country_TGO',
    'country_TAN': 'country_TZA',
    'country_NEP': 'country_NPL',
    'country_MOR': 'country_MAR',
    'country_UNK': 'country_GBR',
    'country_POR': 'country_PRT',
    'country_PHI': 'country_PHL',
    'country_ZAM': 'country_ZMB',
    'country_BHU': 'country_BTN',
    'country_NIG': 'country_NER',
    'country_IDS': 'country_IDN',
    'country_BRK': 'country_BFA',
    'country_HON': 'country_HND',
    'country_BUR': 'country_BDI',
    'country_LEB': 'country_LBN',
    'country_MAD': 'country_MDG',
    'country_HAI': 'country_HTI',
    'country_OMA': 'country_OMN',
    'country_SUD': 'country_SDN',
    'country_GER': 'country_DEU',
    'country_VIE': 'country_VNM',
    'country_NET': 'country_NLD',
    'country_ROM': 'country_ROU',
    'country_SLA': 'country_SVK',
    'country_CBD': 'country_KHM',
    'country_ICE': 'country_ISL',
    'country_VAN': 'country_VUT',
}
LANDUSE_MAPPING = {
    114: 'tech_lu_cropland',
    115: 'tech_lu_cropland',
    116: 'tech_lu_cropland',
    117: 'tech_lu_grazingland',
    118: 'tech_lu_grazingland',
    119: 'tech_lu_forest',
    120: 'tech_lu_forest',
    121: 'tech_lu_forest',
    122: 'tech_lu_mixed',
    123: 'tech_lu_mixed',
    124: 'tech_lu_mixed',
    125: 'tech_lu_mixed',
    126: 'tech_lu_mixed',
    127: 'tech_lu_mines',
    128: 'tech_lu_settlements',
    129: 'tech_lu_waterways',
    130: 'tech_lu_other',
}
LANDUSE_MAPPING_VERBOSE = {
    114: 'Cropland: Ca: Annual cropping',
    115: 'Cropland: Cp: Perennial (non-woody) cropping',
    116: 'Cropland: Ct: Tree and shrub cropping',
    117: 'Grazing land: Ge: Extensive grazing land',
    118: 'Grazing land: Gi: Intensive grazing/ fodder production',
    119: 'Forests / woodlands: Fn: Natural',
    120: 'Forests / woodlands: Fp: Plantations, afforestations',
    121: 'Forests / woodlands: Fo: Other',
    122: 'Mixed: Mf: Agroforestry',
    123: 'Mixed: Mp: Agro-pastoralism',
    124: 'Mixed: Ma: Agro-silvopastoralism',
    125: 'Mixed: Ms: Silvo-pastoralism',
    126: 'Mixed: Mo: Other',
    127: 'Other: Oi: Mines and extractive industries',
    128: 'Other: Os: Settlements, infrastructure networks',
    129: 'Other: Ow: Waterways, drainage lines, ponds, dams',
    130: 'Other: Oo: Other: wastelands, deserts, glaciers, swamps, recreation areas, etc',
}
LANDUSE_CROPLAND_MAPPING = {
    114: 'lu_cropland_ca',
    115: 'lu_cropland_cp',
    116: 'lu_cropland_ct',
}
GROWING_SEASON_MAPPING = {
    131: 'growing_season_1',
    132: 'growing_season_2',
    133: 'growing_season_3',
}
SPREAD_AREA_COVERED = {
    6: 'tech_spread_less_01',
    7: 'tech_spread_01_1',
    8: 'tech_spread_1_10',
    9: 'tech_spread_10_100',
    10: 'tech_spread_100_1000',
    11: 'tech_spread_1000_10000',
    12: 'tech_spread_10000_plus',
}
MEASURE_MAPPING = {
    # Based on measure_type in qt_2_2_2_2_measure
    1: 'tech_measures_agronomic',
    2: 'tech_measures_vegetative',
    3: 'tech_measures_structural',
    4: 'tech_measures_management',
}
MEASURE_AGRONOMIC_MAPPING = {
    134: 'measures_agronomic_a1',
    135: 'measures_agronomic_a2',
    136: 'measures_agronomic_a3',
    137: 'measures_agronomic_a4',
    # measures_agronomic_a5 was newly introduced in QCAT
    138: 'measures_agronomic_a6',
}
MEASURE_VEGETATIVE_MAPPING = {
    139: 'measures_vegetative_v1',
    140: 'measures_vegetative_v2',
    141: 'measures_vegetative_v3',
    # measures_vegetative_v4 was newly introduced in QCAT
    142: 'measures_vegetative_v5',
}
MEASURE_STRUCTURAL_MAPPING = {
    # New categories in QCAT: s7, s8, s9, s10
    143: 'measures_structural_s1',
    144: 'measures_structural_s1',
    145: 'measures_structural_s2',
    146: 'measures_structural_s3',
    147: 'measures_structural_s4',
    148: 'measures_structural_s5',
    149: 'measures_structural_s11',
    150: 'measures_structural_s6',
    151: 'measures_structural_s11',
}
MEASURE_MANAGEMENT_MAPPING = {
    152: 'measures_management_m1',
    153: 'measures_management_m2',
    154: 'measures_management_m3',
    155: 'measures_management_m4',
    156: 'measures_management_m5',
    157: 'measures_management_m6',
    158: 'measures_management_m7',
}
DEGRADATION_TYPE_MAPPING = {
    165: 'degradation_erosion_water',
    166: 'degradation_erosion_water',
    167: 'degradation_erosion_water',
    168: 'degradation_erosion_water',
    169: 'degradation_erosion_water',
    170: 'degradation_erosion_water',
    171: 'degradation_erosion_wind',
    172: 'degradation_erosion_wind',
    173: 'degradation_erosion_wind',
    174: 'degradation_chemical',
    175: 'degradation_chemical',
    176: 'degradation_chemical',
    177: 'degradation_chemical',
    178: 'degradation_physical',
    179: 'degradation_physical',
    180: 'degradation_physical',
    181: 'degradation_physical',
    182: 'degradation_physical',
    183: 'degradation_biological',
    184: 'degradation_biological',
    185: 'degradation_biological',
    186: 'degradation_biological',
    187: 'degradation_biological',
    188: 'degradation_biological',
    189: 'degradation_biological',
    190: 'degradation_water',
    191: 'degradation_water',
    192: 'degradation_water',
    193: 'degradation_water',
    194: 'degradation_water',
    195: 'degradation_water',
}
DEGRADATION_TYPE_MAPPING_WATER_EROSION = {
    165: 'degradation_wt',
    166: 'degradation_wg',
    167: 'degradation_wm',
    168: 'degradation_wr',
    169: 'degradation_wc',
    170: 'degradation_wo',
}
DEGRADATION_TYPE_MAPPING_WIND_EROSION = {
    171: 'degradation_et',
    172: 'degradation_ed',
    173: 'degradation_eo',
}
DEGRADATION_TYPE_MAPPING_CHEMICAL = {
    174: 'degradation_cn',
    175: 'degradation_ca',
    176: 'degradation_cp',
    177: 'degradation_cs',
}
DEGRADATION_TYPE_MAPPING_PHYSICAL = {
    178: 'degradation_pc',
    179: 'degradation_pk',
    180: 'degradation_pw',
    181: 'degradation_ps',
    182: 'degradation_pu',
}
DEGRADATION_TYPE_MAPPING_BIOLOGICAL = {
    183: 'degradation_bc',
    184: 'degradation_bh',
    185: 'degradation_bq',
    186: 'degradation_bf',
    187: 'degradation_bs',
    188: 'degradation_bl',
    189: 'degradation_bp',
}
DEGRADATION_TYPE_MAPPING_WATER = {
    190: 'degradation_ha',
    191: 'degradation_hs',
    192: 'degradation_hg',
    193: 'degradation_hp',
    194: 'degradation_hq',
    195: 'degradation_hw',
}

qg_name = {
    'qg_name': {
        'questions': {
            'name': {
                'mapping': [
                    {
                        'wocat_table': 'qt_1',
                        'wocat_column': 'cmn_name',
                    }
                ],
                'type': 'string',
            },
            'name_local': {
                'mapping': [
                    {
                        'wocat_table': 'qt_1',
                        'wocat_column': 'other_names',
                    }
                ],
                'type': 'string',
            },
        }
    },
}

qg_location = {
    'qg_location': {
        'questions': {
            'country': {
                'mapping': [
                    {
                        'wocat_table': 'qt_1',
                        'wocat_column': 'country_code',
                        'mapping_prefix': 'country_',
                    }
                ],
                'type': 'dropdown',
                'value_mapping_list': COUNTRY_MAPPING,
            },
            'state_province': {
                'mapping': [
                    {
                        'wocat_table': 'qt_1',
                        'wocat_column': 'state_province',
                    }
                ],
                'type': 'string',
            },
            'further_location': {
                'mapping': [
                    {
                        'wocat_table': 'qt_1',
                        'wocat_column': 'district_commune',
                    }
                ],
                'type': 'string',
            },
        }
    },
}

qg_import = {
    'qg_import': {
        'questions': {
            'import_old_code': {
                'mapping': [
                    {
                        'wocat_table': 'qt_1',
                        'wocat_column': 'technology_code',
                    }
                ],
                'type': 'string',
            }
        }
    },
}

qg_accept_conditions = {
    'qg_accept_conditions': {
        'questions': {
            'date_documentation': {
                'mapping': [
                    {
                        'wocat_table': 'qt_1',
                        'wocat_column': 'data_collection_date',
                    }
                ],
                'type': 'date',
            },
            'accept_conditions': {
                'type': 'constant',
                'value': 1
            },
        }
    },
}

# 2.3 Photos of the Technology.
qg_photos = {
    'qg_photos': {
        'questions': {
            'image': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_1_3',
                        'wocat_column': 'blob_id',
                    }
                ],
                'type': 'file'
            },
            'image_caption': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_1_3',
                        'wocat_column': 'description'
                    },
                ],
                'type': 'string',
            },
            'image_date': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_1_3',
                        'wocat_column': 'date'
                    }
                ],
                'type': 'date'
            },
            'image_location': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_1_3',
                        'wocat_column': 'location'
                    },
                    {
                        'wocat_table': 'qt_2_1_3',
                        'wocat_column': 'area'
                    }
                ],
                'type': 'string',
                'composite': {
                    'type': 'merge',
                    'separator': ', '
                }
            },
            'image_photographer': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_1_3',
                        'wocat_column': 'author'
                    },
                    {
                        'wocat_table': 'qt_2_1_3',
                        'wocat_column': 'address',
                        'mapping_prefix': '(',
                        'mapping_suffix': ')',
                    }
                ],
                'type': 'string',
                'composite': {
                    'type': 'merge',
                    'separator': ' '
                }
            },
        },
        'repeating': True,
        'sort_function': 'sort_by_key(k, "photo_h_position", none_value=1000)',
        'wocat_table': 'qt_2_1_3'
    }
}

# Definition
tech_qg_1 = {
    'tech_qg_1': {
        'questions': {
            'tech_definition': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_1',
                        'wocat_column': 'definition',
                    }
                ],
                'type': 'string',
            },
        }
    },
}

# Description
tech_qg_2 = {
    'tech_qg_2': {
        'questions': {
            'tech_description': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_1',
                        'wocat_column': 'description',
                        'mapping_prefix': '',
                    },
                    {
                        'wocat_table': 'qt_2_1',
                        'wocat_column': 'purpose',
                        'mapping_prefix': 'Purpose of the Technology: ',
                    },
                    {
                        'wocat_table': 'qt_2_1',
                        'wocat_column': 'maintenance',
                        'mapping_prefix': 'Establishment / maintenance activities and inputs: ',
                    },
                    {
                        'wocat_table': 'qt_2_1',
                        'wocat_column': 'environment',
                        'mapping_prefix': 'Natural / human environment: ',
                    }
                ],
                'type': 'string',
                'composite': {
                    'type': 'merge'
                }
            }
        }
    },
}

qg_location_map = {
    'qg_location_map': {
        'questions': {
            'location_map': {
                'mapping': [
                    {
                        'wocat_table': 'qt_1',
                        'wocat_column': 'latitude',
                    },
                    {
                        'wocat_table': 'qt_1',
                        'wocat_column': 'longitude'
                    }
                ],
                'type': 'dropdown',
                'composite': {
                    'type': 'geom_point'
                }
            },
        }
    },
}

# Location comments
tech_qg_225 = {
    'tech_qg_225': {
        'questions': {
            'location_comments': {
                'mapping': [
                    {
                        'wocat_table': 'qt_1',
                        'wocat_column': 'outline_boundary_points',
                        'mapping_prefix': 'Boundary points of the Technology area: '
                    }
                ],
                'type': 'string',
                'composite': {
                    'type': 'merge'
                }
            }
        }
    },
}

# 2.6 Date of implementation
tech_qg_160 = {
    'tech_qg_160': {
        'questions': {
            'tech_implementation_decades': {
                'mapping': [
                    # Less than 10 years ago (recently): 198
                    {
                        'wocat_table': 'qt_2_3_1',
                        'wocat_column': 'land_user_initiative',
                        'value_mapping': 'implemenation_less_10',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'land_user_initiative_rank',
                                    }
                                ],
                                'operator': 'contains',
                                'value': '131',
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'land_user_initiative'
                                    }
                                ],
                                'operator': 'contains',
                                'value': '198'
                            }
                        ],
                        'conditions_join': 'and'
                    },
                    {
                        'wocat_table': 'qt_2_3_1',
                        'wocat_column': 'experiments',
                        'value_mapping': 'implemenation_less_10',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'experiments_rank',
                                    }
                                ],
                                'operator': 'contains',
                                'value': '131',
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'experiments'
                                    }
                                ],
                                'operator': 'contains',
                                'value': '198'
                            }
                        ],
                        'conditions_join': 'and'
                    },
                    {
                        'wocat_table': 'qt_2_3_1',
                        'wocat_column': 'externally',
                        'value_mapping': 'implemenation_less_10',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'externally_rank',
                                    }
                                ],
                                'operator': 'contains',
                                'value': '131',
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'externally'
                                    }
                                ],
                                'operator': 'contains',
                                'value': '198'
                            }
                        ],
                        'conditions_join': 'and'
                    },
                    {
                        'wocat_table': 'qt_2_3_1',
                        'wocat_column': 'other1',
                        'value_mapping': 'implemenation_less_10',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'other1_rank',
                                    }
                                ],
                                'operator': 'contains',
                                'value': '131',
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'other1'
                                    }
                                ],
                                'operator': 'contains',
                                'value': '198'
                            }
                        ],
                        'conditions_join': 'and'
                    },
                    # 10-50 years ago: 197
                    {
                        'wocat_table': 'qt_2_3_1',
                        'wocat_column': 'land_user_initiative',
                        'value_mapping': 'implemenation_10_50',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'land_user_initiative_rank',
                                    }
                                ],
                                'operator': 'contains',
                                'value': '131',
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'land_user_initiative'
                                    }
                                ],
                                'operator': 'contains',
                                'value': '197'
                            }
                        ],
                        'conditions_join': 'and'
                    },
                    {
                        'wocat_table': 'qt_2_3_1',
                        'wocat_column': 'experiments',
                        'value_mapping': 'implemenation_10_50',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'experiments_rank',
                                    }
                                ],
                                'operator': 'contains',
                                'value': '131',
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'experiments'
                                    }
                                ],
                                'operator': 'contains',
                                'value': '197'
                            }
                        ],
                        'conditions_join': 'and'
                    },
                    {
                        'wocat_table': 'qt_2_3_1',
                        'wocat_column': 'externally',
                        'value_mapping': 'implemenation_10_50',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'externally_rank',
                                    }
                                ],
                                'operator': 'contains',
                                'value': '131',
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'externally'
                                    }
                                ],
                                'operator': 'contains',
                                'value': '197'
                            }
                        ],
                        'conditions_join': 'and'
                    },
                    {
                        'wocat_table': 'qt_2_3_1',
                        'wocat_column': 'other1',
                        'value_mapping': 'implemenation_10_50',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'other1_rank',
                                    }
                                ],
                                'operator': 'contains',
                                'value': '131',
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'other1'
                                    }
                                ],
                                'operator': 'contains',
                                'value': '197'
                            }
                        ],
                        'conditions_join': 'and'
                    },
                    # More than 50 years ago (traditional): 196
                    {
                        'wocat_table': 'qt_2_3_1',
                        'wocat_column': 'land_user_initiative',
                        'value_mapping': 'implemenation_50_plus',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'land_user_initiative_rank',
                                    }
                                ],
                                'operator': 'contains',
                                'value': '131',
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'land_user_initiative'
                                    }
                                ],
                                'operator': 'contains',
                                'value': '196'
                            }
                        ],
                        'conditions_join': 'and'
                    },
                    {
                        'wocat_table': 'qt_2_3_1',
                        'wocat_column': 'experiments',
                        'value_mapping': 'implemenation_50_plus',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'experiments_rank',
                                    }
                                ],
                                'operator': 'contains',
                                'value': '131',
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'experiments'
                                    }
                                ],
                                'operator': 'contains',
                                'value': '196'
                            }
                        ],
                        'conditions_join': 'and'
                    },
                    {
                        'wocat_table': 'qt_2_3_1',
                        'wocat_column': 'externally',
                        'value_mapping': 'implemenation_50_plus',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'externally_rank',
                                    }
                                ],
                                'operator': 'contains',
                                'value': '131',
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'externally'
                                    }
                                ],
                                'operator': 'contains',
                                'value': '196'
                            }
                        ],
                        'conditions_join': 'and'
                    },
                    {
                        'wocat_table': 'qt_2_3_1',
                        'wocat_column': 'other1',
                        'value_mapping': 'implemenation_50_plus',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'other1_rank',
                                    }
                                ],
                                'operator': 'contains',
                                'value': '131',
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'other1'
                                    }
                                ],
                                'operator': 'contains',
                                'value': '196'
                            }
                        ],
                        'conditions_join': 'and'
                    },
                ],
                'type': 'dropdown',
            },
        }
    }
}

# 2.7 Introduction of the Technology
tech_qg_5 = {
    'tech_qg_5': {
        'questions': {
            'tech_who_implemented': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_3_1',
                        'wocat_column': 'land_user_initiative_rank',
                        'value_mapping': 'implementation_innovation',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'land_user_initiative_rank',
                                    }
                                ],
                                'operator': 'contains',
                                'value': '131',
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'land_user_initiative'
                                    }
                                ],
                                'operator': 'one_of',
                                'value': ['197', '198']
                            }
                        ],
                        'conditions_join': 'and'
                    },
                    {
                        'wocat_table': 'qt_2_3_1',
                        'wocat_column': 'land_user_initiative_rank',
                        'value_mapping': 'implementation_traditional',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'land_user_initiative_rank',
                                    }
                                ],
                                'operator': 'contains',
                                'value': '131',
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'land_user_initiative'
                                    }
                                ],
                                'operator': 'contains',
                                'value': '196'
                            }
                        ],
                        'conditions_join': 'and'
                    },
                    {
                        'wocat_table': 'qt_2_3_1',
                        'wocat_column': 'experiments_rank',
                        'value_mapping': 'implementation_experiments',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'experiments_rank',
                                    }
                                ],
                                'operator': 'contains',
                                'value': '131',
                            }
                        ]
                    },
                    {
                        'wocat_table': 'qt_2_3_1',
                        'wocat_column': 'externally_rank',
                        'value_mapping': 'implementation_externally',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_3_1',
                                        'wocat_column': 'externally_rank',
                                    }
                                ],
                                'operator': 'contains',
                                'value': '131',
                            }
                        ]
                    },
                ],
                'type': 'checkbox',
                'composite': {
                    'type': 'checkbox'
                }
            },
            'tech_who_implemented_other': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_3_1',
                        'wocat_column': 'other1_description',
                    }
                ],
                'type': 'string',
                'conditions': [
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_3_1',
                                'wocat_column': 'other1_rank',
                            }
                        ],
                        'operator': 'contains',
                        'value': '131'
                    }
                ]
            },
            'tech_who_implemented_comments': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_3_1',
                        'wocat_column': 'comment',
                    }
                ],
                'type': 'string',
            }
        }
    }
}

# Land use types
tech_qg_9 = {
    'tech_qg_9': {
         'questions': {
             'tech_landuse': {
                 'mapping': [
                     {
                         'wocat_table': 'qt_2_2_2_1',
                         'wocat_column': 'landuse_sub1'
                     },
                     {
                         'wocat_table': 'qt_2_2_2_1',
                         'wocat_column': 'landuse_sub2'
                     },
                 ],
                 'type': 'checkbox',
                 'composite': {
                     'type': 'checkbox'
                 },
                 'value_mapping_list': LANDUSE_MAPPING,
             }
         }
     },
}

# Cropland subcategories
tech_qg_10 = {
    'tech_qg_10': {
        'questions': {
            'tech_lu_cropland_sub': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_2_2_1',
                        'wocat_column': 'landuse_sub1'
                    },
                    {
                        'wocat_table': 'qt_2_2_2_1',
                        'wocat_column': 'landuse_sub2'
                    }
                ],
                'type': 'checkbox',
                'composite': {
                    'type': 'checkbox',
                    'mapping': 'exclusive',
                },
                'value_mapping_list': LANDUSE_CROPLAND_MAPPING,
            }
        }
    },
}

# Grazing land subcategories.
# Only add if main category "grazing land" was selected in
# qt_2_2_2_1.landuse_sub1 or qt_2_2_2_1.landuse_sub1 (QCAT condition
# tech_qg_11). Else use comments (QCAT tech_qg_7.tech_lu_comments).
tech_qg_11 = {
    'tech_qg_11': {
        'questions': {
            'tech_lu_grazingland_extensive': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'nomadism',
                        'value_mapping': 'tech_lu_grazingland_nomadism'
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'semi_nomadism',
                        'value_mapping': 'tech_lu_grazingland_pastoralism'
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'ranching',
                        'value_mapping': 'tech_lu_grazingland_ranching'
                    },
                ],
                'type': 'checkbox',
                'composite': {
                    'type': 'checkbox',
                }
            },
            'tech_lu_grazingland_intensive': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'cut_carry',
                        'value_mapping': 'tech_lu_grazingland_zerograzing'
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'improved_pasture',
                        'value_mapping': 'tech_lu_grazingland_improvedpasture'
                    },
                ],
                'type': 'checkbox',
                'composite': {
                    'type': 'checkbox',
                }
            },
            'tech_lu_grazingland_specify': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'nomadism_comment',
                        'mapping_prefix': 'Nomadism: '
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'semi_nomadism_comment',
                        'mapping_prefix': 'Semi-nomadism/ pastoralism: '
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'ranching_comment',
                        'mapping_prefix': 'Ranching: '
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'cut_carry_comment',
                        'mapping_prefix': 'Cut-and-carry/ zero grazing: '
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'improved_pasture_comment',
                        'mapping_prefix': 'Improved pastures: '
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'mixed_comment',
                        'mapping_prefix': 'Mixed: (eg agro-pastoralism, silvo-pastoralism): '
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_8_9_2',
                                'wocat_column': 'other12_specify',
                            },
                            {
                                'wocat_table': 'qt_2_8_9_2',
                                'wocat_column': 'other12_comment'
                            }
                        ],
                        'value_prefix': 'Other grazingland: ',
                        'type': 'string',
                        'composite': {
                            'type': 'merge',
                        },
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_8_9_2',
                                'wocat_column': 'other22_specify',
                            },
                            {
                                'wocat_table': 'qt_2_8_9_2',
                                'wocat_column': 'other22_comment'
                            }
                        ],
                        'value_prefix': 'Other grazingland: ',
                        'type': 'string',
                        'composite': {
                            'type': 'merge',
                        },
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_8_9_2',
                                'wocat_column': 'other32_specify',
                            },
                            {
                                'wocat_table': 'qt_2_8_9_2',
                                'wocat_column': 'other32_comment'
                            }
                        ],
                        'value_prefix': 'Other grazingland: ',
                        'type': 'string',
                        'composite': {
                            'type': 'merge',
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_8_9_2',
                                'wocat_column': 'other42_specify',
                            },
                            {
                                'wocat_table': 'qt_2_8_9_2',
                                'wocat_column': 'other42_comment'
                            }
                        ],
                        'value_prefix': 'Other grazingland: ',
                        'type': 'string',
                        'composite': {
                            'type': 'merge',
                        }
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'comments',
                        'mapping_prefix': 'Grazingland comments: '
                    }
                ],
                'type': 'string',
                'composite': {
                    'type': 'merge',
                    'separator': ': '
                }
            }
        },
        'conditions': [
            {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_2_2_1',
                        'wocat_column': 'landuse_sub1'
                    },
                    {
                        'wocat_table': 'qt_2_2_2_1',
                        'wocat_column': 'landuse_sub2'
                    }
                ],
                'operator': 'contains',
                'value': 'tech_lu_grazingland',
                'value_mapping_list': LANDUSE_MAPPING
            }
        ]
    },
}

# Forest subcategories.
# Only add if main category "forest land" was selected in
# qt_2_2_2_1.landuse_sub1 or qt_2_2_2_1.landuse_sub1 (QCAT condition
# tech_qg_11). Else use comments (QCAT tech_qg_7.tech_lu_comments).
tech_qg_12 = {
    'tech_qg_12': {
        'questions': {
            'tech_lu_forest_natural': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_8_10_2',
                        'wocat_column': 'selective_felling',
                        'value_mapping': 'lu_forest_selectivefelling'
                    },
                    {
                        'wocat_table': 'qt_2_8_10_2',
                        'wocat_column': 'clear_felling',
                        'value_mapping': 'lu_forest_clearfelling'
                    },
                    {
                        'wocat_table': 'qt_2_8_10_2',
                        'wocat_column': 'shifting_cultivation',
                        'value_mapping': 'lu_forest_shiftingcultivation'
                    },
                ],
                'type': 'checkbox',
                'composite': {
                    'type': 'checkbox',
                }
            },
            'tech_lu_forest_products': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_8_10_3',
                        'wocat_column': 'timber',
                        'value_mapping': 'tech_lu_forestproducts_timber'
                    },
                    {
                        'wocat_table': 'qt_2_8_10_3',
                        'wocat_column': 'fuelwood',
                        'value_mapping': 'tech_lu_forestproducts_fuelwood'
                    },
                    {
                        'wocat_table': 'qt_2_8_10_3',
                        'wocat_column': 'fruits_nuts',
                        'value_mapping': 'tech_lu_forestproducts_fruitsnuts'
                    },
                    {
                        'wocat_table': 'qt_2_8_10_3',
                        'wocat_column': 'grazing',
                        'value_mapping': 'tech_lu_forestproducts_grazing'
                    },
                    {
                        'wocat_table': 'qt_2_8_10_3',
                        'wocat_column': 'other_forest',
                        'value_mapping': 'tech_lu_forestproducts_otherproducts'
                    },
                    {
                        'wocat_table': 'qt_2_8_10_3',
                        'wocat_column': 'nature_conservation',
                        'value_mapping': 'tech_lu_forestproducts_conservation'
                    },
                    {
                        'wocat_table': 'qt_2_8_10_3',
                        'wocat_column': 'recreation',
                        'value_mapping': 'tech_lu_forestproducts_recreation'
                    },
                    {
                        'wocat_table': 'qt_2_8_10_3',
                        'wocat_column': 'protection',
                        'value_mapping': 'tech_lu_forestproducts_hazards'
                    },
                ],
                'type': 'checkbox',
                'composite': {
                    'type': 'checkbox',
                }
            },
            'tech_lu_forest_other': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_8_10_3',
                        'wocat_column': 'other13_specify'
                    },
                    {
                        'wocat_table': 'qt_2_8_10_3',
                        'wocat_column': 'other23_specify'
                    },
                    {
                        'wocat_table': 'qt_2_8_10_3',
                        'wocat_column': 'other33_specify'
                    },
                    {
                        'wocat_table': 'qt_2_8_10_3',
                        'wocat_column': 'other43_specify'
                    },
                ],
                'type': 'string',
                'composite': {
                    'type': 'merge',
                    'separator': ', '
                }
            },
        },
        'conditions': [
            {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_2_2_1',
                        'wocat_column': 'landuse_sub1'
                    },
                    {
                        'wocat_table': 'qt_2_2_2_1',
                        'wocat_column': 'landuse_sub2'
                    }
                ],
                'operator': 'contains',
                'value': 'tech_lu_forest',
                'value_mapping_list': LANDUSE_MAPPING
            }
        ]
    },
}

# Comments for 3.2 (land use types)
tech_qg_7 = {
    'tech_qg_7': {
        'questions': {
            'tech_lu_comments': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_2_1',
                        'wocat_column': 'landuse_problem_own',
                        'mapping_prefix': 'Major land use problems (compiler’s opinion): '
                    },
                    {
                        'wocat_table': 'qt_2_2_1',
                        'wocat_column': 'landuse_problem_user',
                        'mapping_prefix': 'Major land use problems (land users’ perception): '
                    },
                    # Start of conditional mapping of grazing land information.
                    # Only add if main category "grazing land" was not
                    # specified.
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'nomadism',
                        'value_mapping': 'Yes',
                        'mapping_prefix': 'Nomadism: ',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_grazingland',
                                'value_mapping_list': LANDUSE_MAPPING
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_8_9_2',
                                        'wocat_column': 'nomadism_comment'
                                    }
                                ],
                                'operator': 'is_empty',
                            }
                        ],
                        'condition_message': 'Indications on grazing land in QT 2.8.9.2, but "grazing land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.',
                        'conditions_join': 'and'
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'nomadism_comment',
                        'mapping_prefix': 'Nomadism: ',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_grazingland',
                                'value_mapping_list': LANDUSE_MAPPING
                            }
                        ],
                        'condition_message': 'Indications on grazing land in QT 2.8.9.2, but "grazing land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.'
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'semi_nomadism',
                        'value_mapping': 'Yes',
                        'mapping_prefix': 'Semi-nomadism / pastoralism: ',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_grazingland',
                                'value_mapping_list': LANDUSE_MAPPING
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_8_9_2',
                                        'wocat_column': 'semi_nomadism_comment'
                                    }
                                ],
                                'operator': 'is_empty',
                            }
                        ],
                        'condition_message': 'Indications on grazing land in QT 2.8.9.2, but "grazing land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.',
                        'conditions_join': 'and'
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'semi_nomadism_comment',
                        'mapping_prefix': 'Semi-nomadism / pastoralism: ',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_grazingland',
                                'value_mapping_list': LANDUSE_MAPPING
                            }
                        ],
                        'condition_message': 'Indications on grazing land in QT 2.8.9.2, but "grazing land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.'
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'ranching',
                        'value_mapping': 'Yes',
                        'mapping_prefix': 'Ranching: ',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_grazingland',
                                'value_mapping_list': LANDUSE_MAPPING
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_8_9_2',
                                        'wocat_column': 'ranching_comment'
                                    }
                                ],
                                'operator': 'is_empty',
                            }
                        ],
                        'condition_message': 'Indications on grazing land in QT 2.8.9.2, but "grazing land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.',
                        'conditions_join': 'and'
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'ranching_comment',
                        'mapping_prefix': 'Ranching: ',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_grazingland',
                                'value_mapping_list': LANDUSE_MAPPING
                            }
                        ],
                        'condition_message': 'Indications on grazing land in QT 2.8.9.2, but "grazing land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.'
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'cut_carry',
                        'value_mapping': 'Yes',
                        'mapping_prefix': 'Cut-and-carry/ zero grazing: ',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_grazingland',
                                'value_mapping_list': LANDUSE_MAPPING
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_8_9_2',
                                        'wocat_column': 'cut_carry_comment'
                                    }
                                ],
                                'operator': 'is_empty',
                            }
                        ],
                        'condition_message': 'Indications on grazing land in QT 2.8.9.2, but "grazing land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.',
                        'conditions_join': 'and'
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'cut_carry_comment',
                        'mapping_prefix': 'Cut-and-carry/ zero grazing: ',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_grazingland',
                                'value_mapping_list': LANDUSE_MAPPING
                            }
                        ],
                        'condition_message': 'Indications on grazing land in QT 2.8.9.2, but "grazing land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.'
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'improved_pasture',
                        'value_mapping': 'Yes',
                        'mapping_prefix': 'Improved pasture: ',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_grazingland',
                                'value_mapping_list': LANDUSE_MAPPING
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_8_9_2',
                                        'wocat_column': 'improved_pasture_comment'
                                    }
                                ],
                                'operator': 'is_empty',
                            }
                        ],
                        'condition_message': 'Indications on grazing land in QT 2.8.9.2, but "grazing land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.',
                        'conditions_join': 'and'
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'improved_pasture_comment',
                        'mapping_prefix': 'Improved pasture: ',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_grazingland',
                                'value_mapping_list': LANDUSE_MAPPING
                            }
                        ],
                        'condition_message': 'Indications on grazing land in QT 2.8.9.2, but "grazing land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.'
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'mixed',
                        'value_mapping': 'Yes',
                        'mapping_prefix': 'Mixed: (eg agro-pastoralism, silvo-pastoralism): ',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_grazingland',
                                'value_mapping_list': LANDUSE_MAPPING
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_8_9_2',
                                        'wocat_column': 'mixed_comment'
                                    }
                                ],
                                'operator': 'is_empty',
                            }
                        ],
                        'condition_message': 'Indications on grazing land in QT 2.8.9.2, but "grazing land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.',
                        'conditions_join': 'and'
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'mixed_comment',
                        'mapping_prefix': 'Mixed: (eg agro-pastoralism, silvo-pastoralism): ',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_grazingland',
                                'value_mapping_list': LANDUSE_MAPPING
                            }
                        ],
                        'condition_message': 'Indications on grazing land in QT 2.8.9.2, but "grazing land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.'
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_8_9_2',
                                'wocat_column': 'other12_specify',
                            },
                            {
                                'wocat_table': 'qt_2_8_9_2',
                                'wocat_column': 'other12_comment',
                            }
                        ],
                        'value_prefix': 'Other grazingland: ',
                        'type': 'string',
                        'composite': {
                            'type': 'merge',
                            'separator': ': '
                        },
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_grazingland',
                                'value_mapping_list': LANDUSE_MAPPING
                            }
                        ],
                        'condition_message': 'Indications on grazing land in QT 2.8.9.2, but "grazing land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.'
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_8_9_2',
                                'wocat_column': 'other22_specify',
                            },
                            {
                                'wocat_table': 'qt_2_8_9_2',
                                'wocat_column': 'other22_comment',
                            }
                        ],
                        'value_prefix': 'Other grazingland: ',
                        'type': 'string',
                        'composite': {
                            'type': 'merge',
                            'separator': ': '
                        },
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_grazingland',
                                'value_mapping_list': LANDUSE_MAPPING
                            }
                        ],
                        'condition_message': 'Indications on grazing land in QT 2.8.9.2, but "grazing land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.'
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_8_9_2',
                                'wocat_column': 'other32_specify',
                            },
                            {
                                'wocat_table': 'qt_2_8_9_2',
                                'wocat_column': 'other32_comment',
                            }
                        ],
                        'value_prefix': 'Other grazingland: ',
                        'type': 'string',
                        'composite': {
                            'type': 'merge',
                            'separator': ': '
                        },
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_grazingland',
                                'value_mapping_list': LANDUSE_MAPPING
                            }
                        ],
                        'condition_message': 'Indications on grazing land in QT 2.8.9.2, but "grazing land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.'
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_8_9_2',
                                'wocat_column': 'other42_specify',
                            },
                            {
                                'wocat_table': 'qt_2_8_9_2',
                                'wocat_column': 'other42_comment',
                            }
                        ],
                        'value_prefix': 'Other grazingland: ',
                        'type': 'string',
                        'composite': {
                            'type': 'merge',
                            'separator': ': '
                        },
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_grazingland',
                                'value_mapping_list': LANDUSE_MAPPING
                            }
                        ],
                        'condition_message': 'Indications on grazing land in QT 2.8.9.2, but "grazing land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.'
                    },
                    {
                        'wocat_table': 'qt_2_8_9_2',
                        'wocat_column': 'comments',
                        'mapping_prefix': 'Grazingland comments: ',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_grazingland',
                                'value_mapping_list': LANDUSE_MAPPING
                            }
                        ],
                        'condition_message': 'Indications on grazing land in QT 2.8.9.2, but "grazing land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.'
                    },
                    # End of conditional mapping of grazing land information.

                    # Start of conditional mapping of forest land information.
                    # Only add if main category "forest land" was not specified.
                    {
                        'wocat_table': 'qt_2_8_10_2',
                        'wocat_column': 'selective_felling',
                        'value_mapping': 'Yes',
                        'mapping_prefix': 'Selective felling of (semi-) natural forests: ',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_forest',
                                'value_mapping_list': LANDUSE_MAPPING
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_8_10_2',
                                        'wocat_column': 'selective_felling_comment'
                                    }
                                ],
                                'operator': 'is_empty',
                            }
                        ],
                        'condition_message': 'Indications on forest land in QT 2.8.10.2, but "forest land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.',
                        'conditions_join': 'and'
                    },
                    {
                        'wocat_table': 'qt_2_8_10_2',
                        'wocat_column': 'selective_felling_comment',
                        'mapping_prefix': 'Selective felling of (semi-) natural forests: ',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_forest',
                                'value_mapping_list': LANDUSE_MAPPING
                            }
                        ],
                        'condition_message': 'Indications on forest land in QT 2.8.10.2, but "forest land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.'
                    },
                    {
                        'wocat_table': 'qt_2_8_10_2',
                        'wocat_column': 'clear_felling',
                        'value_mapping': 'Yes',
                        'mapping_prefix': 'Clear felling of (semi-)natural forests: ',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_forest',
                                'value_mapping_list': LANDUSE_MAPPING
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_8_10_2',
                                        'wocat_column': 'clear_felling_comment'
                                    }
                                ],
                                'operator': 'is_empty',
                            }
                        ],
                        'condition_message': 'Indications on forest land in QT 2.8.10.2, but "forest land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.',
                        'conditions_join': 'and'
                    },
                    {
                        'wocat_table': 'qt_2_8_10_2',
                        'wocat_column': 'clear_felling_comment',
                        'mapping_prefix': 'Clear felling of (semi-)natural forests: ',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_forest',
                                'value_mapping_list': LANDUSE_MAPPING
                            }
                        ],
                        'condition_message': 'Indications on forest land in QT 2.8.10.2, but "forest land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.'
                    },
                    {
                        'wocat_table': 'qt_2_8_10_2',
                        'wocat_column': 'shifting_cultivation',
                        'value_mapping': 'Yes',
                        'mapping_prefix': 'Shifting cultivation: ',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_forest',
                                'value_mapping_list': LANDUSE_MAPPING
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_8_10_2',
                                        'wocat_column': 'shifting_cultivation_comment'
                                    }
                                ],
                                'operator': 'is_empty',
                            }
                        ],
                        'condition_message': 'Indications on forest land in QT 2.8.10.2, but "forest land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.',
                        'conditions_join': 'and'
                    },
                    {
                        'wocat_table': 'qt_2_8_10_2',
                        'wocat_column': 'shifting_cultivation_comment',
                        'mapping_prefix': 'Shifting cultivation: ',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_forest',
                                'value_mapping_list': LANDUSE_MAPPING
                            }
                        ],
                        'condition_message': 'Indications on forest land in QT 2.8.10.2, but "forest land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.'
                    },
                    {
                        'wocat_table': 'qt_2_8_10_2',
                        'wocat_column': 'plantation_forestry',
                        'value_mapping': 'Yes',
                        'mapping_prefix': 'Plantation forestry: ',
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_8_10_2',
                                        'wocat_column': 'plantation_forestry_comment'
                                    }
                                ],
                                'operator': 'is_empty',
                            }
                        ],
                        'condition_message': 'Plantation forestry selected in QT 2.8.10.2, but no automatic mapping to one of plantation subcategories possible in QCAT 3.2. Using comment section of QCAT 3.2 for this data.',
                    },
                    {
                        'wocat_table': 'qt_2_8_10_2',
                        'wocat_column': 'plantation_forestry_comment',
                        'mapping_prefix': 'Plantation forestry: ',
                        'mapping_message': 'Plantation forestry selected in QT 2.8.10.2, but no automatic mapping to one of plantation subcategories possible in QCAT 3.2. Using comment section of QCAT 3.2 for this data.'
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_8_10_2',
                                'wocat_column': 'other12_specify',
                            },
                            {
                                'wocat_table': 'qt_2_8_10_2',
                                'wocat_column': 'other12_comment',
                            }
                        ],
                        'value_prefix': 'Other type of forest: ',
                        'type': 'string',
                        'composite': {
                            'type': 'merge',
                            'separator': ': '
                        },
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_8_10_2',
                                'wocat_column': 'other22_specify',
                            },
                            {
                                'wocat_table': 'qt_2_8_10_2',
                                'wocat_column': 'other22_comment',
                            }
                        ],
                        'value_prefix': 'Other type of forest: ',
                        'type': 'string',
                        'composite': {
                            'type': 'merge',
                            'separator': ': '
                        },
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_8_10_2',
                                'wocat_column': 'other32_specify',
                            },
                            {
                                'wocat_table': 'qt_2_8_10_2',
                                'wocat_column': 'other32_comment',
                            }
                        ],
                        'value_prefix': 'Other type of forest: ',
                        'type': 'string',
                        'composite': {
                            'type': 'merge',
                            'separator': ': '
                        },
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_8_10_2',
                                'wocat_column': 'other42_specify',
                            },
                            {
                                'wocat_table': 'qt_2_8_10_2',
                                'wocat_column': 'other42_comment',
                            }
                        ],
                        'value_prefix': 'Other type of forest: ',
                        'type': 'string',
                        'composite': {
                            'type': 'merge',
                            'separator': ': '
                        },
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_8_10_3',
                                'wocat_column': 'timber',
                                'lookup_text': 961,
                            },
                            {
                                'wocat_table': 'qt_2_8_10_3',
                                'wocat_column': 'fuelwood',
                                'lookup_text': 962,
                            },
                            {
                                'wocat_table': 'qt_2_8_10_3',
                                'wocat_column': 'fruits_nuts',
                                'lookup_text': 963,
                            },
                            {
                                'wocat_table': 'qt_2_8_10_3',
                                'wocat_column': 'grazing',
                                'lookup_text': 964,
                            },
                            {
                                'wocat_table': 'qt_2_8_10_3',
                                'wocat_column': 'other_forest',
                                'lookup_text': 965,
                            },
                            {
                                'wocat_table': 'qt_2_8_10_3',
                                'wocat_column': 'nature_conservation',
                                'lookup_text': 966,
                            },
                            {
                                'wocat_table': 'qt_2_8_10_3',
                                'wocat_column': 'recreation',
                                'lookup_text': 967,
                            },
                            {
                                'wocat_table': 'qt_2_8_10_3',
                                'wocat_column': 'protection',
                                'lookup_text': 968,
                            },
                        ],
                        'value_prefix': 'Forest products and services: ',
                        'type': 'string',
                        'composite': {
                            'type': 'merge',
                            'separator': ', '
                        },
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_forest',
                                'value_mapping_list': LANDUSE_MAPPING
                            }
                        ],
                        'condition_message': 'Indications on forest land in QT 2.8.10.3, but "forest land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.'
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_8_10_3',
                                'wocat_column': 'other13_specify'
                            },
                            {
                                'wocat_table': 'qt_2_8_10_3',
                                'wocat_column': 'other23_specify'
                            },
                            {
                                'wocat_table': 'qt_2_8_10_3',
                                'wocat_column': 'other33_specify'
                            },
                            {
                                'wocat_table': 'qt_2_8_10_3',
                                'wocat_column': 'other43_specify'
                            },
                        ],
                        'value_prefix': 'Other forest products and services: ',
                        'type': 'string',
                        'composite': {
                            'type': 'merge',
                            'separator': ', '
                        },
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub1'
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_1',
                                        'wocat_column': 'landuse_sub2'
                                    }
                                ],
                                'operator': 'contains_not',
                                'value': 'tech_lu_forest',
                                'value_mapping_list': LANDUSE_MAPPING
                            }
                        ],
                        'condition_message': 'Indications on forest land in QT 2.8.10.3, but "forest land" not selected as land use type in QT 2.2.2.1 (QCAT 3.2). Using comment section of QCAT 3.2 for this data.'
                    },
                    # End of (conditional) mapping of forest land information.
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_2_2_1',
                                'wocat_column': 'landuse_future',
                            }
                        ],
                        'type': 'string',
                        'value_mapping_list': LANDUSE_MAPPING_VERBOSE,
                        'value_prefix': 'Future (final) land use (after implementation of SLM Technology): ',
                    }
                ],
                'type': 'string',
                'composite': {
                    'type': 'merge'
                }
            },
            'tech_lu_change': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_2_2_1',
                        'wocat_column': 'landuse_original'
                    }
                ],
                'type': 'string',
                'value_mapping_list': LANDUSE_MAPPING_VERBOSE,
            }
        }
    },
}

# 3.5 Spread of the Technology
tech_qg_4 = {
    'tech_qg_4': {
        'questions': {
            'tech_spread_tech': {
                'mapping': [
                    {
                        'wocat_table': 'qt_1',
                        'wocat_column': 'approx_area_id',
                        'value_mapping': 'tech_spread_evenly'
                    }
                ],
                'type': 'dropdown',
            },
            'tech_spread_area': {
                'mapping': [
                    {
                        'wocat_table': 'qt_1',
                        'wocat_column': 'approx_area_id',
                    }
                ],
                'type': 'dropdown',
                'value_mapping_list': SPREAD_AREA_COVERED,
            },
            'tech_spread_tech_comments': {
                'mapping': [
                    {
                        'wocat_table': 'qt_1',
                        'wocat_column': 'precice_area',
                        'mapping_prefix': 'Total area covered by the SLM Technology is ',
                        'mapping_suffix': ' m2.'
                    },
                    {
                        'wocat_table': 'qt_1',
                        'wocat_column': 'comments',
                    }
                ],
                'type': 'string',
            },
        }
    }
}

# 3.3 Water supply
tech_qg_19 = {
    'tech_qg_19': {
        'questions': {
            'tech_watersupply': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_8_8_4',
                        'wocat_column': 'rainfed',
                        'value_mapping': 'tech_watersupply_rainfed'
                    },
                    {
                        'wocat_table': 'qt_2_8_8_4',
                        'wocat_column': 'mixed',
                        'value_mapping': 'tech_watersupply_mixed'
                    },
                    {
                        'wocat_table': 'qt_2_8_8_4',
                        'wocat_column': 'full_irrigation',
                        'value_mapping': 'tech_watersupply_irrigation'
                    },
                    {
                        'wocat_table': 'qt_2_8_9_3',
                        'wocat_column': 'rainfed',
                        'value_mapping': 'tech_watersupply_rainfed'
                    },
                    {
                        'wocat_table': 'qt_2_8_9_3',
                        'wocat_column': 'mixed',
                        'value_mapping': 'tech_watersupply_mixed'
                    },
                    {
                        'wocat_table': 'qt_2_8_9_3',
                        'wocat_column': 'full_irrigation',
                        'value_mapping': 'tech_watersupply_irrigation'
                    },
                ],
                'type': 'dropdown',
                'conditions': [
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_8_8_4',
                                'wocat_column': 'rainfed',
                            },
                            {
                                'wocat_table': 'qt_2_8_8_4',
                                'wocat_column': 'mixed',
                            },
                            {
                                'wocat_table': 'qt_2_8_8_4',
                                'wocat_column': 'full_irrigation',
                            },
                            {
                                'wocat_table': 'qt_2_8_9_3',
                                'wocat_column': 'rainfed',
                            },
                            {
                                'wocat_table': 'qt_2_8_9_3',
                                'wocat_column': 'mixed',
                            },
                            {
                                'wocat_table': 'qt_2_8_9_3',
                                'wocat_column': 'full_irrigation',
                            },
                        ],
                        'operator': 'len_lte',
                        'value': 1,
                    }
                ],
            },
            'tech_watersupply_comments': {
                'mapping': [
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_8_8_4',
                                'wocat_column': 'rainfed',
                                'lookup_text': 895,
                            },
                            {
                                'wocat_table': 'qt_2_8_8_4',
                                'wocat_column': 'mixed',
                                'lookup_text': 897,
                            },
                            {
                                'wocat_table': 'qt_2_8_8_4',
                                'wocat_column': 'full_irrigation',
                                'lookup_text': 898,
                            },
                            {
                                'wocat_table': 'qt_2_8_9_3',
                                'wocat_column': 'rainfed',
                                'lookup_text': 895,
                            },
                            {
                                'wocat_table': 'qt_2_8_9_3',
                                'wocat_column': 'mixed',
                                'lookup_text': 897,
                            },
                            {
                                'wocat_table': 'qt_2_8_9_3',
                                'wocat_column': 'full_irrigation',
                                'lookup_text': 898,
                            },
                        ],
                        'type': 'string',
                        'value_prefix': 'Water supply: ',
                        'composite': {
                            'type': 'merge',
                            'separator': ', '
                        },
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_8_8_4',
                                        'wocat_column': 'rainfed',
                                    },
                                    {
                                        'wocat_table': 'qt_2_8_8_4',
                                        'wocat_column': 'mixed',
                                    },
                                    {
                                        'wocat_table': 'qt_2_8_8_4',
                                        'wocat_column': 'full_irrigation',
                                    },
                                    {
                                        'wocat_table': 'qt_2_8_9_3',
                                        'wocat_column': 'rainfed',
                                    },
                                    {
                                        'wocat_table': 'qt_2_8_9_3',
                                        'wocat_column': 'mixed',
                                    },
                                    {
                                        'wocat_table': 'qt_2_8_9_3',
                                        'wocat_column': 'full_irrigation',
                                    },
                                ],
                                'operator': 'len_gte',
                                'value': 2
                            }
                        ],
                        'condition_message': 'More than one value found for QCAT 3.3 Water supply (QT 2.8.8.4). Using comments in QCAT 3.3 for this data.'
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_8_8_4',
                                'wocat_column': 'post_flooding',
                                'lookup_text': 896,
                            },
                            {
                                'wocat_table': 'qt_2_8_9_3',
                                'wocat_column': 'post_flooding',
                                'lookup_text': 896,
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'Water supply: ',
                        'composite': {
                            'type': 'merge',
                        }
                    }
                ],
                'type': 'string'
            },
            'tech_growing_seasons': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_7_4',
                        'wocat_column': 'no_growing_seasons'
                    },
                ],
                'type': 'dropdown',
                'value_mapping_list': GROWING_SEASON_MAPPING,
            },
            'tech_growing_seasons_specify': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_7_4',
                        'wocat_column': 'longest_growing_season',
                        'mapping_prefix': 'Longest growing period in days: ',
                    },
                    {
                        'wocat_table': 'qt_2_7_4',
                        'wocat_column': 'longest_months',
                        'mapping_prefix': 'Longest growing period from month to month: ',
                    },
                    {
                        'wocat_table': 'qt_2_7_4',
                        'wocat_column': 'second_long_growing_season',
                        'mapping_prefix': 'Second longest growing period in days: ',
                    },
                    {
                        'wocat_table': 'qt_2_7_4',
                        'wocat_column': 'second_long_months',
                        'mapping_prefix': 'Second longest growing period from month to month: ',
                    },
                ],
                'type': 'string',
                'composite': {
                    'type': 'merge'
                }
            },
            'tech_livestock_density': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_8_9_3',
                        'wocat_column': 'livestock_density',
                        'lookup_table': True,
                    }
                ],
                'type': 'string',
            }
        }
    }
}

# 3.6 SLM measures
tech_qg_8 = {
    'tech_qg_8': {
        'questions': {
            'tech_measures': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_2_2_2_measure',
                        'wocat_column': 'measure_type',
                    }
                ],
                'type': 'checkbox',
                'composite': {
                    'type': 'checkbox'
                },
                'value_mapping_list': MEASURE_MAPPING,
            }
        }
    }
}

# 3.6 SLM measures: Agronomic
tech_qg_21 = {
    'tech_qg_21': {
        'questions': {
            'tech_measures_agronomic_sub': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_2_2_2_measure',
                        'wocat_column': 'measure',
                    }
                ],
                'type': 'checkbox',
                'composite': {
                    'type': 'checkbox',
                    'mapping': 'exclusive',
                },
                'value_mapping_list': MEASURE_AGRONOMIC_MAPPING,
            }
        }
    }
}

# 3.6 SLM measures: Vegetative
tech_qg_22 = {
    'tech_qg_22': {
        'questions': {
            'tech_measures_vegetative_sub': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_2_2_2_measure',
                        'wocat_column': 'measure',
                    }
                ],
                'type': 'checkbox',
                'composite': {
                    'type': 'checkbox',
                    'mapping': 'exclusive',
                },
                'value_mapping_list': MEASURE_VEGETATIVE_MAPPING,
            }
        }
    }
}

# 3.6 SLM measures: Structural
tech_qg_23 = {
    'tech_qg_23': {
        'questions': {
            'tech_measures_structural_sub': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_2_2_2_measure',
                        'wocat_column': 'measure',
                    }
                ],
                'type': 'checkbox',
                'composite': {
                    'type': 'checkbox',
                    'mapping': 'exclusive',
                },
                'value_mapping_list': MEASURE_STRUCTURAL_MAPPING,
            }
        }
    }
}

# 3.6 SLM measures: Management
tech_qg_24 = {
    'tech_qg_24': {
        'questions': {
            'tech_measures_management_sub': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_2_2_2_measure',
                        'wocat_column': 'measure',
                    }
                ],
                'type': 'checkbox',
                'composite': {
                    'type': 'checkbox',
                    'mapping': 'exclusive',
                },
                'value_mapping_list': MEASURE_MANAGEMENT_MAPPING,
            }
        }
    }
}

# 3.6 SLM measures: comments
tech_qg_26 = {
    'tech_qg_26': {
        'questions': {
            'tech_measures_comments': {
                'mapping': [
                    # Rank: 131
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_2_2_2',
                                'wocat_column': 'agronomic_rank',
                                'value_mapping': 'agronomic measures',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_2',
                                                'wocat_column': 'agronomic_rank',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_2',
                                'wocat_column': 'vegetative_rank',
                                'value_mapping': 'vegetative measures',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_2',
                                                'wocat_column': 'vegetative_rank',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_2',
                                'wocat_column': 'structural_rank',
                                'value_mapping': 'structural measures',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_2',
                                                'wocat_column': 'structural_rank',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_2',
                                'wocat_column': 'management_rank',
                                'value_mapping': 'management measures',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_2',
                                                'wocat_column': 'management_rank',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'Main measures: ',
                        'composite': {
                            'type': 'merge',
                            'separator': ', '
                        }
                    },
                    # Rank: 132 or 133
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_2_2_2',
                                'wocat_column': 'agronomic_rank',
                                'value_mapping': 'agronomic measures',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_2',
                                                'wocat_column': 'agronomic_rank',
                                            }
                                        ],
                                        'operator': 'contains_not',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_2',
                                'wocat_column': 'vegetative_rank',
                                'value_mapping': 'vegetative measures',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_2',
                                                'wocat_column': 'vegetative_rank',
                                            }
                                        ],
                                        'operator': 'contains_not',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_2',
                                'wocat_column': 'structural_rank',
                                'value_mapping': 'structural measures',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                    'wocat_table': 'qt_2_2_2_2',
                                                'wocat_column': 'structural_rank',
                                            }
                                        ],
                                        'operator': 'contains_not',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_2',
                                'wocat_column': 'management_rank',
                                'value_mapping': 'management measures',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_2',
                                                'wocat_column': 'management_rank',
                                            }
                                        ],
                                        'operator': 'contains_not',
                                        'value': '131'
                                    }
                                ]
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'Secondary measures: ',
                        'composite': {
                            'type': 'merge',
                            'separator': ', '
                        }
                    },
                    # Specify other agronomic measures (A5)
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_2_2_2',
                                'wocat_column': 'other1',
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'Specification of other agronomic measures: '
                    },
                    # Specify other vegetative measures (V4)
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_2_2_2',
                                'wocat_column': 'other2',
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'Specification of other vegetative measures: '
                    },
                    # Specify other structural measures (S9)
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_2_2_2',
                                'wocat_column': 'other3',
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'Specification of other structural measures: '
                    },
                    # Specify other management measures (M7)
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_2_2_2',
                                'wocat_column': 'other4',
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'Specification of other management measures: '
                    },
                    # Type and layout of agronomic measures
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'better_crop_cover',
                                'lookup_text': 483
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'early_planting',
                                'lookup_text': 484
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'relay_cropping',
                                'lookup_text': 485
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'mixed_cropping',
                                'lookup_text': 486
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'contour_planting',
                                'lookup_text': 487
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'cover_cropping',
                                'lookup_text': 488
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'retaining_cover',
                                'lookup_text': 489
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'mulching',
                                'lookup_text': 490
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'temp_trashlines',
                                'lookup_text': 491
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'green_manure',
                                'lookup_text': 493
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'legume',
                                'lookup_text': 494
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'manure',
                                'lookup_text': 495
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'mineral',
                                'lookup_text': 496
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'conditioners',
                                'lookup_text': 497
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'rotations',
                                'lookup_text': 498
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'breaking_crust',
                                'lookup_text': 500
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'breaking_topsoil',
                                'lookup_text': 501
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'zero_tillage',
                                'lookup_text': 502
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'minimum_tillage',
                                'lookup_text': 503
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'non_tillage',
                                'lookup_text': 504
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'contour_tillage',
                                'lookup_text': 505
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'contour_ridging',
                                'lookup_text': 506
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'furrows',
                                'lookup_text': 507
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'pits',
                                'lookup_text': 508
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'breaking_subsoil',
                                'lookup_text': 509
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'deep_tillage',
                                'lookup_text': 510
                            },
                        ],
                        'type': 'string',
                        'value_prefix': 'Type of agronomic measures: ',
                        'composite': {
                            'type': 'merge',
                            'separator': ', '
                        }
                    },
                    # Type and alignment / layout of vegetative measures
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_contour',
                                'lookup_text': 544
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_strips',
                                'lookup_text': 545
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_wind',
                                'lookup_text': 546
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_boundary',
                                'lookup_text': 547
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_linear',
                                'lookup_text': 548
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_scattered',
                                'lookup_text': 549
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_blocks',
                                'lookup_text': 550
                            },
                        ],
                        'type': 'string',
                        'value_prefix': 'Type of vegetative measures: ',
                        'composite': {
                            'type': 'merge',
                            'separator': ', '
                        }
                    }
                ],
                'type': 'string'
            }
        }
    }
}

# 3.7 Main types of land degradation
tech_qg_27 = {
    'tech_qg_27': {
        'questions': {
            'tech_degradation': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_2_2_4',
                        'wocat_column': 'degradation',
                    }
                ],
                'type': 'checkbox',
                'composite': {
                    'type': 'checkbox',
                },
                'value_mapping_list': DEGRADATION_TYPE_MAPPING,
            }
        }
    }
}

# 3.7 Main type of land degradation: Water erosion
tech_qg_28 = {
    'tech_qg_28': {
        'questions': {
            'degradation_erosion_water_sub': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_2_2_4',
                        'wocat_column': 'degradation',
                    }
                ],
                'type': 'checkbox',
                'composite': {
                    'type': 'checkbox',
                    'mapping': 'exclusive',
                },
                'value_mapping_list': DEGRADATION_TYPE_MAPPING_WATER_EROSION,
            }
        }
    }
}

# 3.7 Main type of land degradation: Wind erosion
tech_qg_29 = {
    'tech_qg_29': {
        'questions': {
            'degradation_erosion_wind_sub': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_2_2_4',
                        'wocat_column': 'degradation',
                    }
                ],
                'type': 'checkbox',
                'composite': {
                    'type': 'checkbox',
                    'mapping': 'exclusive',
                },
                'value_mapping_list': DEGRADATION_TYPE_MAPPING_WIND_EROSION,
            }
        }
    }
}

# 3.7 Main type of land degradation: Chemical
tech_qg_30 = {
    'tech_qg_30': {
        'questions': {
            'degradation_chemical_sub': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_2_2_4',
                        'wocat_column': 'degradation',
                    }
                ],
                'type': 'checkbox',
                'composite': {
                    'type': 'checkbox',
                    'mapping': 'exclusive',
                },
                'value_mapping_list': DEGRADATION_TYPE_MAPPING_CHEMICAL,
            }
        }
    }
}

# 3.7 Main type of land degradation: Physical
tech_qg_31 = {
    'tech_qg_31': {
        'questions': {
            'degradation_physical_sub': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_2_2_4',
                        'wocat_column': 'degradation',
                    }
                ],
                'type': 'checkbox',
                'composite': {
                    'type': 'checkbox',
                    'mapping': 'exclusive',
                },
                'value_mapping_list': DEGRADATION_TYPE_MAPPING_PHYSICAL,
            }
        }
    }
}

# 3.7 Main type of land degradation: Biological
tech_qg_32 = {
    'tech_qg_32': {
        'questions': {
            'degradation_biological_sub': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_2_2_4',
                        'wocat_column': 'degradation',
                    }
                ],
                'type': 'checkbox',
                'composite': {
                    'type': 'checkbox',
                    'mapping': 'exclusive',
                },
                'value_mapping_list': DEGRADATION_TYPE_MAPPING_BIOLOGICAL,
            }
        }
    }
}

# 3.7 Main type of land degradation: Water
tech_qg_33 = {
    'tech_qg_33': {
        'questions': {
            'degradation_water_sub': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_2_2_4',
                        'wocat_column': 'degradation',
                    }
                ],
                'type': 'checkbox',
                'composite': {
                    'type': 'checkbox',
                    'mapping': 'exclusive',
                },
                'value_mapping_list': DEGRADATION_TYPE_MAPPING_WATER,
            }
        }
    }
}

# 3.7 Main type of land degradation: Comments
tech_qg_34 = {
    'tech_qg_34': {
        'questions': {
            'degradation_comments': {
                'mapping': [
                    # Rank: 131
                    {
                        'mapping': [
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 165,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [165],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 166,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [166],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 167,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [167],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 168,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [168],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 169,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [169],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 170,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [170],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 171,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [171],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 172,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [172],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 173,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [173],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 174,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [174],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 175,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [175],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 176,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [176],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 177,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [177],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 178,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [178],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 179,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [179],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 180,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [180],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 181,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [181],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 182,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [182],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 183,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [183],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 184,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [184],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 185,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [185],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 186,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [186],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 187,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [187],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 188,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [188],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 189,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [189],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 190,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [190],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 191,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [191],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 192,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [192],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 193,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [193],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 194,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [194],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 195,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [131],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [195],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                        ],
                        'type': 'string',
                        'value_prefix': 'Main type of degradation addressed: ',
                        'composite': {
                            'type': 'merge',
                            'separator': ', '
                        }
                    },
                    # Rank: 132 or 133
                    {
                        'mapping': [
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 165,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [165],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 166,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [166],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 167,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [167],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 168,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [168],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 169,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [169],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 170,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [170],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 171,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [171],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 172,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [172],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 173,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [173],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 174,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [174],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 175,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [175],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 176,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [176],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 177,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [177],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 178,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [178],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 179,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [179],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 180,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [180],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 181,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [181],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 182,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [182],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 183,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [183],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 184,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [184],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 185,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [185],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 186,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [186],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 187,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [187],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 188,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [188],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 189,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [189],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 190,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [190],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 191,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [191],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 192,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [192],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 193,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [193],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 194,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [194],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                            {
                                # Using a table/column which appears only 1x.
                                'wocat_table': 'qt_questionnaire_info',
                                'wocat_column': 'qt_id',
                                'value_mapping': 195,
                                'lookup_table': True,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_4',
                                            },
                                        ],
                                        'operator': 'custom',
                                        'custom': [
                                            {
                                                'key': 'rank',
                                                'value': [132, 133],
                                                'operator': 'one_of',
                                            },
                                            {
                                                'key': 'degradation',
                                                'value': [195],
                                                'operator': 'one_of',
                                            }
                                        ]
                                    },
                                ]
                            },
                        ],
                        'type': 'string',
                        'value_prefix': 'Secondary types of degradation addressed: ',
                        'composite': {
                            'type': 'merge',
                            'separator': ', '
                        }
                    },
                    # QT 2.2.2.5: Main causes of land degradation
                    {
                        'mapping': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'soil_management',
                                        'lookup_text': 408
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'soil_management_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'soil_management',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'crop_management',
                                        'lookup_text': 409
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'crop_management_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'crop_management',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'deforestation',
                                        'lookup_text': 410
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'deforestation_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'deforestation',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'domestic_use',
                                        'lookup_text': 411
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'domestic_use_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'domestic_use',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'overgrazing',
                                        'lookup_text': 412
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'overgrazing_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'overgrazing',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'industrial',
                                        'lookup_text': 413
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'industrial_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'industrial',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'urbanisation',
                                        'lookup_text': 414
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'urbanisation_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'urbanisation',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'discharges',
                                        'lookup_text': 415
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'discharges_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'discharges',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'airborne_pollutants',
                                        'lookup_text': 416
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'airborne_pollutants_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'airborne_pollutants',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'disturbance_water_cycle',
                                        'lookup_text': 417
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'disturbance_water_cycle_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'disturbance_water_cycle',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'over_abstraction',
                                        'lookup_text': 418
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'over_abstraction_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'over_abstraction',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other_human',
                                        'lookup_text': 419
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other_human_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'other_human',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'temperature_change',
                                        'lookup_text': 420
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'temperature_change_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'temperature_change',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'rainfall_change',
                                        'lookup_text': 421
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'rainfall_change_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'rainfall_change',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'heavy_rainfall',
                                        'lookup_text': 422
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'heavy_rainfall_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'heavy_rainfall',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'wind_storms',
                                        'lookup_text': 423
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'wind_storms_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'wind_storms',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'floods',
                                        'lookup_text': 424
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'floods_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'floods',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'droughts',
                                        'lookup_text': 425
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'droughts_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'droughts',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other_natural',
                                        'lookup_text': 426
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other_natural_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'other_natural',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'population',
                                        'lookup_text': 427
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'population_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'population',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'land_tenure',
                                        'lookup_text': 428
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'land_tenure_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'land_tenure',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'poverty_wealth',
                                        'lookup_text': 429
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'poverty_wealth_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'poverty_wealth',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'labour',
                                        'lookup_text': 430
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'labour_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'labour',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'infrastructure',
                                        'lookup_text': 431
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'infrastructure_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'infrastructure',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'education',
                                        'lookup_text': 432
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'education_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'education',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'war',
                                        'lookup_text': 433
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'war_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'war',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'governance',
                                        'lookup_text': 434
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'governance_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'governance',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other1_description',
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other1_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'other1',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other2_description',
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other2_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'other2',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other3_description',
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other3_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'other3',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other4_description',
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other4_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'other4',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                        ],
                        'type': 'string',
                        'value_prefix': 'Main causes of degradation: ',
                        'composite': {
                            'type': 'merge',
                            'separator': ', '
                        }
                    },
                    # QT 2.2.2.5: Secondary causes of land degradation
                    {
                        'mapping': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'soil_management',
                                        'lookup_text': 408,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'soil_management_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'soil_management',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'crop_management',
                                        'lookup_text': 409,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'crop_management_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'crop_management',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'deforestation',
                                        'lookup_text': 410,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'deforestation_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'deforestation',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'domestic_use',
                                        'lookup_text': 411,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'domestic_use_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'domestic_use',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'overgrazing',
                                        'lookup_text': 412,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'overgrazing_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'overgrazing',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'industrial',
                                        'lookup_text': 413,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'industrial_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'industrial',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'urbanisation',
                                        'lookup_text': 414,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'urbanisation_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'urbanisation',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'discharges',
                                        'lookup_text': 415,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'discharges_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'discharges',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'airborne_pollutants',
                                        'lookup_text': 416,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'airborne_pollutants_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'airborne_pollutants',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'disturbance_water_cycle',
                                        'lookup_text': 417,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'disturbance_water_cycle_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'disturbance_water_cycle',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'over_abstraction',
                                        'lookup_text': 418,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'over_abstraction_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'over_abstraction',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other_human',
                                        'lookup_text': 419,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other_human_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'other_human',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'temperature_change',
                                        'lookup_text': 420,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'temperature_change_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'temperature_change',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'rainfall_change',
                                        'lookup_text': 421,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'rainfall_change_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'rainfall_change',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'heavy_rainfall',
                                        'lookup_text': 422,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'heavy_rainfall_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'heavy_rainfall',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'wind_storms',
                                        'lookup_text': 423,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'wind_storms_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'wind_storms',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'floods',
                                        'lookup_text': 424,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'floods_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'floods',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'droughts',
                                        'lookup_text': 425,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'droughts_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'droughts',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other_natural',
                                        'lookup_text': 426,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other_natural_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'other_natural',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'population',
                                        'lookup_text': 427,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'population_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'population',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'land_tenure',
                                        'lookup_text': 428,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'land_tenure_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'land_tenure',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'poverty_wealth',
                                        'lookup_text': 429,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'poverty_wealth_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'poverty_wealth',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'labour',
                                        'lookup_text': 430,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'labour_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'labour',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'infrastructure',
                                        'lookup_text': 431,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'infrastructure_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'infrastructure',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'education',
                                        'lookup_text': 432,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'education_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'education',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'war',
                                        'lookup_text': 433,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'war_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'war',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'governance',
                                        'lookup_text': 434,
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'governance_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'governance',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other1_description',
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other1_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'other1',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other2_description',
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other2_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'other2',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other3_description',
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other3_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'other3',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other4_description',
                                    },
                                    {
                                        'wocat_table': 'qt_2_2_2_5',
                                        'wocat_column': 'other4_specify',
                                        'mapping_prefix': '(',
                                        'mapping_suffix': ')',
                                    }
                                ],
                                'composite': {
                                    'type': 'merge',
                                    'separator': ' ',
                                },
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_5',
                                                'wocat_column': 'other4',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                        ],
                        'type': 'string',
                        'value_prefix': 'Secondary causes of degradation: ',
                        'composite': {
                            'type': 'merge',
                            'separator': ', '
                        }
                    },
                ],
                'type': 'string',
            }
        }
    }
}

# 3.8 Prevention of land degradation
tech_qg_35 = {
    'tech_qg_35': {
        'questions': {
            'tech_prevention': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_2_2_3',
                        'wocat_column': 'prevention_rank',
                        'value_mapping': 'intervention_prevent_ld',
                    },
                    {
                        'wocat_table': 'qt_2_2_2_3',
                        'wocat_column': 'mitigation_rank',
                        'value_mapping': 'intervention_reduce_ld',
                    },
                    {
                        'wocat_table': 'qt_2_2_2_3',
                        'wocat_column': 'rehabilitation_rank',
                        'value_mapping': 'intervention_rehabilitate',
                    },
                ],
                'type': 'checkbox',
                'composite': {
                    'type': 'checkbox',
                },
                'conditions': [
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_2_2_3',
                                'wocat_column': 'prevention_rank',
                                'value_mapping': 'intervention_prevent_ld',
                            },
                            {
                                'wocat_table': 'qt_2_2_2_3',
                                'wocat_column': 'mitigation_rank',
                                'value_mapping': 'intervention_reduce_ld',
                            },
                            {
                                'wocat_table': 'qt_2_2_2_3',
                                'wocat_column': 'rehabilitation_rank',
                                'value_mapping': 'intervention_rehabilitate',
                            },
                        ],
                        'operator': 'len_lte',
                        'value': 2
                    }
                ],
                'condition_message_opposite': 'Too many values for checkbox 3.8 "Prevention, reduction or restoration of land degradation".'
            },
            'tech_prevention_comments': {
                'mapping': [
                    # Rank: 131
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_2_2_3',
                                'wocat_column': 'prevention_rank',
                                'value_mapping': 'prevention of land degradation',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_3',
                                                'wocat_column': 'prevention_rank',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_3',
                                'wocat_column': 'mitigation_rank',
                                'value_mapping': 'mitigation / reduction of land degradation',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_3',
                                                'wocat_column': 'mitigation_rank',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_3',
                                'wocat_column': 'rehabilitation_rank',
                                'value_mapping': 'rehabilitation / reclamation of denuded land',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_3',
                                                'wocat_column': 'rehabilitation_rank',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                        ],
                        'type': 'string',
                        'value_prefix': 'Main goals: ',
                        'composite': {
                            'type': 'merge',
                            'separator': ', '
                        }
                    },
                    # Rank: 132 or 133
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_2_2_3',
                                'wocat_column': 'prevention_rank',
                                'value_mapping': 'prevention of land degradation',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_3',
                                                'wocat_column': 'prevention_rank',
                                            }
                                        ],
                                        'operator': 'contains_not',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_3',
                                'wocat_column': 'mitigation_rank',
                                'value_mapping': 'mitigation / reduction of land degradation',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_3',
                                                'wocat_column': 'mitigation_rank',
                                            }
                                        ],
                                        'operator': 'contains_not',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_3',
                                'wocat_column': 'rehabilitation_rank',
                                'value_mapping': 'rehabilitation / reclamation of denuded land',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_3',
                                                'wocat_column': 'rehabilitation_rank',
                                            }
                                        ],
                                        'operator': 'contains_not',
                                        'value': '131'
                                    }
                                ]
                            },
                        ],
                        'type': 'string',
                        'value_prefix': 'Secondary goals: ',
                        'composite': {
                            'type': 'merge',
                            'separator': ', '
                        }
                    },
                ],
                'type': 'string',
            }
        }
    }
}

# 4.1 Technical drawing
tech_qg_185 = {
    'tech_qg_185': {
        'questions': {
            'tech_drawing': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_4',
                        'wocat_column': 'blob_id',
                    }
                ],
                'type': 'file'
            },
            'tech_drawing_author': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_4',
                        'wocat_column': 'author'
                    },
                    {
                        'wocat_table': 'qt_2_4',
                        'wocat_column': 'address'
                    }
                ],
                'type': 'string',
                'composite': {
                    'type': 'merge',
                    'separator': ', '
                }
            },
        }
    }
}

# 4.2: Technical specifications/ explanations of technical drawing
tech_qg_161 = {
    'tech_qg_161': {
        'questions': {
            'tech_specifications': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_4',
                        'wocat_column': 'description',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_4',
                                'wocat_column': 'location',
                                'mapping_prefix': 'Location: '
                            },
                            {
                                'wocat_table': 'qt_2_4',
                                'wocat_column': 'area'
                            }
                        ],
                        'composite': {
                            'separator': '. '
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_4',
                                'wocat_column': 'date',
                                'mapping_prefix': 'Date: ',
                            }
                        ]
                    },
                    # What level of technical knowledge is required ...
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_3_2',
                                'wocat_column': 'advisor',
                                'lookup_table': True,
                            },
                            {
                                'wocat_table': 'qt_2_3_2',
                                'wocat_column': 'advisor_remark',
                                'mapping_prefix': '(',
                                'mapping_suffix': ')'
                            }
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': ' '
                        },
                        'value_prefix': 'Technical knowledge required for field staff / advisors: ',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_3_2',
                                'wocat_column': 'land_user',
                                'lookup_table': True,
                            },
                            {
                                'wocat_table': 'qt_2_3_2',
                                'wocat_column': 'land_user_remark',
                                'mapping_prefix': '(',
                                'mapping_suffix': ')'
                            }
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': ' '
                        },
                        'value_prefix': 'Technical knowledge required for land users: ',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_3_2',
                                'wocat_column': 'other11_description',
                                'mapping_suffix': ':'
                            },
                            {
                                'wocat_table': 'qt_2_3_2',
                                'wocat_column': 'other11',
                                'lookup_table': True,
                            },
                            {
                                'wocat_table': 'qt_2_3_2',
                                'wocat_column': 'other11_remark',
                                'mapping_prefix': '(',
                                'mapping_suffix': ')'
                            }
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': ' '
                        },
                        'value_prefix': 'Technical knowledge required for ',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_3_2',
                                'wocat_column': 'other21_description',
                                'mapping_suffix': ':'
                            },
                            {
                                'wocat_table': 'qt_2_3_2',
                                'wocat_column': 'other21',
                                'lookup_table': True,
                            },
                            {
                                'wocat_table': 'qt_2_3_2',
                                'wocat_column': 'other21_remark',
                                'mapping_prefix': '(',
                                'mapping_suffix': ')'
                            }
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': ' '
                        },
                        'value_prefix': 'Technical knowledge required for ',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_3_2',
                                'wocat_column': 'other31_description',
                                'mapping_suffix': ':'
                            },
                            {
                                'wocat_table': 'qt_2_3_2',
                                'wocat_column': 'other31',
                                'lookup_table': True,
                            },
                            {
                                'wocat_table': 'qt_2_3_2',
                                'wocat_column': 'other31_remark',
                                'mapping_prefix': '(',
                                'mapping_suffix': ')'
                            }
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': ' '
                        },
                        'value_prefix': 'Technical knowledge required for ',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_3_2',
                                'wocat_column': 'other41_description',
                                'mapping_suffix': ':'
                            },
                            {
                                'wocat_table': 'qt_2_3_2',
                                'wocat_column': 'other41',
                                'lookup_table': True,
                            },
                            {
                                'wocat_table': 'qt_2_3_2',
                                'wocat_column': 'other41_remark',
                                'mapping_prefix': '(',
                                'mapping_suffix': ')'
                            }
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': ' '
                        },
                        'value_prefix': 'Technical knowledge required for ',
                    },
                    # How ... combat LD: Rank 131
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'raindrop_splash',
                                'lookup_text': 435,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'raindrop_splash',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'dispersed_runoff_retain',
                                'lookup_text': 436,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'dispersed_runoff_retain',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'dispersed_runoff_impede',
                                'lookup_text': 437,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'dispersed_runoff_impede',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'concentrated_runoff_retain',
                                'lookup_text': 438,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'concentrated_runoff_retain',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'concentrated_runoff_impede',
                                'lookup_text': 439,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'concentrated_runoff_impede',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'concentrated_runoff_drain',
                                'lookup_text': 440,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'concentrated_runoff_drain',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'slope_angle',
                                'lookup_text': 441,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'slope_angle',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'slope_length',
                                'lookup_text': 442,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'slope_length',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'ground_cover',
                                'lookup_text': 443,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'ground_cover',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'surface_roughness',
                                'lookup_text': 444,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'surface_roughness',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'surface_structure',
                                'lookup_text': 445,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'surface_structure',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'topsoil_structure',
                                'lookup_text': 446,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'topsoil_structure',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'subsoil_structure',
                                'lookup_text': 447,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'subsoil_structure',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'soil_stabilisation',
                                'lookup_text': 448,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'soil_stabilisation',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'organic_matter',
                                'lookup_text': 449,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'organic_matter',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'nutrient_availability',
                                'lookup_text': 450,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'nutrient_availability',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'infiltration',
                                'lookup_text': 451,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'infiltration',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'water_stored',
                                'lookup_text': 452,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'water_stored',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'groundwater_level',
                                'lookup_text': 453,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'groundwater_level',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'water_supply',
                                'lookup_text': 454,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'water_supply',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'water_spreading',
                                'lookup_text': 455,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'water_spreading',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'water_quality',
                                'lookup_text': 456,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'water_quality',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'sedement_retention',
                                'lookup_text': 457,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'sedement_retention',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'wind_speed',
                                'lookup_text': 458,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'wind_speed',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'biomass',
                                'lookup_text': 459,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'biomass',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'vegetation',
                                'lookup_text': 460,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'vegetation',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'fire_control',
                                'lookup_text': 461,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'fire_control',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'dry_material',
                                'lookup_text': 462,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'dry_material',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'land_use',
                                'lookup_text': 463,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'land_use',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'other1_specify',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'other1',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'other2_specify',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'other2',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'other3_specify',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'other3',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'other4_specify',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'other4',
                                            }
                                        ],
                                        'operator': 'contains',
                                        'value': '131'
                                    }
                                ]
                            },
                        ],
                        'type': 'string',
                        'value_prefix': 'Main technical functions: ',
                        'composite': {
                            'type': 'merge',
                            'separator': ', '
                        },
                    },
                    # How ... combat LD: Rank 132 and 133
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'raindrop_splash',
                                'lookup_text': 435,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'raindrop_splash',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'dispersed_runoff_retain',
                                'lookup_text': 436,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'dispersed_runoff_retain',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'dispersed_runoff_impede',
                                'lookup_text': 437,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'dispersed_runoff_impede',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'concentrated_runoff_retain',
                                'lookup_text': 438,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'concentrated_runoff_retain',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'concentrated_runoff_impede',
                                'lookup_text': 439,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'concentrated_runoff_impede',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'concentrated_runoff_drain',
                                'lookup_text': 440,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'concentrated_runoff_drain',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'slope_angle',
                                'lookup_text': 441,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'slope_angle',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'slope_length',
                                'lookup_text': 442,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'slope_length',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'ground_cover',
                                'lookup_text': 443,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'ground_cover',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'surface_roughness',
                                'lookup_text': 444,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'surface_roughness',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'surface_structure',
                                'lookup_text': 445,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'surface_structure',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'topsoil_structure',
                                'lookup_text': 446,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'topsoil_structure',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'subsoil_structure',
                                'lookup_text': 447,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'subsoil_structure',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'soil_stabilisation',
                                'lookup_text': 448,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'soil_stabilisation',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'organic_matter',
                                'lookup_text': 449,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'organic_matter',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'nutrient_availability',
                                'lookup_text': 450,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'nutrient_availability',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'infiltration',
                                'lookup_text': 451,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'infiltration',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'water_stored',
                                'lookup_text': 452,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'water_stored',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'groundwater_level',
                                'lookup_text': 453,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'groundwater_level',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'water_supply',
                                'lookup_text': 454,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'water_supply',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'water_spreading',
                                'lookup_text': 455,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'water_spreading',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'water_quality',
                                'lookup_text': 456,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'water_quality',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'sedement_retention',
                                'lookup_text': 457,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'sedement_retention',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'wind_speed',
                                'lookup_text': 458,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'wind_speed',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'biomass',
                                'lookup_text': 459,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'biomass',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'vegetation',
                                'lookup_text': 460,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'vegetation',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'fire_control',
                                'lookup_text': 461,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'fire_control',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'dry_material',
                                'lookup_text': 462,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'dry_material',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'land_use',
                                'lookup_text': 463,
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'land_use',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'other1_specify',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'other1',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'other2_specify',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'other2',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'other3_specify',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'other3',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_2_2_6',
                                'wocat_column': 'other4_specify',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_2_2_6',
                                                'wocat_column': 'other4',
                                            }
                                        ],
                                        'operator': 'one_of',
                                        'value': ['132', '133']
                                    }
                                ]
                            },
                        ],
                        'type': 'string',
                        'value_prefix': 'Secondary technical functions: ',
                        'composite': {
                            'type': 'merge',
                            'separator': ', '
                        },
                    },
                    # 2.5.1.1 Type and layout of agronomic measures
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'better_crop_cover_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'better_crop_cover_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'better_crop_cover_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: better crop cover\n',
                        'value_prefix': 'Better crop cover\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'early_planting_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'early_planting_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'early_planting_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: early planting\n',
                        'value_prefix': 'Early planting\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'relay_cropping_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'relay_cropping_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'relay_cropping_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: relay cropping\n',
                        'value_prefix': 'Relay cropping\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'mixed_cropping_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'mixed_cropping_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'mixed_cropping_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: mixed cropping / intercropping\n',
                        'value_prefix': 'Mixed cropping / intercropping\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'contour_planting_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'contour_planting_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'contour_planting_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: contour planting / strip cropping\n',
                        'value_prefix': 'Contour planting / strip cropping\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'cover_cropping_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'cover_cropping_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'cover_cropping_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: cover cropping\n',
                        'value_prefix': 'Cover cropping\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'retaining_cover_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'retaining_cover_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'retaining_cover_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: retaining more vegetation cover\n',
                        'value_prefix': 'Retaining more vegetation cover\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'mulching_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'mulching_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'mulching_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: mulching\n',
                        'value_prefix': 'Mulching\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'temp_trashlines_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'temp_trashlines_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'temp_trashlines_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: temporary trashlines\n',
                        'value_prefix': 'Temporary trashlines\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'vegetation_other1_description',
                                'mapping_prefix': 'Agronomic measure: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'vegetation_other1_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'vegetation_other1_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'vegetation_other1_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'vegetation_other2_description',
                                'mapping_prefix': 'Agronomic measure: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'vegetation_other2_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'vegetation_other2_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'vegetation_other2_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'vegetation_other3_description',
                                'mapping_prefix': 'Agronomic measure: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'vegetation_other3_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'vegetation_other3_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'vegetation_other3_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'vegetation_other4_description',
                                'mapping_prefix': 'Agronomic measure: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'vegetation_other4_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'vegetation_other4_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'vegetation_other4_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'green_manure_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'green_manure_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'green_manure_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: green manure\n',
                        'value_prefix': 'Green manure\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'legume_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'legume_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'legume_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: legume inter-planting\n',
                        'value_prefix': 'Legume inter-planting\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'manure_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'manure_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'manure_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: manure / compost / residues\n',
                        'value_prefix': 'Manure / compost / residues\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'mineral_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'mineral_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'mineral_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: mineral (inorganic) fertilizers\n',
                        'value_prefix': 'Mineral (inorganic) fertilizers\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'conditioners_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'conditioners_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'conditioners_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: soil conditioners (lime, gypsum)\n',
                        'value_prefix': 'Soil conditioners (lime, gypsum)\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'rotations_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'rotations_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'rotations_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: rotations / fallows\n',
                        'value_prefix': 'Rotations / fallows\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'organic_other1_description',
                                'mapping_prefix': 'Agronomic measure: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'organic_other1_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'organic_other1_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'organic_other1_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'organic_other2_description',
                                'mapping_prefix': 'Agronomic measure: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'organic_other2_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'organic_other2_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'organic_other2_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'organic_other3_description',
                                'mapping_prefix': 'Agronomic measure: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'organic_other3_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'organic_other3_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'organic_other3_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'organic_other4_description',
                                'mapping_prefix': 'Agronomic measure: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'organic_other4_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'organic_other4_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'organic_other4_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'breaking_crust_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'breaking_crust_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'breaking_crust_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: breaking crust / sealed surface\n',
                        'value_prefix': 'Breaking crust / sealed surface\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'breaking_topsoil_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'breaking_topsoil_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'breaking_topsoil_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: breaking compacted topsoil\n',
                        'value_prefix': 'Breaking compacted topsoil\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'zero_tillage_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'zero_tillage_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'zero_tillage_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: zero tillage / no-till\n',
                        'value_prefix': 'Zero tillage / no-till\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'minimum_tillage_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'minimum_tillage_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'minimum_tillage_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: minimum tillage\n',
                        'value_prefix': 'Minimum tillage\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'non_tillage_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'non_tillage_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'non_tillage_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: non-inversion tillage\n',
                        'value_prefix': 'Non-inversion tillage\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'contour_tillage_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'contour_tillage_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'contour_tillage_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: contour tillage\n',
                        'value_prefix': 'Contour tillage\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'contour_ridging_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'contour_ridging_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'contour_ridging_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: contour ridging\n',
                        'value_prefix': 'Contour ridging\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'furrows_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'furrows_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'furrows_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: furrows (drainage, irrigation)\n',
                        'value_prefix': 'Furrows (drainage, irrigation)\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'pits_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'pits_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'pits_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: pits\n',
                        'value_prefix': 'Pits\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'breaking_subsoil_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'breaking_subsoil_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'breaking_subsoil_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: breaking compacted subsoil\n',
                        'value_prefix': 'Breaking compacted subsoil\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'deep_tillage_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'deep_tillage_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'deep_tillage_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Agronomic measure: deep tillage / double digging\n',
                        'value_prefix': 'Deep tillage / double digging\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'soil_other1_description',
                                'mapping_prefix': 'Agronomic measure: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'soil_other1_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'soil_other1_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'soil_other1_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'soil_other2_description',
                                'mapping_prefix': 'Agronomic measure: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'soil_other2_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'soil_other2_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'soil_other2_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'soil_other3_description',
                                'mapping_prefix': 'Agronomic measure: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'soil_other3_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'soil_other3_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'soil_other3_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'soil_other4_description',
                                'mapping_prefix': 'Agronomic measure: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'soil_other4_material',
                                'mapping_prefix': 'Material/ species: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'soil_other4_quantity',
                                'mapping_prefix': 'Quantity/ density: '
                            },
                            {
                                'wocat_table': 'qt_2_5_1_1',
                                'wocat_column': 'soil_other4_remarks',
                                'mapping_prefix': 'Remarks: '
                            },
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    # 2.5.2.1 Type and alignment / layout of vegetative measures
                    {
                        'mapping': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                        'wocat_column': 'vegetative',
                                        'lookup_table': True,
                                        'index_filter': [
                                            {
                                                'mapping': [
                                                    {
                                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                                        'wocat_column': 'vegetative_type'
                                                    }
                                                ],
                                                'operator': 'equals',
                                                'value': '1',
                                            }
                                        ],
                                    }
                                ],
                                'type': 'string',
                                'value_prefix': 'Vegetative material: ',
                                'composite': {
                                    'separator': ', '
                                }
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_contour_no_plants',
                                'mapping_prefix': 'Number of plants per (ha): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_contour_between_interval',
                                'mapping_prefix': 'Vertical interval between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_contour_between_spacing',
                                'mapping_prefix': 'Spacing between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_contour_within_interval',
                                'mapping_prefix': 'Vertical interval within rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_contour_within_width',
                                'mapping_prefix': 'Width within rows / strips / blocks (m): '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Vegetative measure: aligned: -contour\n',
                        'value_prefix': 'Aligned: -contour\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                        'wocat_column': 'vegetative',
                                        'lookup_table': True,
                                        'index_filter': [
                                            {
                                                'mapping': [
                                                    {
                                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                                        'wocat_column': 'vegetative_type'
                                                    }
                                                ],
                                                'operator': 'equals',
                                                'value': '2',
                                            }
                                        ],
                                    }
                                ],
                                'type': 'string',
                                'value_prefix': 'Vegetative material: ',
                                'composite': {
                                    'separator': ', '
                                }
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_strips_no_plants',
                                'mapping_prefix': 'Number of plants per (ha): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_strips_between_interval',
                                'mapping_prefix': 'Vertical interval between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_strips_between_spacing',
                                'mapping_prefix': 'Spacing between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_strips_within_interval',
                                'mapping_prefix': 'Vertical interval within rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_strips_within_width',
                                'mapping_prefix': 'Width within rows / strips / blocks (m): '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Vegetative measure: aligned: -graded strips\n',
                        'value_prefix': 'Aligned: -graded strips\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                        'wocat_column': 'vegetative',
                                        'lookup_table': True,
                                        'index_filter': [
                                            {
                                                'mapping': [
                                                    {
                                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                                        'wocat_column': 'vegetative_type'
                                                    }
                                                ],
                                                'operator': 'equals',
                                                'value': '3',
                                            }
                                        ],
                                    }
                                ],
                                'type': 'string',
                                'value_prefix': 'Vegetative material: ',
                                'composite': {
                                    'separator': ', '
                                }
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_wind_no_plants',
                                'mapping_prefix': 'Number of plants per (ha): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_wind_between_interval',
                                'mapping_prefix': 'Vertical interval between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_wind_between_spacing',
                                'mapping_prefix': 'Spacing between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_wind_within_interval',
                                'mapping_prefix': 'Vertical interval within rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_wind_within_width',
                                'mapping_prefix': 'Width within rows / strips / blocks (m): '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Vegetative measure: aligned: -against wind\n',
                        'value_prefix': 'Aligned: -against wind\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                        'wocat_column': 'vegetative',
                                        'lookup_table': True,
                                        'index_filter': [
                                            {
                                                'mapping': [
                                                    {
                                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                                        'wocat_column': 'vegetative_type'
                                                    }
                                                ],
                                                'operator': 'equals',
                                                'value': '4',
                                            }
                                        ],
                                    }
                                ],
                                'type': 'string',
                                'value_prefix': 'Vegetative material: ',
                                'composite': {
                                    'separator': ', '
                                }
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_boundary_no_plants',
                                'mapping_prefix': 'Number of plants per (ha): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_boundary_between_interval',
                                'mapping_prefix': 'Vertical interval between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_boundary_between_spacing',
                                'mapping_prefix': 'Spacing between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_boundary_within_interval',
                                'mapping_prefix': 'Vertical interval within rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_boundary_within_width',
                                'mapping_prefix': 'Width within rows / strips / blocks (m): '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Vegetative measure: aligned: -along boundary\n',
                        'value_prefix': 'Aligned: -along boundary\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                        'wocat_column': 'vegetative',
                                        'lookup_table': True,
                                        'index_filter': [
                                            {
                                                'mapping': [
                                                    {
                                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                                        'wocat_column': 'vegetative_type'
                                                    }
                                                ],
                                                'operator': 'equals',
                                                'value': '5',
                                            }
                                        ],
                                    }
                                ],
                                'type': 'string',
                                'value_prefix': 'Vegetative material: ',
                                'composite': {
                                    'separator': ', '
                                }
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_linear_no_plants',
                                'mapping_prefix': 'Number of plants per (ha): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_linear_between_interval',
                                'mapping_prefix': 'Vertical interval between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_linear_between_spacing',
                                'mapping_prefix': 'Spacing between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_linear_within_interval',
                                'mapping_prefix': 'Vertical interval within rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_linear_within_width',
                                'mapping_prefix': 'Width within rows / strips / blocks (m): '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Vegetative measure: aligned: -linear\n',
                        'value_prefix': 'Aligned: -linear\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                        'wocat_column': 'vegetative',
                                        'lookup_table': True,
                                        'index_filter': [
                                            {
                                                'mapping': [
                                                    {
                                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                                        'wocat_column': 'vegetative_type'
                                                    }
                                                ],
                                                'operator': 'equals',
                                                'value': '6',
                                            }
                                        ],
                                    }
                                ],
                                'type': 'string',
                                'value_prefix': 'Vegetative material: ',
                                'composite': {
                                    'separator': ', '
                                }
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_scattered_no_plants',
                                'mapping_prefix': 'Number of plants per (ha): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_scattered_between_interval',
                                'mapping_prefix': 'Vertical interval between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_scattered_between_spacing',
                                'mapping_prefix': 'Spacing between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_scattered_within_interval',
                                'mapping_prefix': 'Vertical interval within rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_scattered_within_width',
                                'mapping_prefix': 'Width within rows / strips / blocks (m): '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Vegetative measure: scattered / dispersed\n',
                        'value_prefix': 'Scattered / dispersed\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                        'wocat_column': 'vegetative',
                                        'lookup_table': True,
                                        'index_filter': [
                                            {
                                                'mapping': [
                                                    {
                                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                                        'wocat_column': 'vegetative_type'
                                                    }
                                                ],
                                                'operator': 'equals',
                                                'value': '7',
                                            }
                                        ],
                                    }
                                ],
                                'type': 'string',
                                'value_prefix': 'Vegetative material: ',
                                'composite': {
                                    'separator': ', '
                                }
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_blocks_no_plants',
                                'mapping_prefix': 'Number of plants per (ha): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_blocks_between_interval',
                                'mapping_prefix': 'Vertical interval between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_blocks_between_spacing',
                                'mapping_prefix': 'Spacing between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_blocks_within_interval',
                                'mapping_prefix': 'Vertical interval within rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_blocks_within_width',
                                'mapping_prefix': 'Width within rows / strips / blocks (m): '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Vegetative measure: in blocks\n',
                        'value_prefix': 'In blocks\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other1',
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                        'wocat_column': 'vegetative',
                                        'lookup_table': True,
                                        'index_filter': [
                                            {
                                                'mapping': [
                                                    {
                                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                                        'wocat_column': 'vegetative_type'
                                                    }
                                                ],
                                                'operator': 'equals',
                                                'value': '8',
                                            }
                                        ],
                                    }
                                ],
                                'type': 'string',
                                'value_prefix': 'Vegetative material: ',
                                'composite': {
                                    'separator': ', '
                                }
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other1_no_plants',
                                'mapping_prefix': 'Number of plants per (ha): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other1_between_interval',
                                'mapping_prefix': 'Vertical interval between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other1_between_spacing',
                                'mapping_prefix': 'Spacing between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other1_within_interval',
                                'mapping_prefix': 'Vertical interval within rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other1_within_width',
                                'mapping_prefix': 'Width within rows / strips / blocks (m): '
                            },
                        ],
                        'type': 'string',
                        'value_prefix': 'Vegetative measure: ',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other2',
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                        'wocat_column': 'vegetative',
                                        'lookup_table': True,
                                        'index_filter': [
                                            {
                                                'mapping': [
                                                    {
                                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                                        'wocat_column': 'vegetative_type'
                                                    }
                                                ],
                                                'operator': 'equals',
                                                'value': '8',
                                            }
                                        ],
                                    }
                                ],
                                'type': 'string',
                                'value_prefix': 'Vegetative material: ',
                                'composite': {
                                    'separator': ', '
                                }
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other2_no_plants',
                                'mapping_prefix': 'Number of plants per (ha): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other2_between_interval',
                                'mapping_prefix': 'Vertical interval between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other2_between_spacing',
                                'mapping_prefix': 'Spacing between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other2_within_interval',
                                'mapping_prefix': 'Vertical interval within rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other2_within_width',
                                'mapping_prefix': 'Width within rows / strips / blocks (m): '
                            },
                        ],
                        'type': 'string',
                        'value_prefix': 'Vegetative measure: ',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other3',
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                        'wocat_column': 'vegetative',
                                        'lookup_table': True,
                                        'index_filter': [
                                            {
                                                'mapping': [
                                                    {
                                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                                        'wocat_column': 'vegetative_type'
                                                    }
                                                ],
                                                'operator': 'equals',
                                                'value': '8',
                                            }
                                        ],
                                    }
                                ],
                                'type': 'string',
                                'value_prefix': 'Vegetative material: ',
                                'composite': {
                                    'separator': ', '
                                }
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other3_no_plants',
                                'mapping_prefix': 'Number of plants per (ha): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other3_between_interval',
                                'mapping_prefix': 'Vertical interval between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other3_between_spacing',
                                'mapping_prefix': 'Spacing between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other3_within_interval',
                                'mapping_prefix': 'Vertical interval within rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other3_within_width',
                                'mapping_prefix': 'Width within rows / strips / blocks (m): '
                            },
                        ],
                        'type': 'string',
                        'value_prefix': 'Vegetative measure: ',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other4',
                            },
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                        'wocat_column': 'vegetative',
                                        'lookup_table': True,
                                        'index_filter': [
                                            {
                                                'mapping': [
                                                    {
                                                        'wocat_table': 'qt_2_5_2_1_vegetative',
                                                        'wocat_column': 'vegetative_type'
                                                    }
                                                ],
                                                'operator': 'equals',
                                                'value': '8',
                                            }
                                        ],
                                    }
                                ],
                                'type': 'string',
                                'value_prefix': 'Vegetative material: ',
                                'composite': {
                                    'separator': ', '
                                }
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other4_no_plants',
                                'mapping_prefix': 'Number of plants per (ha): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other4_between_interval',
                                'mapping_prefix': 'Vertical interval between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other4_between_spacing',
                                'mapping_prefix': 'Spacing between rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other4_within_interval',
                                'mapping_prefix': 'Vertical interval within rows / strips / blocks (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_2_1',
                                'wocat_column': 'aligned_other4_within_width',
                                'mapping_prefix': 'Width within rows / strips / blocks (m): '
                            },
                        ],
                        'type': 'string',
                        'value_prefix': 'Vegetative measure: ',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    # 2.5.2.1 Species and slope/gradient
                    {
                        'wocat_table': 'qt_2_5_2_1_1',
                        'wocat_column': 'trees',
                        'mapping_prefix': 'Trees/ shrubs species: '
                    },
                    {
                        'wocat_table': 'qt_2_5_2_1_1',
                        'wocat_column': 'fruit_trees',
                        'mapping_prefix': 'Fruit trees / shrubs species: '
                    },
                    {
                        'wocat_table': 'qt_2_5_2_1_1',
                        'wocat_column': 'crops',
                        'mapping_prefix': 'Perennial crops species: '
                    },
                    {
                        'wocat_table': 'qt_2_5_2_1_1',
                        'wocat_column': 'grass',
                        'mapping_prefix': 'Grass species: '
                    },
                    {
                        'wocat_table': 'qt_2_5_2_1_1',
                        'wocat_column': 'other',
                        'mapping_prefix': 'Other species: '
                    },
                    {
                        'wocat_table': 'qt_2_5_2_1_1',
                        'wocat_column': 'slope',
                        'mapping_prefix': 'Slope (which determines the spacing indicated above): ',
                        'mapping_suffix': '%',
                    },
                    {
                        'wocat_table': 'qt_2_5_2_1_1',
                        'wocat_column': 'slope_today',
                        'mapping_prefix': 'If the original slope has changed as a result of the Technology, the slope today is (see figure below): ',
                        'mapping_suffix': '%',
                    },
                    {
                        'wocat_table': 'qt_2_5_2_1_1',
                        'wocat_column': 'gradient',
                        'mapping_prefix': 'Gradient along the rows / strips: ',
                        'mapping_suffix': '%',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'ditch_material',
                                'mapping_prefix': 'Material: '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'ditch_interval',
                                'mapping_prefix': 'Vertical interval between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'ditch_spacing',
                                'mapping_prefix': 'Spacing between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'ditch_1_depth',
                                'mapping_prefix': 'Depth of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'ditch_1_width',
                                'mapping_prefix': 'Width of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'ditch_1_length',
                                'mapping_prefix': 'Length of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'ditch_2_height',
                                'mapping_prefix': 'Height of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'ditch_2_width',
                                'mapping_prefix': 'Width of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'ditch_2_length',
                                'mapping_prefix': 'Length of bunds/banks/others (m): '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Structural measure: diversion ditch/ drainage\n',
                        'value_prefix': 'Diversion ditch/ drainage\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'waterway_material',
                                'mapping_prefix': 'Material: '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'waterway_interval',
                                'mapping_prefix': 'Vertical interval between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'waterway_spacing',
                                'mapping_prefix': 'Spacing between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'waterway_1_depth',
                                'mapping_prefix': 'Depth of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'waterway_1_width',
                                'mapping_prefix': 'Width of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'waterway_1_length',
                                'mapping_prefix': 'Length of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'waterway_2_height',
                                'mapping_prefix': 'Height of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'waterway_2_width',
                                'mapping_prefix': 'Width of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'waterway_2_length',
                                'mapping_prefix': 'Length of bunds/banks/others (m): '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Structural measure: waterway\n',
                        'value_prefix': 'Waterway\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'spilway_material',
                                'mapping_prefix': 'Material: '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'spilway_interval',
                                'mapping_prefix': 'Vertical interval between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'spilway_spacing',
                                'mapping_prefix': 'Spacing between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'spilway_1_depth',
                                'mapping_prefix': 'Depth of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'spilway_1_width',
                                'mapping_prefix': 'Width of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'spilway_1_length',
                                'mapping_prefix': 'Length of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'spilway_2_height',
                                'mapping_prefix': 'Height of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'spilway_2_width',
                                'mapping_prefix': 'Width of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'spilway_2_length',
                                'mapping_prefix': 'Length of bunds/banks/others (m): '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Structural measure: spillway\n',
                        'value_prefix': 'Spillway\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'dam_material',
                                'mapping_prefix': 'Material: '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'dam_interval',
                                'mapping_prefix': 'Vertical interval between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'dam_spacing',
                                'mapping_prefix': 'Spacing between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'dam_1_depth',
                                'mapping_prefix': 'Depth of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'dam_1_width',
                                'mapping_prefix': 'Width of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'dam_1_length',
                                'mapping_prefix': 'Length of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'dam_2_height',
                                'mapping_prefix': 'Height of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'dam_2_width',
                                'mapping_prefix': 'Width of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'dam_2_length',
                                'mapping_prefix': 'Length of bunds/banks/others (m): '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Structural measure: dam/ pan/ pond\n',
                        'value_prefix': 'Dam/ pan/ pond\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'wall_material',
                                'mapping_prefix': 'Material: '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'wall_interval',
                                'mapping_prefix': 'Vertical interval between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'wall_spacing',
                                'mapping_prefix': 'Spacing between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'wall_1_depth',
                                'mapping_prefix': 'Depth of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'wall_1_width',
                                'mapping_prefix': 'Width of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'wall_1_length',
                                'mapping_prefix': 'Length of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'wall_2_height',
                                'mapping_prefix': 'Height of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'wall_2_width',
                                'mapping_prefix': 'Width of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'wall_2_length',
                                'mapping_prefix': 'Length of bunds/banks/others (m): '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Structural measure: wall/ barrier\n',
                        'value_prefix': 'Wall/ barrier\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'sediment_material',
                                'mapping_prefix': 'Material: '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'sediment_interval',
                                'mapping_prefix': 'Vertical interval between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'sediment_spacing',
                                'mapping_prefix': 'Spacing between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'sediment_1_depth',
                                'mapping_prefix': 'Depth of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'sediment_1_width',
                                'mapping_prefix': 'Width of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'sediment_1_length',
                                'mapping_prefix': 'Length of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'sediment_2_height',
                                'mapping_prefix': 'Height of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'sediment_2_width',
                                'mapping_prefix': 'Width of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'sediment_2_length',
                                'mapping_prefix': 'Length of bunds/banks/others (m): '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Structural measure: retention/infiltration ditch/pit, sediment/sand trap\n',
                        'value_prefix': 'Retention/infiltration ditch/pit, sediment/sand trap\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_forward_material',
                                'mapping_prefix': 'Material: '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_forward_interval',
                                'mapping_prefix': 'Vertical interval between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_forward_spacing',
                                'mapping_prefix': 'Spacing between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_forward_1_depth',
                                'mapping_prefix': 'Depth of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_forward_1_width',
                                'mapping_prefix': 'Width of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_forward_1_length',
                                'mapping_prefix': 'Length of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_forward_2_height',
                                'mapping_prefix': 'Height of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_forward_2_width',
                                'mapping_prefix': 'Width of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_forward_2_length',
                                'mapping_prefix': 'Length of bunds/banks/others (m): '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Structural measure: terrace: forward sloping\n',
                        'value_prefix': 'Terrace: forward sloping\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_bench_material',
                                'mapping_prefix': 'Material: '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_bench_interval',
                                'mapping_prefix': 'Vertical interval between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_bench_spacing',
                                'mapping_prefix': 'Spacing between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_bench_1_depth',
                                'mapping_prefix': 'Depth of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_bench_1_width',
                                'mapping_prefix': 'Width of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_bench_1_length',
                                'mapping_prefix': 'Length of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_bench_2_height',
                                'mapping_prefix': 'Height of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_bench_2_width',
                                'mapping_prefix': 'Width of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_bench_2_length',
                                'mapping_prefix': 'Length of bunds/banks/others (m): '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Structural measure: terrace: bench level\n',
                        'value_prefix': 'Terrace: bench level\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_backward_material',
                                'mapping_prefix': 'Material: '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_backward_interval',
                                'mapping_prefix': 'Vertical interval between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_backward_spacing',
                                'mapping_prefix': 'Spacing between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_backward_1_depth',
                                'mapping_prefix': 'Depth of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_backward_1_width',
                                'mapping_prefix': 'Width of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_backward_1_length',
                                'mapping_prefix': 'Length of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_backward_2_height',
                                'mapping_prefix': 'Height of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_backward_2_width',
                                'mapping_prefix': 'Width of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'terrace_backward_2_length',
                                'mapping_prefix': 'Length of bunds/banks/others (m): '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Structural measure: terrace: backward sloping\n',
                        'value_prefix': 'Terrace: backward sloping\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_level_material',
                                'mapping_prefix': 'Material: '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_level_interval',
                                'mapping_prefix': 'Vertical interval between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_level_spacing',
                                'mapping_prefix': 'Spacing between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_level_1_depth',
                                'mapping_prefix': 'Depth of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_level_1_width',
                                'mapping_prefix': 'Width of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_level_1_length',
                                'mapping_prefix': 'Length of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_level_2_height',
                                'mapping_prefix': 'Height of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_level_2_width',
                                'mapping_prefix': 'Width of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_level_2_length',
                                'mapping_prefix': 'Length of bunds/banks/others (m): '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Structural measure: bund/ bank: level\n',
                        'value_prefix': 'Bund/ bank: level\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_graded_material',
                                'mapping_prefix': 'Material: '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_graded_interval',
                                'mapping_prefix': 'Vertical interval between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_graded_spacing',
                                'mapping_prefix': 'Spacing between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_graded_1_depth',
                                'mapping_prefix': 'Depth of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_graded_1_width',
                                'mapping_prefix': 'Width of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_graded_1_length',
                                'mapping_prefix': 'Length of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_graded_2_height',
                                'mapping_prefix': 'Height of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_graded_2_width',
                                'mapping_prefix': 'Width of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_graded_2_length',
                                'mapping_prefix': 'Length of bunds/banks/others (m): '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Structural measure: bund/ bank: graded\n',
                        'value_prefix': 'Bund/ bank: graded\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_trape_material',
                                'mapping_prefix': 'Material: '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_trape_interval',
                                'mapping_prefix': 'Vertical interval between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_trape_spacing',
                                'mapping_prefix': 'Spacing between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_trape_1_depth',
                                'mapping_prefix': 'Depth of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_trape_1_width',
                                'mapping_prefix': 'Width of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_trape_1_length',
                                'mapping_prefix': 'Length of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_trape_2_height',
                                'mapping_prefix': 'Height of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_trape_2_width',
                                'mapping_prefix': 'Width of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'bunk_trape_2_length',
                                'mapping_prefix': 'Length of bunds/banks/others (m): '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Structural measure: bund/ bank: semi-circular/V shaped trapezoidal\n',
                        'value_prefix': 'Bund/ bank: semi-circular/V shaped trapezoidal\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'reshaping_material',
                                'mapping_prefix': 'Material: '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'reshaping_interval',
                                'mapping_prefix': 'Vertical interval between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'reshaping_spacing',
                                'mapping_prefix': 'Spacing between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'reshaping_1_depth',
                                'mapping_prefix': 'Depth of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'reshaping_1_width',
                                'mapping_prefix': 'Width of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'reshaping_1_length',
                                'mapping_prefix': 'Length of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'reshaping_2_height',
                                'mapping_prefix': 'Height of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'reshaping_2_width',
                                'mapping_prefix': 'Width of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'reshaping_2_length',
                                'mapping_prefix': 'Length of bunds/banks/others (m): '
                            },
                        ],
                        'type': 'string',
                        # 'value_prefix': 'Structural measure: reshaping surface\n',
                        'value_prefix': 'Reshaping surface\n',
                        'composite': {
                            'separator': '\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other1',
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other1_material',
                                'mapping_prefix': 'Material: '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other1_interval',
                                'mapping_prefix': 'Vertical interval between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other1_spacing',
                                'mapping_prefix': 'Spacing between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other1_1_depth',
                                'mapping_prefix': 'Depth of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other1_1_width',
                                'mapping_prefix': 'Width of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other1_1_length',
                                'mapping_prefix': 'Length of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other1_2_height',
                                'mapping_prefix': 'Height of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other1_2_width',
                                'mapping_prefix': 'Width of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other1_2_length',
                                'mapping_prefix': 'Length of bunds/banks/others (m): '
                            },
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': '\n'
                        },
                        'value_prefix': 'Structural measure: ',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other2',
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other2_material',
                                'mapping_prefix': 'Material: '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other2_interval',
                                'mapping_prefix': 'Vertical interval between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other2_spacing',
                                'mapping_prefix': 'Spacing between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other2_1_depth',
                                'mapping_prefix': 'Depth of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other2_1_width',
                                'mapping_prefix': 'Width of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other2_1_length',
                                'mapping_prefix': 'Length of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other2_2_height',
                                'mapping_prefix': 'Height of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other2_2_width',
                                'mapping_prefix': 'Width of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other2_2_length',
                                'mapping_prefix': 'Length of bunds/banks/others (m): '
                            },
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': '\n'
                        },
                        'value_prefix': 'Structural measure: ',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other3',
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other3_material',
                                'mapping_prefix': 'Material: '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other3_interval',
                                'mapping_prefix': 'Vertical interval between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other3_spacing',
                                'mapping_prefix': 'Spacing between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other3_1_depth',
                                'mapping_prefix': 'Depth of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other3_1_width',
                                'mapping_prefix': 'Width of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other3_1_length',
                                'mapping_prefix': 'Length of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other3_2_height',
                                'mapping_prefix': 'Height of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other3_2_width',
                                'mapping_prefix': 'Width of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other3_2_length',
                                'mapping_prefix': 'Length of bunds/banks/others (m): '
                            },
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': '\n'
                        },
                        'value_prefix': 'Structural measure: ',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other4',
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other4_material',
                                'mapping_prefix': 'Material: '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other4_interval',
                                'mapping_prefix': 'Vertical interval between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other4_spacing',
                                'mapping_prefix': 'Spacing between structures (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other4_1_depth',
                                'mapping_prefix': 'Depth of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other4_1_width',
                                'mapping_prefix': 'Width of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other4_1_length',
                                'mapping_prefix': 'Length of ditches/pits/dams (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other4_2_height',
                                'mapping_prefix': 'Height of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other4_2_width',
                                'mapping_prefix': 'Width of bunds/banks/others (m): '
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1',
                                'wocat_column': 'other4_2_length',
                                'mapping_prefix': 'Length of bunds/banks/others (m): '
                            },
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': '\n'
                        },
                        'value_prefix': 'Structural measure: ',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1_1',
                                'wocat_column': 'earth',
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'Construction material (earth): ',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1_1',
                                'wocat_column': 'stone',
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'Construction material (stone): ',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1_1',
                                'wocat_column': 'wood',
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'Construction material (wood): ',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1_1',
                                'wocat_column': 'concrete',
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'Construction material (concrete): ',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1_1',
                                'wocat_column': 'other',
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'Construction material (other): ',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1_1',
                                'wocat_column': 'slope',
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'Slope (which determines the spacing indicated above): ',
                        'value_suffix': '%',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1_1',
                                'wocat_column': 'slope_today',
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'If the original slope has changed as a result of the Technology, the slope today is: ',
                        'value_suffix': '%',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1_1',
                                'wocat_column': 'gradient',
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'Lateral gradient along the structure: ',
                        'value_suffix': '%',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1_1',
                                'wocat_column': 'capacity',
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'Specification of dams/ pans/ ponds: Capacity ',
                        'value_suffix': 'm3',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1_1',
                                'wocat_column': 'catchment_area',
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'Catchment area: ',
                        'value_suffix': 'm2',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1_1',
                                'wocat_column': 'beneficial_area',
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'Beneficial area: ',
                        'value_suffix': 'm2',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1_1',
                                'wocat_column': 'slope_dam_wall_inside',
                                'mapping_prefix': 'Slope of dam wall inside: ',
                                'mapping_suffix': '%'
                            },
                            {
                                'wocat_table': 'qt_2_5_3_1_1',
                                'wocat_column': 'slope_dam_wall_outside',
                                'mapping_prefix': 'Slope of dam wall outside: ',
                                'mapping_suffix': '%'
                            }
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': ';\n'
                        }
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1_1',
                                'wocat_column': 'dimensions_spillways',
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'Dimensions of spillways: ',
                        'value_suffix': 'm',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1_1',
                                'wocat_column': 'other_specifications',
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'Other specifications: ',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1_1',
                                'wocat_column': 'harvesting_ration',
                            }
                        ],
                        'type': 'string',
                        'value_prefix': 'For water harvesting: the ratio between the area where the harvested water is applied and the total area from which water is collected is: 1:',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_3_1_1',
                                'wocat_column': 'vegetation_used',
                                'value_mapping': 'Vegetation is used for stabilisation of structures.'
                            }
                        ],
                        'conditions': [
                            {
                                'mapping': [
                                    {
                                        'wocat_table': 'qt_2_5_3_1_1',
                                        'wocat_column': 'vegetation_used',
                                    }
                                ],
                                'operator': 'contains',
                                'value': '4',
                            },
                        ],
                        'type': 'string',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_4_1',
                                'wocat_column': 'change_land_use_type',
                                'value_mapping': 'Change of land use type',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_5_4_1',
                                                'wocat_column': 'change_land_use_type_specify',
                                            }
                                        ],
                                        'operator': 'is_empty'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_5_4_1',
                                'wocat_column': 'change_land_use_type_specify',
                                'mapping_prefix': 'Change of land use type: '
                            },
                        ],
                        'type': 'string',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_4_1',
                                'wocat_column': 'change_land_use_practices',
                                'value_mapping': 'Change of land use practices / intensity level',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_5_4_1',
                                                'wocat_column': 'change_land_use_practices_specify',
                                            }
                                        ],
                                        'operator': 'is_empty'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_5_4_1',
                                'wocat_column': 'change_land_use_practices_specify',
                                'mapping_prefix': 'Change of land use practices / intensity level: '
                            },
                        ],
                        'type': 'string',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_4_1',
                                'wocat_column': 'layout_change',
                                'value_mapping': 'Layout change according to natural and human environment',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_5_4_1',
                                                'wocat_column': 'layout_change_specify',
                                            }
                                        ],
                                        'operator': 'is_empty'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_5_4_1',
                                'wocat_column': 'layout_change_specify',
                                'mapping_prefix': 'Layout change according to natural and human environment: '
                            },
                        ],
                        'type': 'string',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_4_1',
                                'wocat_column': 'timing_changes',
                                'value_mapping': 'Major change in timing of activities',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_5_4_1',
                                                'wocat_column': 'timing_changes_specify',
                                            }
                                        ],
                                        'operator': 'is_empty'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_5_4_1',
                                'wocat_column': 'timing_changes_specify',
                                'mapping_prefix': 'Major change in timing of activities: '
                            },
                        ],
                        'type': 'string',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_4_1',
                                'wocat_column': 'change_species',
                                'value_mapping': 'Control / change of species composition',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_5_4_1',
                                                'wocat_column': 'change_species_specify',
                                            }
                                        ],
                                        'operator': 'is_empty'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_5_4_1',
                                'wocat_column': 'change_species_specify',
                                'mapping_prefix': 'Control / change of species composition: '
                            },
                        ],
                        'type': 'string',
                    },
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_4_1',
                                'wocat_column': 'other',
                                'value_mapping': 'Other type of management',
                                'conditions': [
                                    {
                                        'mapping': [
                                            {
                                                'wocat_table': 'qt_2_5_4_1',
                                                'wocat_column': 'other_specify',
                                            }
                                        ],
                                        'operator': 'is_empty'
                                    }
                                ]
                            },
                            {
                                'wocat_table': 'qt_2_5_4_1',
                                'wocat_column': 'other_specify',
                                'mapping_prefix': 'Other type of management: '
                            },
                        ],
                        'type': 'string',
                    },
                ],
                'type': 'string',
            }
        }
    }
}

# 4.4 Establishment activities
tech_qg_165 = {
    'tech_qg_165': {
        'questions': {
            'tech_est_activity': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_5_2_2_1',
                        'wocat_column': 'activity',
                        'order_value': 'v',
                    },
                    {
                        'wocat_table': 'qt_2_5_3_2_1',
                        'wocat_column': 'activity',
                        'order_value': 's',
                    },
                    {
                        'wocat_table': 'qt_2_5_4_2_1',
                        'wocat_column': 'activity',
                        'order_value': 'm',
                    },
                ],
                'type': 'string',
            },
            'tech_est_type': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_5_2_2_1',
                        'order_value': 'v',
                        'value_mapping': 'tech_est_type_v',
                    },
                    {
                        'wocat_table': 'qt_2_5_3_2_1',
                        'order_value': 's',
                        'value_mapping': 'tech_est_type_s',
                    },
                    {
                        'wocat_table': 'qt_2_5_4_2_1',
                        'order_value': 'm',
                        'value_mapping': 'tech_est_type_m',
                    },
                ],
                'type': 'dropdown'
            },
            'tech_est_timing': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_5_2_2_1',
                        'wocat_column': 'timing_frequency',
                        'order_value': 'v',
                    },
                    {
                        'wocat_table': 'qt_2_5_3_2_1',
                        'wocat_column': 'timing_frequency',
                        'order_value': 's',
                    },
                    {
                        'wocat_table': 'qt_2_5_4_2_1',
                        'wocat_column': 'timing_frequency',
                        'order_value': 'm',
                    },
                ],
                'type': 'string',
            },
        },
        'repeating_rows': True,
        'unique': True,
        'mapping_order_column': {
            'wocat_table': 'qt_2_2_2_2',
            'wocat_column': 'sort_order'
        },
        'sort_function': 'sort_by_key(k, "sort_order", none_value=1000)',
    }
}

# 4.6 Maintenance/ recurrent activities
tech_qg_43 = {
    'tech_qg_43': {
        'questions': {
            'tech_maint_activity': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_5_1_3',
                        'wocat_column': 'activity',
                        'order_value': 'a',
                    },
                    {
                        'wocat_table': 'qt_2_5_2_2_2',
                        'wocat_column': 'activity',
                        'order_value': 'v',
                    },
                    {
                        'wocat_table': 'qt_2_5_3_2_2',
                        'wocat_column': 'activity',
                        'order_value': 's',
                    },
                    {
                        'wocat_table': 'qt_2_5_4_2_2',
                        'wocat_column': 'activity',
                        'order_value': 'm',
                    },
                ],
                'type': 'string',
            },
            'tech_maint_type': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_5_1_3',
                        'order_value': 'a',
                        'value_mapping': 'tech_est_type_a',
                    },
                    {
                        'wocat_table': 'qt_2_5_2_2_2',
                        'order_value': 'v',
                        'value_mapping': 'tech_est_type_v',
                    },
                    {
                        'wocat_table': 'qt_2_5_3_2_2',
                        'order_value': 's',
                        'value_mapping': 'tech_est_type_s',
                    },
                    {
                        'wocat_table': 'qt_2_5_4_2_2',
                        'order_value': 'm',
                        'value_mapping': 'tech_est_type_m',
                    },
                ],
                'type': 'dropdown'
            },
            'tech_maint_timing': {
                'mapping': [
                    {
                        'wocat_table': 'qt_2_5_1_3',
                        'wocat_column': 'timing_frequency',
                        'order_value': 'a',
                    },
                    {
                        'wocat_table': 'qt_2_5_2_2_2',
                        'wocat_column': 'timing_frequency',
                        'order_value': 'v',
                    },
                    {
                        'wocat_table': 'qt_2_5_3_2_2',
                        'wocat_column': 'timing_frequency',
                        'order_value': 's',
                    },
                    {
                        'wocat_table': 'qt_2_5_4_2_2',
                        'wocat_column': 'timing_frequency',
                        'order_value': 'm',
                    },
                ],
                'type': 'string',
            },
        },
        'repeating_rows': True,
        'unique': True,
        'mapping_order_column': {
            'wocat_table': 'qt_2_2_2_2',
            'wocat_column': 'sort_order'
        },
        'sort_function': 'sort_by_key(k, "sort_order", none_value=1000)',
    }
}

# 4.7 Maintenance costs: Comments
tech_qg_52 = {
    'tech_qg_52': {
        'questions': {
            # 'tech_input_maint_remaining_costs': {},
            'tech_input_maint_comments': {
                'mapping': [
                    {
                        'mapping': [
                            {
                                'wocat_table': 'qt_2_5_1_3_2',
                                'wocat_column': 'machinery',
                            },
                            {
                                'wocat_table': 'qt_2_5_2_2_3',
                                'wocat_column': 'machinery',
                            },
                            {
                                'wocat_table': 'qt_2_5_3_2_3',
                                'wocat_column': 'machinery',
                            },
                            {
                                'wocat_table': 'qt_2_5_4_2_3',
                                'wocat_column': 'machinery',
                            },
                        ],
                        'type': 'string',
                        'composite': {
                            'separator': ', '
                        },
                        'value_prefix': 'Machinery/ tools: ',
                    },
                ],
                'type': 'string',
            }
        }
    }
}


questiongroups = [
    qg_name,
    qg_location,
    qg_import,
    qg_accept_conditions,
    qg_photos,
    tech_qg_1,  # Definition
    tech_qg_2,  # Description
    qg_location_map,
    tech_qg_225,  # Location comments
    tech_qg_160,  # 2.6 Date of implementation
    tech_qg_5,  # 2.7 Introduction of the Technology
    tech_qg_9,  # Land use types
    tech_qg_10,  # Land use subcategory: Cropland
    tech_qg_11,  # Land use subcategory: Grazing land
    tech_qg_12,  # Land use subcategory: Forest
    tech_qg_7,  # Land use: Comments
    tech_qg_4,  # Spread of the Technology,
    tech_qg_19,  # Water supply
    tech_qg_8,  # SLM measures
    tech_qg_21,  # SLM measures: Agronomic
    tech_qg_22,  # SLM measures: Vegetative
    tech_qg_23,  # SLM measures: Structural
    tech_qg_24,  # SLM measures: Management
    tech_qg_26,  # SLM measures: comments
    tech_qg_35,  # Prevention of land degradation
    tech_qg_27,  # Main types of land degradation
    tech_qg_28,  # Main type of land degradation: Water erosion
    tech_qg_29,  # Main type of land degradation: Wind erosion
    tech_qg_30,  # Main type of land degradation: Chemical
    tech_qg_31,  # Main type of land degradation: Physical
    tech_qg_32,  # Main type of land degradation: Biological
    tech_qg_33,  # Main type of land degradation: Water
    tech_qg_34,  # Main type of land degradation: Comments
    tech_qg_185,  # Technical drawing
    tech_qg_161,  # Technical specifications
    tech_qg_165,  # 4.4 Establishment activities
    tech_qg_43,  # 4.6 Maintenance/ recurrent activities
    tech_qg_52,  # 4.7 Maintenance costs: Comments
]

qt_mapping = {}
for qg in questiongroups:
    qt_mapping.update(qg)
