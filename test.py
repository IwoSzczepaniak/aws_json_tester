from verify import verify_json


def test_verify_json():

    assert not verify_json("test/invalid_path.json")

    assert verify_json("test/empty.json")

    assert not verify_json("test/single_asterisk.json")

    assert verify_json("test/single_resource.json")

    assert verify_json("test/multiple_resources.json")

    print("\nAll tests passed successfully!")


if __name__ == "__main__":
    test_verify_json()
