# pylint: disable=line-too-long
from datetime import date
from src.stages.contracts.extract_contract import ExtractContract

extract_contract_mock = ExtractContract(
    raw_information_content=[
        {'name': 'Zanini, Giuseppe', 'link': 'http://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=11597'},
        {'name': 'Zanini-Viola, Giuseppe', 'link': 'http://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=11597'},
        {'name': 'Zanotti, Giampietro', 'link': 'http://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=11631'},
        {'name': 'Zao Wou-Ki', 'link': 'http://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=3427'},
        {'name': 'Zas-Zie', 'link': 'http://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ2.htm'},
        {'name': 'Zie-Zor', 'link': 'http://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ3.htm'},
        {'name': '<strong>next<br/>page</strong>', 'link': 'http://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ4.htm'}
    ],
    extraction_date=date.today()
)
