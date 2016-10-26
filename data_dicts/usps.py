# From table C2 on pg 72 of http://pe.usps.gov/cpim/ftp/pubs/Pub28/pub28.pdf
usps_unit_designators = {
    'LOWER': 'LOWR', 'OFFICE': 'OFC', 'FLR': 'FL', 'STOP': 'STOP',
    'HANGER': 'HNGR', 'LOT': 'LOT', 'SUITE': 'STE', 'REAR': 'REAR',
    'PENTHOUSE': 'PH', 'ROOM': 'RM', 'SPACE': 'SPC', 'UNIT': 'UNIT',
    'FRONT': 'FRNT', 'LOBBY': 'LBBY', 'APARTMENT': 'APT', 'FLOOR': 'FL',
    'DEPARTMENT': 'DEPT', 'SLIP': 'SLIP', 'BASEMENT': 'BSMT', 'PIER': 'PIER',
    'TRAILER': 'TRLR', 'BUILDING': 'BLDG', 'UPPER': 'UPPR', 'SUTIE': 'STE',
    'KEY': 'KEY', 'SIDE': 'SIDE'
}

# Add custom
usps_unit_designators['FLR'] = 'FL'

usps_unit_designators['NO'] = '#'
usps_unit_designators['NUMBER'] = '#'
usps_unit_designators['CONDO'] = '#'

usps_unit_designators['SUTIE'] = 'STE'
usps_unit_designators['SIOTE'] = 'STE'
usps_unit_designators['SITE'] = 'STE'
usps_unit_designators['STE:'] = 'STE'
usps_unit_designators['SUTE'] = 'STE'
usps_unit_designators['SUIT'] = 'STE'


usps_unit_designators['UNTI'] = 'UNIT'
usps_unit_designators['UNITE'] = 'UNIT'
usps_unit_designators['UNIY'] = 'UNIT'
usps_unit_designators['UNITE'] = 'UNIT'
usps_unit_designators['UNIT, UNIT'] = 'UNIT'


usps_unit_designators['APT. APT'] = 'APT'
usps_unit_designators['APPT'] = 'APT'
# usps_unit_designators[''] = ''
