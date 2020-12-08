import requests
import sys


def requestDependencies(package):

    r = requests.get("https://pypi.python.org/pypi/" + package + "/json")

    r_dict = r.json()

    package_dependencies = r_dict['info']['requires_dist']

    if (package_dependencies):
        for pkg in package_dependencies:
            if (not "extra" in pkg):
                package_name = pkg.split()[0]
                print('\t{0} -> "{1}"'.format(package, package_name))
                requestDependencies(package_name)


def createGraphSyntax():
    if (len(sys.argv) < 2 or sys.argv[1] == "--help" or sys.argv[1] == "-h"):
        print("Usage: $ python index.py <package_name>")
    else:
        package = sys.argv[1]
        print("digraph", package, "{")
        requestDependencies(package)
        print("}")
createGraphSyntax()

