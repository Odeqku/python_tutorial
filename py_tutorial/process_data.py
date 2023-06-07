#!/usr/bin/python3

def process_data(data) -> bool:
	unique_values = set()
	all_values = ()

	for item in data:
		unique_values.add(item)
		all_values += (item,)
	return unique_values in all_values


def main() -> None:
	data = [1, 2, 3, 2, 4, 5, 3, 6]
	print(process_data(data))

if __name__ == "__main__":
	main()
