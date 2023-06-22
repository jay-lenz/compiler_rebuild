# from ast import expr
# from email.base64mime import body_encode
# from platform import node
import sys
from tokenize import Number

class Node:
    def __init__(self, parent=None, childrenList =[],treeDepth=None, nodeLabel=None, symbolTable=[]):
        self.parent = parent
        self.childrenList = list(childrenList)
        self.treeDepth = treeDepth
        self.nodeLabel = nodeLabel
        self.symbolTable = symbolTable
    
    def setParent(self, newNode):
        self.parent = newNode

    def getParent(self):
        return self.parent
    
    def getNumberOfChildren(self):
        return len(self.childrenList)
    
    def addChild(self, node):
        self.childrenList.append(node)

    def addChildrenList(self, nodes):
        for node in nodes:
            self.childrenList.append(node)
        
    def setChildrenList(self, newChildrenlist):
        self.childrenList = newChildrenlist
    
    def getChildrenList(self):
        return self.childrenList

    def setTreeDepth(self, newIndex):
        self.treeDepth =  newIndex

    def getTreeDepth(self):
        return self.treeDepth
    
    def setNodeLabe(self, label):
        self.nodeLabel = label

    def getNodeLabel(self):
        return self.nodeLabel

    def setSymbolTable(self, newSymboltable):
        self.symbolTable = newSymboltable

    def getSymbolTable(self):
        return self.symbolTable

    def addSymbol(self, symbol, symboltype):
        node = self
        while node != None:
            for element in node.symbolTable:
                if element[0] == symbol:
                    if element[1] != symboltype:
                        print("Type error. Variable %s was initialized as: %s " %(symbol[2:], element[1])) #symbol[2:] is a array slice operation that takes the 2 element out
                        sys.exit()
            node = node.getParent()
        self.symbolTable.append([symbol, symboltype, len(self.symbolTable)])

    def getSymbolType(self, symbol):
        node = self
        while node != None:
            for element in node.symbolTable:
                if element[0] == symbol:
                    return element[1]
            node = node.getParent()
        return False
    
    def checkSymbol(self, symbol):
        node = self
        while node != None:
            for element in node.symbolTable:
                if element[1] == symbol:
                    return True
            node = node.getParent()
        return False



##EXPRESSION NODE CLASS BEGINS HERE
class ExpressionNode(Node):

    def __init__(self, parent=None, childrenList=[], treeDepth=None, nodeLabel=None, symbolTable=[],expressionTreeRootNode=None, expressionType=None,expressionStack=None,expressionString=None,expressionTac=None):
        super().__init__(parent, childrenList, treeDepth, nodeLabel, symbolTable)
        self.expressionTreeRootNode = expressionTreeRootNode
        self.expressionType = expressionType
        self.expressionStack = expressionStack
        self.expressionStrig = expressionString
        self.expressionTac = expressionTac

    def setExpressionTreeRootNode(self, newExpressionTreeRootNode):
        self.expressionTreeRootNode = newExpressionTreeRootNode
    
    def getExpressionTreeRootNode(self):
        return self.expressionTreeRootNode
    
    def setExpressionType(self, newExpressiontype):
        self.expressionType = newExpressiontype

    def getExpresionType(self):
        return self.expressionType

    def setExpressionStack(self, newExpressionstack):
        self.expressionStack = newExpressionstack

    def getExpressionStack(self):
        return self.expressionStack
    
    def setExpressionString(self, newExpressionString):
        self.expressionString = newExpressionString

    def getExpressionString(self):
        return self.expressionString
    
    def setExpressionTac(self, newTac):
        self.expressionTac = newTac
    
    def buildExpressionStack(self):
        #Traverse the expression tree to build the stack in postfix representation

        nodeList = []
        nodeList.append(self.getExpressionTreeRootNode())

        expressionStack = []
        expressionString = ""
        expressionTypeTest = []

        while len(nodeList) !=0:
            node = nodeList.pop(len(nodeList)-1)

            if isinstance(node, NumberNode):
                expressionStack.append((node.getValue(), node))
                if not node.getValueType() in expressionTypeTest:
                    expressionTypeTest.append(node.getValueType())
            
            if isinstance(node, OperationNode):
                expressionStack.append((node.getOperation(), node))

            for childNodes in node.getChildrenList():
                nodeList.append(childNodes)
        
        expressionStack.reverse()

        for element in expressionStack:
            expressionString += str(element[0])

        self.expressionStack = expressionStack
        self.expressionString = expressionString

        if len(expressionTypeTest) != 1:
            print("Diffenrent types in expression:  %s" %(self.expressionString))

            print("Expression must have all elements Integer or all elements Real")
            print(expressionTypeTest)
            sys.exit()

        self.setExpressionType(expressionTypeTest[0])


##ASSIGNMENT NODE CLASS BEGINS HERE

class AssignmentNode(Node):
    def __init__(self, parent=None, childrenList=[], treeDepth=None, nodeLabel=None, symbolTable=[], targetId=None, expressionNode=None, expressionType=None,expressionTac=None):
        super().__init__(parent, childrenList, treeDepth, nodeLabel, symbolTable)
        
        self.targetId = targetId
        self.expressionNode = expressionNode
        self.expressionType = expressionType
        self.expressionTac = expressionTac

    def setTargetId(self, newId):
        self.targetId = newId
    
    def getTargetId(self):
        return self.targetId
    
    def setExpressionNode(self, newexpressionNode):
        self.expressionNode = newexpressionNode

    def getExpressionNode(self):
        return self.expressionNode

    def setExpressionTac(self, newExpressionTac):
        self.expressionTac = newExpressionTac

    def getExpressionTac(self):
        return self.expressionTac

    def setExpressionType(self, newExpressionType):
        self.expressionType = newExpressionType

    def getExpressionType(self):
        return self.expressionType


