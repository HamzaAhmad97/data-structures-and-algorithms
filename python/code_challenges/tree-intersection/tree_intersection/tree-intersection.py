from tree_intersection.depenancy_classes import Hashtable, breadth_first, EmptyTree, BinarySearchTree
def tree_intersection(tree_a, tree_b):
    intersections = []
    ht = Hashtable()
    try:
      tree_a_values = breadth_first(tree_a)
      tree_b_values = breadth_first(tree_b)
      for a_value in tree_a_values:
          ht.add(str(a_value), type(a_value).__name__)
      for b_value in tree_b_values:
          if ht.contains(str(b_value)):
              if ht.get(str(b_value)) == type(b_value).__name__:
                  intersections.append(b_value)
      return None or intersections
    except EmptyTree:
      return None


if __name__ == "__main__":
    bta = BinarySearchTree(1,2)
    btb = BinarySearchTree(1,1)
    print(tree_intersection(bta, btb))
