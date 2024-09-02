import bibtexparser

from pais_accomplishments_tool.model import AccLibrary


class TestLibrary:

    def test_true_amount_entries_into_bibtex_file(self):
        l = AccLibrary('sample_data/accomplishments_sample.bib')
        assert len(l.content) == 5

    def test_content_type(self):
        l = AccLibrary('sample_data/accomplishments_sample.bib')
        assert isinstance(l.content, list)
        assert any(isinstance(entry, bibtexparser.library.Entry) for entry in l.content)

    def test_check_datetime_fields(self):
        # _keys = {
        #     'rand1': {
        #         'start': datetime.datetime.strptime('15.02.2023', "%d.%m.%Y"),
        #         'end': datetime.datetime.strptime('15.02.2023', "%d.%m.%Y"),
        #     },
        #     'rand2': {
        #         'start': datetime.datetime.strptime('10.04.2023', "%d.%m.%Y"),
        #         'end': datetime.datetime.strptime('10.04.2023', "%d.%m.%Y"),
        #     },
        #     'rand3': {
        #         'start': datetime.datetime.strptime('20.06.2023', "%d.%m.%Y"),
        #         'end': datetime.datetime.strptime('20.06.2023', "%d.%m.%Y"),
        #     },
        #     'rand4': {
        #         'start': datetime.datetime.strptime('15.09.2023', "%d.%m.%Y"),
        #         'end': datetime.datetime.strptime('15.09.2023', "%d.%m.%Y"),
        #     },
        #     'conf1': {
        #         'start': datetime.datetime.strptime('11.04.2023', "%d.%m.%Y"),
        #         'end': datetime.datetime.strptime('15.04.2023', "%d.%m.%Y"),
        #     },
        # }
        _keys = {
            'rand1': {
                'start': '15.02.2023',
                'end': '15.02.2023',
            },
            'rand2': {
                'start': '10.04.2023',
                'end': '10.04.2023',
            },
            'rand3': {
                'start': '20.06.2023',
                'end': '20.06.2023',
            },
            'rand4': {
                'start': '15.09.2023',
                'end': '15.09.2023',
            },
            'conf1': {
                'start': '11.04.2023',
                'end': '15.04.2023',
            },
        }

        l = AccLibrary('sample_data/accomplishments_sample.bib')
        for entry in l.content:
            assert entry.get('start').value == _keys[entry.key].get('start')
            assert entry.get('end').value == _keys[entry.key].get('end')
