#!/usr/bin/python
import sys

url = sys.argv[1]
for arg in sys.argv[2:]:
    with open(arg.rstrip("/") + '/build.gradle', "a") as myfile:
        myfile.write("uploadArchives {\n")
        myfile.write("  repositories {\n")
        myfile.write("    mavenDeployer {\n")
        myfile.write("      repository(url: 'file://" + url + "')\n")
        myfile.write("    }\n")
        myfile.write("  }\n")
        myfile.write("}\n")