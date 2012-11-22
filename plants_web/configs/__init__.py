# -*- coding: utf-8 -*-
import os
from gettext import gettext

TEMPLATES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../templates")
LOCALE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../locale")
LOCALE_NAME = 'epistemonikos'
ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets/assets")
TANSLATED_FILES_PATH = "/home/production/translated"
LANGUAGES = [
    ('ar', 'العربية'),
	('de', 'Deutsch'),
	('en', 'English') ,
	('es', 'Español' ),
	('fr', 'Français'),
	('it', 'Italiano'),
	('nl', 'Nederlands'),  ('pt', 'Português'),
	('zh', '中文')
]
CLASSIFICATIONS = {
    "primary-study": {
        "singular": gettext("Primary Study"),
        "plural": gettext("Primary Studies")
    },
    "systematic-review": {
        "singular": gettext("Systematic Review"),
        "plural": gettext("Systematic Reviews")
    },
    "overview": {
        "singular": gettext("Overview"),
        "plural": gettext("Overviews")
    },
    "structured-summary-of-systematic-review": {
        "singular": gettext("Structured Summary"),
        "plural": gettext("Structured Summaries")
    },
    "structured-summary-of-primary-study": {
        "singular": gettext("Structured Summary"),
        "plural": gettext("Structured Summaries")
    },
    "raw": {
        "singular": "Raw Category",
        "plural": "Raw Categories"
    }
}

DOLMEN_CLASSIFICATIONS = {
    "primary-study": {
        "singular": gettext("Primary Study"),
        "plural": gettext("Primary Studies")
    },
    "systematic-review": {
        "singular": gettext("Systematic Review"),
        "plural": gettext("Systematic Reviews")
    },
    "overview": {
        "singular": gettext("Overview"),
        "plural": gettext("Overviews")
    },
    "structured-summary-of-systematic-review": {
        "singular": gettext("Structured Summary of Systematic Reviews"),
        "plural": gettext("Structured Summaries of Systematic Reviews")
    },
    "structured-summary-of-primary-study": {
        "singular": gettext("Structured Summary of Primary Studies"),
        "plural": gettext("Structured Summaries of Primary Studies")
    },
    "raw": {
        "singular": "Raw Category",
        "plural": "Raw Categories"
    }
}

TASKS = {
    "add_references": gettext("Add references"),
}

ACTIONS = {
    "document.add_classification": gettext("Add classification"),
    "document.translate": gettext("Translate"),
    "document.add_reference": gettext("Add references"),
    "document.link": gettext("Add relations"),
    "document.add_document": gettext("Add new Document"),
}

ROLES = {
    'user': gettext("User"),
    'admin': gettext("Administrator"),
    'collaborator': gettext("Collaborator"),
    'translator': gettext("Translator"),
    'system_translator': gettext("System Translator"),
    'automatic_translator': gettext("Automatic Translator"),
    'dermatology': gettext("Dermatology"),
    'geriatrics': gettext("Geriatrics"),
    'pediatrics': gettext("Pediatrics"),
    'musculoesqueletal': gettext("Musculoesqueletal Diseases"),
    'health_policy': gettext("Health Policy"),
    'ibd': gettext("IBD"),
    'myeloma': gettext("Hematology"),
    'dermatology_admin': gettext("Dermatology Admin"),
    'geriatrics_admin': gettext("Geriatrics Admin"),
    'pediatrics_admin': gettext("Pediatrics Admin"),
    'musculoesqueletal_admin': gettext("Musculoesqueletal Diseases Admin"),
    'health_policy_admin': gettext("Health Policy Admin"),
    'ibd_admin': gettext("IBD Admin"),
    'myeloma_admin': gettext("Hematology Admin"),
}

