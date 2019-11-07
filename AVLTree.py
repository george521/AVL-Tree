class Node:
    #The Nodes hold Objects of a class Hotel
    def __init__(self, parent, hotel):
        self.leftS = None
        self.rightS = None
        self.parent = parent
        self.hotel = hotel       
        self.height = 0
        self.balance = 0

    def calculate(self):
        self.height = max(self.rightS.height, self.leftS.height) + 1
        self.balance = self.rightS.height - self.leftS.height
        
        
class AvlTree:

    def __init__(self):
        self.root = None  
        
    def insert(self, newHotel):
        if self.root == None:
            self.root = Node(None, newHotel)
            return
        
        node = self.find(self.root, newHotel.id)
        if newHotel.id == node.hotel.id:
            return

        if newHotel.id > node.hotel.id:
            #Right insert
            node.rightS = Node(node, newHotel)
            node.leftS = Node(node, node.hotel)
        else:
            #Left insert
            tempNode = Node(node.parent, newHotel)
            tempNode.leftS = Node(tempNode, newHotel)
            tempNode.rightS = node

            if tempNode.parent == None:
                # node was root of tree
                self.root = tempNode
            else:
                if tempNode.parent.hotel.id >= node.hotel.id:
                    tempNode.parent.leftS = tempNode
                else:
                    tempNode.parent.rightS = tempNode
                    
                node.parent = tempNode

            node = tempNode
            
        self.rebalance(node)


    def findById(self, id):
        if self.root == None:
            return None
        
        node = self.find(self.root, id)
        if node.hotel.id == id:
            return node.hotel
        else:
            return None

    def find(self, rootNode, id):
        ''' Return the node with the hotel of the selected id or the last node of the search'''
        
        if rootNode.hotel.id == id:
            return rootNode
        
        elif id < rootNode.hotel.id:
            if rootNode.leftS == None:
                return rootNode
            else:
                return self.find(rootNode.leftS, id)
            
        else:
            if rootNode.rightS == None:
                return rootNode
            else:
                return self.find(rootNode.rightS, id)

    def rebalance(self, node):
        if node==None:
            return
        
        node.calculate()

        if node.balance>=-1 and node.balance<=1:
            self.rebalance(node.parent)
            return

        if node.balance==2:
            if node.rightS.balance<0:
                #right-left
                self.rotateRight(node.rightS)
                self.rotateLeft(node)


            elif node.rightS.balance>0:
                #right-right
                self.rotateLeft(node)


        elif node.balance==-2:
            if node.leftS.balance<0:
                #left-left
                self.rotateRight(node)


            elif node.leftS.balance>0:
                #left-right
                self.rotateLeft(node.leftS)
                self.rotateRight(node)




    def rotateRight(self, root):
        pivot = root.leftS

        pivot.parent = root.parent

        if root.parent != None:
            if root.parent.hotel.id >= root.hotel.id:
                root.parent.leftS = pivot
            else:
                root.parent.rightS = pivot
        else:
            self.root = pivot

        root.leftS = pivot.rightS
        root.leftS.parent = root
        pivot.rightS = root
        pivot.rightS.parent = pivot
        root.parent = pivot

        root.calculate()
        pivot.calculate()
        if pivot.parent!=None:
            pivot.parent.calculate()
            
    def rotateLeft(self, root):
        pivot = root.rightS

        pivot.parent = root.parent
        
        if root.parent != None:
            if root.parent.hotel.id >= root.hotel.id:
                root.parent.leftS = pivot
            else:
                root.parent.rightS = pivot
        else:
            self.root = pivot

        root.rightS = pivot.leftS
        root.rightS.parent = root
        pivot.leftS = root
        pivot.leftS.parent = pivot
        root.parent = pivot

        root.calculate()
        pivot.calculate()
        if pivot.parent!=None:
            pivot.parent.calculate()
