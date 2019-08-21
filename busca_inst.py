import difflib
base_file = open('base_instituciones.csv')
base_lines = base_file.readlines()
search_file = open('buscar_instituciones.csv')
search_lines = search_file.readlines()
write_file = open('output.csv', 'a+')
total_l = len(search_lines)
counter = 0
for institution in search_lines:
    max_ratio = 0
    best_match_i = ''
    best_match_c = ''
    institution = institution.replace('\n', '').upper()
    for base in base_lines:
        base_i = base.split(',')[0].upper()
        base_c = base.split(',')[1]
        sec_matcher = difflib.SequenceMatcher(a=base_i, b=institution)
        if sec_matcher.ratio() > max_ratio:
            max_ratio = sec_matcher.ratio()
            best_match_i = base_i
            best_match_c = base_c
    counter += 1
    print(counter, '/', total_l)
    write_file.write(institution + ',' + best_match_i + ',' + best_match_c)
    write_file.flush()
write_file.close()
base_file.close()
search_file.close()
