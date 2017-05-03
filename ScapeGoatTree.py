# -*- coding: utf-8 -*-


#from ..AbstractTree import AbstractTree

__author__ = "lukalajovic"



class Node:

    def __init__(self, key = None, parent = None, left = None, right = None,countl=0,countr=0):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.zbrisan=False
        self.countl=countl
        self.countr=countr

    def __repr__(self):
        if self.key is None:
            return 'Null'
        else:
            return '{key} ((Left: {left}) (Right: {right}))'.format(key=self.key, left=self.left, right=self.right)


    
    def zaporedje(self):
        l=[]
        if self.left!=None:
            l=self.left.zaporedje()
        d=[]
        if self.right!=None:
            d=self.right.zaporedje()
        k=[]
        if self.zbrisan==False:
            k=[self.key]
        return l+k+d

    
    def size(self):
        l=0
        if self.left!=None:
            l=self.left.size()
        d=0
        if self.right!=None:
            d=self.right.size()

        return l+self.key+d


    
    def ustvari(self,zap,stars=None):
        if len(zap)>0:
            m=len(zap)//2
            med=zap[m]
            #print("brumhilda")
            
            
            self=Node(med,stars)
            self.countl=len(zap[:m])
            self.countr=len(zap[m+1:])
            self.left=Node(-1,self)
            self.right=Node(-1,self)
            self.left=self.left.ustvari(zap[:m],self)
            self.right=self.right.ustvari(zap[m+1:],self)
            print(self.countl)
            print(self.countr)
            return self
    

    
        

class ScapeGoatTree():

    def __init__(self, data = None,alfa=0.5):
        self.root = None
        self.alfa=alfa
        if data:
            for i in data:
                self.insert(i)
        super().__init__()

    def __repr__(self):
        return str(self.root)

    def insert(self, item):
        parent = None
        side = 0 ## 0 if item is left child of parent, else 1
        node = self.root
        while node is not None:
            
            if item > node.key:
                parent = node
                side = 1
                node.countr+=1
                node = node.right
                
            elif item <= node.key:
                parent = node
                side = 0
                node.countl+=1
                node = node.left
            else:
                return
        node = Node(key=item, parent=parent)
        
        if not parent:
            self.root = node
        elif side:
            parent.right = node
        else:
            parent.left = node
        #sez=[]
        
    
        
        #zap=self.root.zaporedje()
        #print(zap)
        #self.root=self.root.ustvari(zap)
        #print(self.root)
        l=0
        d=0        
        sprememba=False
        parent=None
        while node.parent!=None:
            parent=node
            node=node.parent
            
            """
            if node.parent.key>node.key:
                l+=1
                if node.right!=None:
                    d=node.right.size()
                else:
                    d=0
            else:
                d+=1
                if node.left!=None:
                    l=node.left.size()
                else:
                    l=0
            """    
            
            d=node.countr
  
            l=node.countl
            print(l)
            print(d)
                
            if l>self.alfa*(1+l+d):
                sprememba=True
                print(node.key)
                print(l)
                print(d)
                print(self.alfa)
                print(node.size())
                print("l")
                break
            if d>self.alfa*(1+l+d):
                sprememba=True
                print(node.key)
                print(l)
                print(d)
                
                print(self.alfa)
                print("d")
                break
            
            
          
        if sprememba==True:
            print("alamut")
            #print(node)
            zap=node.zaporedje()
            node=node.ustvari(zap,node.parent)
            #print(node)
            #print(self.root)
            #zap=self.root.zaporedje()
            #print(zap)
            #self.root=self.root.ustvari(zap)
            if not node.parent:
                self.root = node
            else:
                if node.parent.key<node.key:
                    parent.right = node
                else:
                    parent.left = node
       
            
    
    def search(self, item):
        n = self.find(item)
        if n is None:
            return False
        else:
            return True

    def find(self, item):
        node = self.root
        while node is not None:
            if node.key == item:
                return node
            elif node.key > item:
                node = node.left
            else:
                node = node.right
        return None
    #[x,y,data,true,false]

#    def zaporedje(self,node):
#        if node==None:
#            return []
#        else:
#            return self.zaporedje(node.left)+[node.key]+self.zaporedje(node.right)
    



            
         
             
       

        
    def kordinate(self):
        node=self.root
        x=400
        y=50
        n=200
        nova=[(node,400)]
        kord=[]

        while len(nova)>0:
            vmesna=[]
            for i in nova:
                ko=[i[1],y,i[0].key]
                if i[0].left==None:
                    ko+=[False]
                else:
                    ko+=[True]
                    vmesna+=[(i[0].left,i[1]-n)]
                
                if i[0].right==None:
                    
                    ko+=[False]
                else:
                    ko+=[True]
                    vmesna+=[(i[0].right,i[1]+n)]
                ko+=[n]    
                kord.append(ko)
            nova=vmesna
            y+=100
            n=n/2
        return kord

            

                



    def remove(self, item):
        node = self.find(item)
        if not node:
            raise ValueError('The item you are trying to remove does not exist')
        else:
            node.zbrisan=True




        
        