COUNTRIES =[
u'Afghanistan',
u'Åland Islands',
u'Albania',
u'Algeria',
u'American Samoa',
u'Andorra',
u'Angola',
u'Anguilla',
u'Antarctica',
u'Antigua and Barbuda',
u'Argentina',
u'Armenia',
u'Aruba',
u'Australia',
u'Austria',
u'Azerbaijan',
u'Bahamas',
u'Bahrain',
u'Bangladesh',
u'Barbados',
u'Belarus',
u'Belgium',
u'Belize',
u'Benin',
u'Bermuda',
u'Bhutan',
u'Bolivia, Plurinational State of',
u'Bonaire, Sint Eustatius and Saba',
u'Bosnia and Herzegovina',
u'Botswana',
u'Bouvet Island',
u'Brazil',
u'British Indian Ocean Territory',
u'Brunei Darussalam',
u'Bulgaria',
u'Burkina Faso',
u'Burundi',
u'Cambodia',
u'Cameroon',
u'Canada',
u'Cape Verde',
u'Cayman Islands',
u'Central African Republic',
u'Chad',
u'Chile',
u'China',
u'Christmas Island',
u'Cocos (Keeling) Islands',
u'Colombia',
u'Comoros',
u'Congo',
u'Congo, the Democratic Republic of the',
u'Cook Islands',
u'Costa Rica',
u'Côte d\'Ivoire',
u'Croatia',
u'Cuba',
u'Curaçao',
u'Cyprus',
u'Czech Republic',
u'Denmark',
u'Djibouti',
u'Dominica',
u'Dominican Republic',
u'Ecuador',
u'Egypt',
u'El Salvador',
u'Equatorial Guinea',
u'Eritrea',
u'Estonia',
u'Ethiopia',
u'Falkland Islands (Malvinas)',
u'Faroe Islands',
u'Fiji',
u'Finland',
u'France',
u'French Guiana',
u'French Polynesia',
u'French Southern Territories',
u'Gabon',
u'Gambia',
u'Georgia',
u'Germany',
u'Ghana',
u'Gibraltar',
u'Greece',
u'Greenland',
u'Grenada',
u'Guadeloupe',
u'Guam',
u'Guatemala',
u'Guernsey',
u'Guinea',
u'Guinea-Bissau',
u'Guyana',
u'Haiti',
u'Heard Island and McDonald Islands',
u'Holy See (Vatican City State)',
u'Honduras',
u'Hong Kong',
u'Hungary',
u'Iceland',
u'India',
u'Indonesia',
u'Iran, Islamic Republic of',
u'Iraq',
u'Ireland',
u'Isle of Man',
u'Israel',
u'Italy',
u'Jamaica',
u'Japan',
u'Jersey',
u'Jordan',
u'Kazakhstan',
u'Kenya',
u'Kiribati',
u'Korea, Democratic People\'s Republic of',
u'Korea, Republic of',
u'Kuwait',
u'Kyrgyzstan',
u'Lao People\'s Democratic Republic',
u'Latvia',
u'Lebanon',
u'Lesotho',
u'Liberia',
u'Libya',
u'Liechtenstein',
u'Lithuania',
u'Luxembourg',
u'Macao',
u'Macedonia, the former Yugoslav Republic of',
u'Madagascar',
u'Malawi',
u'Malaysia',
u'Maldives',
u'Mali',
u'Malta',
u'Marshall Islands',
u'Martinique',
u'Mauritania',
u'Mauritius',
u'Mayotte',
u'Mexico',
u'Micronesia, Federated States of',
u'Moldova, Republic of',
u'Monaco',
u'Mongolia',
u'Montenegro',
u'Montserrat',
u'Morocco',
u'Mozambique',
u'Myanmar',
u'Namibia',
u'Nauru',
u'Nepal',
u'Netherlands',
u'New Caledonia',
u'New Zealand',
u'Nicaragua',
u'Niger',
u'Nigeria',
u'Niue',
u'Norfolk Island',
u'Northern Mariana Islands',
u'Norway',
u'Oman',
u'Pakistan',
u'Palau',
u'Palestinian Territory, Occupied',
u'Panama',
u'Papua New Guinea',
u'Paraguay',
u'Peru',
u'Philippines',
u'Pitcairn',
u'Poland',
u'Portugal',
u'Puerto Rico',
u'Qatar',
u'Réunion',
u'Romania',
u'Russian Federation',
u'Rwanda',
u'Saint Barthélemy',
u'Saint Helena, Ascension and Tristan da Cunha',
u'Saint Kitts and Nevis',
u'Saint Lucia',
u'Saint Martin (French part)',
u'Saint Pierre and Miquelon',
u'Saint Vincent and the Grenadines',
u'Samoa',
u'San Marino',
u'Sao Tome and Principe',
u'Saudi Arabia',
u'Senegal',
u'Serbia',
u'Seychelles',
u'Sierra Leone',
u'Singapore',
u'Sint Maarten (Dutch part)',
u'Slovakia',
u'Slovenia',
u'Solomon Islands',
u'Somalia',
u'South Africa',
u'South Georgia and the South Sandwich Islands',
u'South Sudan',
u'Spain',
u'Sri Lanka',
u'Sudan',
u'Suriname',
u'Svalbard and Jan Mayen',
u'Swaziland',
u'Sweden',
u'Switzerland',
u'Syrian Arab Republic',
u'Taiwan, Province of China',
u'Tajikistan',
u'Tanzania, United Republic of',
u'Thailand',
u'Timor-Leste',
u'Togo',
u'Tokelau',
u'Tonga',
u'Trinidad and Tobago',
u'Tunisia',
u'Turkey',
u'Turkmenistan',
u'Turks and Caicos Islands',
u'Tuvalu',
u'Uganda',
u'Ukraine',
u'United Arab Emirates',
u'United Kingdom',
u'United States',
u'United States Minor Outlying Islands',
u'Uruguay',
u'Uzbekistan',
u'Vanuatu',
u'Venezuela, Bolivarian Republic of',
u'Viet Nam',
u'Virgin Islands, British',
u'Virgin Islands, U.S.',
u'Wallis and Futuna',
u'Western Sahara',
u'Yemen',
u'Zambia',
u'Zimbabwe']

