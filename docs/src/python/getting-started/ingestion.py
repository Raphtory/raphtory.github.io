# --8<-- [start:new_graph]
from raphtory import Graph
g = Graph()
print(g)
# --8<-- [end:new_graph]

# --8<-- [start:vertex_add]
from raphtory import Graph

g = Graph()
v = g.add_vertex(timestamp=1,id=10)

print(g)
print(v)
# --8<-- [end:vertex_add]

#--8<-- [start:edge_add]
from raphtory import Graph

g = Graph()
e = g.add_edge(timestamp=1,src=15,dst=16)

print(g)
print(e)
#--8<-- [end:edge_add]

#--8<-- [start:edge_layers]
#--8<-- [end:edge_layers]


# --8<-- [start:different_time_types]
from raphtory import Graph
from datetime import datetime

g = Graph()
v = g.add_vertex(timestamp="2021-02-03 14:01:00",id=10)

#Create a python datetime object
datetime_obj = datetime.strptime("2021-01-01 12:32:00", "%Y-%m-%d %H:%M:%S")
v = g.add_vertex(timestamp=datetime_obj,id=10)

print(g)
print(v.history())
print(g.earliest_date_time())
# --8<-- [end:different_time_types]

# --8<-- [start:id_types]
from raphtory import Graph
g = Graph()

g.add_vertex(timestamp=123,id="User 1")
g.add_vertex(timestamp=456,id=200)
g.add_edge(timestamp=789,src="User 1",dst=200)

print(g.vertex("User 1"))
print(g.vertex(200))
print(g.edge("User 1",200))
#--8<-- [end:id_types]

#--8<-- [start:property_types]
from raphtory import Graph
from datetime import datetime

g = Graph()

#Primitive type properties added to a vertex
g.add_vertex(timestamp=1, id="User 1", properties={"count": 1, "greeting": "hi", "encrypted": True})
g.add_vertex(timestamp=2, id="User 1", properties={"count": 2, "balance": 0.6, "encrypted": False})
g.add_vertex(timestamp=3, id="User 1", properties={"balance": 0.9, "greeting": "hello", "encrypted": True})

#Dictionaries and Lists added to a graph
g.add_property(timestamp=1, properties={"inner data": {"name":"bob", "value list": [1,2,3]}, "favourite greetings": ["hi","hello","howdy"]})
datetime_obj = datetime.strptime("2021-01-01 12:32:00", "%Y-%m-%d %H:%M:%S")
g.add_property(timestamp=2, properties={"inner data": {"date of birth":datetime_obj, "fruits":{"apple": 5,"banana": 3} }})

#Graph property on an edge
g2 =Graph()
g2.add_vertex(timestamp=123,id="Inner User")

g.add_edge(timestamp=4,src="User 1", dst="User 2", properties={"i_graph":g2})

#Printing everything on
v=g.vertex(id="User 1")
e=g.edge(src="User 1", dst="User 2")
print(g)
print(v)
print(e)
#--8<-- [end:property_types]

#--8<-- [start:constant_properties]
#--8<-- [end:constant_properties]


