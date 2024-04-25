import subprocess

def get_php_versions():
    """
    Retrieves available PHP versions using 'update-alternatives --query php' and parses the output to exact version numbers.

    Returns:
        list: A list of available PHP version numbers as strings.
    """
    output = subprocess.check_output(["sudo", "update-alternatives", "--query", "php"]).decode()
    versions = []

    for line in output.splitlines():
        if line.startswith("Alternative:"):
            version = line.split()[1]
            versions.append(version)

    return versions

def display_php_versions(versions)
    """
    Presents the available PHP versions in a user-friendly format.

    Args:
        versions (list): List of available PHP version numbers.
    """ 

    print("Available PHP Versions:")
    for i, version in enumerate(versions):
        print(f"{i+1}. {version}")

def select_php_version():
    """
    Prompts the user to select the desired PHP version and validates the input.

    Args:
        versions (list): List of available PHP version numbers.

    Returns: 
        str: The chosen PHP version number.
    """

    while True:
        choice = input("Enter the number corres poding to your desired PHP version (or q to Quit): ")
        if choice.lower() == 'q':
        exit(0)

        try:
            choice_int = int(choice) -1
            if 0 <= choice_int < len(versions):
                return versions[choice_int]
            else:
                print("Invalid selection. Please enter a number or 'q' to Quit.")
        except ValueError:
            print("Invalid selection. Please enter a number or 'q' to Quit.")

def switch_php_version():
    """
    Executes 'update-alternatives --config php' to set the desired version.

    Args:
        version (str): The chosen PHP version number.
    """
    subprocess.run(["sudo", "update-alternatives", "--config", "php"], input=version.encode())

def main():
    """
    The main function that orchestrates the script's execution.
    """
    versions = get_php_versions()
    if not versions:
        print("No PHP versions found..")
        exit(1)

        display_php_versions(versions)
        selected_version = select_php_version()
        switch_php_version(selected_version)
        print(f"PHP Version {selected_version} set successfully..")

if __name__ == "__main__":
    main()
