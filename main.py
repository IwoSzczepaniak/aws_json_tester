import json


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


def test_verify_json():

    assert not verify_json("test/invalid_path.json")

    assert verify_json("test/empty.json")

    assert not verify_json("test/single_asterisk.json")

    assert verify_json("test/single_resource.json")

    assert verify_json("test/multiple_resources.json")


    print("\nAll tests passed successfully!")


if __name__ == "__main__":
    test_verify_json()
