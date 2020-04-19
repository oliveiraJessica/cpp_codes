def main():
    print("Let's Topologicaly sort!")
    user_input()

def user_input():
    #n_nodes = raw_input('How many vertices?');
    graph_string = raw_input('Insert the vertices (A->B->C<-D) like that: A,B,B,C,D,C\n')
    graph_list = graph_string.split(',')
    n_edges = len(graph_list)/2

    if isinstance(n_edges, int):
        print('Your graph has ' + str(n_edges) + ' edges')
    else:
        print('You must inset a even number of vertices')
        user_input();

    visited = [];
    stack = [];
    parents_vertices = graph_list[0:len(graph_list):2]
    print(parents_vertices)
    for i in range(0,len(parents_vertices)):
    #     #marcar no como visitado
        if not (parents_vertices[i] in visited):
            visited.append(parents_vertices[i]);
    #     stack.append()
    print(visited)

if __name__ == '__main__':
    main()