class IfNode(Node):

    def __init__(self, parent=None, childrenList=[], treeDepth=None, nodeLabel=None, symbolTable=[],expressionType = None, expressionTac=None):
        super().__init__(parent, childrenList, treeDepth, nodeLabel, symbolTable)

        self.expressionType = expressionType
        self.expressionTac = expressionTac
    
    def setExpressionType(self, newExpressionType):
        self.expressionType = newExpressionType
    
    def getExpressionType(self):
        return self.expressionType
    
    def setExpressionTac(self, newexpressiontac):
        self.expressionTac = newexpressiontac
    
    def getExpressionTac(self):
        return self.expressionTac

class ThenNode(Node):
    def __init__(self, parent=None, childrenList=[], treeDepth=None, nodeLabel=None, symbolTable=[]):
        super().__init__(parent, childrenList, treeDepth, nodeLabel, symbolTable)

class ElseNode(Node):
    def __init__(self, parent=None, childrenList=[], treeDepth=None, nodeLabel=None, symbolTable=[]):
        super().__init__(parent, childrenList, treeDepth, nodeLabel, symbolTable)

class WhileNode(Node):
    def __init__(self, parent=None, childrenList=[], treeDepth=None, nodeLabel=None, symbolTable=[],expressionType = None, expressionTac=None, expressionNode=None):
        super().__init__(parent, childrenList, treeDepth, nodeLabel, symbolTable)

        self.expressionType = expressionType
        self.expressionTac = expressionTac
        self.expressionNode = expressionNode
    
    def setExpressionType(self, newExpressionType):
        self.expressionType = newExpressionType
    
    def getExpressionType(self):
        return self.expressionType
    
    def setExpressionTac(self, newexpressiontac):
        self.expressionTac = newexpressiontac
    
    def getExpressionTac(self):
        return self.expressionTac

    def setExpressionNode(self, newNode):
        self.expressionNode = newNode

    def getExpressionNode(self):
        return self.expressionNode

class OperationNode(Node):
    def __init__(self, parent=None, childrenList=[], treeDepth=None, nodeLabel=None, symbolTable=[], operation=None):
        super().__init__(parent, childrenList, treeDepth, nodeLabel, symbolTable)
        self.operation = operation
    
    def setOperation(self, newOperation):
        self.operation - newOperation
    
    def getOperation(self):
        return self.operation

class NumberNode(Node):
    def __init__(self, parent=None, childrenList=[], treeDepth=None, nodeLabel=None, symbolTable=[], value=None, valueType=None,sign=None, isVar=False):
        super().__init__(parent, childrenList, treeDepth, nodeLabel, symbolTable)
        self.value = value
        self.valueType = valueType
        self.isVar = isVar
        self.sign = sign

    def setValue (self, newValue):
        self.value = newValue

    def getValue(self):
        return self.value

    def setValueType(self, newValueType):
        self.valueType = newValueType

    def getValueType(self):
        return self.valueType

    def setSign(self, newSign):
        self.sign = newSign

    def getSign(self):
        return self.sign

    def setisVar(self, isVar):
        self.isVar = isVar

    def isVar(self):
        return self.isVar


class PrintNode(Node):
    def __init__(self, parent=None, childrenList=[], treeDepth=None, nodeLabel=None, symbolTable=[],expressionType=None,expressionTac=None):
        super().__init__(parent, childrenList, treeDepth, nodeLabel, symbolTable)
        self.expressionTac = expressionTac
        self.expressionType = expressionType

    def setExpressionType(self, newExpressionType):
        self.expressionType = newExpressionType
    
    def getExpressionType(self):
        return self.expressionType
    
    def setExpressionTac(self, newExpressionTac):
        self.expressionTac = newExpressionTac
    
    def getExpressionTac(self):
        return self.expressionTac
    

class AbstractSyntacTree:
    def __init__(self, root=None, currentNode=None):
        self.root = root
        self.currentNode = currentNode
    
    def setRoot(self, node):
        self.root = node
    
    def getRoot(self):
        return self.root
    
    def setCurrentNode(self, node):
        self.currentNode = node

    def getCurrentNode(self):
        return self.currentNode
    
    def buildTreePassOne(self):
        nodeList = []
        nodeList.append(self.getRoot())

        while len(nodeList) !=0:
            node = nodeList.pop(len(nodeList)-1)

            node.getChildrenList().reserve()
            for child in node.getChildrenList():
                nodeList.append(child)

    def printSymbolTable(self):
        print("\n")
        print("Symbol table: \n")
        print(self.currentNode.getSymbolTable())

    def printTree(self):
        nodeList = []
        nodeList.append(self.getRoot())

        while len(nodeList) !=0:
            node =nodeList.pop(len(nodeList)-1)

            space = ""
            for i in range(node.getTreeDepth()):
                space +="-"
            
            print("%s %s%s" %( str(node.getTreeDepth()), str(space), str(node.getNodeLabel())))

            if isinstance(node, ExpressionNode):
                space = " "

                for i in range(node.getTreeDepth()):
                    space +=" "
                
                print("%sexpression stack: %s" %(space, node.getExpressionString()))
                print("%sexpression type: %s" %(space, node.getExpressionType()))

            for child in node.getChildrenList():
                nodeList.append(child)



        


    