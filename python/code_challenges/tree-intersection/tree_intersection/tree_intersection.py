import os
# from depenancy_classes import Hashtable, breadth_first, EmptyTree, BinarySearchTree
from tree_intersection.depenancy_classes import Hashtable, breadth_first, EmptyTree, BinarySearchTree

def tree_intersection(tree_a, tree_b):
    intersections = []
    ht = Hashtable()
    try:
      tree_a_values = breadth_first(tree_a)
      tree_b_values = breadth_first(tree_b)
      for a_value in tree_a_values:
          ht.add(str(a_value), None)
      for b_value in tree_b_values:

          if ht.contains(str(b_value)):
                intersections.append(b_value)
      return None if not len(list(set(intersections))) else list(set(intersections))
    except EmptyTree:
      return None


if __name__ == "__main__":
    os.system('clear')
    bta = BinarySearchTree(*[1,2,1])
    btb = BinarySearchTree(*[1,2,3])
    print(tree_intersection(bta, btb))
