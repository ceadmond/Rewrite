def read_and_process_file(file_path, output_file):
    result = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("# hostname ="):
                temp = []
                value = line.split("=")[1].strip().split(",")
                for item in value:
                    temp.append(item.strip())
                for item in list(set(temp)):
                    result.append(item)
    result_str = ", ".join(result)
    with open(output_file, "w") as out_file:
        out_file.write(result_str)


file_path = "chongxie.conf"
output_file = "hostname.txt"
read_and_process_file(file_path, output_file)
