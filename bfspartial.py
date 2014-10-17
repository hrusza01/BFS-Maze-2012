while not queue.isEmpty():
    (currentpath,turtle) = queue.dequeue()
    currentNode = currentPath[0]
    
    if currentNode in visited:
        turtle.ht()
        
    else:
        visited.append(currentNode)
        turtle.st()
        turtle.color("red")
        tutle.width(10)
        turtle.pendown()
        goto(turtle, currentNode, maze)
        turtle.speed(int(delay.get()))
        
        if goal(currentNode):
            return (currentPath,turtle)
        adjList = adjacent(currentNode, maze, visited)
        