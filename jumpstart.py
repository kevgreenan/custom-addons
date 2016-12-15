import sys

def main():
    uinput = raw_input("Would you like to create a Python, C#, or HTML project? (p/c/h) ")
    uinput = uinput.lower()
    FileContents = ""
    FileName = ""
    inputRecognized = 1
    if uinput == "p":
        FileContents = "import sys\n\nclass MyClass:\n\tdef __init(self,variable):\n\t\tself.variable = variable\n\n\tdef display(self):\n\t\tprint(self.variable)\n\ndef main():\n\tmyVariable = MyClass(\"Hello, world\")\n\tmyVariable.display()\n\nif __name__ == \"__main__\": main()\n"
        FileName = "Main.py"
    elif uinput == "c":
        FileContents = "using System;\n\nnamespace MyNamespace\n{\n\tclass MainClass\n\t{\n\t\tpublic static void Main(string[] args)\n\t\t{\n\t\t\tConsole.WriteLine(\"Hello World!\");\n\t\t}\n\t}\n}\n"
        FileName = "Program.cs"
    elif uinput == "h":
        FileContents = "<!DOCTYPE html>\n<html lang=\"en\">\n\t<head>\n\t\t<title>Title</title>\n\t</head>\n\n\t<body>\n\t\t<h1>Hello, world!</h1>\n\t</body>\n</html>\n"
        FileName = "index.html"
    else:
        print("Input not recognized, program will exit.")
        inputRecognized = 0
    readmeContents = "# ProjectName\nWrite your project description here\n\n## How do I use it?\nWrite your use description here\n\n### Sample output:\nPut any images or output text here\n"
    readmeFileName = "README.md"
    if inputRecognized != 0:
        text_file = open(FileName, "w")
        text_file.write(FileContents)
        text_file.close()
        text_file = open(readmeFileName, "w")
        text_file.write(readmeContents)
        text_file.close()
if __name__ == "__main__": main()
