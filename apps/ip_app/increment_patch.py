def increment_patch(file_path="apps/ip_app/version.txt"):
    # Get the current version from file
    with open(file_path, "r") as version_file:
        current_version = version_file.read().strip()

    # split version: MAJOR, MINOR, PATCH
    major, minor, patch = map(int, current_version.split("."))

    patch += 1
    new_version = f"{major}.{minor}.{patch}"

    print(new_version)
    return new_version

if __name__ == "__main__":
    increment_patch()
