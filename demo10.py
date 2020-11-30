# coding = utf-8
# @Time: 2020/11/29 16:20
from py2neo import Graph,Node,Relationship
graph=Graph(host='localhost',auth=('neo4j','neo4jlcn'))
a=Node("problem3",pid="P1017",title="进制转换",difficulty=3,type="P")
b=Node("Problem3", name="数论，数学", type="Algorithm", color="red", tagInt=5)
c=Node("Problem3", name=2000, type="Time", color="blue", tagInt=17)
d=Node("Problem3", name="NOIp提高组", type="Origin", color="blue", tagInt=83)
e=Node("Problem3", name="进制", type="Algorithm", color="red", tagInt=244)

graph.create(a)
graph.create(b)
graph.create(c)
graph.create(d)
graph.create(e)

ab=Relationship(b,"标签",a)
ac=Relationship(c,"标签",a)
ad=Relationship(d,"标签",a)
ae=Relationship(e,"标签",a)

graph.create(ab)
graph.create(ac)
graph.create(ad)
graph.create(ae)
