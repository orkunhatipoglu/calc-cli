import sys

def find(name):
	with open("textbook.txt", "r") as file:
		for line in file:
			parts = line.strip().split()
			if len(parts) == 2:
				person, number = parts
				if person.lower() == name.lower():
					return f"{person}: {number}"

def add(name, number):
	with open("textbook.txt", "a") as file:
		file.write(f"{name} {number}\n")


if __name__ == "__main__":
	if len(sys.argv) not in (3, 4):
		print("Usage: python3 pb.py [look name|add name num]\n")
	else:
		if sys.argv[1] == "look":
			if len(sys.argv) != 3:
				print("Usage: python3 pb.py look name\n")
			else:
				print(find(sys.argv[2]))
		else:
			if len(sys.argv) != 4:
				print("Usage: python3 pb.py add name num\n")
			else:
				add(sys.argv[2], sys.argv[3])
				print(f"Successfully added {sys.argv[2]} {sys.argv[3]}")
