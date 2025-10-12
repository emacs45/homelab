errors = []

with open('access.log', 'r') as infile, open('errors.log', 'w') as outfile:
    for line in infile:
        line = line.strip()
        if '500' in line:
            errors.append(line)
    outfile.write("Gefundene 500-Fehler:\n")
    
    for e in errors:
        outfile.write(e)
        outfile.write('\n')
    outfile.write(f'\n\nAnzahl: {len(errors)}')
