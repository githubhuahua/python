# coding = utf-8
# @Time: 2020/11/30 16:14
from py2neo import Graph,Node,Relationship
graph=Graph(host='localhost',auth=('neo4j','neo4jlcn'))

a=Node("node",name="P")
graph.create(a)

b=Node("node",pid="P1017",title="进制转换",difficulty=3,type="P")
graph.create(b)
ab=Relationship(b,"标签",a)
graph.create(ab)

c=Node("node",pid="P1008",title="三连击",type="P")
graph.create(c)
ac=Relationship(c,"类型",a)
graph.create(ac)





