from urllib import parse as p


def parse(query: str) -> dict:
    values = p.urlsplit(query).query
    data = dict(p.parse_qsl(values))
    return data


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

    assert parse('https://example.com/sometest1/test1?someValue2=value2') == {'someValue2': 'value2'}
    assert parse('https://example.com/sometest12/test2/test?eleven=11') == {'eleven': '11'}
    assert parse('http://example.com/sometest3/test/test1?boolean=False') == {'boolean': 'False'}
    assert parse('http://example.com/test4name/?name=someName') == {'name': 'someName'}
    assert parse('http://example.com/sometest5/test5/test5/test5/?test==') == {'test': '='}

    assert parse('https://example.com/path/to/page?value1=1') == {'value1': '1'}
    assert parse('https://example.com/path/to/page?value1=1&value2=2') == {'value1': '1', 'value2': '2'}
    assert parse('http://example.com/?value1=1&value2=v2&value3=False') == {'value1': '1', 'value2': 'v2', 'value3': 'False'}
    assert parse('http://example.com/?value24=17') == {'value24': '17'}
    assert parse('http://example.com/?name=Pavlo') == {'name': 'Pavlo'}


def parse_cookie(query: str) -> dict:
    values = query.replace(';', '&')
    data = dict(p.parse_qsl(values))
    return data


if __name__ == '__main__':
    assert parse_cookie('name=Pavlo;') == {'name': 'Pavlo'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Pavlo;age=28;') == {'name': 'Pavlo', 'age': '28'}
    assert parse_cookie('name=Pavlo=Progg;age=28;') == {'name': 'Pavlo=Progg', 'age': '28'}

    assert parse_cookie('someValuetwo2=value2') == {'someValuetwo2': 'value2'}
    assert parse_cookie('million=1000000') == {'million': '1000000'}
    assert parse_cookie('boolean=False') == {'boolean': 'False'}
    assert parse_cookie('name=Grusha') == {'name': 'Grusha'}
    assert parse_cookie('test==') == {'test': '='}

    assert parse_cookie('value1=1') == {'value1': '1'}
    assert parse_cookie('value1=1;value2=2') == {'value1': '1', 'value2': '2'}
    assert parse_cookie('value1=1;value2=v2;value3=False') == {'value1': '1', 'value2': 'v2', 'value3': 'False'}
    assert parse_cookie('valueqser=7') == {'valueqser': '7'}
    assert parse_cookie('name=Nicolo') == {'name': 'Nicolo'}