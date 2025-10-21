from app import calculate_relatives, calculate_average, get_average_relatives_from_file

class TestCalculateRelatives:

    def test_calculate_all_relatives(self):
        row = {'SibSp': '2', 'Parch': '3'}
        result = calculate_relatives(row)
        assert result == 5

    def test_calculate_only_siblings(self):
        row = {'SibSp': '4', 'Parch': '0'}
        result = calculate_relatives(row)
        assert result == 4

class TestCalculateAverage:

    def test_calcaulte_average(self):
        list = [1, 2, 3, 4, 5]
        average = calculate_average(list)
        assert average == 3

    def test_calculate_average_empty_list(self):
        list = []
        average = calculate_average(list)
        assert average == 0

class TestGetAverageRelativesFromFile:

    def test_get_average_relatives_without_file(self):
        csv_file = ""
        survived, dead = get_average_relatives_from_file(csv_file)
        assert survived == []
        assert dead == []