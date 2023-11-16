#Create the request from an id


def first_norm(vector_1,vector_2):
    n = len(vector_1)
    s = 0
    for i in range(n):
        s = abs(vector_1[i] - vector_2[i])
    return s

def inf_norm(vector_1: list ,vector_2: list) -> float, int:
    """Send the inf norm of two vectors and the topic"""
    n = len(vector_1)
    s = abs(vector_1[0] - vector_2[0])
    topic = 0
    for i in range(1,n):
        u = abs(vector_1[i] - vector_2[i])
        if u < s:
            s=u
            topic = i
    return s, topic
