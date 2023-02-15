import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv()

    keys, values = utils.get_population()
    print(keys, values)

    country = input("Type country => ")

    result = utils.population_by_country(data, country)
    print(result)

if __name__ == "__main__":
    run()