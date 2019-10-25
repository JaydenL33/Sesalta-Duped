from country import Country
from country_generator import CountryGenerator
import json

topo_data = [
    {
        "arcs": [
            [0, 1, 2, 3, 4, 5]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Afghanistan",
            "NAME_LONG": "Afghanistan",
            "ABBREV": "Afg.",
            "FORMAL_EN": "Islamic State of Afghanistan",
            "POP_EST": 34124811,
            "POP_RANK": 15,
            "GDP_MD_EST": 64080,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "AF",
            "ISO_A3": "AFG",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Southern Asia"
        }
    }, {
        "arcs": [
            [
                [6, 7, 8, 9]
            ],
            [
                [10, 11, 12]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Angola",
            "NAME_LONG": "Angola",
            "ABBREV": "Ang.",
            "FORMAL_EN": "People's Republic of Angola",
            "POP_EST": 29310273,
            "POP_RANK": 15,
            "GDP_MD_EST": 189000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "AO",
            "ISO_A3": "AGO",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Middle Africa"
        }
    }, {
        "arcs": [
            [13, 14, 15, 16, 17]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Albania",
            "NAME_LONG": "Albania",
            "ABBREV": "Alb.",
            "FORMAL_EN": "Republic of Albania",
            "POP_EST": 3047987,
            "POP_RANK": 12,
            "GDP_MD_EST": 33900,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "AL",
            "ISO_A3": "ALB",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Southern Europe"
        }
    }, {
        "arcs": [
            [18, 19, 20, 21, 22]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "United Arab Emirates",
            "NAME_LONG": "United Arab Emirates",
            "ABBREV": "U.A.E.",
            "FORMAL_EN": "United Arab Emirates",
            "POP_EST": 6072475,
            "POP_RANK": 13,
            "GDP_MD_EST": 667200,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "AE",
            "ISO_A3": "ARE",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Western Asia"
        }
    }, {
        "arcs": [
            [
                [23, 24]
            ],
            [
                [25, 26, 27, 28, 29, 30]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Argentina",
            "NAME_LONG": "Argentina",
            "ABBREV": "Arg.",
            "FORMAL_EN": "Argentine Republic",
            "POP_EST": 44293293,
            "POP_RANK": 15,
            "GDP_MD_EST": 879400,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "AR",
            "ISO_A3": "ARG",
            "CONTINENT": "South America",
            "REGION_UN": "Americas",
            "SUBREGION": "South America"
        }
    }, {
        "arcs": [
            [31, 32, 33, 34, 35]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Armenia",
            "NAME_LONG": "Armenia",
            "ABBREV": "Arm.",
            "FORMAL_EN": "Republic of Armenia",
            "POP_EST": 3045191,
            "POP_RANK": 12,
            "GDP_MD_EST": 26300,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "AM",
            "ISO_A3": "ARM",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Western Asia"
        }
    }, {
        "arcs": [
            [
                [45]
            ],
            [
                [46]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Australia",
            "NAME_LONG": "Australia",
            "ABBREV": "Auz.",
            "FORMAL_EN": "Commonwealth of Australia",
            "POP_EST": 23232413,
            "POP_RANK": 15,
            "GDP_MD_EST": 1189000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "AU",
            "ISO_A3": "AUS",
            "CONTINENT": "Oceania",
            "REGION_UN": "Oceania",
            "SUBREGION": "Australia and New Zealand"
        }
    }, {
        "arcs": [
            [47, 48, 49, 50, 51, 52, 53]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Austria",
            "NAME_LONG": "Austria",
            "ABBREV": "Aust.",
            "FORMAL_EN": "Republic of Austria",
            "POP_EST": 8754413,
            "POP_RANK": 13,
            "GDP_MD_EST": 416600,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "AT",
            "ISO_A3": "AUT",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Western Europe"
        }
    }, {
        "arcs": [
            [
                [-33, 54, 55, 56, 57]
            ],
            [
                [-35, 58]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Azerbaijan",
            "NAME_LONG": "Azerbaijan",
            "ABBREV": "Aze.",
            "FORMAL_EN": "Republic of Azerbaijan",
            "POP_EST": 9961396,
            "POP_RANK": 13,
            "GDP_MD_EST": 167900,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "AZ",
            "ISO_A3": "AZE",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Western Asia"
        }
    }, {
        "arcs": [
            [59, 60, 61]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Burundi",
            "NAME_LONG": "Burundi",
            "ABBREV": "Bur.",
            "FORMAL_EN": "Republic of Burundi",
            "POP_EST": 11466756,
            "POP_RANK": 14,
            "GDP_MD_EST": 7892,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "BI",
            "ISO_A3": "BDI",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Eastern Africa"
        }
    }, {
        "arcs": [
            [62, 63, 64, 65, 66]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Belgium",
            "NAME_LONG": "Belgium",
            "ABBREV": "Belg.",
            "FORMAL_EN": "Kingdom of Belgium",
            "POP_EST": 11491346,
            "POP_RANK": 14,
            "GDP_MD_EST": 508600,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "BE",
            "ISO_A3": "BEL",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Western Europe"
        }
    }, {
        "arcs": [
            [67, 68, 69, 70, 71]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Benin",
            "NAME_LONG": "Benin",
            "ABBREV": "Benin",
            "FORMAL_EN": "Republic of Benin",
            "POP_EST": 11038805,
            "POP_RANK": 14,
            "GDP_MD_EST": 24310,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "BJ",
            "ISO_A3": "BEN",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Western Africa"
        }
    }, {
        "arcs": [
            [-70, 72, 73, 74, 75, 76]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Burkina Faso",
            "NAME_LONG": "Burkina Faso",
            "ABBREV": "B.F.",
            "FORMAL_EN": "Burkina Faso",
            "POP_EST": 20107509,
            "POP_RANK": 15,
            "GDP_MD_EST": 32990,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "BF",
            "ISO_A3": "BFA",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Western Africa"
        }
    }, {
        "arcs": [
            [77, 78, 79]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Bangladesh",
            "NAME_LONG": "Bangladesh",
            "ABBREV": "Bang.",
            "FORMAL_EN": "People's Republic of Bangladesh",
            "POP_EST": 157826578,
            "POP_RANK": 17,
            "GDP_MD_EST": 628400,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "BD",
            "ISO_A3": "BGD",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Southern Asia"
        }
    }, {
        "arcs": [
            [80, 81, 82, 83, 84, 85]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Bulgaria",
            "NAME_LONG": "Bulgaria",
            "ABBREV": "Bulg.",
            "FORMAL_EN": "Republic of Bulgaria",
            "POP_EST": 7101510,
            "POP_RANK": 13,
            "GDP_MD_EST": 143100,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "BG",
            "ISO_A3": "BGR",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Eastern Europe"
        }
    }, {
        "arcs": [
            [
                [86]
            ],
            [
                [87]
            ],
            [
                [88]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Bahamas",
            "NAME_LONG": "Bahamas",
            "ABBREV": "Bhs.",
            "FORMAL_EN": "Commonwealth of the Bahamas",
            "POP_EST": 329988,
            "POP_RANK": 10,
            "GDP_MD_EST": 9066,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "BS",
            "ISO_A3": "BHS",
            "CONTINENT": "North America",
            "REGION_UN": "Americas",
            "SUBREGION": "Caribbean"
        }
    }, {
        "arcs": [
            [89, 90, 91]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Bosnia and Herz.",
            "NAME_LONG": "Bosnia and Herzegovina",
            "ABBREV": "B.H.",
            "FORMAL_EN": "Bosnia and Herzegovina",
            "POP_EST": 3856181,
            "POP_RANK": 12,
            "GDP_MD_EST": 42530,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "BA",
            "ISO_A3": "BIH",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Southern Europe"
        }
    }, {
        "arcs": [
            [92, 93, 94, 95, 96]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Belarus",
            "NAME_LONG": "Belarus",
            "ABBREV": "Bela.",
            "FORMAL_EN": "Republic of Belarus",
            "POP_EST": 9549747,
            "POP_RANK": 13,
            "GDP_MD_EST": 165400,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "BY",
            "ISO_A3": "BLR",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Eastern Europe"
        }
    }, {
        "arcs": [
            [97, 98, 99]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Belize",
            "NAME_LONG": "Belize",
            "ABBREV": "Belize",
            "FORMAL_EN": "Belize",
            "POP_EST": 360346,
            "POP_RANK": 10,
            "GDP_MD_EST": 3088,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "BZ",
            "ISO_A3": "BLZ",
            "CONTINENT": "North America",
            "REGION_UN": "Americas",
            "SUBREGION": "Central America"
        }
    }, {
        "arcs": [
            [-27, 100, 101, 102, 103]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Bolivia",
            "NAME_LONG": "Bolivia",
            "ABBREV": "Bolivia",
            "FORMAL_EN": "Plurinational State of Bolivia",
            "POP_EST": 11138234,
            "POP_RANK": 14,
            "GDP_MD_EST": 78350,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "BO",
            "ISO_A3": "BOL",
            "CONTINENT": "South America",
            "REGION_UN": "Americas",
            "SUBREGION": "South America"
        }
    }, {
        "arcs": [
            [-29, 104, -103, 105, 106, 107, 108, 109, 110, 111, 112]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Brazil",
            "NAME_LONG": "Brazil",
            "ABBREV": "Brazil",
            "FORMAL_EN": "Federative Republic of Brazil",
            "POP_EST": 207353391,
            "POP_RANK": 17,
            "GDP_MD_EST": 3081000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "BR",
            "ISO_A3": "BRA",
            "CONTINENT": "South America",
            "REGION_UN": "Americas",
            "SUBREGION": "South America"
        }
    }, {
        "arcs": [
            [113, 114]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Brunei",
            "NAME_LONG": "Brunei Darussalam",
            "ABBREV": "Brunei",
            "FORMAL_EN": "Negara Brunei Darussalam",
            "POP_EST": 443593,
            "POP_RANK": 10,
            "GDP_MD_EST": 33730,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "BN",
            "ISO_A3": "BRN",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "South-Eastern Asia"
        }
    }, {
        "arcs": [
            [115, 116]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Bhutan",
            "NAME_LONG": "Bhutan",
            "ABBREV": "Bhutan",
            "FORMAL_EN": "Kingdom of Bhutan",
            "POP_EST": 758288,
            "POP_RANK": 11,
            "GDP_MD_EST": 6432,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "BT",
            "ISO_A3": "BTN",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Southern Asia"
        }
    }, {
        "arcs": [
            [117, 118, 119, 120]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Botswana",
            "NAME_LONG": "Botswana",
            "ABBREV": "Bwa.",
            "FORMAL_EN": "Republic of Botswana",
            "POP_EST": 2214858,
            "POP_RANK": 12,
            "GDP_MD_EST": 35900,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "BW",
            "ISO_A3": "BWA",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Southern Africa"
        }
    }, {
        "arcs": [
            [121, 122, 123, 124, 125, 126]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Central African Rep.",
            "NAME_LONG": "Central African Republic",
            "ABBREV": "C.A.R.",
            "FORMAL_EN": "Central African Republic",
            "POP_EST": 5625118,
            "POP_RANK": 13,
            "GDP_MD_EST": 3206,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "CF",
            "ISO_A3": "CAF",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Middle Africa"
        }
    }, {
        "arcs": [
            [
                [127]
            ],
            [
                [128]
            ],
            [
                [129]
            ],
            [
                [130]
            ],
            [
                [131]
            ],
            [
                [132]
            ],
            [
                [133]
            ],
            [
                [134]
            ],
            [
                [135]
            ],
            [
                [136]
            ],
            [
                [137, 138, 139, 140]
            ],
            [
                [141]
            ],
            [
                [142]
            ],
            [
                [143]
            ],
            [
                [144]
            ],
            [
                [145]
            ],
            [
                [146]
            ],
            [
                [147]
            ],
            [
                [148]
            ],
            [
                [149]
            ],
            [
                [150]
            ],
            [
                [151]
            ],
            [
                [152]
            ],
            [
                [153]
            ],
            [
                [154]
            ],
            [
                [155]
            ],
            [
                [156]
            ],
            [
                [157]
            ],
            [
                [158]
            ],
            [
                [159]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Canada",
            "NAME_LONG": "Canada",
            "ABBREV": "Can.",
            "FORMAL_EN": "Canada",
            "POP_EST": 35623680,
            "POP_RANK": 15,
            "GDP_MD_EST": 1674000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "CA",
            "ISO_A3": "CAN",
            "CONTINENT": "North America",
            "REGION_UN": "Americas",
            "SUBREGION": "Northern America"
        }
    }, {
        "arcs": [
            [-51, 160, 161, 162]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Switzerland",
            "NAME_LONG": "Switzerland",
            "ABBREV": "Switz.",
            "FORMAL_EN": "Swiss Confederation",
            "POP_EST": 8236303,
            "POP_RANK": 13,
            "GDP_MD_EST": 496300,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "CH",
            "ISO_A3": "CHE",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Western Europe"
        }
    }, {
        "arcs": [
            [
                [-24, 163]
            ],
            [
                [-26, 164, 165, -101]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Chile",
            "NAME_LONG": "Chile",
            "ABBREV": "Chile",
            "FORMAL_EN": "Republic of Chile",
            "POP_EST": 17789267,
            "POP_RANK": 14,
            "GDP_MD_EST": 436100,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "CL",
            "ISO_A3": "CHL",
            "CONTINENT": "South America",
            "REGION_UN": "Americas",
            "SUBREGION": "South America"
        }
    }, {
        "arcs": [
            [
                [-4, 166, 167, 168, 169, 170, 171, 172, 173,
                 174, 175, 176, 177, -117, 178, 179, 180, 181]
            ],
            [
                [182]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "China",
            "NAME_LONG": "China",
            "ABBREV": "China",
            "FORMAL_EN": "People's Republic of China",
            "POP_EST": 1379302771,
            "POP_RANK": 18,
            "GDP_MD_EST": 21140000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "CN",
            "ISO_A3": "CHN",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Eastern Asia"
        }
    }, {
        "arcs": [
            [-75, 183, 184, 185, 186, 187]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Côte d'Ivoire",
            "NAME_LONG": "Côte d'Ivoire",
            "ABBREV": "I.C.",
            "FORMAL_EN": "Republic of Ivory Coast",
            "POP_EST": 24184810,
            "POP_RANK": 15,
            "GDP_MD_EST": 87120,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "CI",
            "ISO_A3": "CIV",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Western Africa"
        }
    }, {
        "arcs": [
            [-127, 188, 189, 190, 191, 192, 193, 194]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Cameroon",
            "NAME_LONG": "Cameroon",
            "ABBREV": "Cam.",
            "FORMAL_EN": "Republic of Cameroon",
            "POP_EST": 24994885,
            "POP_RANK": 15,
            "GDP_MD_EST": 77240,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "CM",
            "ISO_A3": "CMR",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Middle Africa"
        }
    }, {
        "arcs": [
            [-9, 195, -13, 196, -125, 197, 198, 199, -60, 200, 201]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Dem. Rep. Congo",
            "NAME_LONG": "Democratic Republic of the Congo",
            "ABBREV": "D.R.C.",
            "FORMAL_EN": "Democratic Republic of the Congo",
            "POP_EST": 83301151,
            "POP_RANK": 16,
            "GDP_MD_EST": 66010,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "CD",
            "ISO_A3": "COD",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Middle Africa"
        }
    }, {
        "arcs": [
            [-12, 202, 203, -189, -126, -197]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Congo",
            "NAME_LONG": "Republic of the Congo",
            "ABBREV": "Rep. Congo",
            "FORMAL_EN": "Republic of the Congo",
            "POP_EST": 4954674,
            "POP_RANK": 12,
            "GDP_MD_EST": 30270,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "CG",
            "ISO_A3": "COG",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Middle Africa"
        }
    }, {
        "arcs": [
            [-107, 204, 205, 206, 207, 208, 209]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Colombia",
            "NAME_LONG": "Colombia",
            "ABBREV": "Col.",
            "FORMAL_EN": "Republic of Colombia",
            "POP_EST": 47698524,
            "POP_RANK": 15,
            "GDP_MD_EST": 688000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "CO",
            "ISO_A3": "COL",
            "CONTINENT": "South America",
            "REGION_UN": "Americas",
            "SUBREGION": "South America"
        }
    }, {
        "arcs": [
            [210, 211, 212, 213]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Costa Rica",
            "NAME_LONG": "Costa Rica",
            "ABBREV": "C.R.",
            "FORMAL_EN": "Republic of Costa Rica",
            "POP_EST": 4930258,
            "POP_RANK": 12,
            "GDP_MD_EST": 79260,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "CR",
            "ISO_A3": "CRI",
            "CONTINENT": "North America",
            "REGION_UN": "Americas",
            "SUBREGION": "Central America"
        }
    }, {
        "arcs": [
            [214]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Cuba",
            "NAME_LONG": "Cuba",
            "ABBREV": "Cuba",
            "FORMAL_EN": "Republic of Cuba",
            "POP_EST": 11147407,
            "POP_RANK": 14,
            "GDP_MD_EST": 132900,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "CU",
            "ISO_A3": "CUB",
            "CONTINENT": "North America",
            "REGION_UN": "Americas",
            "SUBREGION": "Caribbean"
        }
    }, {
        "arcs": [
            [215, 216]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "N. Cyprus",
            "NAME_LONG": "Northern Cyprus",
            "ABBREV": "N. Cy.",
            "FORMAL_EN": "Turkish Republic of Northern Cyprus",
            "POP_EST": 265100,
            "POP_RANK": 10,
            "GDP_MD_EST": 3600,
            "POP_YEAR": 2013,
            "GDP_YEAR": 2013,
            "ISO_A2": "-99",
            "ISO_A3": "-99",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Western Asia"
        }
    }, {
        "arcs": [
            [-217, 217]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Cyprus",
            "NAME_LONG": "Cyprus",
            "ABBREV": "Cyp.",
            "FORMAL_EN": "Republic of Cyprus",
            "POP_EST": 1221549,
            "POP_RANK": 12,
            "GDP_MD_EST": 29260,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "CY",
            "ISO_A3": "CYP",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Western Asia"
        }
    }, {
        "arcs": [
            [-53, 218, 219, 220]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Czechia",
            "NAME_LONG": "Czech Republic",
            "ABBREV": "Cz.",
            "FORMAL_EN": "Czech Republic",
            "POP_EST": 10674723,
            "POP_RANK": 14,
            "GDP_MD_EST": 350900,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "CZ",
            "ISO_A3": "CZE",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Eastern Europe"
        }
    }, {
        "arcs": [
            [-52, -163, 221, 222, -63, 223, 224, 225, 226, 227, -219]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Germany",
            "NAME_LONG": "Germany",
            "ABBREV": "Ger.",
            "FORMAL_EN": "Federal Republic of Germany",
            "POP_EST": 80594017,
            "POP_RANK": 16,
            "GDP_MD_EST": 3979000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "DE",
            "ISO_A3": "DEU",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Western Europe"
        }
    }, {
        "arcs": [
            [228, 229, 230, 231]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Djibouti",
            "NAME_LONG": "Djibouti",
            "ABBREV": "Dji.",
            "FORMAL_EN": "Republic of Djibouti",
            "POP_EST": 865267,
            "POP_RANK": 11,
            "GDP_MD_EST": 3345,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "DJ",
            "ISO_A3": "DJI",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Eastern Africa"
        }
    }, {
        "arcs": [
            [
                [-226, 232]
            ],
            [
                [233]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Denmark",
            "NAME_LONG": "Denmark",
            "ABBREV": "Den.",
            "FORMAL_EN": "Kingdom of Denmark",
            "POP_EST": 5605948,
            "POP_RANK": 13,
            "GDP_MD_EST": 264800,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "DK",
            "ISO_A3": "DNK",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Northern Europe"
        }
    }, {
        "arcs": [
            [234, 235]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Dominican Rep.",
            "NAME_LONG": "Dominican Republic",
            "ABBREV": "Dom. Rep.",
            "FORMAL_EN": "Dominican Republic",
            "POP_EST": 10734247,
            "POP_RANK": 14,
            "GDP_MD_EST": 161900,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "DO",
            "ISO_A3": "DOM",
            "CONTINENT": "North America",
            "REGION_UN": "Americas",
            "SUBREGION": "Caribbean"
        }
    }, {
        "arcs": [
            [236, 237, 238, 239, 240, 241, 242, 243]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Algeria",
            "NAME_LONG": "Algeria",
            "ABBREV": "Alg.",
            "FORMAL_EN": "People's Democratic Republic of Algeria",
            "POP_EST": 40969443,
            "POP_RANK": 15,
            "GDP_MD_EST": 609400,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "DZ",
            "ISO_A3": "DZA",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Northern Africa"
        }
    }, {
        "arcs": [
            [-206, 244, 245]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Ecuador",
            "NAME_LONG": "Ecuador",
            "ABBREV": "Ecu.",
            "FORMAL_EN": "Republic of Ecuador",
            "POP_EST": 16290913,
            "POP_RANK": 14,
            "GDP_MD_EST": 182400,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "EC",
            "ISO_A3": "ECU",
            "CONTINENT": "South America",
            "REGION_UN": "Americas",
            "SUBREGION": "South America"
        }
    }, {
        "arcs": [
            [246, 247, 248, 249, 250]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Egypt",
            "NAME_LONG": "Egypt",
            "ABBREV": "Egypt",
            "FORMAL_EN": "Arab Republic of Egypt",
            "POP_EST": 97041072,
            "POP_RANK": 16,
            "GDP_MD_EST": 1105000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "EG",
            "ISO_A3": "EGY",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Northern Africa"
        }
    }, {
        "arcs": [
            [-232, 251, 252, 253]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Eritrea",
            "NAME_LONG": "Eritrea",
            "ABBREV": "Erit.",
            "FORMAL_EN": "State of Eritrea",
            "POP_EST": 5918919,
            "POP_RANK": 13,
            "GDP_MD_EST": 9169,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "ER",
            "ISO_A3": "ERI",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Eastern Africa"
        }
    }, {
        "arcs": [
            [254, 255, 256, 257]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Spain",
            "NAME_LONG": "Spain",
            "ABBREV": "Sp.",
            "FORMAL_EN": "Kingdom of Spain",
            "POP_EST": 48958159,
            "POP_RANK": 15,
            "GDP_MD_EST": 1690000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "ES",
            "ISO_A3": "ESP",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Southern Europe"
        }
    }, {
        "arcs": [
            [258, 259, 260]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Estonia",
            "NAME_LONG": "Estonia",
            "ABBREV": "Est.",
            "FORMAL_EN": "Republic of Estonia",
            "POP_EST": 1251581,
            "POP_RANK": 12,
            "GDP_MD_EST": 38700,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "EE",
            "ISO_A3": "EST",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Northern Europe"
        }
    }, {
        "arcs": [
            [-231, 261, 262, 263, 264, 265, -252]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Ethiopia",
            "NAME_LONG": "Ethiopia",
            "ABBREV": "Eth.",
            "FORMAL_EN": "Federal Democratic Republic of Ethiopia",
            "POP_EST": 105350020,
            "POP_RANK": 17,
            "GDP_MD_EST": 174700,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "ET",
            "ISO_A3": "ETH",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Eastern Africa"
        }
    }, {
        "arcs": [
            [266, 267, 268, 269]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Finland",
            "NAME_LONG": "Finland",
            "ABBREV": "Fin.",
            "FORMAL_EN": "Republic of Finland",
            "POP_EST": 5491218,
            "POP_RANK": 13,
            "GDP_MD_EST": 224137,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "FI",
            "ISO_A3": "FIN",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Northern Europe"
        }
    }, {
        "arcs": [
            [
                [270]
            ],
            [
                [271]
            ],
            [
                [272]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Fiji",
            "NAME_LONG": "Fiji",
            "ABBREV": "Fiji",
            "FORMAL_EN": "Republic of Fiji",
            "POP_EST": 920938,
            "POP_RANK": 11,
            "GDP_MD_EST": 8374,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "FJ",
            "ISO_A3": "FJI",
            "CONTINENT": "Oceania",
            "REGION_UN": "Oceania",
            "SUBREGION": "Melanesia"
        }
    }, {
        "arcs": [
            [273]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Falkland Is.",
            "NAME_LONG": "Falkland Islands",
            "ABBREV": "Flk. Is.",
            "FORMAL_EN": "Falkland Islands",
            "POP_EST": 2931,
            "POP_RANK": 4,
            "GDP_MD_EST": 281.8,
            "POP_YEAR": 2014,
            "GDP_YEAR": 2012,
            "ISO_A2": "FK",
            "ISO_A3": "FLK",
            "CONTINENT": "South America",
            "REGION_UN": "Americas",
            "SUBREGION": "South America"
        }
    }, {
        "arcs": [
            [
                [-65, 274, -222, -162, 275, 276, -256, 277]
            ],
            [
                [-111, 278, 279]
            ],
            [
                [280]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "France",
            "NAME_LONG": "France",
            "ABBREV": "Fr.",
            "FORMAL_EN": "French Republic",
            "POP_EST": 67106161,
            "POP_RANK": 16,
            "GDP_MD_EST": 2699000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "FR",
            "ISO_A3": "FRA",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Western Europe"
        }
    }, {
        "arcs": [
            [-190, -204, 281, 282]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Gabon",
            "NAME_LONG": "Gabon",
            "ABBREV": "Gabon",
            "FORMAL_EN": "Gabonese Republic",
            "POP_EST": 1772255,
            "POP_RANK": 12,
            "GDP_MD_EST": 35980,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "GA",
            "ISO_A3": "GAB",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Middle Africa"
        }
    }, {
        "arcs": [
            [
                [283, 284]
            ],
            [
                [285]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "United Kingdom",
            "NAME_LONG": "United Kingdom",
            "ABBREV": "U.K.",
            "FORMAL_EN": "United Kingdom of Great Britain and Northern Ireland",
            "POP_EST": 64769452,
            "POP_RANK": 16,
            "GDP_MD_EST": 2788000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "GB",
            "ISO_A3": "GBR",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Northern Europe"
        }
    }, {
        "arcs": [
            [-32, 286, 287, 288, -55]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Georgia",
            "NAME_LONG": "Georgia",
            "ABBREV": "Geo.",
            "FORMAL_EN": "Georgia",
            "POP_EST": 4926330,
            "POP_RANK": 12,
            "GDP_MD_EST": 37270,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "GE",
            "ISO_A3": "GEO",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Western Asia"
        }
    }, {
        "arcs": [
            [-74, 289, 290, -184]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Ghana",
            "NAME_LONG": "Ghana",
            "ABBREV": "Ghana",
            "FORMAL_EN": "Republic of Ghana",
            "POP_EST": 27499924,
            "POP_RANK": 15,
            "GDP_MD_EST": 120800,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "GH",
            "ISO_A3": "GHA",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Western Africa"
        }
    }, {
        "arcs": [
            [-187, 291, 292, 293, 294, 295, 296]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Guinea",
            "NAME_LONG": "Guinea",
            "ABBREV": "Gin.",
            "FORMAL_EN": "Republic of Guinea",
            "POP_EST": 12413867,
            "POP_RANK": 14,
            "GDP_MD_EST": 16080,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "GN",
            "ISO_A3": "GIN",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Western Africa"
        }
    }, {
        "arcs": [
            [297, 298]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Gambia",
            "NAME_LONG": "The Gambia",
            "ABBREV": "Gambia",
            "FORMAL_EN": "Republic of the Gambia",
            "POP_EST": 2051363,
            "POP_RANK": 12,
            "GDP_MD_EST": 3387,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "GM",
            "ISO_A3": "GMB",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Western Africa"
        }
    }, {
        "arcs": [
            [-295, 299, 300]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Guinea-Bissau",
            "NAME_LONG": "Guinea-Bissau",
            "ABBREV": "GnB.",
            "FORMAL_EN": "Republic of Guinea-Bissau",
            "POP_EST": 1792338,
            "POP_RANK": 12,
            "GDP_MD_EST": 2851,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "GW",
            "ISO_A3": "GNB",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Western Africa"
        }
    }, {
        "arcs": [
            [-191, -283, 301]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Eq. Guinea",
            "NAME_LONG": "Equatorial Guinea",
            "ABBREV": "Eq. G.",
            "FORMAL_EN": "Republic of Equatorial Guinea",
            "POP_EST": 778358,
            "POP_RANK": 11,
            "GDP_MD_EST": 31770,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "GQ",
            "ISO_A3": "GNQ",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Middle Africa"
        }
    }, {
        "arcs": [
            [
                [-14, 302, -84, 303, 304]
            ],
            [
                [305]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Greece",
            "NAME_LONG": "Greece",
            "ABBREV": "Greece",
            "FORMAL_EN": "Hellenic Republic",
            "POP_EST": 10768477,
            "POP_RANK": 14,
            "GDP_MD_EST": 290500,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "GR",
            "ISO_A3": "GRC",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Southern Europe"
        }
    }, {
        "arcs": [
            [306]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Greenland",
            "NAME_LONG": "Greenland",
            "ABBREV": "Grlnd.",
            "FORMAL_EN": "Greenland",
            "POP_EST": 57713,
            "POP_RANK": 8,
            "GDP_MD_EST": 2173,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2015,
            "ISO_A2": "GL",
            "ISO_A3": "GRL",
            "CONTINENT": "North America",
            "REGION_UN": "Americas",
            "SUBREGION": "Northern America"
        }
    }, {
        "arcs": [
            [-100, 307, 308, 309, 310, 311]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Guatemala",
            "NAME_LONG": "Guatemala",
            "ABBREV": "Guat.",
            "FORMAL_EN": "Republic of Guatemala",
            "POP_EST": 15460732,
            "POP_RANK": 14,
            "GDP_MD_EST": 131800,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "GT",
            "ISO_A3": "GTM",
            "CONTINENT": "North America",
            "REGION_UN": "Americas",
            "SUBREGION": "Central America"
        }
    }, {
        "arcs": [
            [-109, 312, 313, 314]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Guyana",
            "NAME_LONG": "Guyana",
            "ABBREV": "Guy.",
            "FORMAL_EN": "Co-operative Republic of Guyana",
            "POP_EST": 737718,
            "POP_RANK": 11,
            "GDP_MD_EST": 6093,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "GY",
            "ISO_A3": "GUY",
            "CONTINENT": "South America",
            "REGION_UN": "Americas",
            "SUBREGION": "South America"
        }
    }, {
        "arcs": [
            [-309, 315, 316, 317, 318]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Honduras",
            "NAME_LONG": "Honduras",
            "ABBREV": "Hond.",
            "FORMAL_EN": "Republic of Honduras",
            "POP_EST": 9038741,
            "POP_RANK": 13,
            "GDP_MD_EST": 43190,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "HN",
            "ISO_A3": "HND",
            "CONTINENT": "North America",
            "REGION_UN": "Americas",
            "SUBREGION": "Central America"
        }
    }, {
        "arcs": [
            [-91, 319, 320, 321, 322, 323]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Croatia",
            "NAME_LONG": "Croatia",
            "ABBREV": "Cro.",
            "FORMAL_EN": "Republic of Croatia",
            "POP_EST": 4292095,
            "POP_RANK": 12,
            "GDP_MD_EST": 94240,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "HR",
            "ISO_A3": "HRV",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Southern Europe"
        }
    }, {
        "arcs": [
            [-236, 324]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Haiti",
            "NAME_LONG": "Haiti",
            "ABBREV": "Haiti",
            "FORMAL_EN": "Republic of Haiti",
            "POP_EST": 10646714,
            "POP_RANK": 14,
            "GDP_MD_EST": 19340,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "HT",
            "ISO_A3": "HTI",
            "CONTINENT": "North America",
            "REGION_UN": "Americas",
            "SUBREGION": "Caribbean"
        }
    }, {
        "arcs": [
            [-48, 325, 326, 327, 328, -323, 329]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Hungary",
            "NAME_LONG": "Hungary",
            "ABBREV": "Hun.",
            "FORMAL_EN": "Republic of Hungary",
            "POP_EST": 9850845,
            "POP_RANK": 13,
            "GDP_MD_EST": 267600,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "HU",
            "ISO_A3": "HUN",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Eastern Europe"
        }
    }, {
        "arcs": [
            [
                [330]
            ],
            [
                [331, 332]
            ],
            [
                [333]
            ],
            [
                [334]
            ],
            [
                [335]
            ],
            [
                [336]
            ],
            [
                [337]
            ],
            [
                [338]
            ],
            [
                [339, 340]
            ],
            [
                [341]
            ],
            [
                [342]
            ],
            [
                [343, 344]
            ],
            [
                [345]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Indonesia",
            "NAME_LONG": "Indonesia",
            "ABBREV": "Indo.",
            "FORMAL_EN": "Republic of Indonesia",
            "POP_EST": 260580739,
            "POP_RANK": 17,
            "GDP_MD_EST": 3028000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "ID",
            "ISO_A3": "IDN",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "South-Eastern Asia"
        }
    }, {
        "arcs": [
            [-80, 346, 347, -181, 348, -179, -116, -178, 349]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "India",
            "NAME_LONG": "India",
            "ABBREV": "India",
            "FORMAL_EN": "Republic of India",
            "POP_EST": 1281935911,
            "POP_RANK": 18,
            "GDP_MD_EST": 8721000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "IN",
            "ISO_A3": "IND",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Southern Asia"
        }
    }, {
        "arcs": [
            [-284, 350]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Ireland",
            "NAME_LONG": "Ireland",
            "ABBREV": "Ire.",
            "FORMAL_EN": "Ireland",
            "POP_EST": 5011102,
            "POP_RANK": 13,
            "GDP_MD_EST": 322000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "IE",
            "ISO_A3": "IRL",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Northern Europe"
        }
    }, {
        "arcs": [
            [-6, 351, 352, 353, 354, -59, -34, -58, 355, 356]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Iran",
            "NAME_LONG": "Iran",
            "ABBREV": "Iran",
            "FORMAL_EN": "Islamic Republic of Iran",
            "POP_EST": 82021564,
            "POP_RANK": 16,
            "GDP_MD_EST": 1459000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "IR",
            "ISO_A3": "IRN",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Southern Asia"
        }
    }, {
        "arcs": [
            [-354, 357, 358, 359, 360, 361, 362]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Iraq",
            "NAME_LONG": "Iraq",
            "ABBREV": "Iraq",
            "FORMAL_EN": "Republic of Iraq",
            "POP_EST": 39192111,
            "POP_RANK": 15,
            "GDP_MD_EST": 596700,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "IQ",
            "ISO_A3": "IRQ",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Western Asia"
        }
    }, {
        "arcs": [
            [363]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Iceland",
            "NAME_LONG": "Iceland",
            "ABBREV": "Iceland",
            "FORMAL_EN": "Republic of Iceland",
            "POP_EST": 339747,
            "POP_RANK": 10,
            "GDP_MD_EST": 16150,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "IS",
            "ISO_A3": "ISL",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Northern Europe"
        }
    }, {
        "arcs": [
            [364, 365, 366, 367, 368, 369, -250]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Israel",
            "NAME_LONG": "Israel",
            "ABBREV": "Isr.",
            "FORMAL_EN": "State of Israel",
            "POP_EST": 8299706,
            "POP_RANK": 13,
            "GDP_MD_EST": 297000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "IL",
            "ISO_A3": "ISR",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Western Asia"
        }
    }, {
        "arcs": [
            [
                [-50, 370, 371, -276, -161]
            ],
            [
                [372]
            ],
            [
                [373]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Italy",
            "NAME_LONG": "Italy",
            "ABBREV": "Italy",
            "FORMAL_EN": "Italian Republic",
            "POP_EST": 62137802,
            "POP_RANK": 16,
            "GDP_MD_EST": 2221000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "IT",
            "ISO_A3": "ITA",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Southern Europe"
        }
    }, {
        "arcs": [
            [374]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Jamaica",
            "NAME_LONG": "Jamaica",
            "ABBREV": "Jam.",
            "FORMAL_EN": "Jamaica",
            "POP_EST": 2990561,
            "POP_RANK": 12,
            "GDP_MD_EST": 25390,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "JM",
            "ISO_A3": "JAM",
            "CONTINENT": "North America",
            "REGION_UN": "Americas",
            "SUBREGION": "Caribbean"
        }
    }, {
        "arcs": [
            [-361, 375, 376, -370, 377, -368, 378]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Jordan",
            "NAME_LONG": "Jordan",
            "ABBREV": "Jord.",
            "FORMAL_EN": "Hashemite Kingdom of Jordan",
            "POP_EST": 10248069,
            "POP_RANK": 14,
            "GDP_MD_EST": 86190,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "JO",
            "ISO_A3": "JOR",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Western Asia"
        }
    }, {
        "arcs": [
            [
                [379]
            ],
            [
                [380]
            ],
            [
                [381]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Japan",
            "NAME_LONG": "Japan",
            "ABBREV": "Japan",
            "FORMAL_EN": "Japan",
            "POP_EST": 126451398,
            "POP_RANK": 17,
            "GDP_MD_EST": 4932000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "JP",
            "ISO_A3": "JPN",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Eastern Asia"
        }
    }, {
        "arcs": [
            [-169, 382, 383, 384, 385, 386]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Kazakhstan",
            "NAME_LONG": "Kazakhstan",
            "ABBREV": "Kaz.",
            "FORMAL_EN": "Republic of Kazakhstan",
            "POP_EST": 18556698,
            "POP_RANK": 14,
            "GDP_MD_EST": 460700,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "KZ",
            "ISO_A3": "KAZ",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Central Asia"
        }
    }, {
        "arcs": [
            [-264, 387, 388, 389, 390, 391]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Kenya",
            "NAME_LONG": "Kenya",
            "ABBREV": "Ken.",
            "FORMAL_EN": "Republic of Kenya",
            "POP_EST": 47615739,
            "POP_RANK": 15,
            "GDP_MD_EST": 152700,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "KE",
            "ISO_A3": "KEN",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Eastern Africa"
        }
    }, {
        "arcs": [
            [-168, 392, 393, -383]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Kyrgyzstan",
            "NAME_LONG": "Kyrgyzstan",
            "ABBREV": "Kgz.",
            "FORMAL_EN": "Kyrgyz Republic",
            "POP_EST": 5789122,
            "POP_RANK": 13,
            "GDP_MD_EST": 21010,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "KG",
            "ISO_A3": "KGZ",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Central Asia"
        }
    }, {
        "arcs": [
            [394, 395, 396, 397]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Cambodia",
            "NAME_LONG": "Cambodia",
            "ABBREV": "Camb.",
            "FORMAL_EN": "Kingdom of Cambodia",
            "POP_EST": 16204486,
            "POP_RANK": 14,
            "GDP_MD_EST": 58940,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "KH",
            "ISO_A3": "KHM",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "South-Eastern Asia"
        }
    }, {
        "arcs": [
            [398, 399]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "South Korea",
            "NAME_LONG": "Republic of Korea",
            "ABBREV": "S.K.",
            "FORMAL_EN": "Republic of Korea",
            "POP_EST": 51181299,
            "POP_RANK": 16,
            "GDP_MD_EST": 1929000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "KR",
            "ISO_A3": "KOR",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Eastern Asia"
        }
    }, {
        "arcs": [
            [-17, 400, 401, 402]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Kosovo",
            "NAME_LONG": "Kosovo",
            "ABBREV": "Kos.",
            "FORMAL_EN": "Republic of Kosovo",
            "POP_EST": 1895250,
            "POP_RANK": 12,
            "GDP_MD_EST": 18490,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "XK",
            "ISO_A3": "-99",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Southern Europe"
        }
    }, {
        "arcs": [
            [-359, 403, 404]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Kuwait",
            "NAME_LONG": "Kuwait",
            "ABBREV": "Kwt.",
            "FORMAL_EN": "State of Kuwait",
            "POP_EST": 2875422,
            "POP_RANK": 12,
            "GDP_MD_EST": 301100,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "KW",
            "ISO_A3": "KWT",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Western Asia"
        }
    }, {
        "arcs": [
            [-176, 405, -396, 406, 407]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Laos",
            "NAME_LONG": "Lao PDR",
            "ABBREV": "Laos",
            "FORMAL_EN": "Lao People's Democratic Republic",
            "POP_EST": 7126706,
            "POP_RANK": 13,
            "GDP_MD_EST": 40960,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "LA",
            "ISO_A3": "LAO",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "South-Eastern Asia"
        }
    }, {
        "arcs": [
            [-366, 408, 409]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Lebanon",
            "NAME_LONG": "Lebanon",
            "ABBREV": "Leb.",
            "FORMAL_EN": "Lebanese Republic",
            "POP_EST": 6229794,
            "POP_RANK": 13,
            "GDP_MD_EST": 85160,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "LB",
            "ISO_A3": "LBN",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Western Asia"
        }
    }, {
        "arcs": [
            [-186, 410, 411, -292]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Liberia",
            "NAME_LONG": "Liberia",
            "ABBREV": "Liberia",
            "FORMAL_EN": "Republic of Liberia",
            "POP_EST": 4689021,
            "POP_RANK": 12,
            "GDP_MD_EST": 3881,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "LR",
            "ISO_A3": "LBR",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Western Africa"
        }
    }, {
        "arcs": [
            [-243, 412, 413, -248, 414, 415, 416]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Libya",
            "NAME_LONG": "Libya",
            "ABBREV": "Libya",
            "FORMAL_EN": "Libya",
            "POP_EST": 6653210,
            "POP_RANK": 13,
            "GDP_MD_EST": 90890,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "LY",
            "ISO_A3": "LBY",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Northern Africa"
        }
    }, {
        "arcs": [
            [417]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Sri Lanka",
            "NAME_LONG": "Sri Lanka",
            "ABBREV": "Sri L.",
            "FORMAL_EN": "Democratic Socialist Republic of Sri Lanka",
            "POP_EST": 22409381,
            "POP_RANK": 15,
            "GDP_MD_EST": 236700,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "LK",
            "ISO_A3": "LKA",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Southern Asia"
        }
    }, {
        "arcs": [
            [418]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Lesotho",
            "NAME_LONG": "Lesotho",
            "ABBREV": "Les.",
            "FORMAL_EN": "Kingdom of Lesotho",
            "POP_EST": 1958042,
            "POP_RANK": 12,
            "GDP_MD_EST": 6019,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "LS",
            "ISO_A3": "LSO",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Southern Africa"
        }
    }, {
        "arcs": [
            [-93, 419, 420, 421, 422]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Lithuania",
            "NAME_LONG": "Lithuania",
            "ABBREV": "Lith.",
            "FORMAL_EN": "Republic of Lithuania",
            "POP_EST": 2823859,
            "POP_RANK": 12,
            "GDP_MD_EST": 85620,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "LT",
            "ISO_A3": "LTU",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Northern Europe"
        }
    }, {
        "arcs": [
            [-64, -223, -275]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Luxembourg",
            "NAME_LONG": "Luxembourg",
            "ABBREV": "Lux.",
            "FORMAL_EN": "Grand Duchy of Luxembourg",
            "POP_EST": 594130,
            "POP_RANK": 11,
            "GDP_MD_EST": 58740,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "LU",
            "ISO_A3": "LUX",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Western Europe"
        }
    }, {
        "arcs": [
            [-94, -423, 423, -261, 424]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Latvia",
            "NAME_LONG": "Latvia",
            "ABBREV": "Lat.",
            "FORMAL_EN": "Republic of Latvia",
            "POP_EST": 1944643,
            "POP_RANK": 12,
            "GDP_MD_EST": 50650,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "LV",
            "ISO_A3": "LVA",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Northern Europe"
        }
    }, {
        "arcs": [
            [-240, 425, 426]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Morocco",
            "NAME_LONG": "Morocco",
            "ABBREV": "Mor.",
            "FORMAL_EN": "Kingdom of Morocco",
            "POP_EST": 33986655,
            "POP_RANK": 15,
            "GDP_MD_EST": 282800,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "MA",
            "ISO_A3": "MAR",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Northern Africa"
        }
    }, {
        "arcs": [
            [427, 428]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Moldova",
            "NAME_LONG": "Moldova",
            "ABBREV": "Mda.",
            "FORMAL_EN": "Republic of Moldova",
            "POP_EST": 3474121,
            "POP_RANK": 12,
            "GDP_MD_EST": 18540,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "MD",
            "ISO_A3": "MDA",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Eastern Europe"
        }
    }, {
        "arcs": [
            [429]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Madagascar",
            "NAME_LONG": "Madagascar",
            "ABBREV": "Mad.",
            "FORMAL_EN": "Republic of Madagascar",
            "POP_EST": 25054161,
            "POP_RANK": 15,
            "GDP_MD_EST": 36860,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "MG",
            "ISO_A3": "MDG",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Eastern Africa"
        }
    }, {
        "arcs": [
            [-98, -312, 430, 431, 432]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Mexico",
            "NAME_LONG": "Mexico",
            "ABBREV": "Mex.",
            "FORMAL_EN": "United Mexican States",
            "POP_EST": 124574795,
            "POP_RANK": 17,
            "GDP_MD_EST": 2307000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "MX",
            "ISO_A3": "MEX",
            "CONTINENT": "North America",
            "REGION_UN": "Americas",
            "SUBREGION": "Central America"
        }
    }, {
        "arcs": [
            [-18, -403, 433, -85, -303]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Macedonia",
            "NAME_LONG": "Macedonia",
            "ABBREV": "Mkd.",
            "FORMAL_EN": "Former Yugoslav Republic of Macedonia",
            "POP_EST": 2103721,
            "POP_RANK": 12,
            "GDP_MD_EST": 29520,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "MK",
            "ISO_A3": "MKD",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Southern Europe"
        }
    }, {
        "arcs": [
            [-76, -188, -297, 434, 435, -237, 436]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Mali",
            "NAME_LONG": "Mali",
            "ABBREV": "Mali",
            "FORMAL_EN": "Republic of Mali",
            "POP_EST": 17885245,
            "POP_RANK": 14,
            "GDP_MD_EST": 38090,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "ML",
            "ISO_A3": "MLI",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Western Africa"
        }
    }, {
        "arcs": [
            [-78, -350, -177, -408, 437, 438]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Myanmar",
            "NAME_LONG": "Myanmar",
            "ABBREV": "Myan.",
            "FORMAL_EN": "Republic of the Union of Myanmar",
            "POP_EST": 55123814,
            "POP_RANK": 16,
            "GDP_MD_EST": 311100,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "MM",
            "ISO_A3": "MMR",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "South-Eastern Asia"
        }
    }, {
        "arcs": [
            [-16, 439, -320, -90, 440, -401]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Montenegro",
            "NAME_LONG": "Montenegro",
            "ABBREV": "Mont.",
            "FORMAL_EN": "Montenegro",
            "POP_EST": 642550,
            "POP_RANK": 11,
            "GDP_MD_EST": 10610,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "ME",
            "ISO_A3": "MNE",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Southern Europe"
        }
    }, {
        "arcs": [
            [-171, 441]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Mongolia",
            "NAME_LONG": "Mongolia",
            "ABBREV": "Mong.",
            "FORMAL_EN": "Mongolia",
            "POP_EST": 3068243,
            "POP_RANK": 12,
            "GDP_MD_EST": 37000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "MN",
            "ISO_A3": "MNG",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Eastern Asia"
        }
    }, {
        "arcs": [
            [442, 443, 444, 445, 446, 447, 448, 449]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Mozambique",
            "NAME_LONG": "Mozambique",
            "ABBREV": "Moz.",
            "FORMAL_EN": "Republic of Mozambique",
            "POP_EST": 26573706,
            "POP_RANK": 15,
            "GDP_MD_EST": 35010,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "MZ",
            "ISO_A3": "MOZ",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Eastern Africa"
        }
    }, {
        "arcs": [
            [-238, -436, 450, 451, 452]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Mauritania",
            "NAME_LONG": "Mauritania",
            "ABBREV": "Mrt.",
            "FORMAL_EN": "Islamic Republic of Mauritania",
            "POP_EST": 3758571,
            "POP_RANK": 12,
            "GDP_MD_EST": 16710,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "MR",
            "ISO_A3": "MRT",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Western Africa"
        }
    }, {
        "arcs": [
            [-450, 453, 454]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Malawi",
            "NAME_LONG": "Malawi",
            "ABBREV": "Mal.",
            "FORMAL_EN": "Republic of Malawi",
            "POP_EST": 19196246,
            "POP_RANK": 14,
            "GDP_MD_EST": 21200,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "MW",
            "ISO_A3": "MWI",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Eastern Africa"
        }
    }, {
        "arcs": [
            [
                [-115, 455, -344, 456]
            ],
            [
                [457, 458]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Malaysia",
            "NAME_LONG": "Malaysia",
            "ABBREV": "Malay.",
            "FORMAL_EN": "Malaysia",
            "POP_EST": 31381992,
            "POP_RANK": 15,
            "GDP_MD_EST": 863000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "MY",
            "ISO_A3": "MYS",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "South-Eastern Asia"
        }
    }, {
        "arcs": [
            [-7, 459, -119, 460, 461]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Namibia",
            "NAME_LONG": "Namibia",
            "ABBREV": "Nam.",
            "FORMAL_EN": "Republic of Namibia",
            "POP_EST": 2484780,
            "POP_RANK": 12,
            "GDP_MD_EST": 25990,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "NA",
            "ISO_A3": "NAM",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Southern Africa"
        }
    }, {
        "arcs": [
            [462]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "New Caledonia",
            "NAME_LONG": "New Caledonia",
            "ABBREV": "New C.",
            "FORMAL_EN": "New Caledonia",
            "POP_EST": 279070,
            "POP_RANK": 10,
            "GDP_MD_EST": 10770,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "NC",
            "ISO_A3": "NCL",
            "CONTINENT": "Oceania",
            "REGION_UN": "Oceania",
            "SUBREGION": "Melanesia"
        }
    }, {
        "arcs": [
            [-71, -77, -437, -244, -417, 463, -194, 464]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Niger",
            "NAME_LONG": "Niger",
            "ABBREV": "Niger",
            "FORMAL_EN": "Republic of Niger",
            "POP_EST": 19245344,
            "POP_RANK": 14,
            "GDP_MD_EST": 20150,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "NE",
            "ISO_A3": "NER",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Western Africa"
        }
    }, {
        "arcs": [
            [-72, -465, -193, 465]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Nigeria",
            "NAME_LONG": "Nigeria",
            "ABBREV": "Nigeria",
            "FORMAL_EN": "Federal Republic of Nigeria",
            "POP_EST": 190632261,
            "POP_RANK": 17,
            "GDP_MD_EST": 1089000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "NG",
            "ISO_A3": "NGA",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Western Africa"
        }
    }, {
        "arcs": [
            [-212, 466, -317, 467]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Nicaragua",
            "NAME_LONG": "Nicaragua",
            "ABBREV": "Nic.",
            "FORMAL_EN": "Republic of Nicaragua",
            "POP_EST": 6025951,
            "POP_RANK": 13,
            "GDP_MD_EST": 33550,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "NI",
            "ISO_A3": "NIC",
            "CONTINENT": "North America",
            "REGION_UN": "Americas",
            "SUBREGION": "Central America"
        }
    }, {
        "arcs": [
            [-67, 468, -224]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Netherlands",
            "NAME_LONG": "Netherlands",
            "ABBREV": "Neth.",
            "FORMAL_EN": "Kingdom of the Netherlands",
            "POP_EST": 17084719,
            "POP_RANK": 14,
            "GDP_MD_EST": 870800,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "NL",
            "ISO_A3": "NLD",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Western Europe"
        }
    }, {
        "arcs": [
            [
                [-268, 469, 470, 471]
            ],
            [
                [472]
            ],
            [
                [473]
            ],
            [
                [474]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Norway",
            "NAME_LONG": "Norway",
            "ABBREV": "Nor.",
            "FORMAL_EN": "Kingdom of Norway",
            "POP_EST": 5320045,
            "POP_RANK": 13,
            "GDP_MD_EST": 364700,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "NO",
            "ISO_A3": "NOR",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Northern Europe"
        }
    }, {
        "arcs": [
            [-180, -349]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Nepal",
            "NAME_LONG": "Nepal",
            "ABBREV": "Nepal",
            "FORMAL_EN": "Nepal",
            "POP_EST": 29384297,
            "POP_RANK": 15,
            "GDP_MD_EST": 71520,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "NP",
            "ISO_A3": "NPL",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Southern Asia"
        }
    }, {
        "arcs": [
            [
                [475]
            ],
            [
                [476]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "New Zealand",
            "NAME_LONG": "New Zealand",
            "ABBREV": "N.Z.",
            "FORMAL_EN": "New Zealand",
            "POP_EST": 4510327,
            "POP_RANK": 12,
            "GDP_MD_EST": 174800,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "NZ",
            "ISO_A3": "NZL",
            "CONTINENT": "Oceania",
            "REGION_UN": "Oceania",
            "SUBREGION": "Australia and New Zealand"
        }
    }, {
        "arcs": [
            [
                [-20, 477]
            ],
            [
                [-22, 478, 479, 480]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Oman",
            "NAME_LONG": "Oman",
            "ABBREV": "Oman",
            "FORMAL_EN": "Sultanate of Oman",
            "POP_EST": 3424386,
            "POP_RANK": 12,
            "GDP_MD_EST": 173100,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "OM",
            "ISO_A3": "OMN",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Western Asia"
        }
    }, {
        "arcs": [
            [-5, -182, -348, 481, -352]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Pakistan",
            "NAME_LONG": "Pakistan",
            "ABBREV": "Pak.",
            "FORMAL_EN": "Islamic Republic of Pakistan",
            "POP_EST": 204924861,
            "POP_RANK": 17,
            "GDP_MD_EST": 988200,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "PK",
            "ISO_A3": "PAK",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Southern Asia"
        }
    }, {
        "arcs": [
            [-208, 482, -214, 483]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Panama",
            "NAME_LONG": "Panama",
            "ABBREV": "Pan.",
            "FORMAL_EN": "Republic of Panama",
            "POP_EST": 3753142,
            "POP_RANK": 12,
            "GDP_MD_EST": 93120,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "PA",
            "ISO_A3": "PAN",
            "CONTINENT": "North America",
            "REGION_UN": "Americas",
            "SUBREGION": "Central America"
        }
    }, {
        "arcs": [
            [-102, -166, 484, -245, -205, -106]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Peru",
            "NAME_LONG": "Peru",
            "ABBREV": "Peru",
            "FORMAL_EN": "Republic of Peru",
            "POP_EST": 31036656,
            "POP_RANK": 15,
            "GDP_MD_EST": 410400,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "PE",
            "ISO_A3": "PER",
            "CONTINENT": "South America",
            "REGION_UN": "Americas",
            "SUBREGION": "South America"
        }
    }, {
        "arcs": [
            [
                [485]
            ],
            [
                [486]
            ],
            [
                [487]
            ],
            [
                [488]
            ],
            [
                [489]
            ],
            [
                [490]
            ],
            [
                [491]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Philippines",
            "NAME_LONG": "Philippines",
            "ABBREV": "Phil.",
            "FORMAL_EN": "Republic of the Philippines",
            "POP_EST": 104256076,
            "POP_RANK": 17,
            "GDP_MD_EST": 801900,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "PH",
            "ISO_A3": "PHL",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "South-Eastern Asia"
        }
    }, {
        "arcs": [
            [
                [-340, 492]
            ],
            [
                [493]
            ],
            [
                [494]
            ],
            [
                [495]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Papua New Guinea",
            "NAME_LONG": "Papua New Guinea",
            "ABBREV": "P.N.G.",
            "FORMAL_EN": "Independent State of Papua New Guinea",
            "POP_EST": 6909701,
            "POP_RANK": 13,
            "GDP_MD_EST": 28020,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "PG",
            "ISO_A3": "PNG",
            "CONTINENT": "Oceania",
            "REGION_UN": "Oceania",
            "SUBREGION": "Melanesia"
        }
    }, {
        "arcs": [
            [-97, 496, 497, -220, -228, 498, 499, -420]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Poland",
            "NAME_LONG": "Poland",
            "ABBREV": "Pol.",
            "FORMAL_EN": "Republic of Poland",
            "POP_EST": 38476269,
            "POP_RANK": 15,
            "GDP_MD_EST": 1052000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "PL",
            "ISO_A3": "POL",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Eastern Europe"
        }
    }, {
        "arcs": [
            [500]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Puerto Rico",
            "NAME_LONG": "Puerto Rico",
            "ABBREV": "P.R.",
            "FORMAL_EN": "Commonwealth of Puerto Rico",
            "POP_EST": 3351827,
            "POP_RANK": 12,
            "GDP_MD_EST": 131000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "PR",
            "ISO_A3": "PRI",
            "CONTINENT": "North America",
            "REGION_UN": "Americas",
            "SUBREGION": "Caribbean"
        }
    }, {
        "arcs": [
            [-173, 501, 502, -400, 503]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "North Korea",
            "NAME_LONG": "Dem. Rep. Korea",
            "ABBREV": "N.K.",
            "FORMAL_EN": "Democratic People's Republic of Korea",
            "POP_EST": 25248140,
            "POP_RANK": 15,
            "GDP_MD_EST": 40000,
            "POP_YEAR": 2013,
            "GDP_YEAR": 2016,
            "ISO_A2": "KP",
            "ISO_A3": "PRK",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Eastern Asia"
        }
    }, {
        "arcs": [
            [-258, 504]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Portugal",
            "NAME_LONG": "Portugal",
            "ABBREV": "Port.",
            "FORMAL_EN": "Portuguese Republic",
            "POP_EST": 10839514,
            "POP_RANK": 14,
            "GDP_MD_EST": 297100,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "PT",
            "ISO_A3": "PRT",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Southern Europe"
        }
    }, {
        "arcs": [
            [-28, -104, -105]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Paraguay",
            "NAME_LONG": "Paraguay",
            "ABBREV": "Para.",
            "FORMAL_EN": "Republic of Paraguay",
            "POP_EST": 6943739,
            "POP_RANK": 13,
            "GDP_MD_EST": 64670,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "PY",
            "ISO_A3": "PRY",
            "CONTINENT": "South America",
            "REGION_UN": "Americas",
            "SUBREGION": "South America"
        }
    }, {
        "arcs": [
            [-369, -378]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Palestine",
            "NAME_LONG": "Palestine",
            "ABBREV": "Pal.",
            "FORMAL_EN": "West Bank and Gaza",
            "POP_EST": 4543126,
            "POP_RANK": 12,
            "GDP_MD_EST": 21220.77,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "PS",
            "ISO_A3": "PSE",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Western Asia"
        }
    }, {
        "arcs": [
            [505, 506]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Qatar",
            "NAME_LONG": "Qatar",
            "ABBREV": "Qatar",
            "FORMAL_EN": "State of Qatar",
            "POP_EST": 2314307,
            "POP_RANK": 12,
            "GDP_MD_EST": 334500,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "QA",
            "ISO_A3": "QAT",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Western Asia"
        }
    }, {
        "arcs": [
            [-81, 507, -328, 508, -429, 509, 510]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Romania",
            "NAME_LONG": "Romania",
            "ABBREV": "Rom.",
            "FORMAL_EN": "Romania",
            "POP_EST": 21529967,
            "POP_RANK": 15,
            "GDP_MD_EST": 441000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "RO",
            "ISO_A3": "ROU",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Eastern Europe"
        }
    }, {
        "arcs": [
            [
                [-56, -289, 511, 512, -95, -425, -260, 513, -269, -
                 472, 514, -502, -172, -442, -170, -387, 515]
            ],
            [
                [-421, -500, 516]
            ],
            [
                [517, 518]
            ],
            [
                [519]
            ],
            [
                [520]
            ],
            [
                [521]
            ],
            [
                [522]
            ],
            [
                [523]
            ],
            [
                [524]
            ],
            [
                [525]
            ],
            [
                [526]
            ],
            [
                [527]
            ],
            [
                [528]
            ],
            [
                [529]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Russia",
            "NAME_LONG": "Russian Federation",
            "ABBREV": "Rus.",
            "FORMAL_EN": "Russian Federation",
            "POP_EST": 142257519,
            "POP_RANK": 17,
            "GDP_MD_EST": 3745000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "RU",
            "ISO_A3": "RUS",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Eastern Europe"
        }
    }, {
        "arcs": [
            [-61, -200, 530, 531]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Rwanda",
            "NAME_LONG": "Rwanda",
            "ABBREV": "Rwa.",
            "FORMAL_EN": "Republic of Rwanda",
            "POP_EST": 11901484,
            "POP_RANK": 14,
            "GDP_MD_EST": 21970,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "RW",
            "ISO_A3": "RWA",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Eastern Africa"
        }
    }, {
        "arcs": [
            [-239, -453, 532, -426]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "W. Sahara",
            "NAME_LONG": "Western Sahara",
            "ABBREV": "W. Sah.",
            "FORMAL_EN": "Sahrawi Arab Democratic Republic",
            "POP_EST": 603253,
            "POP_RANK": 11,
            "GDP_MD_EST": 906.5,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2007,
            "ISO_A2": "EH",
            "ISO_A3": "ESH",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Northern Africa"
        }
    }, {
        "arcs": [
            [-23, -481, 533, 534, -376, -360, -405, 535, -507, 536]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Saudi Arabia",
            "NAME_LONG": "Saudi Arabia",
            "ABBREV": "Saud.",
            "FORMAL_EN": "Kingdom of Saudi Arabia",
            "POP_EST": 28571770,
            "POP_RANK": 15,
            "GDP_MD_EST": 1731000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "SA",
            "ISO_A3": "SAU",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Western Asia"
        }
    }, {
        "arcs": [
            [-123, 537, -415, -247, 538, -253, -266, 539]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Sudan",
            "NAME_LONG": "Sudan",
            "ABBREV": "Sudan",
            "FORMAL_EN": "Republic of the Sudan",
            "POP_EST": 37345935,
            "POP_RANK": 15,
            "GDP_MD_EST": 176300,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "SD",
            "ISO_A3": "SDN",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Northern Africa"
        }
    }, {
        "arcs": [
            [-124, -540, -265, -392, 540, -198]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "S. Sudan",
            "NAME_LONG": "South Sudan",
            "ABBREV": "S. Sud.",
            "FORMAL_EN": "Republic of South Sudan",
            "POP_EST": 13026129,
            "POP_RANK": 14,
            "GDP_MD_EST": 20880,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "SS",
            "ISO_A3": "SSD",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Eastern Africa"
        }
    }, {
        "arcs": [
            [-296, -301, 541, -299, 542, -451, -435]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Senegal",
            "NAME_LONG": "Senegal",
            "ABBREV": "Sen.",
            "FORMAL_EN": "Republic of Senegal",
            "POP_EST": 14668522,
            "POP_RANK": 14,
            "GDP_MD_EST": 39720,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "SN",
            "ISO_A3": "SEN",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Western Africa"
        }
    }, {
        "arcs": [
            [
                [543]
            ],
            [
                [544]
            ],
            [
                [545]
            ],
            [
                [546]
            ],
            [
                [547]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Solomon Is.",
            "NAME_LONG": "Solomon Islands",
            "ABBREV": "S. Is.",
            "FORMAL_EN": "",
            "POP_EST": 647581,
            "POP_RANK": 11,
            "GDP_MD_EST": 1198,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "SB",
            "ISO_A3": "SLB",
            "CONTINENT": "Oceania",
            "REGION_UN": "Oceania",
            "SUBREGION": "Melanesia"
        }
    }, {
        "arcs": [
            [-293, -412, 548]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Sierra Leone",
            "NAME_LONG": "Sierra Leone",
            "ABBREV": "S.L.",
            "FORMAL_EN": "Republic of Sierra Leone",
            "POP_EST": 6163195,
            "POP_RANK": 13,
            "GDP_MD_EST": 10640,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "SL",
            "ISO_A3": "SLE",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Western Africa"
        }
    }, {
        "arcs": [
            [-310, -319, 549]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "El Salvador",
            "NAME_LONG": "El Salvador",
            "ABBREV": "El. S.",
            "FORMAL_EN": "Republic of El Salvador",
            "POP_EST": 6172011,
            "POP_RANK": 13,
            "GDP_MD_EST": 54790,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "SV",
            "ISO_A3": "SLV",
            "CONTINENT": "North America",
            "REGION_UN": "Americas",
            "SUBREGION": "Central America"
        }
    }, {
        "arcs": [
            [-230, 550, 551, -262]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Somaliland",
            "NAME_LONG": "Somaliland",
            "ABBREV": "Solnd.",
            "FORMAL_EN": "Republic of Somaliland",
            "POP_EST": 3500000,
            "POP_RANK": 12,
            "GDP_MD_EST": 12250,
            "POP_YEAR": 2013,
            "GDP_YEAR": 2013,
            "ISO_A2": "-99",
            "ISO_A3": "-99",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Eastern Africa"
        }
    }, {
        "arcs": [
            [-263, -552, 552, -388]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Somalia",
            "NAME_LONG": "Somalia",
            "ABBREV": "Som.",
            "FORMAL_EN": "Federal Republic of Somalia",
            "POP_EST": 7531386,
            "POP_RANK": 13,
            "GDP_MD_EST": 4719,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "SO",
            "ISO_A3": "SOM",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Eastern Africa"
        }
    }, {
        "arcs": [
            [-86, -434, -402, -441, -92, -324, -329, -508]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Serbia",
            "NAME_LONG": "Serbia",
            "ABBREV": "Serb.",
            "FORMAL_EN": "Republic of Serbia",
            "POP_EST": 7111024,
            "POP_RANK": 13,
            "GDP_MD_EST": 101800,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "RS",
            "ISO_A3": "SRB",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Southern Europe"
        }
    }, {
        "arcs": [
            [-110, -315, 553, -279]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Suriname",
            "NAME_LONG": "Suriname",
            "ABBREV": "Sur.",
            "FORMAL_EN": "Republic of Suriname",
            "POP_EST": 591919,
            "POP_RANK": 11,
            "GDP_MD_EST": 8547,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "SR",
            "ISO_A3": "SUR",
            "CONTINENT": "South America",
            "REGION_UN": "Americas",
            "SUBREGION": "South America"
        }
    }, {
        "arcs": [
            [-54, -221, -498, 554, -326]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Slovakia",
            "NAME_LONG": "Slovakia",
            "ABBREV": "Svk.",
            "FORMAL_EN": "Slovak Republic",
            "POP_EST": 5445829,
            "POP_RANK": 13,
            "GDP_MD_EST": 168800,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "SK",
            "ISO_A3": "SVK",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Eastern Europe"
        }
    }, {
        "arcs": [
            [-49, -330, -322, 555, -371]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Slovenia",
            "NAME_LONG": "Slovenia",
            "ABBREV": "Slo.",
            "FORMAL_EN": "Republic of Slovenia",
            "POP_EST": 1972126,
            "POP_RANK": 12,
            "GDP_MD_EST": 68350,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "SI",
            "ISO_A3": "SVN",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Southern Europe"
        }
    }, {
        "arcs": [
            [-267, 556, -470]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Sweden",
            "NAME_LONG": "Sweden",
            "ABBREV": "Swe.",
            "FORMAL_EN": "Kingdom of Sweden",
            "POP_EST": 9960487,
            "POP_RANK": 13,
            "GDP_MD_EST": 498100,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "SE",
            "ISO_A3": "SWE",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Northern Europe"
        }
    }, {
        "arcs": [
            [-446, 557]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Swaziland",
            "NAME_LONG": "Swaziland",
            "ABBREV": "Swz.",
            "FORMAL_EN": "Kingdom of Swaziland",
            "POP_EST": 1467152,
            "POP_RANK": 12,
            "GDP_MD_EST": 11060,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "SZ",
            "ISO_A3": "SWZ",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Southern Africa"
        }
    }, {
        "arcs": [
            [-362, -379, -367, -410, 558, 559]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Syria",
            "NAME_LONG": "Syria",
            "ABBREV": "Syria",
            "FORMAL_EN": "Syrian Arab Republic",
            "POP_EST": 18028549,
            "POP_RANK": 14,
            "GDP_MD_EST": 50280,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2015,
            "ISO_A2": "SY",
            "ISO_A3": "SYR",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Western Asia"
        }
    }, {
        "arcs": [
            [-122, -195, -464, -416, -538]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Chad",
            "NAME_LONG": "Chad",
            "ABBREV": "Chad",
            "FORMAL_EN": "Republic of Chad",
            "POP_EST": 12075985,
            "POP_RANK": 14,
            "GDP_MD_EST": 30590,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "TD",
            "ISO_A3": "TCD",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Middle Africa"
        }
    }, {
        "arcs": [
            [-69, 560, -290, -73]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Togo",
            "NAME_LONG": "Togo",
            "ABBREV": "Togo",
            "FORMAL_EN": "Togolese Republic",
            "POP_EST": 7965055,
            "POP_RANK": 13,
            "GDP_MD_EST": 11610,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "TG",
            "ISO_A3": "TGO",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Western Africa"
        }
    }, {
        "arcs": [
            [-395, 561, -459, 562, -438, -407]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Thailand",
            "NAME_LONG": "Thailand",
            "ABBREV": "Thai.",
            "FORMAL_EN": "Kingdom of Thailand",
            "POP_EST": 68414135,
            "POP_RANK": 16,
            "GDP_MD_EST": 1161000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "TH",
            "ISO_A3": "THA",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "South-Eastern Asia"
        }
    }, {
        "arcs": [
            [-3, 563, -393, -167]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Tajikistan",
            "NAME_LONG": "Tajikistan",
            "ABBREV": "Tjk.",
            "FORMAL_EN": "Republic of Tajikistan",
            "POP_EST": 8468555,
            "POP_RANK": 13,
            "GDP_MD_EST": 25810,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "TJ",
            "ISO_A3": "TJK",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Central Asia"
        }
    }, {
        "arcs": [
            [-1, -357, 564, -385, 565]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Turkmenistan",
            "NAME_LONG": "Turkmenistan",
            "ABBREV": "Turkm.",
            "FORMAL_EN": "Turkmenistan",
            "POP_EST": 5351277,
            "POP_RANK": 13,
            "GDP_MD_EST": 94720,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "TM",
            "ISO_A3": "TKM",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Central Asia"
        }
    }, {
        "arcs": [
            [-332, 566]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Timor-Leste",
            "NAME_LONG": "Timor-Leste",
            "ABBREV": "T.L.",
            "FORMAL_EN": "Democratic Republic of Timor-Leste",
            "POP_EST": 1291358,
            "POP_RANK": 12,
            "GDP_MD_EST": 4975,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "TL",
            "ISO_A3": "TLS",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "South-Eastern Asia"
        }
    }, {
        "arcs": [
            [567]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Trinidad and Tobago",
            "NAME_LONG": "Trinidad and Tobago",
            "ABBREV": "Tr.T.",
            "FORMAL_EN": "Republic of Trinidad and Tobago",
            "POP_EST": 1218208,
            "POP_RANK": 12,
            "GDP_MD_EST": 43570,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "TT",
            "ISO_A3": "TTO",
            "CONTINENT": "North America",
            "REGION_UN": "Americas",
            "SUBREGION": "Caribbean"
        }
    }, {
        "arcs": [
            [-242, 568, -413]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Tunisia",
            "NAME_LONG": "Tunisia",
            "ABBREV": "Tun.",
            "FORMAL_EN": "Republic of Tunisia",
            "POP_EST": 11403800,
            "POP_RANK": 14,
            "GDP_MD_EST": 130800,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "TN",
            "ISO_A3": "TUN",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Northern Africa"
        }
    }, {
        "arcs": [
            [
                [-36, -355, -363, -560, 569, -287]
            ],
            [
                [-83, 570, -304]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Turkey",
            "NAME_LONG": "Turkey",
            "ABBREV": "Tur.",
            "FORMAL_EN": "Republic of Turkey",
            "POP_EST": 80845215,
            "POP_RANK": 16,
            "GDP_MD_EST": 1670000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "TR",
            "ISO_A3": "TUR",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Western Asia"
        }
    }, {
        "arcs": [
            [571]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Taiwan",
            "NAME_LONG": "Taiwan",
            "ABBREV": "Taiwan",
            "FORMAL_EN": "",
            "POP_EST": 23508428,
            "POP_RANK": 15,
            "GDP_MD_EST": 1127000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "TW",
            "ISO_A3": "TWN",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Eastern Asia"
        }
    }, {
        "arcs": [
            [-62, -532, 572, -390, 573, -443, -455, 574, -201]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Tanzania",
            "NAME_LONG": "Tanzania",
            "ABBREV": "Tanz.",
            "FORMAL_EN": "United Republic of Tanzania",
            "POP_EST": 53950935,
            "POP_RANK": 16,
            "GDP_MD_EST": 150600,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "TZ",
            "ISO_A3": "TZA",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Eastern Africa"
        }
    }, {
        "arcs": [
            [-199, -541, -391, -573, -531]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Uganda",
            "NAME_LONG": "Uganda",
            "ABBREV": "Uga.",
            "FORMAL_EN": "Republic of Uganda",
            "POP_EST": 39570125,
            "POP_RANK": 15,
            "GDP_MD_EST": 84930,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "UG",
            "ISO_A3": "UGA",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Eastern Africa"
        }
    }, {
        "arcs": [
            [-96, -513, 575, -518, 576, -510, -428, -509, -327, -555, -497]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Ukraine",
            "NAME_LONG": "Ukraine",
            "ABBREV": "Ukr.",
            "FORMAL_EN": "Ukraine",
            "POP_EST": 44033874,
            "POP_RANK": 15,
            "GDP_MD_EST": 352600,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "UA",
            "ISO_A3": "UKR",
            "CONTINENT": "Europe",
            "REGION_UN": "Europe",
            "SUBREGION": "Eastern Europe"
        }
    }, {
        "arcs": [
            [-30, -113, 577]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Uruguay",
            "NAME_LONG": "Uruguay",
            "ABBREV": "Ury.",
            "FORMAL_EN": "Oriental Republic of Uruguay",
            "POP_EST": 3360148,
            "POP_RANK": 12,
            "GDP_MD_EST": 73250,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "UY",
            "ISO_A3": "URY",
            "CONTINENT": "South America",
            "REGION_UN": "Americas",
            "SUBREGION": "South America"
        }
    }, {
        "arcs": [
            [
                [-141, 578, -432, 579]
            ],
            [
                [-139, 580]
            ],
            [
                [581]
            ],
            [
                [582]
            ],
            [
                [583]
            ],
            [
                [584]
            ],
            [
                [585]
            ],
            [
                [586]
            ],
            [
                [587]
            ],
            [
                [588]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "United States of America",
            "NAME_LONG": "United States",
            "ABBREV": "U.S.A.",
            "FORMAL_EN": "United States of America",
            "POP_EST": 326625791,
            "POP_RANK": 17,
            "GDP_MD_EST": 18560000,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "US",
            "ISO_A3": "USA",
            "CONTINENT": "North America",
            "REGION_UN": "Americas",
            "SUBREGION": "Northern America"
        }
    }, {
        "arcs": [
            [-2, -566, -384, -394, -564]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Uzbekistan",
            "NAME_LONG": "Uzbekistan",
            "ABBREV": "Uzb.",
            "FORMAL_EN": "Republic of Uzbekistan",
            "POP_EST": 29748859,
            "POP_RANK": 15,
            "GDP_MD_EST": 202300,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "UZ",
            "ISO_A3": "UZB",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Central Asia"
        }
    }, {
        "arcs": [
            [-108, -210, 589, -313]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Venezuela",
            "NAME_LONG": "Venezuela",
            "ABBREV": "Ven.",
            "FORMAL_EN": "Bolivarian Republic of Venezuela",
            "POP_EST": 31304016,
            "POP_RANK": 15,
            "GDP_MD_EST": 468600,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "VE",
            "ISO_A3": "VEN",
            "CONTINENT": "South America",
            "REGION_UN": "Americas",
            "SUBREGION": "South America"
        }
    }, {
        "arcs": [
            [-175, 590, -397, -406]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Vietnam",
            "NAME_LONG": "Vietnam",
            "ABBREV": "Viet.",
            "FORMAL_EN": "Socialist Republic of Vietnam",
            "POP_EST": 96160163,
            "POP_RANK": 16,
            "GDP_MD_EST": 594900,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "VN",
            "ISO_A3": "VNM",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "South-Eastern Asia"
        }
    }, {
        "arcs": [
            [
                [591]
            ],
            [
                [592]
            ]
        ],
        "type": "MultiPolygon",
                "properties": {
            "NAME": "Vanuatu",
            "NAME_LONG": "Vanuatu",
            "ABBREV": "Van.",
            "FORMAL_EN": "Republic of Vanuatu",
            "POP_EST": 282814,
            "POP_RANK": 10,
            "GDP_MD_EST": 723,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "VU",
            "ISO_A3": "VUT",
            "CONTINENT": "Oceania",
            "REGION_UN": "Oceania",
            "SUBREGION": "Melanesia"
        }
    }, {
        "arcs": [
            [-480, 593, -534]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Yemen",
            "NAME_LONG": "Yemen",
            "ABBREV": "Yem.",
            "FORMAL_EN": "Republic of Yemen",
            "POP_EST": 28036829,
            "POP_RANK": 15,
            "GDP_MD_EST": 73450,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "YE",
            "ISO_A3": "YEM",
            "CONTINENT": "Asia",
            "REGION_UN": "Asia",
            "SUBREGION": "Western Asia"
        }
    }, {
        "arcs": [
            [-118, 594, -447, -558, -445, 595, -461],
            [-419]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "South Africa",
            "NAME_LONG": "South Africa",
            "ABBREV": "S.Af.",
            "FORMAL_EN": "Republic of South Africa",
            "POP_EST": 54841552,
            "POP_RANK": 16,
            "GDP_MD_EST": 739100,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "ZA",
            "ISO_A3": "ZAF",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Southern Africa"
        }
    }, {
        "arcs": [
            [-10, -202, -575, -454, -449, 596, -120, -460]
        ],
        "type": "Polygon",
                "properties": {
            "NAME": "Zambia",
            "NAME_LONG": "Zambia",
            "ABBREV": "Zambia",
            "FORMAL_EN": "Republic of Zambia",
            "POP_EST": 15972000,
            "POP_RANK": 14,
            "GDP_MD_EST": 65170,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "ZM",
            "ISO_A3": "ZMB",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Eastern Africa"
        }
    }, {
        "arcs": [
            [-121, -597, -448, -595]
        ],
        "type": "Polygon",
        "properties": {
            "NAME": "Zimbabwe",
            "NAME_LONG": "Zimbabwe",
            "ABBREV": "Zimb.",
            "FORMAL_EN": "Republic of Zimbabwe",
            "POP_EST": 13805084,
            "POP_RANK": 14,
            "GDP_MD_EST": 28330,
            "POP_YEAR": 2017,
            "GDP_YEAR": 2016,
            "ISO_A2": "ZW",
            "ISO_A3": "ZWE",
            "CONTINENT": "Africa",
            "REGION_UN": "Africa",
            "SUBREGION": "Eastern Africa"
        }
    }
]

country_capitals = [
    {
        "country": "Afghanistan",
        "city": "Kabul"
    },
    {
        "country": "Albania",
        "city": "Tirana"
    },
    {
        "country": "Algeria",
        "city": "Algiers"
    },
    {
        "country": "American Samoa",
        "city": "Pago Pago"
    },
    {
        "country": "Andorra",
        "city": "Andorra la Vella"
    },
    {
        "country": "Angola",
        "city": "Luanda"
    },
    {
        "country": "Anguilla",
        "city": "The Valley"
    },
    # {
    #     "country": "Antarctica",
    #     "city": null
    # },
    {
        "country": "Antigua and Barbuda",
        "city": "Saint John's"
    },
    {
        "country": "Argentina",
        "city": "Buenos Aires"
    },
    {
        "country": "Armenia",
        "city": "Yerevan"
    },
    {
        "country": "Aruba",
        "city": "Oranjestad"
    },
    {
        "country": "Australia",
        "city": "Canberra"
    },
    {
        "country": "Austria",
        "city": "Vienna"
    },
    {
        "country": "Azerbaijan",
        "city": "Baku"
    },
    {
        "country": "Bahamas",
        "city": "Nassau"
    },
    {
        "country": "Bahrain",
        "city": "Manama"
    },
    {
        "country": "Bangladesh",
        "city": "Dhaka"
    },
    {
        "country": "Barbados",
        "city": "Bridgetown"
    },
    {
        "country": "Belarus",
        "city": "Minsk"
    },
    {
        "country": "Belgium",
        "city": "Brussels"
    },
    {
        "country": "Belize",
        "city": "Belmopan"
    },
    {
        "country": "Benin",
        "city": "Porto-Novo"
    },
    {
        "country": "Bermuda",
        "city": "Hamilton"
    },
    {
        "country": "Bhutan",
        "city": "Thimphu"
    },
    {
        "country": "Bolivia",
        "city": "Sucre/La Paz"
    },
    {
        "country": "Bosnia and Herzegovina",
        "city": "Sarajevo"
    },
    {
        "country": "Botswana",
        "city": "Gaborone"
    },
    # {
    #     "country": "Bouvet Island",
    #     "city": null
    # },
    {
        "country": "Brazil",
        "city": "Brasilia"
    },
    # {
    #     "country": "British Indian Ocean Territory",
    #     "city": null
    # },
    {
        "country": "Brunei Darussalam",
        "city": "Bandar Seri Begawan"
    },
    {
        "country": "Bulgaria",
        "city": "Sofia"
    },
    {
        "country": "Burkina Faso",
        "city": "Ouagadougou"
    },
    {
        "country": "Burundi",
        "city": "Gitega"
    },
    {
        "country": "Cambodia",
        "city": "Phnom Penh"
    },
    {
        "country": "Cameroon",
        "city": "Yaound"
    },
    {
        "country": "Canada",
        "city": "Ottawa"
    },
    {
        "country": "Cape Verde",
        "city": "Praia"
    },
    {
        "country": "Cayman Islands",
        "city": "George Town"
    },
    {
        "country": "Central African Republic",
        "city": "Bangui"
    },
    {
        "country": "Chad",
        "city": "N'Djam"
    },
    {
        "country": "Chile",
        "city": "Santiago de Chile"
    },
    {
        "country": "China",
        "city": "Peking"
    },
    {
        "country": "Christmas Island",
        "city": "Flying Fish Cove"
    },
    {
        "country": "Cocos (Keeling) Islands",
        "city": "West Island"
    },
    {
        "country": "Colombia",
        "city": "Santaf"
    },
    {
        "country": "Comoros",
        "city": "Moroni"
    },
    {
        "country": "Republic of the Congo",
        "city": "Brazzaville"
    },
    {
        "country": "Cook Islands",
        "city": "Avarua"
    },
    {
        "country": "Costa Rica",
        "city": "San Jos"
    },
    {
        "country": "Croatia",
        "city": "Zagreb"
    },
    {
        "country": "Cuba",
        "city": "La Habana"
    },
    {
        "country": "Cyprus",
        "city": "Nicosia"
    },
    {
        "country": "Northern Cyprus",
        "city": "North Nicosia"
    },
    {
        "country": "Czech Republic",
        "city": "Praha"
    },
    {
        "country": "Denmark",
        "city": "Copenhagen"
    },
    {
        "country": "Djibouti",
        "city": "Djibouti"
    },
    {
        "country": "Dominica",
        "city": "Roseau"
    },
    {
        "country": "Dominican Republic",
        "city": "Santo Domingo de Guzm"
    },
    {
        "country": "Timor-Leste",
        "city": "Dili"
    },
    {
        "country": "Ecuador",
        "city": "Quito"
    },
    {
        "country": "Egypt",
        "city": "Cairo"
    },
    {
        "country": "El Salvador",
        "city": "San Salvador"
    },
    {
        "country": "England",
        "city": "London"
    },
    {
        "country": "Equatorial Guinea",
        "city": "Malabo"
    },
    {
        "country": "Eritrea",
        "city": "Asmara"
    },
    {
        "country": "Estonia",
        "city": "Tallinn"
    },
    {
        "country": "Ethiopia",
        "city": "Addis Abeba"
    },
    {
        "country": "Falkland Islands",
        "city": "Stanley"
    },
    {
        "country": "Faroe Islands",
        "city": "Tórshavn"
    },
    {
        "country": "Fiji",
        "city": "Suva"
    },
    {
        "country": "Finland",
        "city": "Helsinki"
    },
    {
        "country": "France",
        "city": "Paris"
    },
    {
        "country": "French Guiana",
        "city": "Cayenne"
    },
    {
        "country": "French Polynesia",
        "city": "Papeete"
    },
    # {
    #     "country": "French Southern territories",
    #     "city": null
    # },
    {
        "country": "Gabon",
        "city": "Libreville"
    },
    {
        "country": "The Gambia",
        "city": "Banjul"
    },
    {
        "country": "Georgia",
        "city": "Tbilisi"
    },
    {
        "country": "Germany",
        "city": "Berlin"
    },
    {
        "country": "Ghana",
        "city": "Accra"
    },
    {
        "country": "Gibraltar",
        "city": "Gibraltar"
    },
    {
        "country": "Greece",
        "city": "Athenai"
    },
    {
        "country": "Greenland",
        "city": "Nuuk"
    },
    {
        "country": "Grenada",
        "city": "Saint George's"
    },
    {
        "country": "Guadeloupe",
        "city": "Basse-Terre"
    },
    {
        "country": "Guam",
        "city": "Aga"
    },
    {
        "country": "Guatemala",
        "city": "Ciudad de Guatemala"
    },
    {
        "country": "Guinea",
        "city": "Conakry"
    },
    {
        "country": "Guinea-Bissau",
        "city": "Bissau"
    },
    {
        "country": "Guyana",
        "city": "Georgetown"
    },
    {
        "country": "Haiti",
        "city": "Port-au-Prince"
    },
    # {
    #     "country": "Heard Island and McDonald Islands",
    #     "city": null
    # },
    {
        "country": "Holy See (Vatican City State)",
        "city": "Citt"
    },
    {
        "country": "Honduras",
        "city": "Tegucigalpa"
    },
    {
        "country": "Hong Kong",
        "city": "Victoria"
    },
    {
        "country": "Hungary",
        "city": "Budapest"
    },
    {
        "country": "Iceland",
        "city": "Reykjav"
    },
    {
        "country": "India",
        "city": "New Delhi"
    },
    {
        "country": "Indonesia",
        "city": "Jakarta"
    },
    {
        "country": "Iran",
        "city": "Tehran"
    },
    {
        "country": "Iraq",
        "city": "Baghdad"
    },
    {
        "country": "Ireland",
        "city": "Dublin"
    },
    {
        "country": "Israel",
        "city": "Jerusalem"
    },
    {
        "country": "Italy",
        "city": "Roma"
    },
    {
        "country": "Côte d'Ivoire",
        "city": "Yamoussoukro"
    },
    {
        "country": "Jamaica",
        "city": "Kingston"
    },
    {
        "country": "Japan",
        "city": "Tokyo"
    },
    {
        "country": "Jordan",
        "city": "Amman"
    },
    {
        "country": "Kazakhstan",
        "city": "Astana"
    },
    {
        "country": "Kenya",
        "city": "Nairobi"
    },
    {
        "country": "Kiribati",
        "city": "Bairiki"
    },
    {
        "country": "Kosovo",
        "city": "Prishtina"
    },
    {
        "country": "Kuwait",
        "city": "Kuwait"
    },
    {
        "country": "Kyrgyzstan",
        "city": "Bishkek"
    },
    {
        "country": "Lao PDR",
        "city": "Vientiane"
    },
    {
        "country": "Latvia",
        "city": "Riga"
    },
    {
        "country": "Lebanon",
        "city": "Beirut"
    },
    {
        "country": "Lesotho",
        "city": "Maseru"
    },
    {
        "country": "Liberia",
        "city": "Monrovia"
    },
    {
        "country": "Libya",
        "city": "Tripoli"
    },
    {
        "country": "Liechtenstein",
        "city": "Vaduz"
    },
    {
        "country": "Lithuania",
        "city": "Vilnius"
    },
    {
        "country": "Luxembourg",
        "city": "Luxembourg [Luxemburg/L"
    },
    {
        "country": "Macao",
        "city": "Macao"
    },
    {
        "country": "Macedonia",
        "city": "Skopje"
    },
    {
        "country": "Madagascar",
        "city": "Antananarivo"
    },
    {
        "country": "Malawi",
        "city": "Lilongwe"
    },
    {
        "country": "Malaysia",
        "city": "Kuala Lumpur"
    },
    {
        "country": "Maldives",
        "city": "Male"
    },
    {
        "country": "Mali",
        "city": "Bamako"
    },
    {
        "country": "Malta",
        "city": "Valletta"
    },
    {
        "country": "Marshall Islands",
        "city": "Dalap-Uliga-Darrit"
    },
    {
        "country": "Martinique",
        "city": "Fort-de-France"
    },
    {
        "country": "Mauritania",
        "city": "Nouakchott"
    },
    {
        "country": "Mauritius",
        "city": "Port-Louis"
    },
    {
        "country": "Mayotte",
        "city": "Mamoutzou"
    },
    {
        "country": "Mexico",
        "city": "Ciudad de M"
    },
    {
        "country": "Micronesia, Federated States of",
        "city": "Palikir"
    },
    {
        "country": "Moldova",
        "city": "Chisinau"
    },
    {
        "country": "Monaco",
        "city": "Monaco-Ville"
    },
    {
        "country": "Mongolia",
        "city": "Ulan Bator"
    },
    {
        "country": "Montenegro",
        "city": "Podgorica"
    },
    {
        "country": "Montserrat",
        "city": "Plymouth"
    },
    {
        "country": "Morocco",
        "city": "Rabat"
    },
    {
        "country": "Mozambique",
        "city": "Maputo"
    },
    {
        "country": "Myanmar",
        "city": "Rangoon (Yangon)"
    },
    {
        "country": "Namibia",
        "city": "Windhoek"
    },
    {
        "country": "Nauru",
        "city": "Yaren"
    },
    {
        "country": "Nepal",
        "city": "Kathmandu"
    },
    {
        "country": "Netherlands",
        "city": "Amsterdam"
    },
    {
        "country": "Netherlands Antilles",
        "city": "Willemstad"
    },
    {
        "country": "New Caledonia",
        "city": "Noum"
    },
    {
        "country": "New Zealand",
        "city": "Wellington"
    },
    {
        "country": "Nicaragua",
        "city": "Managua"
    },
    {
        "country": "Niger",
        "city": "Niamey"
    },
    {
        "country": "Nigeria",
        "city": "Abuja"
    },
    {
        "country": "Niue",
        "city": "Alofi"
    },
    {
        "country": "Norfolk Island",
        "city": "Kingston"
    },
    {
        "country": "Dem. Rep. Korea",
        "city": "Pyongyang"
    },
    {
        "country": "Northern Ireland",
        "city": "Belfast"
    },
    {
        "country": "Northern Mariana Islands",
        "city": "Garapan"
    },
    {
        "country": "Norway",
        "city": "Oslo"
    },
    {
        "country": "Oman",
        "city": "Masqat"
    },
    {
        "country": "Pakistan",
        "city": "Islamabad"
    },
    {
        "country": "Palau",
        "city": "Koror"
    },
    {
        "country": "Palestine",
        "city": "Gaza"
    },
    {
        "country": "Panama",
        "city": "Ciudad de Panam"
    },
    {
        "country": "Papua New Guinea",
        "city": "Port Moresby"
    },
    {
        "country": "Paraguay",
        "city": "Asunci"
    },
    {
        "country": "Peru",
        "city": "Lima"
    },
    {
        "country": "Philippines",
        "city": "Manila"
    },
    {
        "country": "Pitcairn",
        "city": "Adamstown"
    },
    {
        "country": "Poland",
        "city": "Warszawa"
    },
    {
        "country": "Portugal",
        "city": "Lisboa"
    },
    {
        "country": "Puerto Rico",
        "city": "San Juan"
    },
    {
        "country": "Qatar",
        "city": "Doha"
    },
    {
        "country": "Reunion",
        "city": "Saint-Denis"
    },
    {
        "country": "Romania",
        "city": "Bucuresti"
    },
    {
        "country": "Russian Federation",
        "city": "Moscow"
    },
    {
        "country": "Rwanda",
        "city": "Kigali"
    },
    {
        "country": "Saint Helena",
        "city": "Jamestown"
    },
    {
        "country": "Saint Kitts and Nevis",
        "city": "Basseterre"
    },
    {
        "country": "Saint Lucia",
        "city": "Castries"
    },
    {
        "country": "Saint Pierre and Miquelon",
        "city": "Saint-Pierre"
    },
    {
        "country": "Saint Vincent and the Grenadines",
        "city": "Kingstown"
    },
    {
        "country": "Samoa",
        "city": "Apia"
    },
    {
        "country": "San Marino",
        "city": "San Marino"
    },
    {
        "country": "Sao Tome and Principe",
        "city": "S"
    },
    {
        "country": "Saudi Arabia",
        "city": "Riyadh"
    },
    {
        "country": "Scotland",
        "city": "Edinburgh"
    },
    {
        "country": "Senegal",
        "city": "Dakar"
    },
    {
        "country": "Serbia",
        "city": "Belgrade"
    },
    {
        "country": "Seychelles",
        "city": "Victoria"
    },
    {
        "country": "Sierra Leone",
        "city": "Freetown"
    },
    {
        "country": "Singapore",
        "city": "Singapore"
    },
    {
        "country": "Slovakia",
        "city": "Bratislava"
    },
    {
        "country": "Slovenia",
        "city": "Ljubljana"
    },
    {
        "country": "Solomon Islands",
        "city": "Honiara"
    },
    {
        "country": "Somalia",
        "city": "Mogadishu"
    },
    {
        "country": "Somaliland",
        "city": "Hargeisa"
    },
    {
        "country": "South Africa",
        "city": "Pretoria"
    },
    # {
    #     "country": "South Georgia and the South Sandwich Islands",
    #     "city": null
    # },
    {
        "country": "Republic of Korea",
        "city": "Seoul"
    },
    {
        "country": "South Sudan",
        "city": "Juba"
    },
    {
        "country": "Spain",
        "city": "Madrid"
    },
    {
        "country": "Sri Lanka",
        "city": "Sri Jayawardenepura Kotte"
    },
    {
        "country": "Sudan",
        "city": "Khartum"
    },
    {
        "country": "Suriname",
        "city": "Paramaribo"
    },
    {
        "country": "Svalbard and Jan Mayen",
        "city": "Longyearbyen"
    },
    {
        "country": "Swaziland",
        "city": "Mbabane"
    },
    {
        "country": "Sweden",
        "city": "Stockholm"
    },
    {
        "country": "Switzerland",
        "city": "Bern"
    },
    {
        "country": "Syria",
        "city": "Damascus"
    },
    {
        "country": "Taiwan",
        "city": "Taipei"
    },
    {
        "country": "Tajikistan",
        "city": "Dushanbe"
    },
    {
        "country": "Tanzania",
        "city": "Dodoma"
    },
    {
        "country": "Thailand",
        "city": "Bangkok"
    },
    {
        "country": "Democratic Republic of the Congo",
        "city": "Kinshasa"
    },
    {
        "country": "Togo",
        "city": "Lom"
    },
    {
        "country": "Tokelau",
        "city": "Fakaofo"
    },
    {
        "country": "Tonga",
        "city": "Nuku'alofa"
    },
    {
        "country": "Trinidad and Tobago",
        "city": "Port-of-Spain"
    },
    {
        "country": "Tunisia",
        "city": "Tunis"
    },
    {
        "country": "Turkey",
        "city": "Ankara"
    },
    {
        "country": "Turkmenistan",
        "city": "Ashgabat"
    },
    {
        "country": "Turks and Caicos Islands",
        "city": "Cockburn Town"
    },
    {
        "country": "Tuvalu",
        "city": "Funafuti"
    },
    {
        "country": "Uganda",
        "city": "Kampala"
    },
    {
        "country": "Ukraine",
        "city": "Kyiv"
    },
    {
        "country": "United Arab Emirates",
        "city": "Abu Dhabi"
    },
    {
        "country": "United Kingdom",
        "city": "London"
    },
    {
        "country": "United States",
        "city": "Washington"
    },
    # {
    #     "country": "United States Minor Outlying Islands",
    #     "city": null
    # },
    {
        "country": "Uruguay",
        "city": "Montevideo"
    },
    {
        "country": "Uzbekistan",
        "city": "Toskent"
    },
    {
        "country": "Vanuatu",
        "city": "Port-Vila"
    },
    {
        "country": "Venezuela",
        "city": "Caracas"
    },
    {
        "country": "Vietnam",
        "city": "Hanoi"
    },
    {
        "country": "Virgin Islands, British",
        "city": "Road Town"
    },
    {
        "country": "Virgin Islands, U.S.",
        "city": "Charlotte Amalie"
    },
    {
        "country": "Wales",
        "city": "Cardiff"
    },
    {
        "country": "Wallis and Futuna",
        "city": "Mata-Utu"
    },
    {
        "country": "Western Sahara",
        "city": "El-Aai"
    },
    {
        "country": "Yemen",
        "city": "Sanaa"
    },
    {
        "country": "Yugoslavia",
        "city": "Beograd"
    },
    {
        "country": "Zambia",
        "city": "Lusaka"
    },
    {
        "country": "Zimbabwe",
        "city": "Harare"
    }
]

map_capitals = {}

for stats in topo_data:
    country = (stats["properties"])["NAME_LONG"]
    map_capitals[country] = None

for country_capital in country_capitals:
    country = country_capital["country"]
    capital = country_capital["city"]

    try:
        map_capitals[country] = capital
    except KeyError:
        print(f"{country} not on map")

countries = []

for country, capital in map_capitals.items():
    if capital == None:
        print(f"{country} has no capital")

    countries.append(
        {
            "name": country,
            "capital": capital
        }
    )

print(json.dumps(countries))
