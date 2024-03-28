import csv

with open("ouput.xml", "w", encoding="utf-8") as output:
    output.write("<quiz>\n")

    with open("Texto.csv", "r", encoding="utf-8") as csv_file:
        csv_read = csv.reader(csv_file, delimiter=";",)

        for i, linha in enumerate(csv_read):
            if i % 5 == 1:
                continue
            elif i % 5 == 0:
                if i != 0:
                    output.write('  </question>\n')
                output.write('  <question type="multichoice">\n')
                output.write('      <name>\n')
                output.write('          <text>Pergunta {}</text>\n'.format(str(i // 5 + 1)))
                output.write('      </name>\n')
                output.write('    <questiontext format="html">\n')
                output.write('      <text>{}</text>\n'.format(str(linha[0])))
                output.write('    </questiontext>\n')
                output.write('    <shuffleanswers>true</shuffleanswers>\n')
                
            else:
                valores = linha[-1].strip()
                if valores == "":
                    output.write('    <answer fraction= "0">\n')
                else:
                    output.write('    <answer fraction= "{}">\n'.format(str(valores)))
                output.write('      <text>{}</text>\n'.format(str(linha[0])))
                output.write('    </answer>\n')

    output.write('  </question>\n')
    output.write('<script/></quiz>')