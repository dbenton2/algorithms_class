from collections import defaultdict

#create adjacency list to represent a directed graph
class Graph:

    def __init__(self,vertices):
        #number of vertices
        self.V=vertices
        
        #dictionary to store graph
        self.graph = defaultdict(list)
        
        
        self.Time = 0

    #function to add edge to graph
    def addEdge(self,j,i):
        self.graph[j].append(i)

    #function that will be called to recursivley to do the depth first search traversal
    def FindSCC(self,j,low,disc,stackMember, st):

        #initalize variables
        disc[j] = self.Time
        low[j] = self.Time
        #mark the node as visited and add to stack
        self.Time += 1
        stackMember[j] = True
        st.append(j)

        #visit adjacent vertices
        for i in self.graph[j]:

            #if vertex has not been visited call recursiveley on that vertex
            if disc[i] == -1:

                self.FindSCC(i, low, disc, stackMember, st)

                #check if the subtree has a connection to one of the parents of u
                low[j] = min(low[j],low[i])
            elif stackMember[i] == True:
                low[j] = min(low[j], disc[i])

        #head node found, pop the stack and print strongly connected components
        w = -1
        if low[j] == disc[j]:
            while w != j:
                w = st.pop()
                print w,
                stackMember[w] = False
            
            print""


    #calls FindSCC recursively 
    def SCC(self):

        #mark all nodes as not visited
        disc = [-1] * (self.V)
        low = [-1] * (self.V)
        stackMember = [False] * (self.V)
        st = []

        #check all vertices
        for x in range(self.V):
            if disc[x] == -1:
                self.FindSCC(x, low, disc, stackMember, st)


#create graph
graph1 = Graph(9)
#add edges to the graph
graph1.addEdge(0,1)
graph1.addEdge(1,2)
graph1.addEdge(2,3)
graph1.addEdge(3,4)
graph1.addEdge(3,5)
graph1.addEdge(5,6)
graph1.addEdge(6,7)
graph1.addEdge(7,5)
graph1.addEdge(5,8)
graph1.addEdge(4,0)
print "Strongly Connected Components in first graph"
#run algorith to find all strongly connected components
graph1.SCC()

#this is a representation of the gif on the wikipedia
#page for Tarjan's algorithm where vertex 8 in the gif is 0 in my code
#graph2 = Graph(8)
#graph2.addEdge(0,0)
#graph2.addEdge(0,7)
#graph2.addEdge(0,5)
#graph2.addEdge(7,6)
#graph2.addEdge(6,7)
#graph2.addEdge(5,6)
#graph2.addEdge(5,4)
#graph2.addEdge(4,5)
#graph2.addEdge(6,3)
#graph2.addEdge(4,3)
#graph2.addEdge(4,2)
#graph2.addEdge(3,1)
#graph2.addEdge(1,2)
#graph2.addEdge(2,3)
#print "Strongly Connected Components in second graph"
#graph2.SCC()
