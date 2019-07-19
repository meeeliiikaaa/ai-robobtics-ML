from itertools import chain, combinations

ID_FIELD, DATE_FIELD, ORG_FIELD, TLD_FIELD, CCS_FIELD, BCCED_FIELD, MAIL_TYPE_FIELD, IMAGES_FIELD, URLS_FIELD, SALUTATIONS_FIELD, DESIGNATION_FIELD, CHARS_IN_SUBJECT_FIELD, CHARS_IN_BODY_FIELD, LABEL_FIELD = 'Id', 'date', 'org', 'tld', 'ccs', 'bcced', 'mail_type', 'images', 'urls', 'salutations', 'designation', 'chars_in_subject', 'chars_in_body', 'label'

QUANTITATIVE_FIELD_NAMES = [ CCS_FIELD, BCCED_FIELD, IMAGES_FIELD, URLS_FIELD, SALUTATIONS_FIELD, DESIGNATION_FIELD, CHARS_IN_SUBJECT_FIELD, CHARS_IN_BODY_FIELD ]

ALL_FIELDS = [ ORG_FIELD, TLD_FIELD, CCS_FIELD, BCCED_FIELD, MAIL_TYPE_FIELD, IMAGES_FIELD, URLS_FIELD, SALUTATIONS_FIELD, DESIGNATION_FIELD, CHARS_IN_SUBJECT_FIELD, CHARS_IN_BODY_FIELD, LABEL_FIELD ]

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)))
