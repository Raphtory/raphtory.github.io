# --8<-- [start:new_graph]
from raphtory import Graph
g = Graph()
print(g)
# --8<-- [end:new_graph]

# --8<-- [start:vertex_add_1]
from raphtory import Graph

g = Graph()
v = g.add_vertex(timestamp=1,id=10)

print(g)
print(v)
# --8<-- [end:vertex_add_1]

# --8<-- [start:vertex_add_2]
from raphtory import Graph
from datetime import datetime

g = Graph()
v = g.add_vertex(timestamp="2021-01-01 12:32:00",id=10)

#Create a python datetime object
datetime_obj = datetime.strptime("2021-02-03 14:01:00", "%Y-%m-%d %H:%M:%S")
v = g.add_vertex(timestamp=datetime_obj,id=10)

print(g)
print(v.history())
# --8<-- [end:vertex_add_2]

# --8<-- [start:vertex_add_3]
from raphtory import Graph
g = Graph()
g.add_vertex(timestamp=123,id="User 1")
g.add_vertex(timestamp="2021-01-01 12:32:00",id=200)

print(g.vertex("User 1"))
print(g.vertex(200))
#--8<-- [end:vertex_add_3]

#--8<-- [start:vertex_add_4]
from raphtory import Graph
g = Graph()

#Primitive type properties 
g.add_vertex(timestamp=1, id="User 1", properties={"Int Property": 1, "String Property": "hi", "Boolean Property": True})
g.add_vertex(timestamp=2, id="User 1", properties={"Int Property": 2, "Float Property": 0.6, "Boolean Property": False})
g.add_vertex(timestamp=3, id="User 1", properties={"Float Property": 0.9, "String Property": "hello", "Boolean Property": True})

#Complex property types
g.add_vertex(timestamp=1, id="User 1", properties={"Dict Property": {"greeting":"hello", "inner list": [1,2,3]}, "List property": [6,5,4]})

v=g.vertex("User 1")
print(v)

#Storing graphs as properties
g2 =Graph()
g2.add_vertex(timestamp=1,id="User 2")

g.add_vertex(timestamp=4,id="User 1", properties={"Graph Property":g2})
print(v.properties.get("Graph Property"))
#--8<-- [end:vertex_add_4]

#--8<-- [start:vertex_add_5]
#--8<-- [end:vertex_add_5]


