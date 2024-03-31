import json, os


def verify_json(file_path):
    try:
        with open(file_path, "r") as file:
            json_data = json.load(file)
            policy_document = json_data["PolicyDocument"]
            statement = policy_document["Statement"]
            for s in statement:
                for resource in s["Resource"]:
                    if resource != "*":
                        return True
            return False

    except FileNotFoundError as e:
        print(f"\nFile {file_path} doesnt'exist!\nError: {e}")
        return False

    except Exception as e:
        print(f"\nFile {file_path} does not have AWS style!\nError: {e}")
        return True


if __name__ == "__main__":
    if len(os.sys.argv) != 2:
        print("Usage: python3 verify.py <filename.json>")
        os.sys.exit(1)

    arg = os.sys.argv[1]
    if not arg.endswith(".json"):
        print("Please provide a valid json file!")
        os.sys.exit(1)

    val = verify_json(arg)

    if val:
        print(f"\nFile {arg} is verified positevely(True)!")
    else:
        print(f"\nFile {arg} is rejected(False)!")

