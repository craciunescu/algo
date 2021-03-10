"""
    @author: David E. Craciunescu
      @date: 2021/02/22 (yyyy/mm/dd)

    2. We are given a vector of unordered positive integers that we cannot alter 
    or copy in any way, shape, or form. Yet, we'd like to obtain information from
    this vector as if it were ordered.

    One idea we have is creating an index vector Ind[1...N]. This type of vector
    would store the position in which each element of the original vector would be
    if the original vector were ordered.

    This would be an example of a vector right next to his index vector.
    - Vector[1...N] => [50, 98, 10, 63, 31, 25, 63, 74]
    -  Index[1...N] => [ 3,  6,  5,  1,  4,  7,  8,  2]

    As you can see, the index vector simply stores the position in which every
    element of the original vector would be if this were ordered.

    => Modify the standard MergeSort algorithm in order to obtain the vector
    indices of a vector V[1...N] given as a parameter.

"""
