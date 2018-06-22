# py-hostlist: a tool for manipulating lists of hosts

##### Author: Christopher Moussa
##### Mentor: Elsa Gonsiorowski
****
## Description

py-hostlist processes slurm-style hostlist strings and can return those strings in manipulated fashion. 
****

## Methods

**expand(nodelist)**

expand takes in a hostlist string and returns a list of individual hostnames. For example, the input string **node[1-4]** will return **node1,node2,node3,node4**. The expand method can recognize the following input strings:

- node[1-9]
- node1234[1-9]
- node[1-9].somesuffix.org
- node[1-9,14-17,22,24-50]

Note: the expand method will not return the suffix string in its final expansion, only the nodes.

**compress_range(nodelist)**

compress_range takes in a hostlist list string and returns an ordered hostlist with a range. For example, the input string **['node1','node2','node3','node4']** will return **node[1-4]**. The compress_range method can also recognize multiple ranges.

**compress(nodelist)**

compress takes in a hostlist list string and returns an ordered hotlist string. For example, the input string **['node1','node2','node3','node4']** will return **[node1,node2,node3,node4]**.

**diff(nodelist1, nodelist2)**

diff will subtract elements in nodelist2 from nodelist1 and return a remaining hostlist. 

**intersect(\*arg)**

intersect will return a list of intersection nodes given n lists of nodes.

**union(\*arg)**

union will return the union between n lists of nodes.

**nth(nodelist, n)**

nth takes in two parameters: a hostlist string (similar to expand()'s parameter) and an index *n*. It will return the *nth* node in that range. 

### Helper Methods

**append_hostname(machine_name, num_list)**

append_hostname takes in two parameters: the name of the machine and its range of nodes; it is a helper method that will append the machine name (the host) to the node numbers it contains.

**sort_nodes(nodelist)**

sort_nodes takes in a list of nodes; it is a helper method that will return a sorted string of those nodes in ascending order.