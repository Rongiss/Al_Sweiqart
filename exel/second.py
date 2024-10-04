import openpyxl, pprint


def main():
    ex = openpyxl.load_workbook('censuspopdata.xlsx')
    wb = ex['Population by Census Tract']
    countyData = {}

    for row in range(2, wb.max_row + 1):
        state = wb['B' + str(row)].value
        county = wb['C' + str(row)].value
        pop = wb['D' + str(row)].value

        countyData.setdefault(state, {})
        countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
        countyData[state][county]['tracts'] += 1
        countyData[state][county]['pop'] += int(pop)
    pprint.pprint(countyData)


if __name__ == '__main__':
    main()
