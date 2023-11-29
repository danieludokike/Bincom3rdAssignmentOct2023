import re


def quick_sort(*arg):
    """Chronologically (ascending ) sort the names"""
    if len(arg[0]) <= 1:
        return arg[0]
    else:
        mid = arg[0][0]
        lower = [name for name in arg[0][1:] if name < mid]
        upper = [name for name in arg[0][1:] if name > mid]

        return quick_sort(lower) + [mid] + quick_sort(upper)


class NameReader:
    def __init__(self, file_name=None):
        self._file_name = file_name
        self._sorted_baby_names = []

    def get_total_baby_names(self):
        return len(self._sorted_baby_names)

    def read_baby_names(self):
        """Read babies names from the html file and get only the names"""
        try:
            pattern = re.compile(r'<td>(.*?)</td>')
            with open(self._file_name, 'r') as file:
                file_content = file.read()
            name_matches = pattern.findall(file_content)
            name_matches = [name for name in name_matches if not name.isdigit()]

            # Sorting the names in ascending orders
            self._sorted_baby_names = quick_sort(name_matches)

        except FileNotFoundError:
            print(f"{self._file_name} not found!")
        except PermissionError:
            print(f"You don't have permissions {self._file_name}!")
        except IsADirectoryError:
            print(f"{self._file_name} is a directory not a file!")

        return self._sorted_baby_names

    def get_name(self, name):
        """Recursively finds the index of the given name and return it"""
        lowest_index = 0
        highest_index = len(self._sorted_baby_names) - 1

        while lowest_index <= highest_index:
            middle_index = (lowest_index + highest_index) // 2
            middle_value = self._sorted_baby_names[middle_index]

            if middle_value == name:
                return middle_index
            elif middle_value < name:
                lowest_index = middle_index + 1
            else:
                highest_index = middle_index - 1

        return -1


obj = NameReader("baby2008.html")
obj.read_baby_names()
print(obj.get_name('Emma'))
