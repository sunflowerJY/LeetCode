# __author__ = "Tian Yafu"
# -*- coding:UTF-8 -*-

# generate leetcode type of binary tree
# rely: Graphviz, os

class TreeNode(object):
    # from leetcode
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def constructBinaryTree(elemList):
    # generate leetcode type of binary tree
    # :param elemList: leetcode unit test (hierachy form)
    # :return: root node
    # sample: constructBinaryTree([3,9,20,None,None,15,7])
    length = len(elemList)
    if (length == 0):
        return None
    _root = TreeNode(elemList[0])

    def recr(root, num):
        # num: number of node, start by 0 (root)
        leftNumber = 2 * num + 1
        rightNumber = 2 * num + 2
        if (leftNumber < length and elemList[leftNumber] != None):
            root.left = TreeNode(elemList[leftNumber])
            recr(root.left, leftNumber)
        else:
            root.left = None
        if (rightNumber < length and elemList[rightNumber] != None):
            root.right = TreeNode(elemList[rightNumber])
            recr(root.right, rightNumber)
        else:
            root.right = None

    recr(_root, 0)
    return _root


def outputBinaryTreeByDot(root):
    # generate graphviz file
    if (root == None):
        print
        "receive None input"
        exit()
    head = ["digraph G{\n"]
    nodeSector = ["\n"]
    edgeSector = ["\n"]
    tail = ["\n}"]

    def recr(root, num):
        _str = 'node{0}[label = "{1}"];\n'.format(num, root.val)
        nodeSector.append(_str)
        if (root.left != None):
            edgeSector.append("node{0} -> node{1};\n".format(num, 2 * num + 1))
            recr(root.left, 2 * num + 1)
        if (root.right != None):
            edgeSector.append("node{0} -> node{1};\n".format(num, 2 * num + 2))
            recr(root.right, 2 * num + 2)

    recr(root, 0)
    return "".join(head) + "".join(nodeSector) + "".join(edgeSector) + "".join(tail)


def showDotFile(_strDotFile, _fileName=None, _outputName=None):
    import os
    if (_fileName != None):
        fileName = _fileName
    else:
        fileName = "tempBinaryTreeFile.dot"
    if (_outputName != None):
        outputName = _outputName
    else:
        outputName = "tempBinaryTreeFile.pdf"
    ##  save .dot file
    with open(fileName, "w") as fileHandler:
        fileHandler.write(_strDotFile)
    path = os.getcwd()
    ## command to generate grapg with graphviz
    cmd = "dot {0}\{1} -Tpdf -o {0}\{2}".format(path, fileName, outputName)
    print(cmd)
    consoleHandler = os.popen(cmd)
    print(consoleHandler.read())
    ## open PDF file
    print(os.popen("{0}\{1}".format(path, outputName)).read())


if (__name__ == "__main__"):
    ## Test:
    null = None
    # tree = constructBinaryTree([3,9,20,null,null,15,7])
    tree = constructBinaryTree([3, 9, 20, null, null, 15, 7, null, null, null, null, 7, 9, 2, 5])
    strFile = outputBinaryTreeByDot(tree)
    showDotFile(strFile)