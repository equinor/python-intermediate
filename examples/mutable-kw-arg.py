def run_simulation(realisations=[], ignore=[]):
    ignore.append(1)  # Always ignore first realization
    return sum(realisations) - sum(ignore)


def main():
    assert run_simulation([1, 2, 3]) == 5
    print(run_simulation([1, 2, 3]))


if __name__ == "__main__":
    main()