EXTERNAL_LINKS = (
    ('pubmed', 'Pubmed', 'http://www.ncbi.nlm.nih.gov/pubmed/%s'),
	('dare', gettext('Publisher Site'), 'http://www.crd.york.ac.uk/CRDWeb/ShowRecord.asp?ID=%s'),
#	('cochrane', 'Cochrane Library','http://onlinelibrary.wiley.com/o/cochrane/clsysrev/articles/%s/frame.html'),
	('bireme','LILACS', 'http://bases.bireme.br/cgi-bin/wxislind.exe/iah/online/?IsisScript=iah/iah.xis&base=LILACS&lang=p&nextAction=lnk&exprSearch=%s&indexSearch=ID'),
	('doi', gettext('Publisher Site'), 'http://dx.doi.org/%s'),
    ('cochrane_espanol', gettext('Cochrane Plus'), 'http://www.bibliotecacochrane.com/BCPGetDocument.asp?DocumentID=%s'),
    ('pmc', gettext('PubMed Central'), 'http://www.ncbi.nlm.nih.gov/pmc/articles/%s/'),
)

_COUNTRY_OPTION_LIST = {'': ''}
for country in COUNTRIES:
    _COUNTRY_OPTION_LIST[country] = country

ROLES_ICONS = {
    'admin': 'admin.png',
    'collaborator': 'collaborator.png',
    'translator': 'translator.png',
    'user': 'user.png',
    'default': 'default.png'
}

METADATA = {
    'health_policy': {
        'name': 'Health Policy',
        'options': {
            '': '',
            'no': 'No',
            'yes': 'Yes',
            'maybe': 'Maybe'
        },
        'multiple': False,
        'public': False,
        'roles': ['admin', 'health_policy']
    },
    'country': {
        'name': gettext('Country'),
        'options' : _COUNTRY_OPTION_LIST,
        'multiple': True,
        'public': True
    },
    'dermatology': {
        'name': 'Dermatology',
        'options': {
            '': '',
            'no': 'No',
            'yes': 'Yes',
            'maybe': 'Maybe'
        },
        'multiple': False,
        'public': False,
        'roles': ['admin', 'dermatology']
    },
    'geriatrics': {
        'name': 'Geriatrics',
        'options': {
            '': '',
            'no': 'No',
            'yes': 'Yes',
            'maybe': 'Maybe'
        },
        'multiple': False,
        'public': False,
        'roles': ['admin', 'geriatrics']
    },
    'study_design': {
        'name': gettext('Study Design'),
        'options': {
            '': '',
            'rct': gettext('Randomized controlled trial (RCT)'),
            'nrct': gettext('Non-randomized controlled trial'),
            'its': gettext('Interrupted-time-series study (ITS)'),
            'cba': gettext('Controlled before-after (CBA) studies'),
            'other': gettext('Observational study'),
            'nc': gettext('Not clear'),
        },
        'multiple': True,
        'public': True
    },
    'musculoesqueletal': {
        'name': 'Musculoesqueletal Diseases',
        'options': {
            '': '',
            'no': 'No',
            'yes': 'Yes',
            'maybe': 'Maybe'
        },
        'multiple': False,
        'public': False,
        'roles': ['admin', 'musculoesqueletal']
    },
    'pediatrics': {
        'name': 'Pediatrics',
        'options': {
            '': '',
            'no': 'No',
            'yes': 'Yes',
            'maybe': 'Maybe'
        },
        'multiple': False,
        'public': False,
        'roles': ['admin', 'pediatrics']
    },
    'ibd': {
        'name': 'IBD',
        'options': {
            '': '',
            'no': 'No',
            'yes': 'Yes',
            'maybe': 'Maybe'
        },
        'multiple': False,
        'public': False,
        'roles': ['admin', 'ibd']
    },
    'myeloma': {
        'name': 'Hematology',
        'options': {
            '': '',
            'no': 'No',
            'yes': 'Yes',
            'maybe': 'Maybe'
        },
        'multiple': False,
        'public': False,
        'roles': ['admin', 'myeloma']
    },
    
}

SUBDOMAINS = {
    'healthsystems': {
        'host_url': 'http://www.pdq-evidence.org',
        'name': 'PDQ',
    },
    'hps-primary': {
        'host_url': 'http://hps-primary.epistemonikos.org',
        'name': 'HPSSudies',
    },
    'epistemonikos': {
        'host_url': 'http://www.epistemonikos.org',
        'name': 'Epistemonikos',
    }
}

MONTHS = [
    gettext("January"),
    gettext("February"),
	gettext("March"),
	gettext("April"),
	gettext("May"),
	gettext("June"),
	gettext("July"),
	gettext("August"),
	gettext("September"),
	gettext("October"),
	gettext("November"),
	gettext("December"),
]

CRAWLERS = [
    'Googlebot'
]

from local import SALT
