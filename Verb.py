forms = [
    'inf-form-of',
    'pres|act|part-form-of',
    'past|act|part-form-of',
    'pres|pass|part-form-of',
    'past|pass|part-form-of',
    'pres|adv|part-form-of',
    'past|adv|part-form-of',
    'past|adv|part-form-of',
    '1|s|pres|ind-form-of',
    '2|s|pres|ind-form-of',
    '3|s|pres|ind-form-of',
    '1|p|pres|ind-form-of',
    '2|p|pres|ind-form-of',
    '3|p|pres|ind-form-of',
    '2|s|imp-form-of',
    '2|p|imp-form-of',
    'm|s|past|ind-form-of',
    'p|past|ind-form-of',
    'f|s|past|ind-form-of',
    'n|s|past|ind-form-of'
]


class Verb:
    """docstring for Verb."""

    conjugation = {}
    english = []

    def __init__(self, conjugation, english):
        self.conjugation = conjugation
        self.english = english

    def conjugations(self):
        return {
            'infinitive' : self.conjugation['inf-form-of'],
            'past' : {
                'male' : self.conjugation['m|s|past|ind-form-of'],
                'female' : self.conjugation['f|s|past|ind-form-of'],
                'neuter' : self.conjugation['n|s|past|ind-form-of'],
                'plural' : self.conjugation['p|past|ind-form-of']
            },
            'present' : {
                'singular' : {
                    'first' : self.conjugation['1|s|pres|ind-form-of'],
                    'second' : self.conjugation['2|s|pres|ind-form-of'],
                    'third' : self.conjugation['3|s|pres|ind-form-of']
                },
                'plural' : {
                    'first' : self.conjugation['1|p|pres|ind-form-of'],
                    'second' : self.conjugation['2|p|pres|ind-form-of'],
                    'third' : self.conjugation['3|p|pres|ind-form-of']
                }
            },
            'participles' : {
                'present' : {
                    'passive' : self.conjugation['pres|pass|part-form-of'],
                    'active:' : self.conjugation['pres|act|part-form-of']
                },
                'past' : {
                    'passive' : self.conjugation['past|pass|part-form-of'],
                    'active:' : self.conjugation['past|act|part-form-of']
                }
            },
            'imperative' : self.conjugation['2|s|imp-form-of'],
            'gerund' : self.conjugation['pres|adv|part-form-of'],
            'english' : self.english
        }

def new_sub_verb():
    sv = {
        'title' : '',
        'english' : '',
        'inf-form-of' : '',
        'pres|act|part-form-of' : '',
        'past|act|part-form-of' : '',
        'pres|pass|part-form-of' : '',
        'past|pass|part-form-of' : '',
        'pres|adv|part-form-of' : '',
        'past|adv|part-form-of' : '',
        '1|s|pres|ind-form-of' : '',
        '2|s|pres|ind-form-of' : '',
        '3|s|pres|ind-form-of' : '',
        '1|p|pres|ind-form-of' : '',
        '2|p|pres|ind-form-of' : '',
        '3|p|pres|ind-form-of' : '',
        '2|s|imp-form-of' : '',
        '2|p|imp-form-of' : '',
        'm|s|past|ind-form-of' : '',
        'p|past|ind-form-of' : '',
        'f|s|past|ind-form-of' : '',
        'n|s|past|ind-form-of' : ''
    }
    return sv

htmltodb = {
    'title' : 'title',
    'english' : 'english',
    'inf-form-of' : 'inf',
    'pres|act|part-form-of' : 'pres_act_part',
    'past|act|part-form-of' : 'past_act_part',
    'pres|pass|part-form-of' : 'pres_pass_part',
    'past|pass|part-form-of' : 'past_pass_part',
    'pres|adv|part-form-of' : 'pres_adv_part',
    'past|adv|part-form-of' : 'past_adv_part',
    '1|s|pres|ind-form-of' : '_1_s_pres_ind',
    '2|s|pres|ind-form-of' : '_2_s_pres_ind',
    '3|s|pres|ind-form-of' : '_3_s_pres_ind',
    '1|p|pres|ind-form-of' : '_1_p_pres_ind',
    '2|p|pres|ind-form-of' : '_2_p_pres_ind',
    '3|p|pres|ind-form-of' : '_3_p_pres_ind',
    '2|s|imp-form-of' : '_2_s_imp',
    '2|p|imp-form-of' : '_2_p_imp',
    'm|s|past|ind-form-of' : 'm_s_past_ind',
    'p|past|ind-form-of' : 'p_past_ind',
    'f|s|past|ind-form-of' : 'f_s_past_ind',
    'n|s|past|ind-form-of' : 'n_s_past_ind'
}

dbtohum = {
    'inf' : 'infinitive',
    'pres_act_part' : 'active participle present tense',
    'past_act_part' : 'active participle past tense',
    'pres_pass_part' : 'passive participle present tense',
    'past_pass_part' : 'passive participle past tense',
    'pres_adv_part' : 'adverbial participle present tense',
    'past_adv_part' : 'adverbial participle past tense',
    '_1_s_pres_ind' : '1st person singular',
    '_2_s_pres_ind' : '2nd person singular',
    '_3_s_pres_ind' : '3rd person singular',
    '_1_p_pres_ind' : '1st person plural',
    '_2_p_pres_ind' : '2nd person plural',
    '_3_p_pres_ind' : '3rd person plural',
    '_2_s_imp' : 'imperative singular',
    '_2_p_imp' : 'imperative plural',
    'm_s_past_ind' : 'male past tense',
    'p_past_ind' : 'plural past tense',
    'f_s_past_ind' : 'female past tense',
    'n_s_past_ind' : 'neuter past tense'
}
