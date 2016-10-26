import usaddress

from replacement_dicts import (
    state_replacement_dict,
    street_type_replacement_dict,
    street_direction_replacement_dict
)

from data_dict import usps_unit_designators

fields_to_strip_periods = [
    'StreetNamePostType', 'StreetNamePreDirectional', 'AddressNumberSuffix',
    'StreetNamePostModifier', 'StreetNamePostDirectional', 'OccupancyType',
    'SubaddressType', 'SecondStreetNamePostType', 'USPSBoxGroupType'
]


def standardize_us_address(mailing_address):

    """
    This function takes an text address (street address, city, state, zip),
    tokenizes it with the usaddress library, and runs basic search and replace
    to help standardize the address

    """

    try:
        usaddress_address = usaddress.tag(mailing_address)

        # print 'usaddress addy:', usaddress_address

        address_dict = dict(usaddress_address[0])

        address_type = usaddress_address[1]
        address_dict['address_type'] = address_type
        address_dict['original_address'] = mailing_address

        # Make sure we're using state abbreviation instead of full state name
        if ('StateName' in address_dict and
                address_dict['StateName'] in state_replacement_dict):

            address_dict['StateName'] = state_replacement_dict[
                                            address_dict['StateName']]

        # Remove trailing '.' from any abbreviations
        for field in fields_to_strip_periods:
            if field in address_dict:
                address_dict[field] = address_dict[field].strip('.')

        # Use standard abbreviated for street direction (N instead of North)
        if 'StreetNamePreDirectional' in address_dict:
            address_dict['StreetNamePreDirectional'] = address_dict['StreetNamePreDirectional'].strip().replace(' ', '').replace('.', '')
            if address_dict['StreetNamePreDirectional'] in street_direction_replacement_dict:
                address_dict['StreetNamePreDirectional'] = street_direction_replacement_dict[address_dict['StreetNamePreDirectional']]

        if 'StreetNamePostDirectional' in address_dict:
            address_dict['StreetNamePostDirectional'] = address_dict['StreetNamePostDirectional'].strip().replace(' ', '').replace('.', '')
            if address_dict['StreetNamePostDirectional'] in street_direction_replacement_dict:
                address_dict['StreetNamePostDirectional'] = street_direction_replacement_dict[address_dict['StreetNamePostDirectional']]

        if 'SecondStreetNamePostDirectional' in address_dict:
            address_dict['SecondStreetNamePostDirectional'] = address_dict['SecondStreetNamePostDirectional'].strip().replace(' ', '').replace('.', '')
            if address_dict['SecondStreetNamePostDirectional'] in street_direction_replacement_dict:
                address_dict['SecondStreetNamePostDirectional'] = street_direction_replacement_dict[address_dict['SecondStreetNamePostDirectional']]

        # Use standard abbreviated for street type (Rd instead of Road)
        if 'StreetNamePostType' in address_dict and address_dict['StreetNamePostType'].strip() in street_type_replacement_dict:
                address_dict['StreetNamePostType'] = street_type_replacement_dict[address_dict['StreetNamePostType'].strip()]

        if 'SecondStreetNamePostType' in address_dict and address_dict['SecondStreetNamePostType'].strip() in street_type_replacement_dict:
                address_dict['SecondStreetNamePostType'] = street_type_replacement_dict[address_dict['SecondStreetNamePostType'].strip()]

        if 'USPSBoxGroupType' in address_dict and address_dict['USPSBoxGroupType'].strip() in street_type_replacement_dict:
                address_dict['USPSBoxGroupType'] = street_type_replacement_dict[address_dict['USPSBoxGroupType'].strip()]

        # Standardize unit types
        if 'OccupancyType' in address_dict and address_dict['OccupancyType'].strip() in usps_unit_designators:
                address_dict['OccupancyType'] = usps_unit_designators[address_dict['OccupancyType'].strip()]

        if 'SubaddressType' in address_dict and address_dict['SubaddressType'].strip() in usps_unit_designators:
                address_dict['SubaddressType'] = usps_unit_designators[address_dict['SubaddressType'].strip()]

        # Remove preceiding '#' from OccupancyIdentifier
        if 'OccupancyIdentifier' in address_dict and address_dict['OccupancyIdentifier'][0] == '#':
            address_dict['OccupancyIdentifier'] = address_dict['OccupancyIdentifier'].strip('#').strip()

            # If OccupancyType is not set, and OccupancyIdentifier is set, and OccupancyIdentifier starts with '#'
            # then make '#' the OccupancyType
            if 'OccupancyType' not in address_dict:
                address_dict['OccupancyType'] = '#'

        # If USPSBoxType is set, just make it 'PO BOX'
        if 'USPSBoxType' in address_dict:
            address_dict['USPSBoxType'] = 'PO BOX'

        # Only connect multiple streets with '&'
        if 'IntersectionSeparator' in address_dict and address_dict['IntersectionSeparator'] == 'AND':
            address_dict['IntersectionSeparator'] = '&'

        # Only use first 5 digits in zip code, don't care about extended
        if 'ZipCode' in address_dict and len(address_dict['ZipCode']) > 5:
            address_dict['ZipCode'] = ''.join([i for i in address_dict['ZipCode'] if i.isdigit()])[:5]

        # Clean up state name. Remove ', DE' if length is 6 and last three == ', DE'
        if 'StateName' in address_dict and len(address_dict['StateName']) == 6 and address_dict['StateName'][2:] == ', DE':
            address_dict['StateName'] = address_dict['StateName'][:2]

        return address_dict

    # TODO: Replace with a less broad exception
    except Exception as err:

        print('usaddress ERROR:')
        print(err)

        return err
